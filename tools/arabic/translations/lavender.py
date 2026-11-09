# -*- coding: utf-8 -*-
"""Batch 19 - Diglett's Cave, Route 11, Routes 9-10, Rock Tunnel, Lavender Town
and the Pokémon Tower. Spacetoon-dub voice; lines to the player gendered. Death and
ghosts keep their weight without religious claims (memorial = «مراسم التأبين»,
"possessed" = «لم أكن في وعيي»)."""
import importlib, json, os
from mtmoon import DIALOG
_en = {l: (m, t) for m, l, t in json.load(open(os.path.join(os.path.dirname(__file__), 'lavender_en.json'), encoding='utf-8'))}
A = {}
for n in (1, 2, 3, 4):
    try:
        A.update(getattr(importlib.import_module('lavender_p%d' % n), 'P%d' % n))
    except ImportError:
        pass
ENTRIES = []
for label, ar in A.items():
    m, en = _en[label]
    ENTRIES.append(dict(id=label, file='data/maps/%s/text.inc' % m, screen=m.replace('_', ' '), where=label.split('_Text_')[-1],
                        box=DIALOG, ar=ar, note=''))
README = [
    ('Pokémon FireRed – Arabic translation – Batch 19: Rock Tunnel, Lavender Town, Pokémon Tower', 'title'),
    ("Diglett's Cave, Route 11, Routes 9 and 10, Rock Tunnel, Lavender Town and every floor of the Pokémon Tower, "
     'in the Spacetoon-dub voice. Mourning and ghosts keep their weight, without religious claims.', 'text'),
    ('Lines addressed to the player use [[masculine|feminine]].', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py lavender, then make.', 'text'),
]
GLOSSARY = [('MR. FUJI', 'السيد فوجي', ''), ('NAME RATER', 'مقيّم الأسماء', ''), ('memorial services', 'مراسم التأبين', ''),
            ('possessed', 'لم أكن في وعيي', 'No religious possession.'), ('CHANNELER', 'ناسكة', 'Trainer class, batch 07.')]
