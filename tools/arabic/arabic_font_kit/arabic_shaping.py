"""Arabic shaping for the 8x16 pixel font (from the Mega Man BN1 Arabic translation).

shape_line(text) -> list of glyph keys ("U+FE8D", ...) in DRAW ORDER: index 0 is
the right-most glyph on screen, so an RTL text engine draws them right to left.
Each key is a key of glyph_map.json. Spaces come back as " ", digits and Latin
as the plain character (draw those with the game's own font).

Needs:  pip install arabic-reshaper python-bidi
"""
import re
import arabic_reshaper
from bidi.algorithm import get_display

_MIDWORD_ALEF = re.compile("(?<=[ء-يﹰ-ﻼ])[ﺁﺃﺇﺍ]")
_ARTICLE = re.compile("(?<![ء-يﹰ-ﻼ-])ﺍﻟ")


def shape_line(text: str):
    # no glyphs for tatweel or vowel marks
    text = re.sub("[ـً-ْٰ]", "", text)
    shaped = arabic_reshaper.reshape(text).replace("ﷲ", "ﺍﻟﻠﻪ")
    visual = get_display(shaped, base_dir="R")
    store = visual[::-1]  # reading order = draw order for an RTL engine
    # alef that follows a non-joining letter inside a word: glyph drawn at the
    # right of its cell so the gap to the previous letter stays small
    store = _MIDWORD_ALEF.sub(lambda m: chr(ord(m.group(0)) - 0xFE81 + 0xE081), store)
    store = store.replace("", "")  # two alefs in one cell
    store = _ARTICLE.sub("", store)            # word-initial ال in one cell
    out = []
    for ch in store:
        o = ord(ch)
        if 0xFE80 <= o <= 0xFEFC or 0xE000 <= o <= 0xE0FF or ch in "،؛؟":
            out.append(f"U+{o:04X}")
        else:
            out.append(ch)
    return out


if __name__ == "__main__":
    print(shape_line("مرحبا يا مدرب! هل أنت مستعد؟"))
