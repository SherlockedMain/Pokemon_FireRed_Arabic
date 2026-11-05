# -*- coding: utf-8 -*-
"""Batch 11 - Map names (src/data/region_map/region_map_sections.json, "name";
"name_en" keeps the English, used for the C symbol names and to match rows):
the map-name popup, the region map, the summary memo ("Met in…") and anywhere
{STR_VAR} inserts a place. One Arabic name per English name; every map section
that shares it gets it. Budget 108 px (popup 14 tiles, centred)."""
import json, os
from arabic_text import ROOT

FILE = 'src/data/region_map/region_map_sections.json'
BOX = ('line', 108, 'normal', 1)
ORD = ['الأولى', 'الثانية', 'الثالثة', 'الرابعة', 'الخامسة', 'السادسة', 'السابعة']
AR = {
 'PALLET TOWN':'بلدة باليت','VIRIDIAN CITY':'مدينة فيريديان','PEWTER CITY':'مدينة بيوتر','CERULEAN CITY':'مدينة سيرولين',
 'LAVENDER TOWN':'بلدة لافندر','VERMILION CITY':'مدينة فيرمليون','CELADON CITY':'مدينة سيلادون','FUCHSIA CITY':'مدينة فوشيا',
 'CINNABAR ISLAND':'جزيرة سينابار','INDIGO PLATEAU':'هضبة إنديغو','SAFFRON CITY':'مدينة سافرون',
 'VIRIDIAN FOREST':'غابة فيريديان','MT. MOON':'جبل القمر','S.S. ANNE':'باخرة إس إس آن','UNDERGROUND PATH':'الممر السفلي',
 'DIGLETT\'S CAVE':'كهف ديغليت','VICTORY ROAD':'طريق النصر','ROCKET HIDEOUT':'مخبأ الصاروخ','SILPH CO.':'شركة سيلف',
 'POKéMON MANSION':'قصر البوكيمون','SAFARI ZONE':'منطقة السفاري','POKéMON LEAGUE':'دوري البوكيمون','ROCK TUNNEL':'نفق الصخور',
 'SEAFOAM ISLANDS':'جزر الزبد','POKéMON TOWER':'برج البوكيمون','CERULEAN CAVE':'كهف سيرولين','POWER PLANT':'محطة الكهرباء',
 'KINDLE ROAD':'طريق الجمر','TREASURE BEACH':'شاطئ الكنز','CAPE BRINK':'رأس الحافة','BOND BRIDGE':'جسر الرباط',
 'THREE ISLE PORT':'ميناء الجزيرة 3','RESORT GORGEOUS':'المنتجع الفاخر','WATER LABYRINTH':'متاهة الماء',
 'FIVE ISLE MEADOW':'مرج الجزيرة 5','MEMORIAL PILLAR':'عمود الذكرى','OUTCAST ISLAND':'الجزيرة المنبوذة',
 'GREEN PATH':'الممر الأخضر','WATER PATH':'الممر المائي','RUIN VALLEY':'وادي الأطلال','TRAINER TOWER':'برج المدربين',
 'CANYON ENTRANCE':'مدخل الوادي','SEVAULT CANYON':'وادي سيفولت','TANOBY RUINS':'أطلال تانوبي','NAVEL ROCK':'صخرة نافل',
 'MT. EMBER':'جبل الجمر','BERRY FOREST':'غابة التوت','ICEFALL CAVE':'كهف الجليد','ROCKET WAREHOUSE':'مستودع الصاروخ',
 'DOTTED HOLE':'الحفرة المنقطة','LOST CAVE':'الكهف المفقود','PATTERN BUSH':'الأيكة المنقوشة','ALTERING CAVE':'كهف التحول',
 'TANOBY CHAMBERS':'حجرات تانوبي','THREE ISLE PATH':'ممر الجزيرة 3','TANOBY KEY':'مفتاح تانوبي','BIRTH ISLAND':'جزيرة الميلاد',
 'MONEAN CHAMBER':'حجرة مونين','LIPTOO CHAMBER':'حجرة ليبتو','WEEPTH CHAMBER':'حجرة ويبث','DILFORD CHAMBER':'حجرة ديلفورد',
 'SCUFIB CHAMBER':'حجرة سكوفيب','RIXY CHAMBER':'حجرة ريكسي','VIAPOIS CHAMBER':'حجرة فيابويس','EMBER SPA':'منتجع الجمر',
 'CELADON DEPT.':'متجر سيلادون',
}
for i, n in enumerate(['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN']):
    AR[n + ' ISLAND'] = 'الجزيرة ' + ORD[i]
for n in range(1, 26):
    AR['ROUTE %d' % n] = 'الطريق %d' % n
for n in (6, 7, 8, 9, 22, 23, 24):
    AR['SEVII ISLE %d' % n] = 'جزيرة سيفي %d' % n

_secs = json.load(open(os.path.join(os.path.dirname(__file__), 'names_maps_en.json'), encoding='utf-8'))
ENTRIES, _seen, _missing = [], set(), []
for sid, en in _secs:
    if en in _seen:
        continue
    _seen.add(en)
    if en not in AR:
        _missing.append(en)
        continue
    ENTRIES.append(dict(id=sid, json=en, json_key='name_en', json_list='map_sections', json_field='name', file=FILE,
                        screen='Map names', where=en.title(), box=BOX, ar=AR[en], note=''))
if _missing:
    print('names_maps.py: no Arabic for', _missing)

README = [
    ('Pokémon FireRed – Arabic translation – Batch 11: map names', 'title'),
    ('Every place name: the popup when you enter a map, the region map, the summary memo and dialogue inserts. '
     'Sections that share an English name share the Arabic one.', 'text'),
    ('Limit: 108 px (the popup box is 14 tiles and centres the name).', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py names_maps, then make.', 'text'),
]
GLOSSARY = [
    ('… TOWN / … CITY', 'بلدة … / مدينة …', 'As in the dialogue.'),
    ('ROUTE n', 'الطريق n', ''), ('ONE … SEVEN ISLAND', 'الجزيرة الأولى … السابعة', ''),
    ('… ISLE (Sevii)', 'جزيرة سيفي n / الجزيرة n', 'Digits where space is short (ميناء الجزيرة 3).'),
    ('ROCKET HIDEOUT / WAREHOUSE', 'مخبأ / مستودع الصاروخ', 'TEAM ROCKET = فريق الصاروخ.'),
    ('SEAFOAM ISLANDS', 'جزر الزبد', ''), ('MT. EMBER', 'جبل الجمر', ''),
]
