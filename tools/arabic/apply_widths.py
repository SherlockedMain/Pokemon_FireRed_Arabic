#!/usr/bin/env python3
"""Write Arabic glyph widths (from arabic_widths.json) into the width tables in src/text.c."""
import json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TABLES = {'normal': ['sFontNormalLatinGlyphWidths', 'sFontNormalCopy1LatinGlyphWidths',
                     'sFontMaleLatinGlyphWidths', 'sFontFemaleLatinGlyphWidths'],
          'small': ['sFontSmallLatinGlyphWidths']}
data = json.load(open(os.path.join(os.path.dirname(__file__), 'arabic_widths.json')))
path = os.path.join(ROOT, 'src', 'text.c')
src = open(path).read()
for font, tables in TABLES.items():
    widths = {int(k): v for k, v in data[font].items()}
    for t in tables:
        m = re.search(t + r'\[\]\s*=\s*\{(.*?)\};', src, re.S)
        vals = [int(v) for v in re.findall(r'\d+', m.group(1))]
        for gid, w in widths.items():
            vals[gid] = w
        rows = ['    ' + ', '.join('%2d' % v for v in vals[i:i + 16]) + ',' for i in range(0, len(vals), 16)]
        src = src[:m.start(1)] + '\n' + '\n'.join(rows) + '\n' + src[m.end(1):]
open(path, 'w').write(src)
print('widths written for', ', '.join(TABLES))
