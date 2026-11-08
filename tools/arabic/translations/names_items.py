# -*- coding: utf-8 -*-
"""Batch 09a - Item names (src/data/items.json, field "english").

Items Crystal also has use the Pokémon Crystal Arabic names
(tools/arabic/crystal_names), matched by English name. Gen 3 items, berries,
mail and FireRed's own key items are new, in the same style (Poké Balls
transliterated as «… بول», TMs/HMs as «ق.ت / ق.م»)."""
import json, os, re
from arabic_text import ROOT, measure, shape, tokens

FILE = 'src/data/items.json'
PX, MAX_BYTES = 98, 14   # bag list: name from x=8, quantity printed at x=110
_norm = lambda s: re.sub(r'[^A-Z0-9]', '', s.upper().replace('É', 'E').replace('é', 'E'))
_cr = {_norm(m['english']): m['arabic'] for m in json.load(open(os.path.join(os.path.dirname(__file__), '..', 'crystal_names',
       'crystal_arabic_names.json'), encoding='utf-8'))['items']}

_B = 'توتة '
NEW = {
 'SAFARI BALL':'سفاري بول','NET BALL':'نت بول','DIVE BALL':'دايف بول','NEST BALL':'نست بول','REPEAT BALL':'ريبيت بول',
 'TIMER BALL':'تايمر بول','LUXURY BALL':'لاكشري بول','PREMIER BALL':'بريمير بول','ELIXIR':'الإكسير','MAX ELIXIR':'الإكسير الأقصى',
 'LAVA COOKIE':'كعكة الحمم','BLUE FLUTE':'ناي أزرق','YELLOW FLUTE':'ناي أصفر','RED FLUTE':'ناي أحمر','BLACK FLUTE':'ناي أسود',
 'WHITE FLUTE':'ناي أبيض','SHOAL SALT':'ملح الشاطئ','SHOAL SHELL':'صدفة الشاطئ','RED SHARD':'شظية حمراء','BLUE SHARD':'شظية زرقاء',
 'YELLOW SHARD':'شظية صفراء','GREEN SHARD':'شظية خضراء','ZINC':'الزنك','PP MAX':'PP الأقصى','FLUFFY TAIL':'ذيل منفوش',
 'HEART SCALE':'حرشفة القلب','ORANGE MAIL':'بريد برتقالي','HARBOR MAIL':'بريد الميناء','GLITTER MAIL':'بريد لامع',
 'MECH MAIL':'بريد آلي','WOOD MAIL':'بريد خشبي','WAVE MAIL':'بريد الموج','BEAD MAIL':'بريد الخرز','SHADOW MAIL':'بريد الظل',
 'TROPIC MAIL':'بريد استوائي','DREAM MAIL':'بريد الحلم','FAB MAIL':'بريد فاخر','RETRO MAIL':'بريد قديم',
 'CHERI BERRY':_B+'شيري','CHESTO BERRY':_B+'تشستو','PECHA BERRY':_B+'بيتشا','RAWST BERRY':_B+'راوست','ASPEAR BERRY':_B+'أسبير',
 'LEPPA BERRY':_B+'ليبا','ORAN BERRY':_B+'أوران','PERSIM BERRY':_B+'بيرسيم','LUM BERRY':_B+'لوم','SITRUS BERRY':_B+'سيتروس',
 'FIGY BERRY':_B+'فيغي','WIKI BERRY':_B+'ويكي','MAGO BERRY':_B+'ماغو','AGUAV BERRY':_B+'أغواف','IAPAPA BERRY':_B+'إيابابا',
 'RAZZ BERRY':_B+'راز','BLUK BERRY':_B+'بلوك','NANAB BERRY':_B+'نانب','WEPEAR BERRY':_B+'ويبير','PINAP BERRY':_B+'بيناب',
 'POMEG BERRY':_B+'بوميغ','KELPSY BERRY':_B+'كيلبسي','QUALOT BERRY':_B+'كوالوت','HONDEW BERRY':_B+'هونديو','GREPA BERRY':_B+'غريبا',
 'TAMATO BERRY':_B+'تاماتو','CORNN BERRY':_B+'كورن','MAGOST BERRY':_B+'ماغوست','RABUTA BERRY':_B+'رابوتا','NOMEL BERRY':_B+'نوميل',
 'SPELON BERRY':_B+'سبيلون','PAMTRE BERRY':_B+'بامتري','WATMEL BERRY':_B+'واتميل','DURIN BERRY':_B+'دورين','BELUE BERRY':_B+'بيلو',
 'LIECHI BERRY':_B+'لايتشي','GANLON BERRY':_B+'غانلون','SALAC BERRY':_B+'سالاك','PETAYA BERRY':_B+'بيتايا','APICOT BERRY':_B+'أبيكوت',
 'LANSAT BERRY':_B+'لانسات','STARF BERRY':_B+'ستارف','ENIGMA BERRY':_B+'إنيغما',
 'WHITE HERB':'عشبة بيضاء','MACHO BRACE':'سوار القوة','SOOTHE BELL':'جرس السكينة','MENTAL HERB':'عشبة الذهن',
 'CHOICE BAND':'عصابة الاختيار','SOUL DEW':'ندى الروح','DEEPSEATOOTH':'ناب الأعماق','DEEPSEASCALE':'حرشفة الأعماق',
 'SILK SCARF':'وشاح حريري','SHELL BELL':'جرس الصدفة','SEA INCENSE':'بخور البحر','LAX INCENSE':'بخور مهدئ',
 'RED SCARF':'وشاح أحمر','BLUE SCARF':'وشاح أزرق','PINK SCARF':'وشاح وردي','GREEN SCARF':'وشاح أخضر','YELLOW SCARF':'وشاح أصفر',
 'MACH BIKE':'دراجة ماخ','CONTEST PASS':'تصريح المسابقة','WAILMER PAIL':'دلو ويلمر','DEVON GOODS':'بضائع ديفون',
 'SOOT SACK':'كيس الرماد','ACRO BIKE':'دراجة أكرو','{POKEBLOCK} CASE':'علبة {POKEBLOCK}','LETTER':'الرسالة',
 'EON TICKET':'تذكرة إيون','RED ORB':'الجوهرة الحمراء','BLUE ORB':'الجوهرة الزرقاء','SCANNER':'الماسح','GO-GOGGLES':'نظارة واقية',
 'METEORITE':'النيزك','RM. 1 KEY':'مفتاح الغرفة 1','RM. 2 KEY':'مفتاح الغرفة 2','RM. 4 KEY':'مفتاح الغرفة 4',
 'RM. 6 KEY':'مفتاح الغرفة 6','STORAGE KEY':'مفتاح المخزن','ROOT FOSSIL':'أحفورة الجذر','CLAW FOSSIL':'أحفورة المخلب',
 'DEVON SCOPE':'منظار ديفون','HM08':'ق.م 08','OAK\'S PARCEL':'طرد أوك','POKé FLUTE':'ناي البوكيمون','SECRET KEY':'المفتاح السري',
 'BIKE VOUCHER':'قسيمة الدراجة','GOLD TEETH':'أسنان ذهبية','OLD AMBER':'الكهرمان القديم','LIFT KEY':'مفتاح المصعد',
 'HELIX FOSSIL':'أحفورة الحلزون','DOME FOSSIL':'أحفورة القبة','SILPH SCOPE':'منظار سيلف','TOWN MAP':'خريطة البلدات',
 'VS SEEKER':'باحث النزالات','FAME CHECKER':'سجل المشاهير','TM CASE':'علبة الأقراص','BERRY POUCH':'جراب التوت',
 'TEACHY TV':'تلفاز التعليم','TRI-PASS':'التصريح الثلاثي','RAINBOW PASS':'تصريح الألوان','TEA':'الشاي',
 'MYSTICTICKET':'التذكرة الغامضة','AURORATICKET':'تذكرة الشفق','POWDER JAR':'جرة المسحوق','RUBY':'الياقوت','SAPPHIRE':'الزفير',
}

_items = json.load(open(os.path.join(os.path.dirname(__file__), 'names_items_en.json'), encoding='utf-8'))
ENTRIES, _missing = [], []
for item_id, en in _items:
    n = _norm(en)
    if n in _cr:
        ar, note = _cr[n], 'From Pokémon Crystal Arabic.'
    elif en in NEW:
        ar, note = NEW[en], 'New (not in Crystal).'
    else:
        if '?' not in en:
            _missing.append(en)
        continue
    ENTRIES.append(dict(id=item_id, json=item_id, json_field='english', file=FILE, screen='Item names', where=en.title(),
                        box=('line', PX, 'normal', 1), max_bytes=MAX_BYTES, ar=ar, note=note))
if _missing:
    print('names_items.py: no Arabic for', _missing)

README = [
    ('Pokémon FireRed – Arabic translation – Batch 09a: item names', 'title'),
    ('Every item that Crystal also has uses your Crystal Arabic name; the Gen 3 items, berries, mail and FireRed key items are new. '
     'Descriptions (the bag text) come in the next batch.', 'text'),
    ('Limits: 14 letters and 98 px in the bag list (the quantity starts at x=110); the Fit column checks both.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py names_items, then make.', 'text'),
]
GLOSSARY = [
    ('… BALL (Gen 3)', '… بول', 'As in Crystal: سفاري بول، نت بول، تايمر بول…'),
    ('… BERRY (Gen 3)', 'توتة …', 'توتة سيتروس، توتة أوران…'),
    ('TM / HM', 'ق.ت / ق.م', 'As in Crystal.'),
    ('… MAIL', 'بريد …', ''),
    ('… FLUTE', 'ناي …', ''),
    ('SAPPHIRE / RUBY', 'الزفير / الياقوت', '«الزفير» is the classical Arabic name of sapphire.'),
    ('VS SEEKER', 'باحث النزالات', ''),
    ('FAME CHECKER', 'سجل المشاهير', ''),
]
