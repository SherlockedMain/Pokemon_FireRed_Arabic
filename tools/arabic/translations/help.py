# -*- coding: utf-8 -*-
"""Batch 15 - The L/R help system (data/text/help_system.inc): every question,
answer, how-to topic and glossary term not done in batch 01. Questions are in
the player's voice (gender-neutral); answers address the player like the other
system texts."""
import importlib, json, os, re
HERE = os.path.dirname(__file__)
FILE = 'data/text/help_system.inc'
_en = dict(json.load(open(os.path.join(HERE, 'help_en.json'), encoding='utf-8')))
H = {}
for n in range(1, 6):
    try:
        m = importlib.import_module('help_data%d' % n)
    except ImportError:
        continue
    H.update(getattr(m, 'H%d' % n))
ENTRIES = []
for key, ar in H.items():
    label = 'Help_Text_' + key
    en = _en.get(label, '')
    lines = en.count('\\n') + en.count('\\l') + 1
    if '\n\n' in ar:                               # type matchup tables: rows separated by \\p
        box = ('help', 204, 'normal', 8)
    elif '\n' in ar:                                 # written line by line (numbered steps)
        box = ('steps', 204, 'normal', max(lines, 6))
    elif len(ar) < 48 and lines == 1:
        box = ('line', 196, 'normal', 1)
    else:
        box = ('help', 204, 'normal', max(6, lines))
    ENTRIES.append(dict(id=label, file=FILE, screen='Help system', where=key, box=box, ar=ar, note=''))

README = [
    ('Pokémon FireRed – Arabic translation – Batch 15: the L/R help system', 'title'),
    ('Every help question, answer, how-to topic and glossary term (batch 01 did the greeting and the menu).', 'text'),
    ('Answers wrap automatically in the help window (204 px); they may use as many lines as the English did.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py help, then make.', 'text'),
]
GLOSSARY = [('HIDDEN move / HM', 'الحركة الخاصة / القرص الخاص', ''), ('TM', 'القرص التقني', ''), ('vitality', 'الحيوية', ''),
            ('status problem', 'الحالة السيئة', ''), ('Control Pad', 'لوحة الاتجاهات', '')]
