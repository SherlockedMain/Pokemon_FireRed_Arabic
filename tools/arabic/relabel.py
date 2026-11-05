#!/usr/bin/env python3
"""Redraw English labels baked into graphics with Arabic, in the game's own small
font (or Kufam for big titles), using each image's own palette colours.

    python3 tools/arabic/relabel.py [--preview DIR]

Every asset is restored from tools/arabic/graphics_orig/ (made on first run) so
the script can be re-run after editing a label."""
import os, sys, shutil, collections
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from arabic_text import charmap, width_table, tokens
from shape import shape

ORIG = os.path.join(HERE, 'graphics_orig')

def small_rows(text):
    """Rows of 1 (ink) / 2 (shadow) / 0 for `text` in the game's small font, laid out right to left,
    trimmed to the rows that hold pixels."""
    sheet = Image.open(os.path.join(ROOT, 'graphics', 'fonts', 'latin_small.png')).load()
    cm, wt = charmap(), width_table('small')
    glyphs = []
    for tok in tokens(shape(text)):
        if tok == ' ':
            glyphs.append((None, 3)); continue
        b = cm['chars'][tok]
        gid = 0x100 + b[1] if b[0] == 0xF9 else b[0]
        glyphs.append((gid, wt[gid]))
    total = sum(w for _, w in glyphs)
    rows = [[0] * total for _ in range(16)]
    rtl = any('\u0600' <= ch <= '\u06FF' for ch in text)     # Latin-only labels (HP, PP) stay left to right
    x = total if rtl else 0
    for gid, w in glyphs:
        if rtl:
            x -= w
        else:
            x += w
        if not rtl:
            x -= w
        if gid is None:
            continue
        cx, cy = (gid % 32) * 8, (gid // 32) * 16
        for y in range(16):
            for k in range(w):
                v = sheet[cx + k, cy + y]
                rows[y][x + k] = v if v in (1, 2) else 0
        if not rtl:
            x += w
    used = [y for y in range(16) if any(rows[y])]
    return rows[used[0]:used[-1] + 1] if used else [[0]]

def kufam_rows(text, max_h):
    import title_screen
    return title_screen.small_text(text, max_h)

def restore(rel):
    src, dst = os.path.join(ORIG, rel), os.path.join(ROOT, 'graphics', rel)
    if not os.path.exists(src):
        os.makedirs(os.path.dirname(src), exist_ok=True)
        shutil.copy(dst, src)
    shutil.copy(src, dst)
    return dst

def relabel(im, box, rows, ink, shadow=None, erase=None, bg=None, anchor='center'):
    """Erase the old text inside box (x0,y0,x1,y1 inclusive) and stamp rows centred in it."""
    px = im.load()
    x0, y0, x1, y1 = box
    if bg is None:
        bg = collections.Counter(px[x, y] for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)
                                 if px[x, y] not in (ink, shadow)).most_common(1)[0][0]
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            if px[x, y] in (erase or (ink, shadow)):
                px[x, y] = bg
    h, w = len(rows), len(rows[0])
    ox = x0 + (x1 - x0 + 1 - w) // 2 if anchor == 'center' else x1 - w + 1
    oy = y0 + (y1 - y0 + 1 - h + 1) // 2
    for y, row in enumerate(rows):
        for x, v in enumerate(row):
            tx, ty = ox + x, oy + y
            if v and x0 <= tx <= x1 and y0 - 1 <= ty <= y1 + 1:
                if v == 1:
                    px[tx, ty] = ink
                elif shadow is not None:
                    px[tx, ty] = shadow
    return w, h

def pills(im, body, region=None):
    px = im.load(); W, H = im.size
    seen, out = set(), []
    x0, y0, x1, y1 = region or (0, 0, W - 1, H - 1)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if px[x, y] == body and (x, y) not in seen:
                st = [(x, y)]; seen.add((x, y)); xs, ys = [], []
                while st:
                    a, b = st.pop(); xs.append(a); ys.append(b)
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        c, d = a + dx, b + dy
                        if x0 <= c <= x1 and y0 <= d <= y1 and (c, d) not in seen and px[c, d] in (body, body + 1):
                            seen.add((c, d)); st.append((c, d))
                if len(xs) > 60:
                    out.append((min(xs), min(ys), max(xs), max(ys)))
    return sorted(out, key=lambda b: (b[0] > 60, b[1]))

SUMMARY = {45: ['مذكرة المدرب', 'الرقم', 'الاسم', 'النوع', 'المدرب', 'الهوية', 'الأداة', 'الحالة'],
           61: ['HP', 'الهجوم', 'الدفاع', 'ه. خاص', 'د. خاص', 'السرعة', 'الخبرة', 'القدرة'],
           77: ['القوة', 'الدقة', 'التأثير']}
TYPES = [['عادي', 'ناري', 'مائي', 'عشبي'], ['كهربي', 'صخري', 'أرضي', 'جليدي'], ['طائر', 'مقاتل', 'شبحي', 'حشري'],
         ['سام', 'نفسي', 'فولاذي', 'ظلامي'], ['تنيني', None]]
MOVE_LABELS = ['النوع', 'القوة', 'الدقة', 'PP', 'التأثير']
TABS = {'page_swap_lower.png': 'عربي', 'page_swap_upper.png': 'ABC', 'page_swap_others.png': '123'}   # 8 px tall: only these read well

def do_summary(report):
    path = restore('summary_screen/bg.png'); im = Image.open(path)
    for body, names in SUMMARY.items():
        found = pills(im, body)
        report.append('summary body %d: %d pills for %d labels' % (body, len(found), len(names)))
        for (x0, y0, x1, y1), name in zip(found, names):
            relabel(im, (x0 + 2, y0 + 1, x1 - 2, y1 - 1), small_rows(name), ink=body + 1, erase=(body + 1,), bg=body)
    im.save(path)

def do_types(report):
    path = restore('interface/menu_info.png'); im = Image.open(path)
    for r, row in enumerate(TYPES):
        for c, name in enumerate(row):
            if name:
                relabel(im, (c * 32, 16 + r * 16 + 1, c * 32 + 31, 16 + r * 16 + 10), small_rows(name), ink=31, shadow=30)
    found = pills(im, 30, region=(0, 80, 127, 127))
    found = [b for b in found if not (b[0] < 64 and b[1] < 92)]          # skip the DRAGON / ??? badges
    found = sorted(found, key=lambda b: (b[1] // 8, b[0]))
    report.append('menu_info: %d move-info pills' % len(found))
    order = ['النوع', 'القوة', 'الدقة', 'PP', 'التأثير']
    for (x0, y0, x1, y1), name in zip(found, order):
        relabel(im, (x0 + 2, y0 + 1, x1 - 2, y1 - 1), small_rows(name), ink=31, erase=(31,), bg=30)
    im.save(path)

def do_tabs(report):
    for f, name in TABS.items():
        path = restore('naming_screen/' + f); im = Image.open(path); px = im.load()
        cols = collections.Counter(px[x, y] for x in range(0, 30) for y in range(8))
        pal = im.getpalette()
        lum = lambda i: sum(pal[i * 3:i * 3 + 3])
        ink = max(cols, key=lum); bg = cols.most_common(1)[0][0]
        rows = small_rows(name)[:8]
        relabel(im, (0, 0, 29, 7), rows, ink=ink, erase=(ink,), bg=bg)
        im.save(path)
    report.append('naming tabs: %s' % ', '.join(TABS.values()))

def do_trainer_card(report):
    path = restore('trainer_card/tiles.png'); im = Image.open(path); px = im.load()
    pal = im.getpalette(); lum = lambda i: sum(pal[i * 3:i * 3 + 3])
    def colours(box):
        x0, y0, x1, y1 = box
        c = collections.Counter(px[x, y] for x in range(x0, x1 + 1) for y in range(y0, y1 + 1))
        bg = c.most_common(1)[0][0]
        others = [i for i, _ in c.most_common(4) if i != bg]
        return bg, others
    # big title: "TRAINER" (left) + "CARD" (right) -> «المدرب» + «بطاقة»
    for box, word in (((64, 27, 121, 38), 'المدرب'), ((64, 42, 95, 53), 'بطاقة')):
        bg, others = colours(box)
        ink = max(others[:2], key=lum); shadow = min(others[:2], key=lum)
        relabel(im, box, kufam_rows(word, 10), ink=ink, shadow=shadow, erase=tuple(others[:2]), bg=bg)
    for box, word in (((0, 70, 60, 78), 'المدرب:'),):          # "BADGES" (6 px tall) stays English
        bg, others = colours(box)
        ink = max(others[:1] or [bg], key=lum)
        relabel(im, box, small_rows(word), ink=ink, erase=tuple(others[:2]), bg=bg)
    im.save(path)
    report.append('trainer card: «بطاقة المدرب», «المدرب:»')

def main():
    report = []
    do_summary(report); do_types(report); do_tabs(report); do_trainer_card(report)
    print('\n'.join(report))
    if '--preview' in sys.argv:
        out = sys.argv[sys.argv.index('--preview') + 1]
        os.makedirs(out, exist_ok=True)
        for rel, s in (('summary_screen/bg.png', 3), ('interface/menu_info.png', 3), ('trainer_card/tiles.png', 3),
                       ('naming_screen/page_swap_lower.png', 6), ('naming_screen/page_swap_upper.png', 6),
                       ('naming_screen/page_swap_others.png', 6)):
            im = Image.open(os.path.join(ROOT, 'graphics', rel)).convert('RGB')
            im.resize((im.width * s, im.height * s), Image.NEAREST).save(os.path.join(out, rel.replace('/', '_')))

if __name__ == '__main__':
    main()
