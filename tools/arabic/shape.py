#!/usr/bin/env python3
"""Shape Arabic for FireRed's RTL renderer (font kit glyph set).

Same rules as the BN1 build (arabic_font_kit/source/arabic_bn1.py), except the
text stays in LOGICAL order: no python-bidi, no reversal. FireRed's renderer
mirrors the line and keeps digit/Latin runs left-to-right by itself.

Usage: python3 shape.py "نص عربي"     (or import shape())
"""
import re, sys
import arabic_reshaper

_MIDWORD_ALEF = re.compile("(?<=[\u0621-\u064A\uFE70-\uFEFC])[\uFE81\uFE83\uFE87\uFE8D]")
_ARTICLE = re.compile("(?<![\u0621-\u064A\uFE70-\uFEFC\uE000-\uE0FF])\uFE8D\uFEDF")

def shape(text):
    text = re.sub("[\u0640\u064B-\u0652\u0670]", "", text)          # no tatweel / harakat glyphs
    s = arabic_reshaper.reshape(text)
    s = s.replace("\uFDF2", "\uFE8D\uFEDF\uFEE0\uFEEA")              # spell out the Allah ligature
    s = _MIDWORD_ALEF.sub(lambda m: chr(ord(m.group(0)) - 0xFE81 + 0xE081), s)
    s = s.replace("\uE08D\uE08D", "\uE090")                           # pack alef runs two per cell
    return _ARTICLE.sub("\uE0A0", s)                                   # word-initial ال in one cell

if __name__ == '__main__':
    print(shape(' '.join(sys.argv[1:])))
