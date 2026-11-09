# -*- coding: utf-8 -*-
"""Batch 16 - Route 3, Mt. Moon (1F, B1F, B2F), Route 4 and its Pokémon Center.
Spacetoon-dub voice: clear, warm Fusha with energy, dramatic pauses, villains that
sound like villains. TEAM ROCKET = «عصابة روكيت» (feminine agreement). Names of
moves, species and items come from batches 06, 08 and 09."""
import names_moves, names_species, names_items
DIALOG = ('dialog', 200, 'normal', 2)
SIGN = ('manual', 200, 'normal', 2)
_M = 'data/maps/%s/text.inc'
_mv = {e['id']: e['ar'] for e in names_moves.ENTRIES}
_sp = {e['id']: e['ar'] for e in names_species.ENTRIES}
_it = {e['id']: e['ar'] for e in names_items.ENTRIES}
def MV(k): return _mv['MOVE_' + k]
def SP(k): return next(v for i, v in _sp.items() if i.endswith(k))
def IT(k): return next(v for i, v in _it.items() if i.endswith(k) and not i.endswith('_DESC'))
def G(m, f): return '[[%s|%s]]' % (m, f)

def T(label, mapname, where, ar, note='', box=DIALOG):
    return dict(id=label, file=_M % mapname, screen=mapname.replace('_', ' '), where=where, box=box, ar=ar, note=note)

M1, M2, R3, R4, PC = 'MtMoon_1F', 'MtMoon_B2F', 'Route3', 'Route4', 'Route4_PokemonCenter_1F'
DOME, HELIX = IT('DOME_FOSSIL'), IT('HELIX_FOSSIL')
MP, MK = MV('MEGA_PUNCH'), MV('MEGA_KICK')
ENTRIES = [
 # ---- Route 3 -----------------------------------------------------------------------
 T('Route3_Text_TunnelFromCeruleanTiring', R3, 'Tired hiker', 'فيو… يجب أن أرتاح قليلا… آه…\n\nذلك النفق القادم من سيرولين يهد الحيل!'),
 T('Route3_Text_ColtonIntro', R3, 'Bug Catcher Colton', 'مهلا! لقد رأيتك في غابة فيريديان!'),
 T('Route3_Text_ColtonDefeat', R3, 'Bug Catcher Colton', 'هزمتني مرة أخرى!'),
 T('Route3_Text_ColtonPostBattle', R3, 'Bug Catcher Colton', 'ليست كل البوكيمونات تعيش في الغابات، فهناك أنواع أخرى كثيرة!'),
 T('Route3_Text_BenIntro', R3, 'Youngster Ben', 'مرحبا! أنا أعشق السراويل القصيرة!\n\nإنها مريحة جدا، وسهلة اللبس!'),
 T('Route3_Text_BenDefeat', R3, 'Youngster Ben', 'لا أصدق هذا!'),
 T('Route3_Text_BenPostBattle', R3, 'Youngster Ben', 'هل ' + G('تستخدم', 'تستخدمين') + ' حاسوب مركز البوكيمون لتخزين بوكيموناتك؟\n\nكل صندوق يتسع لثلاثين بوكيمونا.'),
 T('Route3_Text_JaniceIntro', R3, 'Lass Janice', 'عفوا! كنت ' + G('تحدق', 'تحدقين') + ' بي، أليس كذلك؟'),
 T('Route3_Text_JaniceDefeat', R3, 'Lass Janice', 'يا لك من ' + G('قاس!', 'قاسية!')),
 T('Route3_Text_JanicePostBattle', R3, 'Lass Janice', 'إن لم ' + G('تكن تريد', 'تكوني تريدين') + ' النزال، فلا ' + G('تحدق', 'تحدقي') + ' في الناس!'),
 T('Route3_Text_GregIntro', R3, 'Bug Catcher Greg', 'هل أنت ' + G('مدرب؟', 'مدربة؟') + ' هيا نبدأ فورا!'),
 T('Route3_Text_GregDefeat', R3, 'Bug Catcher Greg', 'لو كانت لدي بوكيمونات جديدة لفزت!'),
 T('Route3_Text_GregPostBattle', R3, 'Bug Catcher Greg', 'إن امتلأ صندوق في الحاسوب، ' + G('فانتقل', 'فانتقلي') + ' إلى صندوق آخر.'),
 T('Route3_Text_SallyIntro', R3, 'Lass Sally', 'تلك النظرة التي رمقتني بها… يا لها من نظرة مثيرة للفضول!'),
 T('Route3_Text_SallyDefeat', R3, 'Lass Sally', G('كن لطيفا!', 'كوني لطيفة!')),
 T('Route3_Text_SallyPostBattle', R3, 'Lass Sally', 'يمكنك تجنب النزالات إن لم ' + G('تدع', 'تدعي') + ' المدربين يرونك.'),
 T('Route3_Text_CalvinIntro', R3, 'Youngster Calvin', 'مهلا! أنت لا ' + G('ترتدي', 'ترتدين') + ' سروالا قصيرا! ما خطبك؟'),
 T('Route3_Text_CalvinDefeat', R3, 'Youngster Calvin', 'خسرت! خسرت! خسرت!'),
 T('Route3_Text_CalvinPostBattle', R3, 'Youngster Calvin', 'أرتدي السروال القصير دائما، حتى في الشتاء! هذه سياستي!'),
 T('Route3_Text_JamesIntro', R3, 'Bug Catcher James', 'سأنازلك بالبوكيمون الذي أمسكته للتو!'),
 T('Route3_Text_JamesDefeat', R3, 'Bug Catcher James', 'انتهى أمري تماما!'),
 T('Route3_Text_JamesPostBattle', R3, 'Bug Catcher James', 'البوكيمونات المدرَّبة أقوى من البوكيمونات البرية!'),
 T('Route3_Text_RobinIntro', R3, 'Lass Robin', 'آه! هل لمستني؟'),
 T('Route3_Text_RobinDefeat', R3, 'Lass Robin', 'هذا كل شيء؟'),
 T('Route3_Text_RobinPostBattle', R3, 'Lass Robin', 'الطريق 4 عند سفح جبل القمر.'),
 T('Route3_Text_RouteSign', R3, 'Route sign', 'الطريق 3\nجبل القمر أمامك', box=SIGN),
 # ---- Mt. Moon 1F ---------------------------------------------------------------------
 T('MtMoon_1F_Text_MarcosIntro', M1, 'Hiker Marcos', 'واو! لقد أفزعتني! …آه، ' + G('أنت مجرد فتى صغير!', 'أنت مجرد فتاة صغيرة!')),
 T('MtMoon_1F_Text_MarcosDefeat', M1, 'Hiker Marcos', 'واو! أفزعتني مرة أخرى!'),
 T('MtMoon_1F_Text_MarcosPostBattle', M1, 'Hiker Marcos', 'لا ينبغي لصغار مثلك أن يتجولوا هنا في الظلام.'),
 T('MtMoon_1F_Text_JoshIntro', M1, 'Youngster Josh', 'أجئت أنت أيضا ' + G('لتستكشف', 'لتستكشفي') + ' الكهف؟'),
 T('MtMoon_1F_Text_JoshDefeat', M1, 'Youngster Josh', 'الخسارة مزعجة! ليست رائعة أبدا!'),
 T('MtMoon_1F_Text_JoshPostBattle', M1, 'Youngster Josh', 'نزلت إلى هنا كي أستعرض أمام الفتيات!'),
 T('MtMoon_1F_Text_MiriamIntro', M1, 'Lass Miriam', 'واو! المكان هنا أكبر بكثير مما توقعت!'),
 T('MtMoon_1F_Text_MiriamDefeat', M1, 'Lass Miriam', 'أوه! خسرت!'),
 T('MtMoon_1F_Text_MiriamPostBattle', M1, 'Lass Miriam', 'كيف يخرج المرء من هنا؟ إنه كبير جدا… قد أضيع!'),
 T('MtMoon_1F_Text_JovanIntro', M1, 'Super Nerd Jovan', 'ماذا! لا ' + G('تتسلل', 'تتسللي') + ' خلفي هكذا!'),
 T('MtMoon_1F_Text_JovanDefeat', M1, 'Super Nerd Jovan', 'بوكيموناتي لا تكفي!'),
 T('MtMoon_1F_Text_JovanPostBattle', M1, 'Super Nerd Jovan', 'علي أن أجد بوكيمونات أقوى… ترى أين هي؟'),
 T('MtMoon_1F_Text_IrisIntro', M1, 'Lass Iris', 'ماذا؟ أنا أنتظر أصدقائي ليجدوني هنا.'),
 T('MtMoon_1F_Text_IrisDefeat', M1, 'Lass Iris', 'خسرت؟'),
 T('MtMoon_1F_Text_IrisPostBattle', M1, 'Lass Iris', 'جئت لأنني سمعت أن هنا أحافير نادرة جدا.'),
 T('MtMoon_1F_Text_KentIntro', M1, 'Bug Catcher Kent', 'هناك رجال مريبون في الكهف… وأنت، ' + G('من تكون؟', 'من تكونين؟')),
 T('MtMoon_1F_Text_KentDefeat', M1, 'Bug Catcher Kent', 'أوقعت بي!'),
 T('MtMoon_1F_Text_KentPostBattle', M1, 'Bug Catcher Kent', 'لقد رأيتهم! أنا متأكد أنهم من عصابة روكيت!'),
 T('MtMoon_1F_Text_RobbyIntro', M1, 'Bug Catcher Robby', 'عليك أن ' + G('تعبر', 'تعبري') + ' هذا الكهف لتصل إلى مدينة سيرولين.'),
 T('MtMoon_1F_Text_RobbyDefeat', M1, 'Bug Catcher Robby', 'خسرت.'),
 T('MtMoon_1F_Text_RobbyPostBattle', M1, 'Bug Catcher Robby', SP('ZUBAT') + ' صعب المراس! لكن إن أمسكت واحدا، ' + G('فستعتمد', 'فستعتمدين') + ' عليه كثيرا.'),
 T('MtMoon_1F_Text_ZubatIsABloodsucker', M1, 'Warning', G('احذر!', 'احذري!') + ' ' + SP('ZUBAT') + ' يمتص الدماء!'),
 T('MtMoon_1F_Text_BrockHelpsExcavateFossils', M1, 'Fossil digger', 'مرحبا! أنا أنقب عن الأحافير تحت جبل القمر.\n\nوأحيانا يمد لي بروك، قائد صالة بيوتر، يد العون.'),
 # ---- Mt. Moon B2F: Miguel and Team Rocket --------------------------------------------
 T('MtMoon_B2F_Text_MiguelIntro', M2, 'Super Nerd Miguel', G('قف', 'قفي') + ' مكانك!\n\nأنا من وجد هاتين الأحفورتين، وكلتاهما لي وحدي!'),
 T('MtMoon_B2F_Text_MiguelDefeat', M2, 'Super Nerd Miguel', 'حسنا! حسنا! سنتقاسمهما!'),
 T('MtMoon_B2F_Text_WellEachTakeAFossil', M2, 'Super Nerd Miguel', 'لكل منا أحفورة واحدة… ولا مكان للطمع بيننا!'),
 T('MtMoon_B2F_Text_ThenThisFossilIsMine', M2, 'Super Nerd Miguel', 'حسنا… إذن هذه الأحفورة لي!'),
 T('MtMoon_B2F_Text_LabOnCinnabarRegeneratesFossils', M2, 'Super Nerd Miguel', 'بعيدا من هنا، في جزيرة سينابار، يوجد مختبر للبوكيمون.\n\nيبحثون هناك في إعادة إحياء الأحافير.'),
 T('MtMoon_B2F_Text_Grunt1Intro', M2, 'Rocket grunt 1', 'نحن عصابة روكيت، وسنعثر على الأحافير قبل الجميع!\n\nسنعيد إحياء البوكيمونات منها… ونجني ثروة طائلة!'),
 T('MtMoon_B2F_Text_Grunt1Defeat', M2, 'Rocket grunt 1', 'آه! لقد أغضبتني الآن!'),
 T('MtMoon_B2F_Text_Grunt1PostBattle', M2, 'Rocket grunt 1', 'لقد أغضبتني! ستضعك عصابة روكيت على قائمتها السوداء!'),
 T('MtMoon_B2F_Text_Grunt2Intro', M2, 'Rocket grunt 2', 'نحن عصابة روكيت، أشرس أشرار البوكيمون!\n\nننطلق بسرعة الضوء… ' + G('فاستسلم', 'فاستسلمي') + ' الآن، أو ' + G('استعد', 'استعدي') + ' للقتال!',
   note='A nod to the Arabic dub: «ننطلق بسرعة الضوء… استسلموا الآن أو استعدوا للقتال!»'),
 T('MtMoon_B2F_Text_Grunt2Defeat', M2, 'Rocket grunt 2', 'لقد أفسدت كل شيء!'),
 T('MtMoon_B2F_Text_Grunt2PostBattle', M2, 'Rocket grunt 2', 'تبا! لن يسكت رفاقي على هذا!'),
 T('MtMoon_B2F_Text_Grunt3Intro', M2, 'Rocket grunt 3', 'نحن في مهمة كبرى هنا! ' + G('اغرب عن وجهي يا صغير!', 'اغربي عن وجهي يا صغيرة!')),
 T('MtMoon_B2F_Text_Grunt3Defeat', M2, 'Rocket grunt 3', 'إذن… أنت ' + G('قوي', 'قوية') + '…'),
 T('MtMoon_B2F_Text_Grunt3PostBattle', M2, 'Rocket grunt 3', 'إن وجدت أحفورة، ' + G('فأعطني', 'فأعطيني') + ' إياها ' + G('واغرب', 'واغربي') + ' عن وجهي!'),
 T('MtMoon_B2F_Text_Grunt4Intro', M2, 'Rocket grunt 4', 'الصغار لا يعبثون مع الكبار!\n\nقد ' + G('تندم', 'تندمين') + ' على هذا!'),
 T('MtMoon_B2F_Text_Grunt4Defeat', M2, 'Rocket grunt 4', 'أنا أغلي غضبا!'),
 T('MtMoon_B2F_Text_Grunt4PostBattle', M2, 'Rocket grunt 4', 'عاشت البوكيمونات في هذا الجبل… قبل أن تطأه أقدام البشر بزمن طويل.'),
 T('MtMoon_B2F_Text_YouWantDomeFossil', M2, 'Fossil choice', G('أتريد', 'أتريدين') + ' ' + DOME + '؟'),
 T('MtMoon_B2F_Text_YouWantHelixFossil', M2, 'Fossil choice', G('أتريد', 'أتريدين') + ' ' + HELIX + '؟'),
 T('MtMoon_B2F_Text_ObtainedHelixFossil', M2, 'Fossil obtained', 'لقد حصلت على ' + HELIX + '!'),
 T('MtMoon_B2F_Text_ObtainedDomeFossil', M2, 'Fossil obtained', 'لقد حصلت على ' + DOME + '!'),
 # ---- Route 4 -------------------------------------------------------------------------
 T('Route4_Text_TrippedOverGeodude', R4, 'Girl near Mt. Moon', 'آخ! تعثرت بـ' + SP('GEODUDE') + '، البوكيمون الصخري!'),
 T('Route4_Text_CrissyIntro', R4, 'Lass Crissy', 'جئت إلى جبل القمر بحثا عن بوكيمونات الفطر.'),
 T('Route4_Text_CrissyDefeat', R4, 'Lass Crissy', 'بعد كل ما بذلته لإمساكها!'),
 T('Route4_Text_CrissyPostBattle', R4, 'Lass Crissy', 'ربما لم يبق هنا أي فطر…\n\nأظنني أمسكتها كلها!'),
 T('Route4_Text_MtMoonEntrance', R4, 'Sign', 'مدخل نفق جبل القمر', box=SIGN),
 T('Route4_Text_RouteSign', R4, 'Route sign', 'الطريق 4\nجبل القمر - مدينة سيرولين', box=SIGN),
 T('Text_MegaPunchTeach', R4, 'Mega Punch tutor', 'لكمة من الضراوة الهادرة!\n\nتختزن قوة تدميرية هائلة!\n\nحين تشتد الأمور، تكون ' + MP + ' الهجوم الأعظم! ' + G('أتوافقني', 'أتوافقينني') + '، أليس كذلك؟\n\nهيا! دعني أعلمها لبوكيمونك!'),
 T('Text_MegaPunchDeclined', R4, 'Mega Punch tutor', G('ستعود', 'ستعودين') + ' حين ' + G('تدرك', 'تدركين') + ' قيمة ' + MP + '!'),
 T('Text_MegaPunchWhichMon', R4, 'Mega Punch tutor', 'رائع! أي بوكيمون سيتعلمها؟'),
 T('Text_MegaPunchTaught', R4, 'Mega Punch tutor', 'الآن صرنا رفيقين في طريق اللكم!\n\n' + G('اذهب', 'اذهبي') + ' قبل أن يراك ذلك الأحمق المضلَّل هناك… الذي لا يتدرب إلا على ركلاته السخيفة!'),
 T('Text_MegaKickTeach', R4, 'Mega Kick tutor', 'ركلة من الضراوة الوحشية!\n\nتختزن قوة تدميرية هائلة!\n\nحين تصل إلى جوهر الأمر، تكون ' + MK + ' الهجوم الأعظم! ألا ' + G('توافقني', 'توافقينني') + '؟\n\nحسنا! سأعلمها لبوكيمونك!'),
 T('Text_MegaKickDeclined', R4, 'Mega Kick tutor', G('ستعود', 'ستعودين') + ' زحفا حين ' + G('تدرك', 'تدركين') + ' قيمة ' + MK + '!'),
 T('Text_MegaKickWhichMon', R4, 'Mega Kick tutor', 'حسنا! أي بوكيمون يريد أن يتعلمها؟'),
 T('Text_MegaKickTaught', R4, 'Mega Kick tutor', 'الآن صرنا توأمي روح في طريق الركل!\n\n' + G('اركض', 'اركضي') + ' قبل أن يراك ذلك المغفل الواهم هناك… الذي لا يتدرب إلا على لكماته البسيطة!'),
 T('Route4_Text_PeopleLikeAndRespectBrock', R4, 'Boy near Cerulean', 'واو، هذا وسام الصخرة! حصلت عليه من بروك، أليس كذلك؟\n\nبروك رائع! ليس قويا فحسب، بل يحبه الناس ويحترمونه.\n\nأريد أن أصبح قائد صالة مثله!'),
 # ---- Route 4 Pokémon Center ------------------------------------------------------------
 T('Route4_PokemonCenter_1F_Text_CanHaveSixMonsWithYou', PC, 'Gentleman', 'حسنا، ست كرات بوكيمون في حزامي…\n\nأجل، هذا يكفي، فلا يمكنك أن ' + G('تحمل', 'تحملي') + ' معك أكثر من ستة بوكيمونات.'),
 T('Route4_PokemonCenter_1F_Text_TeamRocketAttacksCerulean', PC, 'Young man', 'عصابة روكيت تهاجم سكان سيرولين…\n\nلا يمر يوم دون أن تتحدث عنها الأخبار!'),
 T('Route4_PokemonCenter_1F_Text_LaddieBuyMagikarpForJust500', PC, 'Magikarp salesman (boy)', 'الرجل: أهلا أهلا يا فتى! عندي لك صفقة العمر!\n\nسأبيعك بوكيمونا سريا… ' + SP('MAGIKARP') + '… بخمسمئة ين فقط!\n\nستشتريه، أليس كذلك؟'),
 T('Route4_PokemonCenter_1F_Text_SweetieBuyMagikarpForJust500', PC, 'Magikarp salesman (girl)', 'الرجل: أهلا أهلا يا آنسة! عندي لك صفقة العمر!\n\nسأبيعك بوكيمونا سريا… ' + SP('MAGIKARP') + '… بخمسمئة ين فقط!\n\nستشترينه، أليس كذلك؟'),
 T('Route4_PokemonCenter_1F_Text_PaidOutrageouslyForMagikarp', PC, 'Bought Magikarp', G('دفع', 'دفعت') + ' {PLAYER} مبلغا باهظا قدره ¥500… ' + G('واشترى', 'واشترت') + ' ' + SP('MAGIKARP') + '!'),
 T('Route4_PokemonCenter_1F_Text_OnlyDoingThisAsFavorToYou', PC, 'Magikarp salesman', 'لا؟ ' + G('تقول', 'تقولين') + ' لا؟ إنما أفعل هذا معروفا لك!'),
 T('Route4_PokemonCenter_1F_Text_NoRoomForMorePokemon', PC, 'Magikarp salesman', 'يبدو أنه لا مكان معك لبوكيمونات أخرى.'),
 T('Route4_PokemonCenter_1F_Text_YoullNeedMoreMoney', PC, 'Magikarp salesman', G('ستحتاج', 'ستحتاجين') + ' إلى مال أكثر من هذا!'),
 T('Route4_PokemonCenter_1F_Text_IDontGiveRefunds', PC, 'Magikarp salesman', 'الرجل: آسف، لا أرد المال! كنت ' + G('تعرف', 'تعرفين') + ' ما ' + G('تشتريه!', 'تشترينه!')),
 T('Route4_PokemonCenter_1F_Text_ShouldStoreMonsUsingPC', PC, 'Girl', 'أحيانا يكون معك من البوكيمونات ما لا يسمح بإضافة المزيد.\n\nحينها، ' + G('خزّن', 'خزّني') + ' بعضها في أي حاسوب.'),
 T('Route4_PokemonCenter_1F_Text_ItsANewspaper', PC, 'Newspaper', 'إنها جريدة.'),
]

README = [
    ('Pokémon FireRed – Arabic translation – Batch 16: Route 3, Mt. Moon, Route 4', 'title'),
    ('Every line of Route 3, Mt. Moon and Route 4 with its Pokémon Center, in a Spacetoon-dub voice: clear, warm Fusha '
     'with energy and drama. TEAM ROCKET is «عصابة روكيت» (feminine: «ستضعك عصابة روكيت على قائمتها»).', 'text'),
    ('Lines addressed to the player use [[masculine|feminine]]. Move, species and item names come from batches 06, 08, 09.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py mtmoon, then make.', 'text'),
]
GLOSSARY = [('TEAM ROCKET', 'عصابة روكيت', 'Feminine agreement.'), ('MT. MOON', 'جبل القمر', ''), ('fossil', 'أحفورة / أحافير', ''),
            ('CINNABAR ISLAND', 'جزيرة سينابار', ''), ('"Get lost, kid!"', 'اغرب عن وجهي يا صغير!', '')]
