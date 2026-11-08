# -*- coding: utf-8 -*-
"""Batch 05b - Battle text, the rest: abilities and held items at work,
weather, multi-turn and special moves, double and link battles, Safari Zone,
disobedience, evolution. Move names inside messages come from batch 08."""
from battle import B, BATTLE, PROMPT, WORD
from battle05b_data1 import D1
from battle05b_data2 import D2
from battle05b_data3 import D3

SHORT = ('line', 120, 'normal', 1)
_box = {k: WORD for k in ('AllyPkmnPrefix', 'AllyPkmnPrefix2', 'AllyPkmnPrefix3', 'gText_Sleep', 'gText_Poison', 'gText_Burn',
                          'gText_Paralysis', 'gText_Ice', 'gText_Confusion', 'gText_Love', 'gText_Win', 'gText_Loss',
                          'gText_Draw', 'gText_BadEgg', 'gText_HighlightRed_Left', 'EnigmaBerry')}
_box_bad_egg = ('line', 80, 'normal', 1)
_box.update({k: SHORT for k in ('gText_SafariBalls', 'gText_TimeBoard', 'gText_ClearTime', 'gText_XMinYZSec', 'gText_LinkStandby')})
_box['gText_WhatWillOldManDo'] = PROMPT
_box['EnigmaBerry'] = ('line', 98, 'normal', 1)
_box['gText_BadEgg'] = ('line', 80, 'normal', 1)        # party name slot          # an item name: bag-list budget
_box['gText_XMinYZSec'] = ('line', 240, 'normal', 1)       # {STR_VAR_n} are 2-digit numbers here

_ALL = {}
for d in (D1, D2, D3):
    _ALL.update(d)
ENTRIES = []
for k, v in _ALL.items():
    label = k if k.startswith(('gText_', 'gBattleText_')) else 'sText_' + k
    box = _box.get(k, BATTLE)
    if k.startswith('gText_A') and k.endswith('Move'):
        box = ('line', 130, 'normal', 1)
    e = B(label, k, v, box=box)
    if e:
        ENTRIES.append(e)
_ghost = B('sText_TheGhostWas', 'Pokémon Tower ghost revealed', 'كان الشبح ماروك!', suffix='\\p\\n')
if _ghost:
    ENTRIES.append(_ghost)
for k in ('gText_BattleYesNoChoice',):
    e = B(k, 'Battle YES/NO', 'نعم\nلا', box=('manual', 40, 'normal', 2))
    if e: ENTRIES.append(e)
e = B('gText_BattleSwitchWhich', 'Switch which?', 'تبديل\nأي واحد؟', box=('manual', 56, 'normal', 2))
if e: ENTRIES.append(e)

README = [
    ('Pokémon FireRed – Arabic translation – Batch 05b: battle text, the rest', 'title'),
    ('Abilities and held items at work, weather, multi-turn and special moves, double and link battles, the Safari Zone, '
     'disobedience and evolution. Move names inside messages are the batch 08 names, so they match the move menu.', 'text'),
    ('{B_ATK_PREFIX1/2/3} become «فريقك» or «الخصم». Verbs with the player as subject are gendered with [[m|f]].', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py battle05b, then make.', 'text'),
    ('Not translated (unused in FireRed): Japanese leftovers, Pokéblock and Wally lines, Battle Tower floor labels; the '
     'level-up window stat labels stay Latin until the HUD/graphics pass.', 'text'),
]
GLOSSARY = [
    ('Ally / Foe (prefix)', 'فريقك / الخصم', ''), ("X's ABILITY did Y", 'فعلت ABILITY لدى X…', 'Verb first, «لدى» for the owner.'),
    ('fell in love / infatuated', 'افتُتن', 'Not «وقع في الحب».'), ('flinched', 'أجفل', ''),
    ('rain / downpour / sandstorm / hail', 'المطر / الوابل الغزير / العاصفة الرملية / البرد', ''),
    ('POKé DUDE', 'خبير البوكيمون', ''), ('evolved into', 'تطور إلى', ''),
]
