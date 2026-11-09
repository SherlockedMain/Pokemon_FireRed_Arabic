# -*- coding: utf-8 -*-
# Shared helpers for batch 18: names from earlier batches.
from mtmoon import G, MV, SP, IT
import names_maps
_maps = {e.get('where', '').upper(): e['ar'] for e in names_maps.ENTRIES}
def PLACE(en):
    return next(v for k, v in _maps.items() if k.startswith(en.upper()))
VER, SAF, CER = PLACE('VERMILION CITY'), PLACE('SAFFRON CITY'), PLACE('CERULEAN CITY')
ANNE = next(v for k, v in _maps.items() if 'ANNE' in k)
