# -*- coding: utf-8 -*-
"""Batch 09b - Item descriptions (src/data/items.json, field "description_english"),
shown in the bag in up to 3 lines of 200 px. TM descriptions are the move
descriptions (separate batch). Families (berries, mail, type-boosting held
items, stones, vitamins, X items, scarves, room keys) share one pattern each."""
import json, os

FILE = 'src/data/items.json'
BOX = ('static', 200, 'normal', 3)
HELD = 'يحمله البوكيمون. '

def heal(n):            return 'دواء رذاذ يعالج الجروح.\nيعيد %s نقطة من HP لبوكيمون واحد.' % n
def drink(what, n):     return '%s\nيعيد %s نقطة من HP لبوكيمون واحد.' % (what, n)
def vitamin(stat):      return 'مشروب مغذّ للبوكيمون.\nيرفع %s الأساسي\nلدى بوكيمون واحد.' % stat
def xitem(stat):        return 'يرفع %s لدى البوكيمون في النزال.\nيزول أثره إن سُحب البوكيمون.' % stat
def stone(look):        return 'حجر عجيب يجعل أنواعا معينة\nمن البوكيمون تتطور.\n%s' % look
def mail(mon):          return 'بريد عليه رسم لطيف لـ%s.\nيحمله البوكيمون.' % mon
def boost(thing, t):    return HELD + '%s\nيقوي حركات %s.' % (thing, t)
def berry(effect):      return 'إن حمله البوكيمون، يُستخدم\nفي النزال %s.' % effect
def pinch(stat):        return 'إن حمله البوكيمون، يرفع %s\nحين يكون في خطر.' % stat
def scarf(cond):        return HELD + 'يعزز حالة %s\nلدى حامله في المسابقات.' % cond
def roomkey(n):         return 'مفتاح يفتح باب الغرفة %s\nفي السفينة المهجورة.\nقديم ويبدو سهل الكسر.' % n
def fossil(part):       return 'أحفورة بوكيمون قديم من قاع\nالبحر، يبدو أنها جزء من\n%s.' % part
GROUND = 'يمكن طحنها مسحوقا يدخل\nفي صنع الأدوية.'
CONFUSE = 'أداة تُحمل تعيد HP، لكنها قد\nتسبب الحيرة عند استخدامها.'
SHARD = 'شظية %s صغيرة.\nيبدو أنها من أداة ما صُنعت\nمنذ زمن بعيد.'
FLUTE = 'ناي زجاجي %s %s'

D = {
 'MASTER_BALL':'أفضل كرة على الإطلاق!\nتمسك أي بوكيمون بري\nدون أن تخطئ أبدا.',
 'ULTRA_BALL':'كرة عالية الجودة، فرص الإمساك\nبها أعلى من غريت بول.',
 'GREAT_BALL':'كرة جيدة، فرص الإمساك بها\nأعلى من بوكي بول العادية.',
 'POKE_BALL':'كرة تُرمى لإمساك بوكيمون بري.\nمصممة على شكل كبسولة.',
 'SAFARI_BALL':'كرة خاصة لا تُستخدم إلا في\nمنطقة السفاري. عليها نقش مموه.',
 'NET_BALL':'كرة مميزة فعالة جدا مع\nبوكيمون الماء والحشرات.',
 'DIVE_BALL':'كرة مميزة فعالة جدا مع\nالبوكيمون في أعماق البحر.',
 'NEST_BALL':'كرة مميزة فعالة جدا مع\nالبوكيمون الأضعف.',
 'REPEAT_BALL':'كرة مميزة فعالة جدا مع\nبوكيمون أمسكته من قبل.',
 'TIMER_BALL':'كرة مميزة تزداد فعاليتها\nكلما طال النزال.',
 'LUXURY_BALL':'كرة مريحة تجعل البوكيمون\nالذي تمسكه يألفك بسرعة.',
 'PREMIER_BALL':'كرة نادرة صُنعت خصيصا\nلإحياء ذكرى مناسبة ما.',
 'POTION':heal(20), 'SUPER_POTION':heal(50), 'HYPER_POTION':heal(200),
 'MAX_POTION':'دواء رذاذ يعالج الجروح.\nيعيد HP بوكيمون واحد كاملة.',
 'ANTIDOTE':'دواء رذاذ يشفي بوكيمونا\nواحدا من التسمم.',
 'BURN_HEAL':'دواء رذاذ يشفي بوكيمونا\nواحدا من الحروق.',
 'ICE_HEAL':'دواء رذاذ يذيب الجليد عن\nبوكيمون متجمد.',
 'AWAKENING':'دواء رذاذ يوقظ بوكيمونا نائما.',
 'PARALYZE_HEAL':'دواء رذاذ يشفي بوكيمونا\nواحدا من الشلل.',
 'FULL_RESTORE':'دواء يعيد HP كاملة ويشفي\nكل الحالات السيئة لبوكيمون واحد.',
 'FULL_HEAL':'دواء رذاذ يشفي كل الحالات\nالسيئة لبوكيمون واحد.',
 'REVIVE':'دواء يوقظ بوكيمونا مغمى عليه،\nويعيد إليه نصف HP.',
 'MAX_REVIVE':'دواء يوقظ بوكيمونا مغمى عليه،\nويعيد إليه HP كاملة.',
 'FRESH_WATER':drink('ماء غني بالمعادن.', 50), 'SODA_POP':drink('مشروب غازي منعش.', 60),
 'LEMONADE':drink('عصير ليمون حلو جدا.', 80), 'MOOMOO_MILK':drink('حليب مغذّ جدا.', 100),
 'ENERGY_POWDER':drink('مسحوق دوائي مُرّ جدا.', 50), 'ENERGY_ROOT':drink('جذر مُرّ جدا.', 200),
 'HEAL_POWDER':'مسحوق دوائي مُرّ جدا.\nيشفي كل الحالات السيئة\nلبوكيمون واحد.',
 'REVIVAL_HERB':'عشبة دوائية مُرّة جدا.\nتوقظ بوكيمونا مغمى عليه\nوتعيد إليه HP كاملة.',
 'ETHER':'يعيد 10 نقاط PP لحركة\nمختارة لدى بوكيمون واحد.',
 'MAX_ETHER':'يعيد PP حركة مختارة كاملة\nلدى بوكيمون واحد.',
 'ELIXIR':'يعيد 10 نقاط PP لكل حركات\nبوكيمون واحد.',
 'MAX_ELIXIR':'يعيد PP كل حركات بوكيمون\nواحد كاملة.',
 'LAVA_COOKIE':'الحلوى الشهيرة لبلدة لافاريدج.\nتشفي كل الحالات السيئة\nلبوكيمون واحد.',
 'BLUE_FLUTE':FLUTE % ('أزرق', 'يوقظ\nالبوكيمون النائم.'),
 'YELLOW_FLUTE':FLUTE % ('أصفر', 'يعيد\nالبوكيمون إلى صوابه.'),
 'RED_FLUTE':FLUTE % ('أحمر', 'يحرر\nالبوكيمون من الافتتان.'),
 'BLACK_FLUTE':'ناي زجاجي أسود.\nإن نفخت فيه، قلّ ظهور\nالبوكيمون البرية.',
 'WHITE_FLUTE':'ناي زجاجي أبيض.\nإن نفخت فيه، كثر ظهور\nالبوكيمون البرية.',
 'BERRY_JUICE':drink('عصير طبيعي 100%.', 20),
 'SACRED_ASH':'يوقظ كل البوكيمون المغمى عليها،\nويعيد إليها HP كاملة.',
 'SHOAL_SALT':'ملح نقي من أعماق كهف الشاطئ.\nمالح جدا!',
 'SHOAL_SHELL':'صدفة جميلة من أعماق كهف الشاطئ،\nمخططة بالأزرق والأبيض.',
 'RED_SHARD':SHARD % 'حمراء', 'BLUE_SHARD':SHARD % 'زرقاء', 'YELLOW_SHARD':SHARD % 'صفراء', 'GREEN_SHARD':SHARD % 'خضراء',
 'HP_UP':vitamin('HP'), 'PROTEIN':vitamin('الهجوم'), 'IRON':vitamin('الدفاع'), 'CARBOS':vitamin('السرعة'),
 'CALCIUM':vitamin('الهجوم الخاص'), 'ZINC':vitamin('الدفاع الخاص'),
 'RARE_CANDY':'حلوى مليئة بالطاقة!\nترفع مستوى البوكيمون درجة.',
 'PP_UP':'يرفع الحد الأقصى من PP قليلا\nلحركة مختارة لدى بوكيمون واحد.',
 'PP_MAX':'يرفع PP حركة مختارة إلى أعلى\nمستوى لدى بوكيمون واحد.',
 'GUARD_SPEC':'يمنع خفض قدرات بوكيمون الفريق\nخمس دورات بعد استخدامه.',
 'DIRE_HIT':'يزيد فرص الضربات الحاسمة\nفي النزال. يزول أثره إن\nسُحب البوكيمون.',
 'X_ATTACK':xitem('الهجوم'), 'X_DEFEND':xitem('الدفاع'), 'X_SPEED':xitem('السرعة'),
 'X_ACCURACY':xitem('الدقة'), 'X_SPECIAL':xitem('الهجوم الخاص'),
 'POKE_DOLL':'دمية جذابة.\nاستخدمها للهرب من أي نزال\nمع بوكيمون بري.',
 'FLUFFY_TAIL':'ذيل جذاب.\nاستخدمه للهرب من أي نزال\nمع بوكيمون بري.',
 'REPEL':'يمنع ظهور البوكيمون البرية\nالضعيفة لمدة 100 خطوة.',
 'SUPER_REPEL':'يمنع ظهور البوكيمون البرية\nالضعيفة لمدة 200 خطوة.',
 'MAX_REPEL':'يمنع ظهور البوكيمون البرية\nالضعيفة لمدة 250 خطوة.',
 'ESCAPE_ROPE':'حبل طويل ومتين.\nاستخدمه للخروج فورا من كهف\nأو متاهة.',
 'SUN_STONE':stone('أحمر كالشمس.'), 'MOON_STONE':stone('أسود كسماء الليل.'),
 'FIRE_STONE':stone('لونه برتقالي.'), 'THUNDER_STONE':stone('عليه نقش صاعقة.'),
 'WATER_STONE':stone('أزرق صاف.'), 'LEAF_STONE':stone('عليه نقش ورقة.'),
 'TINY_MUSHROOM':'فطر صغير ونادر.\nمحبوب جدا عند بعض الناس.',
 'BIG_MUSHROOM':'فطر كبير ونادر.\nمحبوب جدا عند بعض الناس.',
 'PEARL':'لؤلؤة صغيرة تلمع بلون فضي\nجميل. تُباع بثمن زهيد.',
 'BIG_PEARL':'لؤلؤة كبيرة تلمع بلون فضي\nجميل. تُباع بثمن مرتفع.',
 'STARDUST':'رمل أحمر جميل، ناعم كالحرير.\nيُباع بثمن مرتفع.',
 'STAR_PIECE':'شظية حجر كريم تلمع بلون\nأحمر. تُباع بثمن مرتفع.',
 'NUGGET':'سبيكة من الذهب الخالص تلمع\nببريق آسر. تُباع بثمن مرتفع.',
 'HEART_SCALE':'حرشفة جميلة على شكل قلب،\nنادرة جدا. تتوهج بألوان\nقوس قزح.',
 'ORANGE_MAIL':mail('زيغزاغون'), 'HARBOR_MAIL':mail('وينغل'), 'GLITTER_MAIL':mail('بيكاتشو'),
 'MECH_MAIL':mail('ماغنمايت'), 'WOOD_MAIL':mail('سلاكوث'), 'WAVE_MAIL':mail('ويلمر'),
 'SHADOW_MAIL':mail('داسكل'), 'TROPIC_MAIL':mail('بيلوسوم'),
 'BEAD_MAIL':'بريد يحمله البوكيمون.\nيظهر عليه رسم البوكيمون\nالذي يحمله.',
 'DREAM_MAIL':'بريد يحمله البوكيمون.\nيظهر عليه رسم البوكيمون\nالذي يحمله.',
 'FAB_MAIL':'بريد عليه رسم فاخر باذخ.\nيحمله البوكيمون.',
 'RETRO_MAIL':'بريد عليه رسم ثلاثة بوكيمون\nلطيفة. يحمله البوكيمون.',
 'CHERI_BERRY':berry('لشفاء الشلل'), 'CHESTO_BERRY':berry('للاستيقاظ'), 'PECHA_BERRY':berry('لشفاء التسمم'),
 'RAWST_BERRY':berry('لشفاء الحروق'), 'ASPEAR_BERRY':berry('لإذابة الجليد'), 'LEPPA_BERRY':berry('لاستعادة 10 PP'),
 'ORAN_BERRY':berry('لاستعادة 10 HP'), 'PERSIM_BERRY':berry('لإزالة الحيرة'), 'LUM_BERRY':berry('لشفاء أي حالة'),
 'SITRUS_BERRY':berry('لاستعادة 30 HP'),
 'FIGY_BERRY':CONFUSE, 'WIKI_BERRY':CONFUSE, 'MAGO_BERRY':CONFUSE, 'AGUAV_BERRY':CONFUSE, 'IAPAPA_BERRY':CONFUSE,
 'LIECHI_BERRY':pinch('الهجوم'), 'GANLON_BERRY':pinch('الدفاع'), 'SALAC_BERRY':pinch('السرعة'),
 'PETAYA_BERRY':pinch('الهجوم الخاص'), 'APICOT_BERRY':pinch('الدفاع الخاص'),
 'LANSAT_BERRY':pinch('فرص الضربات الحاسمة'),
 'STARF_BERRY':'إن حمله البوكيمون، يرفع إحدى\nقدراته بشدة حين يكون في خطر.',
 'BRIGHT_POWDER':HELD + 'يشع وهجا خادعا\nيخفض دقة الخصم.',
 'WHITE_HERB':HELD + 'يعيد أي قدرة\nانخفضت في النزال. يُستخدم مرة واحدة.',
 'MACHO_BRACE':HELD + 'يعزز النمو بقوة،\nلكنه يخفض السرعة ما دام محمولا.',
 'EXP_SHARE':HELD + 'ينال حامله نصيبا\nمن نقاط الخبرة دون أن ينازل.',
 'QUICK_CLAW':HELD + 'مخلب خفيف\nوحاد، قد يجعل حامله يضرب أولا.',
 'SOOTHE_BELL':HELD + 'جرس رنينه مريح،\nيجعل حامله هادئا ودودا.',
 'MENTAL_HERB':HELD + 'يحرر حامله من\nالافتتان. يُستخدم مرة واحدة.',
 'CHOICE_BAND':HELD + 'يقوي حركة واحدة،\nفتصبح الحركة الوحيدة المتاحة.',
 'KINGS_ROCK':HELD + 'قد يجعل الخصم\nيجفل حين يتلقى الضرر.',
 'SILVER_POWDER':boost('مسحوق فضي لامع', 'الحشرات'),
 'AMULET_COIN':HELD + 'يضاعف مال النزال\nإن شارك حامله فيه.',
 'CLEANSE_TAG':HELD + 'يبعد البوكيمون\nالبرية إن كان حامله أول الفريق.',
 'SOUL_DEW':'جوهرة يحملها لاتيوس أو لاتياس.\nترفع الهجوم الخاص والدفاع الخاص.',
 'DEEP_SEA_TOOTH':HELD + 'ناب يلمع بلون\nفضي حاد. يرفع الهجوم الخاص.',
 'DEEP_SEA_SCALE':HELD + 'حرشفة تلمع بلون\nوردي خافت. ترفع الدفاع الخاص.',
 'SMOKE_BALL':HELD + 'يضمن لحامله الهرب\nمن أي بوكيمون بري.',
 'EVERSTONE':HELD + 'يمنع حامله\nمن التطور.',
 'FOCUS_BAND':HELD + 'قد يصمد حامله أمام\nهجمة قاضية، فيبقى له 1 HP.',
 'LUCKY_EGG':HELD + 'بيضة مليئة\nبالسعادة، تكسب حاملها خبرة إضافية.',
 'SCOPE_LENS':HELD + 'عدسة تزيد فرص\nالضربات الحاسمة لحاملها.',
 'METAL_COAT':boost('غشاء معدني خاص', 'الفولاذ'),
 'LEFTOVERS':HELD + 'يستعيد حامله\nبعض HP تدريجيا خلال النزال.',
 'DRAGON_SCALE':'حرشفة سميكة وصلبة.\nقد يحملها بوكيمون من نوع التنين.',
 'LIGHT_BALL':'كرة يحملها بيكاتشو لترفع\nهجومه الخاص. لمسها قد يصعقك!',
 'SOFT_SAND':boost('رمل ناعم كالحرير', 'الأرض'), 'HARD_STONE':boost('حجر لا ينكسر', 'الصخر'),
 'MIRACLE_SEED':boost('بذرة تنبض بالحياة', 'العشب'), 'BLACK_GLASSES':boost('نظارة سوداء غامضة', 'الظلام'),
 'BLACK_BELT':boost('حزام يشحذ العزيمة', 'القتال'), 'MAGNET':boost('مغنطيس قوي', 'الكهرباء'),
 'MYSTIC_WATER':boost('جوهرة على شكل دمعة', 'الماء'), 'SHARP_BEAK':boost('منقار طويل حاد', 'الطيران'),
 'POISON_BARB':boost('شوكة صغيرة سامة', 'السم'), 'NEVER_MELT_ICE':boost('جليد لا يذوب', 'الجليد'),
 'SPELL_TAG':boost('بطاقة غريبة مخيفة', 'الأشباح'), 'TWISTED_SPOON':boost('ملعقة تحمل قوة ذهنية', 'النفس'),
 'CHARCOAL':boost('فحم سريع الاشتعال', 'النار'), 'DRAGON_FANG':boost('ناب صلب وحاد', 'التنين'),
 'SILK_SCARF':boost('وشاح فاخر', 'النوع العادي'),
 'UP_GRADE':'جهاز شفاف مليء بالبيانات\nمن كل نوع. من صنع شركة سيلف.',
 'SHELL_BELL':HELD + 'يستعيد حامله بعض\nHP كلما ضرب الخصم.',
 'SEA_INCENSE':HELD + 'يقوي حركات الماء\nقليلا.',
 'LAX_INCENSE':HELD + 'رائحته الخادعة\nتخفض دقة الخصم قليلا.',
 'LUCKY_PUNCH':'قفاز يحمله تشانسي، يزيد\nفرص ضرباته الحاسمة.',
 'METAL_POWDER':'مسحوق ناعم وصلب يحمله ديتو.\nيرفع دفاعه.',
 'THICK_CLUB':'عظمة صلبة يحملها كيوبون أو\nماروك. ترفع الهجوم.',
 'STICK':'ساق كرّاث يحمله فارفتشد،\nيزيد فرص ضرباته الحاسمة.',
 'RED_SCARF':scarf('الأناقة'), 'BLUE_SCARF':scarf('الجمال'), 'PINK_SCARF':scarf('اللطافة'),
 'GREEN_SCARF':scarf('الذكاء'), 'YELLOW_SCARF':scarf('القوة'),
 'MACH_BIKE':'دراجة قابلة للطي، أسرع من\nالمشي مرتين على الأقل.',
 'COIN_CASE':'علبة لقطع اللعب من صالة\nالألعاب. تتسع لـ9999 قطعة.',
 'ITEMFINDER':'جهاز يبحث عن الأدوات.\nيطلق إشارة إن كانت هناك أداة\nمخفية قريبة.',
 'OLD_ROD':'صنارة قديمة متهالكة.\nاستخدمها قرب أي ماء لاصطياد\nالبوكيمون البرية.',
 'GOOD_ROD':'صنارة جديدة جيدة.\nاستخدمها قرب أي ماء لاصطياد\nالبوكيمون البرية.',
 'SUPER_ROD':'صنارة رائعة متطورة.\nاستخدمها قرب أي ماء لاصطياد\nالبوكيمون البرية.',
 'SS_TICKET':'تذكرة الإبحار على متن الباخرة\nإس إس آن. عليها رسم سفينة.',
 'CONTEST_PASS':'تصريح دخول مسابقات البوكيمون.\nعليه رسم شريط جائزة.',
 'WAILMER_PAIL':'دلو سقي أنيق.\nاستخدمه لتنمو التوتات المزروعة\nفي التربة الرطبة.',
 'DEVON_GOODS':'طرد فيه قطع آلية من نوع ما،\nمن صنع شركة ديفون.',
 'SOOT_SACK':'كيس يجمع الرماد البركاني\nتلقائيا وأنت تمشي فوقه.',
 'BASEMENT_KEY':'مفتاح موفيل الجديدة، المبنية\nتحت مدينة موفيل.',
 'ACRO_BIKE':'دراجة قابلة للطي، تتيح حركات\nبهلوانية كالقفز والدوران.',
 'POKEBLOCK_CASE':'علبة لحفظ {POKEBLOCK} المصنوعة\nفي خلاط التوت.',
 'LETTER':'رسالة مهمة جدا إلى ستيفن\nمن رئيس شركة ديفون.',
 'EON_TICKET':'تذكرة الإبحار إلى جزيرة بعيدة\nفي الجنوب. عليها رسم جزيرة.',
 'RED_ORB':'جوهرة تتوهج بالأحمر.\nيقال إن فيها قوة هائلة من\nالأزمنة الغابرة.',
 'BLUE_ORB':'جوهرة تتوهج بالأزرق.\nيقال إن فيها قوة هائلة من\nالأزمنة الغابرة.',
 'SCANNER':'جهاز يبحث عن الكائنات الحية\nفي الماء. يبدو صعب الاستخدام.',
 'GO_GOGGLES':'نظارة واقية تتيح للمدرب عبور\nالعواصف الرملية في الصحراء.',
 'METEORITE':'نيزك سقط من الفضاء على جبل\nالقمر منذ زمن بعيد. صلب ووعر.',
 'ROOM_1_KEY':roomkey(1), 'ROOM_2_KEY':roomkey(2), 'ROOM_4_KEY':roomkey(4), 'ROOM_6_KEY':roomkey(6),
 'STORAGE_KEY':'مفتاح يفتح المخزن في السفينة\nالمهجورة. قديم ويبدو سهل الكسر.',
 'ROOT_FOSSIL':fossil('جذر نبتة'), 'CLAW_FOSSIL':fossil('مخلب'),
 'HELIX_FOSSIL':fossil('صدفة حلزونية'), 'DOME_FOSSIL':fossil('قوقعة'),
 'DEVON_SCOPE':'منظار يكشف وجود أي بوكيمون\nخفي. من صنع شركة ديفون.',
 'OAKS_PARCEL':'طرد للبروفيسور أوك من متجر\nالبوكيمون في مدينة فيريديان.',
 'POKE_FLUTE':'ناي يقال إنه يوقظ أي بوكيمون\nفي الحال. صوته عذب جميل.',
 'SECRET_KEY':'مفتاح الباب الأمامي لصالة\nجزيرة سينابار. أحمر مزخرف.',
 'BIKE_VOUCHER':'خذ هذه القسيمة إلى متجر الدراجات\nفي مدينة سيرولين، واستبدلها\nبدراجة.',
 'GOLD_TEETH':'طقم أسنان صناعية أضاعه حارس\nمنطقة السفاري. تجعل ابتسامته\nتتلألأ!',
 'OLD_AMBER':'قطعة كهرمان فيها جينات\nبوكيمون قديم. صافية تميل\nإلى الحمرة.',
 'CARD_KEY':'بطاقة مفتاح تفتح الأبواب في مقر\nشركة سيلف بمدينة سافرون.',
 'LIFT_KEY':'مفتاح يشغل المصعد في مخبأ فريق\nالصاروخ. عليه شعار الفريق.',
 'SILPH_SCOPE':'منظار يجعل البوكيمون الخفية\nمرئية. من صنع شركة سيلف.',
 'BICYCLE':'دراجة قابلة للطي، أسرع\nمن حذاء الجري.',
 'TOWN_MAP':'خريطة مفيدة جدا، تراها متى شئت.\nوتُظهر حتى مكانك الحالي!',
 'VS_SEEKER':'جهاز يكشف المدربين الراغبين\nفي النزال. يُشحن وأنت تتجول.',
 'FAME_CHECKER':'جهاز يتيح لك تذكر ما سمعته\nورأيته عن المشاهير.',
 'TM_CASE':'علبة لحفظ الأقراص التقنية والخاصة.\nمثبتة في جيب الأدوات المهمة.',
 'BERRY_POUCH':'جراب لحمل التوت.\nمثبت في جيب الأدوات المهمة.',
 'TEACHY_TV':'تلفاز مضبوط على برنامج فيه\nنصائح مفيدة للمدربين المبتدئين.',
 'TRI_PASS':'تصريح للعبّارات بين الجزيرة\nالأولى والثانية والثالثة.\nعليه رسم ثلاث جزر.',
 'RAINBOW_PASS':'تصريح للعبّارات بين فيرميليون\nوجزر سيفي. عليه رسم قوس قزح.',
 'TEA':'شاي عطري أعدته سيدة عجوز.\nيروي أشد العطش!',
 'MYSTIC_TICKET':'تذكرة لركوب السفينة إلى صخرة\nنافل. تتوهج بضوء غامض.',
 'AURORA_TICKET':'تذكرة لركوب السفينة إلى جزيرة\nالميلاد. تتوهج بجمال.',
 'POWDER_JAR':'جرة لحفظ مسحوق التوت المصنوع\nفي كسارة التوت.',
 'RUBY':'جوهرة بديعة تتوهج بالأحمر.\nترمز إلى الشغف.',
 'SAPPHIRE':'جوهرة بديعة تتوهج بالأزرق.\nترمز إلى الصدق.',
}
for b in ('RAZZ','BLUK','NANAB','WEPEAR','PINAP','POMEG','KELPSY','QUALOT','HONDEW','GREPA','TAMATO','CORNN',
          'MAGOST','RABUTA','NOMEL','SPELON','PAMTRE','WATMEL','DURIN','BELUE','ENIGMA'):
    D[b + '_BERRY'] = GROUND

_ids = [i for i, _ in json.load(open(os.path.join(os.path.dirname(__file__), 'names_items_en.json'), encoding='utf-8'))]
ENTRIES = []
for item_id in _ids:
    k = item_id[5:]
    if k in D:
        ENTRIES.append(dict(id=item_id + '_DESC', json=item_id, json_field='description_english', file=FILE,
                            screen='Item descriptions', where=k.replace('_', ' ').title(), box=BOX, ar=D[k], note=''))
_missing = [i for i in _ids if i[5:] not in D and not i.startswith(('ITEM_TM', 'ITEM_HM'))]
if _missing:
    print('names_itemdesc.py: no Arabic for', _missing)

README = [
    ('Pokémon FireRed – Arabic translation – Batch 09b: item descriptions', 'title'),
    ('The bag text for every item except TMs/HMs (those show the move description). Up to 3 lines of 200 px; '
     'lines are wrapped automatically, a single line break in the Arabic is kept.', 'text'),
    ('Families share one wording: berries, mail, type-boosting held items, stones, vitamins, X items, scarves, room keys.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py names_itemdesc, then make.', 'text'),
]
GLOSSARY = [
    ('An item to be held by a POKéMON.', 'يحمله البوكيمون.', 'Opening of every held-item description.'),
    ('…-type moves', 'حركات الماء / النار / …', ''),
    ('wild POKéMON', 'البوكيمون البرية', ''),
    ('in a pinch', 'حين يكون في خطر', ''),
]

# ---- Revision 3: plural «البوكيمونات» and player gender ([[masc|fem]]) -----------------
_R3 = {'ITEM_SACRED_ASH_DESC': 'يوقظ كل البوكيمونات المغمى عليها،\nويعيد إليها HP كاملة.', 'ITEM_GUARD_SPEC_DESC': 'يمنع خفض قدرات بوكيمونات الفريق\nخمس دورات بعد استخدامه.', 'ITEM_RETRO_MAIL_DESC': 'بريد عليه رسم ثلاثة بوكيمونات\nلطيفة. يحمله البوكيمون.', 'ITEM_BLACK_FLUTE_DESC': 'ناي زجاجي أسود.\nإن نفخت فيه، قلّ ظهور\nالبوكيمونات البرية.', 'ITEM_WHITE_FLUTE_DESC': 'ناي زجاجي أبيض.\nإن نفخت فيه، كثر ظهور\nالبوكيمونات البرية.', 'ITEM_SUPER_REPEL_DESC': 'يمنع ظهور البوكيمونات البرية\nالضعيفة لمدة 200 خطوة.', 'ITEM_MAX_REPEL_DESC': 'يمنع ظهور البوكيمونات البرية\nالضعيفة لمدة 250 خطوة.', 'ITEM_REPEL_DESC': 'يمنع ظهور البوكيمونات البرية\nالضعيفة لمدة 100 خطوة.', 'ITEM_OLD_ROD_DESC': 'صنارة قديمة متهالكة.\nاستخدمها قرب أي ماء لاصطياد\nالبوكيمونات البرية.', 'ITEM_GOOD_ROD_DESC': 'صنارة جديدة جيدة.\nاستخدمها قرب أي ماء لاصطياد\nالبوكيمونات البرية.', 'ITEM_SUPER_ROD_DESC': 'صنارة رائعة متطورة.\nاستخدمها قرب أي ماء لاصطياد\nالبوكيمونات البرية.', 'ITEM_CLEANSE_TAG_DESC': 'يحمله البوكيمون. يبعد البوكيمونات\nالبرية إن كان حامله أول الفريق.'}
for _e in ENTRIES:
    if _e['id'] in _R3:
        _e['ar'] = _R3[_e['id']]
