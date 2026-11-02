"""Measuring, wrapping and encoding helpers for Arabic FireRed text.

Widths come from the game's own tables (src/text.c) and charmap.txt, so a line
that measures as fitting here fits in the game.
"""
import os, re
from shape import shape

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KEYPAD_WIDTHS = {0x0: 8, 0x1: 8, 0x2: 16, 0x3: 16, 0x4: 24, 0x5: 24}   # A B L R START SELECT; d-pad icons are 8
NAME_WIDTH = 42          # {PLAYER} / {RIVAL}: up to 7 Latin letters
VAR_WIDTH = 60           # {STR_VAR_n}: a Pokémon or item name, up to 10 Latin letters

_charmap = None
_widths = {}

def charmap():
    global _charmap
    if _charmap is None:
        _charmap = {'chars': {}, 'names': {}}
        for line in open(os.path.join(ROOT, 'charmap.txt'), encoding='utf-8'):
            line = line.split('@')[0].strip()
            m = re.match(r"^'(.+)'\s*=\s*((?:[0-9A-F]{2}\s*)+)$", line)
            if m:
                _charmap['chars'].setdefault(m.group(1), [int(b, 16) for b in m.group(2).split()])
                continue
            m = re.match(r"^(\w+)\s*=\s*((?:[0-9A-F]{2}\s*)+)$", line)
            if m:
                _charmap['names'].setdefault(m.group(1), [int(b, 16) for b in m.group(2).split()])
    return _charmap

def width_table(font):
    if font not in _widths:
        name = {'normal': 'sFontNormalLatinGlyphWidths', 'small': 'sFontSmallLatinGlyphWidths'}[font]
        src = open(os.path.join(ROOT, 'src', 'text.c')).read()
        body = re.search(name + r'\[\]\s*=\s*\{(.*?)\};', src, re.S).group(1)
        _widths[font] = [int(v) for v in re.findall(r'\d+', body)]
    return _widths[font]

def tokens(text):
    """Split a (shaped) string into tokens: single characters and {MACROS}."""
    return re.findall(r'\{[^}]*\}|.', text, re.S)

def token_width(tok, font):
    cm, w = charmap(), width_table(font)
    if tok.startswith('{'):
        name = tok[1:-1].split()[0]
        if name in ('PLAYER', 'RIVAL'):
            return NAME_WIDTH
        if name.startswith('STR_VAR'):
            return VAR_WIDTH
        b = cm['names'].get(name)
        if not b:
            return 0
        if b[0] == 0xF8:
            return KEYPAD_WIDTHS.get(b[1], 8)
        if b[0] == 0xF9:
            return w[0x100 + b[1]]
        return 0 if b[0] >= 0xFA else w[b[0]]
    b = cm['chars'].get(tok)
    if b is None:
        raise ValueError('no glyph for %r (U+%04X)' % (tok, ord(tok)))
    return w[0x100 + b[1]] if b[0] == 0xF9 else w[b[0]]

def measure(shaped, font='normal'):
    return sum(token_width(t, font) for t in tokens(shaped))

def wrap_pairs(text, max_width, font='normal'):
    """Like wrap(), but returns (shaped_line, readable_line) pairs. Words are
    shaped one by one (letters never join across a space, so this is the same
    as shaping the whole line)."""
    lines = []
    for raw in text.split('\n'):
        indent = raw[:len(raw) - len(raw.lstrip(' '))]
        words = raw.strip(' ').split(' ') if raw.strip() else ['']
        cur, cur_raw = indent, indent
        for wd in words:
            sw = shape(wd)
            cand = sw if cur == indent else cur + ' ' + sw
            cand = cand if cur != indent else indent + sw
            if cur.strip() and measure(cand, font) > max_width:
                lines.append((cur, cur_raw))
                cur, cur_raw = sw, wd
            else:
                cur = cand
                cur_raw = (cur_raw + ' ' + wd) if cur_raw.strip() else indent + wd
        lines.append((cur, cur_raw))
    return lines

def wrap(text, max_width, font='normal'):
    """Shape and word-wrap one paragraph. Explicit newlines are kept.
    Returns a list of shaped lines."""
    lines = []
    for raw in text.split('\n'):
        words = shape(raw.strip(' ')).split(' ') if raw.strip() else ['']
        cur = ''
        for wd in words:
            cand = wd if not cur else cur + ' ' + wd
            if cur and measure(cand, font) > max_width:
                lines.append(cur)
                cur = wd
            else:
                cur = cand
        lines.append(cur)
    return lines

def paragraphs(text):
    """Blank line = paragraph (or page) break; single newline = line break."""
    return [p.strip('\n') for p in re.split(r'\n\s*\n', text.strip('\n'))]
