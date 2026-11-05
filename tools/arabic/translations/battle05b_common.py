# -*- coding: utf-8 -*-
"""Shared helpers for batch 05b: placeholder shorthands and move names taken
from batch 08 (your Crystal names), so messages always match the move menu."""
import names_moves
A, D, E_, S = '{B_ATK_NAME_WITH_PREFIX}', '{B_DEF_NAME_WITH_PREFIX}', '{B_EFF_NAME_WITH_PREFIX}', '{B_SCR_ACTIVE_NAME_WITH_PREFIX}'
AB_S, AB_D, AB_A = '{B_SCR_ACTIVE_ABILITY}', '{B_DEF_ABILITY}', '{B_ATK_ABILITY}'
P = '{B_PLAYER_NAME}'
_MV = {e['id']: e['ar'] for e in names_moves.ENTRIES}
def MV(name):
    return _MV['MOVE_' + name]
def G(m, f):
    return '[[%s|%s]]' % (m, f)
