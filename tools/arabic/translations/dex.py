# -*- coding: utf-8 -*-
"""Batch 14 - Pokédex entries (src/data/pokemon/pokedex_text_fr.h) and categories
(src/data/pokemon/pokedex_entries.h). Epic, adventurous tone; facts kept; metric
units; one flowing paragraph per entry (commas, a full stop only at the end).
The screen shows «بوكيمون» + category («بوكيمون البذرة»)."""
import json, os, importlib
HERE = os.path.dirname(__file__)
_rows = json.load(open(os.path.join(HERE, 'dex_en.json'), encoding='utf-8'))   # [key, category, species, english]
D, CAT = {}, {}
for n in range(1, 7):
    try:
        m = importlib.import_module('dex_data%d' % n)
    except ImportError:
        continue
    D.update(getattr(m, 'D%d' % n)); CAT.update(getattr(m, 'CAT%d' % n))
DESC = ('static', 232, 'normal', 3)
ENTRIES, _seen_cat = [], {}
for key, cat, sp, en in _rows:
    if sp in D:
        ENTRIES.append(dict(id='g%sPokedexText' % sp, file='src/data/pokemon/pokedex_text_fr.h', screen='Pokédex entries',
                            where=sp, box=DESC, ar=D[sp], no_mid_stop=True, note=''))
    if cat in CAT:
        ENTRIES.append(dict(id=key + '_CATEGORY', key=key, file='src/data/pokemon/pokedex_entries.h',
                            pattern=r'\[%s\]\s*=\s*\{\s*\.categoryName = _\("(.*?)"\)', screen='Categories',
                            where='%s (%s)' % (sp, cat.title()), box=('line', 80, 'small', 1), max_bytes=11, ar=CAT[cat],
                            note='Shown as «بوكيمون %s».' % CAT[cat]))
ENTRIES.append(dict(id='gText_PokedexPokemon', file='src/strings.c', screen='Categories', where='Word before the category',
                    box=('line', 60, 'small', 1), ar='بوكيمون ', note='Keep the trailing space: «بوكيمون البذرة».'))

README = [
    ('Pokémon FireRed – Arabic translation – Batch 14: Pokédex entries', 'title'),
    ('All 386 entries and their categories, with an epic, adventurous voice: the facts stay, the telling gets drama '
     '(«…», «يقال إن…», a strong last line). Units are metric.', 'text'),
    ('Each entry is ONE paragraph: commas between sentences, a full stop or ! only at the very end (the Fit column flags '
     'a full stop in the middle). 3 lines of 232 px. Categories: 11 letters at most («ال» counts as one).', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py dex, then make.', 'text'),
]
GLOSSARY = [('X POKéMON (category)', 'بوكيمون X', '«بوكيمون البذرة»'), ('feet / pounds / miles / inches', 'متر / كيلوغرام / كيلومتر / سنتيمتر', 'Converted.'),
            ('PIG MONKEY', 'القرد الغاضب', 'No pig.'), ('bewitching', 'آسر', 'No magic.')]
