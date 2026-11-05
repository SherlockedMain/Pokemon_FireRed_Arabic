# -*- coding: utf-8 -*-
"""Batch 12 - Move descriptions (src/move_descriptions.c), shown on the summary
moves page and for TMs/HMs in the bag: up to 4 lines of 112 px."""
from movedesc_data1 import D1
from movedesc_data2 import D2
FILE = 'src/move_descriptions.c'
BOX = ('static', 112, 'normal', 4)
D = dict(D1); D.update(D2)
ENTRIES = [dict(id='gMoveDescription_' + k, file=FILE, screen='Move descriptions', where=k, box=BOX, ar=v, note='')
           for k, v in D.items()]
README = [
    ('Pokémon FireRed – Arabic translation – Batch 12: move descriptions', 'title'),
    ('The text of every move on the summary moves page and for TMs/HMs in the bag. Up to 4 lines of 112 px '
     '(about 15 letters a line): short, clear sentences about what the move does.', 'text'),
    ('Shared endings: «قد يحرق / يشل / يجمّد / يسمم / يحيّر الخصم.», «قد يجعل الخصم يجفل.», «فرص الضربة الحاسمة فيه عالية.»', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py movedesc, then make.', 'text'),
]
GLOSSARY = [('burn / paralyze / freeze / poison / confuse', 'يحرق / يشل / يجمّد / يسمم / يحيّر', ''),
            ('flinch', 'يجفل', ''), ('high critical-hit ratio', 'فرص الضربة الحاسمة فيه عالية', ''),
            ('one-hit KO', 'يُسقط الخصم بضربة واحدة', ''), ('2-5 times', 'من 2 إلى 5 مرات', '')]
