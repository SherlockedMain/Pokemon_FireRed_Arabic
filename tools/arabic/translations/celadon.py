# -*- coding: utf-8 -*-
"""Batch 20 - Celadon City (department store, condominiums, Game Corner, Erika's gym,
restaurant, hotel), the Rocket Hideout, Routes 7 and 8. Spacetoon-dub voice; lines to
the player gendered."""
import importlib, json, os
from mtmoon import DIALOG
_en = {l: (m, t) for m, l, t in json.load(open(os.path.join(os.path.dirname(__file__), 'celadon_en.json'), encoding='utf-8'))}
A = {}
for n in (1, 2, 3, 4, 5):
    try:
        A.update(getattr(importlib.import_module('celadon_p%d' % n), 'P%d' % n))
    except ImportError:
        pass
ENTRIES = []
for label, ar in A.items():
    m, en = _en[label]
    ENTRIES.append(dict(id=label, file='data/maps/%s/text.inc' % m, screen=m.replace('_', ' '), where=label.split('_Text_')[-1],
                        box=DIALOG, ar=ar, note=''))
README = [
    ('Pokémon FireRed – Arabic translation – Batch 20: Celadon City, Rocket Hideout', 'title'),
    ("Celadon City with its department store, condominiums, Game Corner, Erika's gym, restaurant and hotel, "
     'the Rocket Hideout under the Game Corner, and Routes 7 and 8, in the Spacetoon-dub voice.', 'text'),
    ('Lines addressed to the player use [[masculine|feminine]].', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py celadon, then make.', 'text'),
]
GLOSSARY = [('ERIKA', 'إيريكا', ''), ('RAINBOWBADGE', 'وسام قوس قزح', ''), ('GAME CORNER', 'صالة الألعاب', ''),
            ('COINS', 'القطع', 'Game Corner coins.'), ('ROCKET HIDEOUT', 'مخبأ روكيت', ''), ('GIOVANNI', 'جيوفاني', '')]
