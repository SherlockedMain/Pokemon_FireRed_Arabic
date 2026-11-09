# -*- coding: utf-8 -*-
"""Batch 17 - Cerulean City (the city, houses, bike shop, Misty's gym), Route 24
(the Nugget Bridge), Route 25 and Bill's Sea Cottage. Same Spacetoon-dub voice as
batch 16; lines addressed to the player are gendered."""
import importlib, json, os
from mtmoon import DIALOG, SIGN
_en = {l: (m, t) for m, l, t in json.load(open(os.path.join(os.path.dirname(__file__), 'cerulean_en.json'), encoding='utf-8'))}
_SIGNS = {'CeruleanCity_Text_CitySign', 'CeruleanCity_Text_BikeShopSign', 'Route24_Text_RouteSign' if False else '', 'Route25_Text_RouteSign' if False else ''}
A = {}
for n in (1, 2, 3):
    try:
        A.update(getattr(importlib.import_module('cerulean_p%d' % n), 'P%d' % n))
    except ImportError:
        pass
ENTRIES = []
for label, ar in A.items():
    m, en = _en[label]
    box = SIGN if label in _SIGNS else DIALOG
    ENTRIES.append(dict(id=label, file='data/maps/%s/text.inc' % m, screen=m.replace('_', ' '), where=label.split('_Text_')[-1],
                        box=box, ar=ar, note=''))
README = [
    ('Pokémon FireRed – Arabic translation – Batch 17: Cerulean City, Routes 24-25, Bill', 'title'),
    ('Cerulean City with its houses, bike shop and Misty\'s gym, the Nugget Bridge (Route 24), Route 25 and Bill\'s Sea '
     'Cottage, in the Spacetoon-dub voice. MISTY = «ميستي»; TEAM ROCKET = «عصابة روكيت».', 'text'),
    ('Lines addressed to the player use [[masculine|feminine]].', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py cerulean, then make.', 'text'),
]
GLOSSARY = [('MISTY', 'ميستي', ''), ('The Tomboyish Mermaid!', 'حورية البحر الشقية!', ''), ('CASCADEBADGE', 'وسام الشلال', ''),
            ('GRUNT (Team Rocket)', 'المجرم', ''), ('BILL', 'بيل', ''), ('Smell ya later!', 'أراك لاحقا… إن لحقت بي!', '')]
