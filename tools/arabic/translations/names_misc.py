# -*- coding: utf-8 -*-
"""Batch 07 - Types (from the Crystal Arabic translation), abilities (names and
summary-screen descriptions) and trainer classes. Width budgets come from the
windows each table is printed in (see BUDGET)."""

TYPES_FILE, AB_FILE, CL_FILE = 'src/battle_main.c', 'src/data/text/abilities.h', 'src/data/text/trainer_class_names.h'
BUDGET = dict(type=60, ability=110, desc=220, cls=100)  # px, normal font: move-type box 64 px; summary ability window 232 px
                                                       # (name at x=66, description at x=2); class + trainer name share a 216 px battle line

TYPES = {  # Pokémon Crystal Arabic v1.0.2
 'NORMAL':'عادي','FIGHTING':'مقاتل','FLYING':'طائر','POISON':'سام','GROUND':'أرضي','ROCK':'صخري','BUG':'حشري',
 'GHOST':'شبحي','STEEL':'فولاذي','MYSTERY':'غامض','FIRE':'ناري','WATER':'مائي','GRASS':'عشبي','ELECTRIC':'كهربي',
 'PSYCHIC':'نفسي','ICE':'جليدي','DRAGON':'تنيني','DARK':'ظلامي'}

ABILITIES = {  # name, description
 'NONE':('-------','لا توجد قدرة خاصة.'),
 'STENCH':('رائحة كريهة','تبعد البوكيمون البرية.'),
 'DRIZZLE':('رذاذ','تستدعي المطر في النزال.'),
 'SPEED_BOOST':('تسارع','ترفع السرعة تدريجيا.'),
 'BATTLE_ARMOR':('درع قتالي','تمنع الضربات الحاسمة.'),
 'STURDY':('صمود','تصد ضربة الإسقاط الواحدة.'),
 'DAMP':('رطوبة','تمنع التدمير الذاتي.'),
 'LIMBER':('ليونة','تمنع الشلل.'),
 'SAND_VEIL':('ستار الرمل','مراوغة أعلى في عاصفة الرمل.'),
 'STATIC':('كهرباء ساكنة','تشل من يلمسها.'),
 'VOLT_ABSORB':('شحن ذاتي','تحول الكهرباء إلى HP.'),
 'WATER_ABSORB':('امتصاص الماء','تحول الماء إلى HP.'),
 'OBLIVIOUS':('غفلة','تمنع الافتتان.'),
 'CLOUD_NINE':('صفاء الجو','تلغي آثار الطقس.'),
 'COMPOUND_EYES':('عيون مركبة','ترفع الدقة.'),
 'INSOMNIA':('أرق','تمنع النوم.'),
 'COLOR_CHANGE':('تبدل اللون','يأخذ نوع حركة الخصم.'),
 'IMMUNITY':('مناعة','تمنع التسمم.'),
 'FLASH_FIRE':('وهج النار','تقويه النار إن أصابته.'),
 'SHIELD_DUST':('غبار واق','تمنع الآثار الإضافية.'),
 'OWN_TEMPO':('إيقاع خاص','تمنع الحيرة.'),
 'SUCTION_CUPS':('ممصات','تثبت الجسم في مكانه.'),
 'INTIMIDATE':('ترهيب','تخفض هجوم الخصم.'),
 'SHADOW_TAG':('فخ الظل','تمنع الخصم من الهرب.'),
 'ROUGH_SKIN':('جلد خشن','تؤذي من يلمسها.'),
 'WONDER_GUARD':('حارس عجيب','لا تؤذيه إلا الضربة الفعالة.'),
 'LEVITATE':('تحليق','لا تصيبه حركات الأرض.'),
 'EFFECT_SPORE':('أبواغ مؤثرة','تنثر الأبواغ عند اللمس.'),
 'SYNCHRONIZE':('تزامن','تنقل حالته السيئة للخصم.'),
 'CLEAR_BODY':('جسم نقي','تمنع خفض القدرات.'),
 'NATURAL_CURE':('شفاء طبيعي','يشفى حين يُبدَّل.'),
 'LIGHTNING_ROD':('مانعة صواعق','تجذب الحركات الكهربية.'),
 'SERENE_GRACE':('نعمة الهدوء','تزيد فرص الآثار الإضافية.'),
 'SWIFT_SWIM':('سباحة سريعة','ترفع السرعة تحت المطر.'),
 'CHLOROPHYLL':('يخضور','ترفع السرعة تحت الشمس.'),
 'ILLUMINATE':('إنارة','تكثر المواجهات البرية.'),
 'TRACE':('محاكاة','تنسخ قدرة الخصم.'),
 'HUGE_POWER':('قوة هائلة','ترفع الهجوم.'),
 'POISON_POINT':('شوكة سامة','تسمم الخصم عند اللمس.'),
 'INNER_FOCUS':('تركيز','تمنع الإجفال.'),
 'MAGMA_ARMOR':('درع الحمم','تمنع التجمد.'),
 'WATER_VEIL':('ستار الماء','تمنع الحروق.'),
 'MAGNET_PULL':('جذب مغنطي','تحبس بوكيمون الفولاذ.'),
 'SOUNDPROOF':('عازل للصوت','تحمي من الحركات الصوتية.'),
 'RAIN_DISH':('طبق المطر','تستعيد HP تحت المطر.'),
 'SAND_STREAM':('عاصفة رملية','تستدعي عاصفة رملية.'),
 'PRESSURE':('ضغط','تجعل الخصم يستهلك PP أكثر.'),
 'THICK_FAT':('شحم كثيف','تحمي من الحر والبرد.'),
 'EARLY_BIRD':('استيقاظ مبكر','يصحو من النوم سريعا.'),
 'FLAME_BODY':('جسد ملتهب','تحرق الخصم عند اللمس.'),
 'RUN_AWAY':('فرار','تسهل الهرب.'),
 'KEEN_EYE':('عين ثاقبة','تمنع فقدان الدقة.'),
 'HYPER_CUTTER':('قاطع مفرط','تمنع خفض الهجوم.'),
 'PICKUP':('التقاط','قد يلتقط أدوات.'),
 'TRUANT':('كسل','يتحرك مرة كل دورتين.'),
 'HUSTLE':('اندفاع','قوة أكبر ودقة أقل.'),
 'CUTE_CHARM':('جاذبية لطيفة','تفتن من يلمسها.'),
 'PLUS':('موجب','تقوى مع قدرة سالب.'),
 'MINUS':('سالب','تقوى مع قدرة موجب.'),
 'FORECAST':('تنبؤ الطقس','يتغير مع الطقس.'),
 'STICKY_HOLD':('قبضة لزجة','تمنع سرقة الأداة.'),
 'SHED_SKIN':('انسلاخ','يشفى بالانسلاخ.'),
 'GUTS':('شجاعة','يزيد هجومه إن أصابته حالة.'),
 'MARVEL_SCALE':('حراشف مذهلة','يزيد دفاعه إن أصابته حالة.'),
 'LIQUID_OOZE':('سائل لزج','يؤذي من يمتص طاقته.'),
 'OVERGROW':('نمو مفرط','حركات العشب أقوى عند الخطر.'),
 'BLAZE':('لهيب','حركات النار أقوى عند الخطر.'),
 'TORRENT':('سيل','حركات الماء أقوى عند الخطر.'),
 'SWARM':('سرب','حركات الحشرات أقوى عند الخطر.'),
 'ROCK_HEAD':('رأس صخري','تمنع ضرر الارتداد.'),
 'DROUGHT':('جفاف','تستدعي الشمس في النزال.'),
 'ARENA_TRAP':('فخ الحلبة','تمنع الهرب.'),
 'VITAL_SPIRIT':('روح حيوية','تمنع النوم.'),
 'WHITE_SMOKE':('دخان أبيض','تمنع خفض القدرات.'),
 'PURE_POWER':('قوة صافية','ترفع الهجوم.'),
 'SHELL_ARMOR':('درع صدفي','تمنع الضربات الحاسمة.'),
 'CACOPHONY':('نشاز','تحمي من الحركات الصوتية.'),
 'AIR_LOCK':('قفل الهواء','تلغي آثار الطقس.'),
}

CLASSES = {
 'NONE':'مدرب بوكيمون','PKMN_TRAINER_UNUSED':'مدرب بوكيمون','PKMN_TRAINER':'مدرب بوكيمون',
 'AQUA_LEADER':'زعيم أكوا','TEAM_AQUA':'فريق أكوا','RS_AROMA_LADY':'سيدة العطور','AROMA_LADY':'سيدة العطور',
 'RS_RUIN_MANIAC':'هاوي الآثار','RUIN_MANIAC':'هاوي الآثار','INTERVIEWER':'مراسل','RS_TUBER_F':'سباح صغير',
 'RS_TUBER_M':'سباح صغير','TUBER':'سباح صغير','RS_COOLTRAINER':'مدرب محترف','COOLTRAINER':'مدرب محترف',
 'HEX_MANIAC':'هاوية الغموض','RS_LADY':'سيدة','LADY':'سيدة','RS_BEAUTY':'حسناء','BEAUTY':'حسناء',
 'RICH_BOY':'ولد ثري','RS_POKEMANIAC':'هاوي بوكيمون','POKEMANIAC':'هاوي بوكيمون','RS_SWIMMER_M':'سباح',
 'SWIMMER_M':'سباح','RS_SWIMMER_F':'سباحة','SWIMMER_F':'سباحة','RS_BLACK_BELT':'حزام أسود','BLACK_BELT':'حزام أسود',
 'GUITARIST':'عازف غيتار','KINDLER':'مشعل النار','RS_CAMPER':'كشاف','CAMPER':'كشاف','BUG_MANIAC':'هاوي حشرات',
 'RS_PSYCHIC':'ذو قوى خارقة','PSYCHIC':'ذو قوى خارقة','RS_GENTLEMAN':'نبيل','GENTLEMAN':'نبيل',
 'RS_ELITE_FOUR':'عضو النخبة','ELITE_FOUR':'عضو النخبة','RS_LEADER':'قائد الصالة','LEADER':'قائد الصالة',
 'SCHOOL_KID':'تلميذ','SR_AND_JR':'الأب والابن','POKEFAN':'محب بوكيمون','EXPERT':'خبير',
 'RS_YOUNGSTER':'فتى','YOUNGSTER':'فتى','RS_CHAMPION':'البطل','CHAMPION':'البطل','RS_FISHERMAN':'صياد',
 'FISHERMAN':'صياد','TRIATHLETE':'متسابق ثلاثي','DRAGON_TAMER':'مروض تنانين','RS_BIRD_KEEPER':'مربي طيور',
 'BIRD_KEEPER':'مربي طيور','NINJA_BOY':'فتى نينجا','BATTLE_GIRL':'مقاتلة','PARASOL_LADY':'سيدة المظلة',
 'RS_PICNICKER':'متنزهة','PICNICKER':'متنزهة','RS_TWINS':'توأمان','TWINS':'توأمان','RS_SAILOR':'بحار',
 'SAILOR':'بحار','BOARDER':'متزلج','COLLECTOR':'جامع تحف','RS_PKMN_BREEDER':'مربي بوكيمون',
 'PKMN_BREEDER':'مربي بوكيمون','RS_PKMN_RANGER':'حارس بوكيمون','PKMN_RANGER':'حارس بوكيمون',
 'MAGMA_LEADER':'زعيم ماغما','TEAM_MAGMA':'فريق ماغما','RS_LASS':'فتاة','LASS':'فتاة',
 'RS_BUG_CATCHER':'صائد حشرات','BUG_CATCHER':'صائد حشرات','RS_HIKER':'متسلق جبال','HIKER':'متسلق جبال',
 'RS_YOUNG_COUPLE':'زوجان شابان','YOUNG_COUPLE':'زوجان شابان','OLD_COUPLE':'زوجان عجوزان',
 'RS_SIS_AND_BRO':'الأخت والأخ','SIS_AND_BRO':'الأخت والأخ','AQUA_ADMIN':'مسؤول أكوا','MAGMA_ADMIN':'مسؤول ماغما',
 'SUPER_NERD':'مهووس علوم','BIKER':'دراج','BURGLAR':'لص','ENGINEER':'مهندس','CUE_BALL':'أقرع','GAMER':'لاعب',
 'ROCKER':'مغني روك','JUGGLER':'بهلوان','TAMER':'مروض','RIVAL_EARLY':'المنافس','RIVAL_LATE':'المنافس',
 'SCIENTIST':'عالم','BOSS':'الزعيم','TEAM_ROCKET':'فريق الصاروخ','CHANNELER':'ناسكة','COOL_COUPLE':'زوجان رائعان',
 'CRUSH_KIN':'إخوة القتال','PKMN_PROF':'بروفيسور','PLAYER':'اللاعب','CRUSH_GIRL':'فتاة القتال','PAINTER':'رسامة',
}
CLASS_NOTES = {'GAMER':'Gen 1 GAMERs are gamblers: «لاعب» keeps them neutral.',
               'CHANNELER':'Spirit mediums in the Pokémon Tower: «ناسكة» (an ascetic) avoids the occult reading.',
               'HEX_MANIAC':'«هاوية الغموض» rather than anything about witchcraft.',
               'CUE_BALL':'Bald bikers: «أقرع».'}

ENTRIES = []
for k, v in TYPES.items():
    ENTRIES.append(dict(id='TYPE_' + k, key='TYPE_' + k, file=TYPES_FILE, screen='Types', where=k.title(),
                        box=('line', BUDGET['type'], 'normal', 1), max_bytes=6, ar=v, note='From Pokémon Crystal Arabic.'))
for k, (name, desc) in ABILITIES.items():
    camel = ''.join(w.title() for w in k.split('_')).replace('CompoundEyes', 'CompoundEyes')
    ENTRIES.append(dict(id='ABILITY_' + k, key='ABILITY_' + k, file=AB_FILE, screen='Ability names', where=k.replace('_', ' ').title(),
                        box=('line', BUDGET['ability'], 'normal', 1), max_bytes=12, ar=name,
                        note='' if k != 'CUTE_CHARM' else '«جاذبية لطيفة» rather than «سحر».'))
    ENTRIES.append(dict(id='s%sDescription' % camel, file=AB_FILE, screen='Ability descriptions', where=k.replace('_', ' ').title(),
                        box=('line', BUDGET['desc'], 'normal', 1), max_bytes=51, ar=desc, note=''))
for k, v in CLASSES.items():
    ENTRIES.append(dict(id='TRAINER_CLASS_' + k, key='TRAINER_CLASS_' + k, file=CL_FILE, screen='Trainer classes',
                        where=k.replace('RS_', '').replace('_', ' ').title(), box=('line', BUDGET['cls'], 'normal', 1),
                        max_bytes=12, ar=v, note=CLASS_NOTES.get(k, '')))
ENTRIES.append(dict(id='gText_MoveInterfaceType', file='src/battle_message.c', screen='Battle', where='Move screen: type label',
                    box=('line', 4, 'normal', 1), ar='',
                    note='Left empty on purpose: the 64 px type box cannot hold «النوع/» plus a type like «تنيني», so only the type name is shown.'))

README = [
    ('Pokémon FireRed – Arabic translation – Batch 07: types, abilities, trainer classes', 'title'),
    ('Types use the names from Pokémon Crystal Arabic so both games agree. Abilities have a name (12 letters) and a '
     'one-line description for the summary screen. Trainer classes appear in battle: «صائد حشرات RICK يتحداك…».', 'text'),
    ('Widths: types 60 px (move-screen box), ability names 110 px and descriptions 220 px (summary window), trainer classes 100 px; the Fit column checks them.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py names_misc, then make.', 'text'),
]
GLOSSARY = [
    ('Types', 'عادي، مقاتل، طائر، سام، أرضي، صخري، حشري، شبحي، فولاذي، ناري، مائي، عشبي، كهربي، نفسي، جليدي، تنيني، ظلامي', 'From Crystal.'),
    ('POKéMON TRAINER', 'مدرب بوكيمون', ''),
    ('GAMER (gambler)', 'لاعب', 'Avoids gambling.'),
    ('CHANNELER', 'ناسكة', 'Avoids the occult reading.'),
    ('PSYCHIC (class)', 'ذو قوى خارقة', 'Type stays «نفسي» as in Crystal.'),
    ('CAMPER', 'كشاف', 'Scout.'),
    ('SUPER NERD', 'مهووس علوم', ''),
    ('COOLTRAINER', 'مدرب محترف', ''),
    ('CUTE CHARM', 'جاذبية لطيفة', 'Not «سحر».'),
    ('flinch', 'الإجفال', 'Used in INNER FOCUS.'),
]
