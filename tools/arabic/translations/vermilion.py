# -*- coding: utf-8 -*-
"""Batch 18 - Routes 5-6 (Day Care, gates), Vermilion City (Lt. Surge's gym, the
Pokémon Fan Club, houses) and every cabin of the S.S. Anne. Spacetoon-dub voice;
lines addressed to the player are gendered."""
import importlib, json, os
from mtmoon import DIALOG
_en = {l: (m, t) for m, l, t in json.load(open(os.path.join(os.path.dirname(__file__), 'vermilion_en.json'), encoding='utf-8'))}
A = {}
for n in (1, 2, 3, 4):
    try:
        A.update(getattr(importlib.import_module('vermilion_p%d' % n), 'P%d' % n))
    except ImportError:
        pass
ENTRIES = []
for label, ar in A.items():
    m, en = _en[label]
    ENTRIES.append(dict(id=label, file='data/maps/%s/text.inc' % m, screen=m.replace('_', ' '), where=label.split('_Text_')[-1],
                        box=DIALOG, ar=ar, note=''))
README = [
    ('Pokémon FireRed – Arabic translation – Batch 18: Routes 5-6, Vermilion City, S.S. Anne', 'title'),
    ("Routes 5 and 6 with the Day Care and the gates, Vermilion City with Lt. Surge's gym and the Pokémon Fan Club, "
     'and every cabin of the S.S. Anne, in the Spacetoon-dub voice.', 'text'),
    ('Lines addressed to the player use [[masculine|feminine]].', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py vermilion, then make.', 'text'),
]
GLOSSARY = [('LT. SURGE', 'الملازم سيرج', ''), ('THUNDERBADGE', 'وسام الرعد', ''), ('DAY-CARE', 'دار الرعاية', ''),
            ('S.S. ANNE', 'باخرة إس إس آن', 'From the map names.')]
