"""Arabic support for the RTL text engine.

The patched dialogue renderer draws the first character of a line at the
right edge and moves left. So text is stored in right-to-left order:

  1. arabic_reshaper turns base letters (U+0621..) into contextual
     presentation forms (U+FE80..U+FEFC), including lam-alef ligatures.
  2. python-bidi computes the visual order for an RTL paragraph, which
     reverses embedded left-to-right runs (digits, Latin names).
  3. That visual (left-to-right) string is reversed, so index 0 is the
     right-most glyph on screen.

Glyphs live in 8x16 cells of assets/images/ui/charset.png, in the cells
the US release left blank (the old Japanese kana).
"""

import re
import unicodedata

try:
    import arabic_reshaper
except ImportError:  # pragma: no cover
    arabic_reshaper = None

try:
    from bidi.algorithm import get_display
except ImportError:  # python-bidi >= 0.5 also exposes it at the top level
    try:
        from bidi import get_display
    except ImportError:  # pragma: no cover
        get_display = None


# Free single-byte cells in the dialogue font (the blanked kana), in order.
# 0x93-0x96 stay free: the bold UI font keeps . × = : there (battle screens,
# chip counts, play time), so meem-medial and noon live at 0xA9-0xAC instead.
FREE_SLOTS = list(range(0x0D, 0x5E)) + list(range(0x97, 0xE5))

# Every glyph the translation can use: all Arabic presentation forms
# (U+FE80..U+FEFC, incl. lam-alef ligatures) plus Arabic punctuation.
ARABIC_GLYPHS = [chr(c) for c in range(0xFE80, 0xFEFD)] + [
    "\u060C",  # ، comma
    "\u061B",  # ؛ semicolon
    "\u061F",  # ؟ question mark
]

# Presentation form -> font slot(s). The glyph art follows the 8x16 Arabic
# font from the Pokemon Crystal translation, so forms that share a shape
# there share a slot here (e.g. beh isolated/final). Seen, sheen, sad and dad
# in isolated/final form are one cell (they used to take two).
charmap_arabic = {
    "\uFE80": (0x0D,),  # ﺀ letter hamza isolated form
    "\uFE81": (0x0E,),  # ﺁ letter alef with madda above isolated form
    "\uFE82": (0x0F,),  # ﺂ letter alef with madda above final form
    "\uFE83": (0x10,),  # ﺃ letter alef with hamza above isolated form
    "\uFE84": (0x11,),  # ﺄ letter alef with hamza above final form
    "\uFE85": (0x12,),  # ﺅ letter waw with hamza above isolated form
    "\uFE86": (0x12,),  # ﺆ letter waw with hamza above final form
    "\uFE87": (0x13,),  # ﺇ letter alef with hamza below isolated form
    "\uFE88": (0x14,),  # ﺈ letter alef with hamza below final form
    "\uFE89": (0x15,),  # ﺉ letter yeh with hamza above isolated form
    "\uFE8A": (0x16,),  # ﺊ letter yeh with hamza above final form
    "\uFE8B": (0x17,),  # ﺋ letter yeh with hamza above initial form
    "\uFE8C": (0x18,),  # ﺌ letter yeh with hamza above medial form
    "\uFE8D": (0x19,),  # ﺍ letter alef isolated form
    "\uFE8E": (0x1A,),  # ﺎ letter alef final form
    "\uFE8F": (0x1B,),  # ﺏ letter beh isolated form
    "\uFE90": (0x1B,),  # ﺐ letter beh final form
    "\uFE91": (0x1C,),  # ﺑ letter beh initial form
    "\uFE92": (0x1D,),  # ﺒ letter beh medial form
    "\uFE93": (0x1E,),  # ﺓ letter teh marbuta isolated form
    "\uFE94": (0x1F,),  # ﺔ letter teh marbuta final form
    "\uFE95": (0x20,),  # ﺕ letter teh isolated form
    "\uFE96": (0x20,),  # ﺖ letter teh final form
    "\uFE97": (0x21,),  # ﺗ letter teh initial form
    "\uFE98": (0x22,),  # ﺘ letter teh medial form
    "\uFE99": (0x23,),  # ﺙ letter theh isolated form
    "\uFE9A": (0x23,),  # ﺚ letter theh final form
    "\uFE9B": (0x24,),  # ﺛ letter theh initial form
    "\uFE9C": (0x25,),  # ﺜ letter theh medial form
    "\uFE9D": (0x26,),  # ﺝ letter jeem isolated form
    "\uFE9E": (0xB2,),  # ﺞ letter jeem final form
    "\uFE9F": (0x27,),  # ﺟ letter jeem initial form
    "\uFEA0": (0x28,),  # ﺠ letter jeem medial form
    "\uFEA1": (0x29,),  # ﺡ letter hah isolated form
    "\uFEA2": (0xB3,),  # ﺢ letter hah final form
    "\uFEA3": (0x2A,),  # ﺣ letter hah initial form
    "\uFEA4": (0x2B,),  # ﺤ letter hah medial form
    "\uFEA5": (0x2C,),  # ﺥ letter khah isolated form
    "\uFEA6": (0xB4,),  # ﺦ letter khah final form
    "\uFEA7": (0x2D,),  # ﺧ letter khah initial form
    "\uFEA8": (0x2E,),  # ﺨ letter khah medial form
    "\uFEA9": (0x2F,),  # ﺩ letter dal isolated form
    "\uFEAA": (0x30,),  # ﺪ letter dal final form
    "\uFEAB": (0x31,),  # ﺫ letter thal isolated form
    "\uFEAC": (0x32,),  # ﺬ letter thal final form
    "\uFEAD": (0x33,),  # ﺭ letter reh isolated form
    "\uFEAE": (0x34,),  # ﺮ letter reh final form
    "\uFEAF": (0x35,),  # ﺯ letter zain isolated form
    "\uFEB0": (0x36,),  # ﺰ letter zain final form
    "\uFEB1": (0x37,),  # ﺱ letter seen isolated form
    "\uFEB2": (0x37,),  # ﺲ letter seen final form
    "\uFEB3": (0x39,),  # ﺳ letter seen initial form
    "\uFEB4": (0x3A,),  # ﺴ letter seen medial form
    "\uFEB5": (0x3B,),  # ﺵ letter sheen isolated form
    "\uFEB6": (0x3B,),  # ﺶ letter sheen final form
    "\uFEB7": (0x3C,),  # ﺷ letter sheen initial form
    "\uFEB8": (0x3D,),  # ﺸ letter sheen medial form
    "\uFEB9": (0x3E,),  # ﺹ letter sad isolated form
    "\uFEBA": (0x3E,),  # ﺺ letter sad final form
    "\uFEBB": (0x3F,),  # ﺻ letter sad initial form
    "\uFEBC": (0x40,),  # ﺼ letter sad medial form
    "\uFEBD": (0x41,),  # ﺽ letter dad isolated form
    "\uFEBE": (0x41,),  # ﺾ letter dad final form
    "\uFEBF": (0x42,),  # ﺿ letter dad initial form
    "\uFEC0": (0x43,),  # ﻀ letter dad medial form
    "\uFEC1": (0x44,),  # ﻁ letter tah isolated form
    "\uFEC2": (0x44,),  # ﻂ letter tah final form
    "\uFEC3": (0x44,),  # ﻃ letter tah initial form
    "\uFEC4": (0x45,),  # ﻄ letter tah medial form
    "\uFEC5": (0x46,),  # ﻅ letter zah isolated form
    "\uFEC6": (0x46,),  # ﻆ letter zah final form
    "\uFEC7": (0x46,),  # ﻇ letter zah initial form
    "\uFEC8": (0x47,),  # ﻈ letter zah medial form
    "\uFEC9": (0x48,),  # ﻉ letter ain isolated form
    "\uFECA": (0x49,),  # ﻊ letter ain final form
    "\uFECB": (0x4A,),  # ﻋ letter ain initial form
    "\uFECC": (0x4B,),  # ﻌ letter ain medial form
    "\uFECD": (0x4C,),  # ﻍ letter ghain isolated form
    "\uFECE": (0x4D,),  # ﻎ letter ghain final form
    "\uFECF": (0x4E,),  # ﻏ letter ghain initial form
    "\uFED0": (0x4F,),  # ﻐ letter ghain medial form
    "\uFED1": (0x50,),  # ﻑ letter feh isolated form
    "\uFED2": (0x50,),  # ﻒ letter feh final form
    "\uFED3": (0x51,),  # ﻓ letter feh initial form
    "\uFED4": (0x52,),  # ﻔ letter feh medial form
    "\uFED5": (0x53,),  # ﻕ letter qaf isolated form
    "\uFED6": (0x53,),  # ﻖ letter qaf final form
    "\uFED7": (0x54,),  # ﻗ letter qaf initial form
    "\uFED8": (0x55,),  # ﻘ letter qaf medial form
    "\uFED9": (0x56,),  # ﻙ letter kaf isolated form
    "\uFEDA": (0x56,),  # ﻚ letter kaf final form
    "\uFEDB": (0x57,),  # ﻛ letter kaf initial form
    "\uFEDC": (0x58,),  # ﻜ letter kaf medial form
    "\uFEDD": (0x59,),  # ﻝ letter lam isolated form
    "\uFEDE": (0x59,),  # ﻞ letter lam final form
    "\uFEDF": (0x5A,),  # ﻟ letter lam initial form
    "\uFEE0": (0x5B,),  # ﻠ letter lam medial form
    "\uFEE1": (0x5C,),  # ﻡ letter meem isolated form
    "\uFEE2": (0x5C,),  # ﻢ letter meem final form
    "\uFEE3": (0x5D,),  # ﻣ letter meem initial form
    "\uFEE4": (0xA9,),  # ﻤ letter meem medial form
    "\uFEE5": (0xAA,),  # ﻥ letter noon isolated form
    "\uFEE6": (0xAA,),  # ﻦ letter noon final form
    "\uFEE7": (0xAB,),  # ﻧ letter noon initial form
    "\uFEE8": (0xAC,),  # ﻨ letter noon medial form
    "\uFEE9": (0x97,),  # ﻩ letter heh isolated form
    "\uFEEA": (0x98,),  # ﻪ letter heh final form
    "\uFEEB": (0x99,),  # ﻫ letter heh initial form
    "\uFEEC": (0x9A,),  # ﻬ letter heh medial form
    "\uFEED": (0x9B,),  # ﻭ letter waw isolated form
    "\uFEEE": (0x9B,),  # ﻮ letter waw final form
    "\uFEEF": (0x9C,),  # ﻯ letter alef maksura isolated form
    "\uFEF0": (0x9D,),  # ﻰ letter alef maksura final form
    "\uFEF1": (0x9E,),  # ﻱ letter yeh isolated form
    "\uFEF2": (0x9F,),  # ﻲ letter yeh final form
    "\uFEF3": (0xA0,),  # ﻳ letter yeh initial form
    "\uFEF4": (0xA1,),  # ﻴ letter yeh medial form
    "\uFEF5": (0xA2,),  # ﻵ ligature lam with alef with madda above isolated form
    "\uFEF6": (0xA2,),  # ﻶ ligature lam with alef with madda above final form
    "\uFEF7": (0xA3,),  # ﻷ ligature lam with alef with hamza above isolated form
    "\uFEF8": (0xA3,),  # ﻸ ligature lam with alef with hamza above final form
    "\uFEF9": (0xA4,),  # ﻹ ligature lam with alef with hamza below isolated form
    "\uFEFA": (0xA4,),  # ﻺ ligature lam with alef with hamza below final form
    # Isolated alef after a letter that does not join (دار، رأى): the
    # word-initial glyphs sit at the left of their cell, these mid-word
    # copies sit at the right so the gap to the previous letter stays small.
    "\uE081": (0xAD,),  # mid-word ﺁ
    "\uE083": (0xAE,),  # mid-word ﺃ
    "\uE087": (0xAF,),  # mid-word ﺇ
    "\uE08D": (0xB0,),  # mid-word ﺍ
    "\uE090": (0xB1,),  # two mid-word ﺍ in one cell (runs like آااا)
    "\uE0A0": (0xB5,),  # the article ال (alef + initial lam) in one cell
    "\uFEFB": (0xA5,),  # ﻻ ligature lam with alef isolated form
    "\uFEFC": (0xA5,),  # ﻼ ligature lam with alef final form
    "\u060C": (0xA6,),  # ، comma
    "\u061B": (0xA7,),  # ؛ semicolon
    "\u061F": (0xA8,),  # ؟ question mark
}

assert all(c in charmap_arabic for c in ARABIC_GLYPHS)
assert all(s in FREE_SLOTS for v in charmap_arabic.values() for s in v)


# Invisible right-to-left mark. The insert tool puts it at the start of a
# translated box that has no Arabic letters (say a chip name kept in English),
# so the build still treats the box as RTL text. It is dropped when stored.
RLM = "\u200f"


def is_arabic(ch: str) -> bool:
    o = ord(ch)
    return (
        o == 0x200F
        or 0x0600 <= o <= 0x06FF
        or 0x0750 <= o <= 0x077F
        or 0xFB50 <= o <= 0xFDFF
        or 0xFE70 <= o <= 0xFEFF
    )


def glyph_name(ch: str) -> str:
    try:
        return unicodedata.name(ch)
    except ValueError:
        return f"U+{ord(ch):04X}"


# An isolated alef form that directly follows another Arabic letter is inside
# a word (the letter before it does not join); it gets the mid-word glyph.
_MIDWORD_ALEF = re.compile("(?<=[\u0621-\u064A\uFE70-\uFEFC])[\uFE81\uFE83\uFE87\uFE8D]")


_ARTICLE = re.compile("(?<![\u0621-\u064A\uFE70-\uFEFC\uE000-\uE0FF])\uFE8D\uFEDF")


def to_rtl_storage(run: str) -> str:
    """Convert one run of plain text (no newlines, no markup) to the order
    the RTL renderer expects."""
    if not run:
        return run
    if arabic_reshaper is None or get_display is None:
        raise SystemExit(
            "Arabic text needs the 'arabic-reshaper' and 'python-bidi' packages.\n"
            "Install them into the build venv: python -m pip install -r requirements.txt"
        )
    # No glyphs for tatweel (the stretching stroke) or harakat (vowel marks).
    run = re.sub("[\u0640\u064B-\u0652\u0670]", "", run)
    shaped = arabic_reshaper.reshape(run)
    # no glyph for the Allah ligature (ﷲ): spell the word out letter by letter
    shaped = shaped.replace("\uFDF2", "\uFE8D\uFEDF\uFEE0\uFEEA")
    visual = get_display(shaped, base_dir="R").replace(RLM, "")
    # Storage order is reading order for the Arabic, so the glyph swaps go
    # here (private-use code points would be reordered by the bidi step).
    store = _MIDWORD_ALEF.sub(lambda m: chr(ord(m.group(0)) - 0xFE81 + 0xE081), visual[::-1])
    # A run of alefs (هيآاااخ) is packed two to a cell so it keeps the normal
    # letter spacing instead of one alef per 8px cell.
    store = store.replace("\uE08D\uE08D", "\uE090")
    # the article ال at the start of a word fits in one cell
    return _ARTICLE.sub("\uE0A0", store)


_KEY_WIDTHS = None


def _key_item_widths() -> dict:
    """Cells of each key item name as translated in assets/text/item/name.txt,
    so {key X} in dialogue is measured by its Arabic name."""
    global _KEY_WIDTHS
    if _KEY_WIDTHS is None:
        import os
        import re
        _KEY_WIDTHS = {}
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            src = open(os.path.join(root, "tools", "build_script.py"), encoding="utf-8").read()
            block = src[src.index("key_item_map = {"):]
            block = block[: block.index("}")]
            ids = {int(v, 16): k for k, v in re.findall(r'"([^"]+)":\s*(0x[0-9A-Fa-f]+)', block)}
            names = open(os.path.join(root, "assets", "text", "item", "name.txt"), encoding="utf-8").read()
            for sec, txt in re.findall(r'section_start\((0x[0-9A-Fa-f]+)\)\s*\ntext\("((?:[^"\\]|\\.)*)"\)', names):
                key = ids.get(int(sec, 16))
                if key:
                    _KEY_WIDTHS[key] = measure_line(txt)
        except (OSError, ValueError):
            pass
    return _KEY_WIDTHS


def command_width(cmd: str) -> int:
    """Approximate on-screen cells for a {command} inside a dialogue line."""
    body = cmd.strip("{}").split()
    if not body:
        return 0
    name = body[0]
    if name in ("..", "..."):
        return len(name)
    if name == "key" and len(body) > 1:
        w = _key_item_widths().get(body[1])
        return w if w is not None else len(body[1])
    if name == "chip" and len(body) > 1:
        return len(" ".join(body[1:]))  # name, plus " X" when a code is given
    if name == "c":
        return 2  # option arrow padding
    return 0  # timing, animation, flags, sounds...


def measure_line(line: str) -> int:
    """On-screen width in 8px cells of one dialogue line as the build will
    draw it (shaping, lam-alef ligatures and two-cell letters included)."""
    cells = 0
    run = []

    def flush():
        nonlocal cells
        if run:
            text = "".join(run)
            if any(is_arabic(c) for c in text):
                text = to_rtl_storage(text)
            for c in text:
                cells += len(charmap_arabic[c]) if c in charmap_arabic else 1
            run.clear()

    i = 0
    while i < len(line):
        c = line[i]
        if c == "{":
            j = line.find("}", i)
            j = len(line) - 1 if j == -1 else j
            flush()
            cells += command_width(line[i : j + 1])
            i = j + 1
            continue
        if c in "<>":
            flush()
        else:
            run.append(c)
        i += 1
    flush()
    return cells
