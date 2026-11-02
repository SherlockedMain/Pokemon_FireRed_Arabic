#!/usr/bin/env python3
"""Arabic title screen: «بوكيمون» logo, «الأحمر الناري» plate, «اضغط زر البدء»
and the translator credit, written into the title screen tile sheets/tilemaps.

    python3 tools/arabic/title_screen.py [--from-vanilla DIR]

Reads the ORIGINAL title graphics (from a vanilla checkout, or the backups this
script keeps as *.orig the first time) so it can be re-run safely.
Logo lettering: Lalezar (SIL Open Font License), tools/arabic/fonts/.
Small text: the game's own Arabic font (latin_normal.png).
"""
import os, re, shutil, struct, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from arabic_text import charmap, width_table, tokens
from shape import shape

GFX = os.path.join(ROOT, 'graphics', 'title_screen')
LOGO_PNG, LOGO_BIN, LOGO_PAL = [os.path.join(GFX, 'firered', 'game_title_logo' + e) for e in ('.png', '.bin', '.pal')]
PS_PNG, PS_BIN = [os.path.join(GFX, 'copyright_press_start' + e) for e in ('.png', '.bin')]
FONTS = {'lalezar': 'Lalezar-Regular.ttf', 'jomhuria': 'Jomhuria-Regular.ttf',
         'marhey': 'Marhey[wght].ttf', 'mada': 'Mada[wght].ttf'}
LOGO_FONT = 'jomhuria'     # «بوكيمون»
PLATE_FONT = 'jomhuria'    # «الأحمر الناري»
PLATE_RIGHT = 132          # plate's right edge: Charizard's head starts at x≈140
PLATE_MAX_W = 112

def load_font(name, size):
    font = ImageFont.truetype(os.path.join(HERE, 'fonts', FONTS[name]), size, layout_engine=ImageFont.Layout.RAQM)
    try:                                           # variable fonts: use the heaviest weight
        names = [n.decode() if isinstance(n, bytes) else n for n in font.get_variation_names()]
        for want in ('Black', 'ExtraBold', 'Bold'):
            if want in names:
                font.set_variation_by_name(want)
                break
    except Exception:
        pass
    return font

TITLE, PLATE = 'بوكيمون', 'الأحمر الناري'
PRESS, CREDIT = 'اضغط زر البدء', 'تعريب أيوب شكري'

# Logo palette (8bpp): existing yellows/blues, plus fire colours in unused slots 80-87.
YELLOW = [37, 6, 18, 2, 14, 120, 116]           # light -> dark, top -> bottom
BLUE, BLUE_DARK, NAVY = 12, 72, 65
FIRE = {80: (255, 250, 150), 81: (255, 222, 41), 82: (255, 164, 0), 83: (246, 106, 0),
        84: (213, 41, 0), 85: (148, 16, 0), 86: (57, 0, 0), 87: (255, 255, 255)}
FIRE_RAMP = [80, 81, 82, 83, 84]

def backup(path):
    if not os.path.exists(path + '.orig'):
        shutil.copy(path, path + '.orig')
    return path + '.orig'

def decode(sheet_path, bin_path, size=(256, 160)):
    sheet = Image.open(sheet_path); w = sheet.size[0] // 8
    data = open(bin_path, 'rb').read()
    scr = Image.new('P', size, 0); scr.putpalette(sheet.getpalette())
    for i in range(len(data) // 2):
        e = struct.unpack('<H', data[2 * i:2 * i + 2])[0]; t = e & 0x3FF
        if not t:
            continue
        tile = sheet.crop(((t % w) * 8, (t // w) * 8, (t % w) * 8 + 8, (t // w) * 8 + 8))
        if e & 0x400: tile = tile.transpose(Image.FLIP_LEFT_RIGHT)
        if e & 0x800: tile = tile.transpose(Image.FLIP_TOP_BOTTOM)
        scr.paste(tile, ((i % 32) * 8, (i // 32) * 8))
    return scr

def encode(scr, sheet_cols, palbits, max_tiles, sheet_path, bin_path, palette):
    tiles, index, entries = [bytes(64)], {bytes(64): 0}, []
    px = scr.load()
    for ty in range(scr.size[1] // 8):
        for tx in range(32):
            b = bytes(px[tx * 8 + x, ty * 8 + y] for y in range(8) for x in range(8))
            if b not in index:
                index[b] = len(tiles); tiles.append(b)
            entries.append(index[b] | (palbits << 12))
    assert len(tiles) <= max_tiles, '%d tiles > %d' % (len(tiles), max_tiles)
    rows = (len(tiles) + sheet_cols - 1) // sheet_cols
    sheet = Image.new('P', (sheet_cols * 8, rows * 8), 0); sheet.putpalette(palette)
    sp = sheet.load()
    for n, b in enumerate(tiles):
        ox, oy = (n % sheet_cols) * 8, (n // sheet_cols) * 8
        for k, v in enumerate(b):
            sp[ox + k % 8, oy + k // 8] = v
    sheet.save(sheet_path)
    open(bin_path, 'wb').write(b''.join(struct.pack('<H', e) for e in entries))
    return len(tiles)

def text_mask(text, size, scale=4, font_name='lalezar'):
    """Anti-aliasing-free mask of `text`, rendered big and reduced."""
    font = load_font(font_name, size * scale)
    l, t, r, b = font.getbbox(text, direction='rtl', language='ar')
    big = Image.new('L', (r - l + 8 * scale, b - t + 8 * scale), 0)
    ImageDraw.Draw(big).text((4 * scale - l, 4 * scale - t), text, font=font, fill=255, direction='rtl', language='ar')
    small = big.resize((big.size[0] // scale, big.size[1] // scale), Image.BOX)
    m = small.point(lambda v: 255 if v >= 110 else 0)
    return m.crop(m.getbbox())

def arc(mask, rise):
    """Bow the word upwards in the middle, like the original logo."""
    w, h = mask.size
    out = Image.new('L', (w, h + rise), 0)
    for x in range(w):
        d = (x - w / 2) / (w / 2)
        dy = int(round(rise * (1 - d * d)))
        out.paste(mask.crop((x, 0, x + 1, h)), (x, rise - dy))
    return out

def dilate(mask, r):
    return mask.filter(ImageFilter.MaxFilter(2 * r + 1)) if r else mask

def paint(scr, mask, ox, oy, fill_ramp, outline, outline_r, extrude, extrude_n, inner=None):
    """Layers: extrusion (down-right), outline, fill gradient, optional highlight."""
    px = scr.load()
    w, h = mask.size
    pad = outline_r + extrude_n + 1
    m = Image.new('L', (w + 2 * pad, h + 2 * pad), 0); m.paste(mask, (pad, pad))
    o = dilate(m, outline_r)
    ext = Image.new('L', m.size, 0)
    for k in range(1, extrude_n + 1):
        ext.paste(255, (0, 0), o.transform(o.size, Image.AFFINE, (1, 0, -k, 0, 1, -k)))
    mp, op, ep = m.load(), o.load(), ext.load()
    fy = [y for y in range(m.size[1]) if any(mp[x, y] for x in range(m.size[0]))]
    y0, y1 = min(fy), max(fy)
    for y in range(m.size[1]):
        for x in range(m.size[0]):
            X, Y = ox + x - pad, oy + y - pad
            if not (0 <= X < scr.size[0] and 0 <= Y < scr.size[1]):
                continue
            if mp[x, y]:
                t = (y - y0) / max(1, y1 - y0)
                px[X, Y] = fill_ramp[min(len(fill_ramp) - 1, int(t * len(fill_ramp)))]
                if inner and y > 0 and not mp[x, y - 1]:
                    px[X, Y] = inner            # 1px highlight along the top edges
            elif op[x, y]:
                px[X, Y] = outline
            elif ep[x, y]:
                px[X, Y] = extrude

def game_text(text):
    """Pixels of `text` in the game font: list of rows of 1 (ink) / 2 (shadow) / 0, right-to-left laid out."""
    sheet = Image.open(os.path.join(ROOT, 'graphics', 'fonts', 'latin_normal.png')).load()
    cm, wt = charmap(), width_table('normal')
    glyphs = []
    for tok in tokens(shape(text)):
        b = cm['chars'][tok]
        gid = 0x100 + b[1] if b[0] == 0xF9 else b[0]
        glyphs.append((gid, wt[gid]))
    total = sum(w for _, w in glyphs)
    rows = [[0] * total for _ in range(14)]
    x = total
    for gid, w in glyphs:                         # first character at the right
        x -= w
        cx, cy = (gid % 16) * 16, (gid // 16) * 16
        for y in range(14):
            for k in range(w):
                v = sheet[cx + k, cy + y]
                rows[y][x + k] = v if v in (1, 2) else 0
    return rows

def stamp(scr, rows, ox, oy, ink, shadow):
    px = scr.load()
    for y, row in enumerate(rows):
        for x, v in enumerate(row):
            if v:
                px[ox + x, oy + y] = ink if v == 1 else shadow

def build_logo(vanilla):
    src_png = os.path.join(vanilla, 'graphics/title_screen/firered/game_title_logo.png') if vanilla else backup(LOGO_PNG)
    src_bin = os.path.join(vanilla, 'graphics/title_screen/firered/game_title_logo.bin') if vanilla else backup(LOGO_BIN)
    if not vanilla:
        backup(LOGO_PAL)
    orig = decode(src_png, src_bin)
    pal = orig.getpalette()
    for i, c in FIRE.items():
        pal[3 * i:3 * i + 3] = c
    area = orig.crop((152, 48, 176, 62)); ap = area.load(); opal = orig.getpalette()
    white = [(x, y) for y in range(area.size[1]) for x in range(area.size[0])
             if ap[x, y] and sum(opal[3 * ap[x, y]:3 * ap[x, y] + 3]) > 700]
    xs, ys = [p[0] for p in white], [p[1] for p in white]
    tm = area.crop((min(xs) - 1, min(ys) - 1, max(xs) + 2, max(ys) + 2))   # keep the ™ mark, tightly
    scr = Image.new('P', orig.size, 0); scr.putpalette(pal)

    size = 20
    while text_mask(TITLE, size + 2, font_name=LOGO_FONT).size[0] <= 158 and size < 120:   # original logo width
        size += 2
    word = arc(text_mask(TITLE, size, font_name=LOGO_FONT), 6)
    if word.size[1] > 56:
        word = word.resize((word.size[0], 56), Image.NEAREST)
    wx = (176 - word.size[0]) // 2 + 2
    paint(scr, word, wx, 7, YELLOW, BLUE, 2, NAVY, 3, inner=37)
    tmask = Image.new('1', tm.size, 0)
    pal_rgb = lambda v: tuple(pal[3 * v:3 * v + 3])
    tmask.putdata([1 if v and (sum(pal_rgb(v)) < 60 or sum(pal_rgb(v)) > 700) else 0
                   for v in tm.get_flattened_data()])   # only the ™'s own black/white pixels
    scr.paste(tm, (max(0, wx - 14), 7 + word.size[1] - 6), tmask)   # ™ after the word = its left end

    ps = 14
    while text_mask(PLATE, ps + 2, font_name=PLATE_FONT).size[0] <= PLATE_MAX_W and ps < 80:
        ps += 2
    plate = text_mask(PLATE, ps, font_name=PLATE_FONT)
    if plate.size[1] > 28:
        plate = plate.resize((plate.size[0], 28), Image.NEAREST)
    px_ = PLATE_RIGHT - plate.size[0]
    paint(scr, plate, px_, 68, FIRE_RAMP, 86, 2, 85, 2, inner=87)
    n = encode(scr.crop((0, 0, 256, 160)), 32, 0, 256, LOGO_PNG, LOGO_BIN, pal)

    lines = open(LOGO_PAL).read().replace('\r\n', '\n').split('\n')
    for i, c in FIRE.items():
        lines[3 + i] = '%d %d %d' % c
    open(LOGO_PAL, 'w', newline='\r\n').write('\n'.join(lines))
    return n

def build_press_start(vanilla):
    src_png = os.path.join(vanilla, 'graphics/title_screen/copyright_press_start.png') if vanilla else backup(PS_PNG)
    src_bin = os.path.join(vanilla, 'graphics/title_screen/copyright_press_start.bin') if vanilla else backup(PS_BIN)
    scr = decode(src_png, src_bin)
    px = scr.load()
    for y in range(128, 160):                     # clear PRESS START row and the copyright rows
        for x in range(256):
            px[x, y] = 0
    press = game_text(PRESS)
    w = len(press[0])
    bx0, bx1 = 40, 40 + w + 12                    # black box, now 16px tall (rows 16-17)
    for y in range(128, 144):
        for x in range(bx0, bx1):
            px[x, y] = 6
    stamp(scr, press, bx0 + 6, 129, 5, 3)         # colours 1-5 blink, 6 stays
    for y in range(144, 160):                     # bottom strip: black line + dark red, 16px tall
        for x in range(256):
            px[x, y] = 6 if y < 146 else 12
    credit = game_text(CREDIT)
    stamp(scr, credit, (240 - len(credit[0])) // 2, 146, 10, 7)
    return encode(scr, 16, 15, 512, PS_PNG, PS_BIN, scr.getpalette())

if __name__ == '__main__':
    vanilla = sys.argv[sys.argv.index('--from-vanilla') + 1] if '--from-vanilla' in sys.argv else None
    if '--font' in sys.argv:                       # --font NAME  or  --font LOGO,PLATE
        f = sys.argv[sys.argv.index('--font') + 1].split(',')
        LOGO_FONT, PLATE_FONT = f[0], f[-1]
    print('logo tiles:', build_logo(vanilla), '/ 256')
    print('press start / credit tiles:', build_press_start(vanilla), '/ 512')
