# -*- coding: utf-8 -*-
"""Batch 02 - Pallet Town: the player's house, the town, the rival's house and
Prof. Oak's lab, including lines seen later in the game in these places.
Box rules: see intro.py. All of these are standard dialogue boxes."""

DIALOG = ('dialog', 200, 'normal', 2)
_M = 'data/maps/%s/text.inc'

def T(label, mapname, where, ar, note='', **kw):
    d = dict(id=label, file=_M % mapname, screen=mapname.replace('PalletTown_', '').replace('_', ' '),
             where=where, box=DIALOG, ar=ar, note=note)
    d.update(kw)
    return d

H2, H1, PT, RH, LAB = ('PalletTown_PlayersHouse_2F', 'PalletTown_PlayersHouse_1F', 'PalletTown',
                       'PalletTown_RivalsHouse', 'PalletTown_ProfessorOaksLab')
L = 'PalletTown_ProfessorOaksLab_Text_'
R = 'PalletTown_RivalsHouse_Text_'

ENTRIES = [
    # ---- Player's house ---------------------------------------------------------
    T('PalletTown_PlayersHouse_2F_Text_PlayedWithNES', H2, 'Bedroom: the NES',
      '{PLAYER} يلعب بجهاز NES.\n\n…حسنا!\nحان وقت الانطلاق!'),
    T('PalletTown_PlayersHouse_2F_Text_PressLRForHelp', H2, 'Bedroom: notice on the wall',
      'إنها ورقة معلّقة على الحائط…\n\nإن احترت في أمر ما، فاطلب المساعدة!\nاضغط زر L أو R!'),
    T('PalletTown_PlayersHouse_1F_Text_AllBoysLeaveOakLookingForYou', H1, 'Mom (boy player)',
      'الأم: …نعم، أعرف.\nكل الأولاد يغادرون البيت يوما ما.\nهكذا قالوا في التلفاز.\n\nآه، صحيح! جارنا البروفيسور أوك\nكان يبحث عنك.',
      'Speaker label MOM -> "الأم:" (a narrator label, not the player\'s own words).'),
    T('PalletTown_PlayersHouse_1F_Text_AllGirlsLeaveOakLookingForYou', H1, 'Mom (girl player)',
      'الأم: …نعم، أعرف.\nكل البنات يحلمن بالسفر.\nهكذا قالوا في التلفاز.\n\nآه، صحيح! جارنا البروفيسور أوك\nكان يبحث عنك.'),
    T('PalletTown_PlayersHouse_1F_Text_YouShouldTakeQuickRest', H1, 'Mom heals your team',
      'الأم: {PLAYER}!\nعليك أن تأخذ قسطا من الراحة.'),
    T('PalletTown_PlayersHouse_1F_Text_LookingGreatTakeCare', H1, 'Mom after healing',
      'الأم: رائع! تبدو أنت وبوكيمونك\nفي أحسن حال.\nاعتنِ بنفسك!'),
    T('PalletTown_PlayersHouse_1F_Text_MovieOnTVFourBoysOnRailroad', H1, 'TV (boy player)',
      'يعرض التلفاز فيلما.\nأربعة فتيان على سكة قطار.\n\n…حان وقت انطلاقي أنا أيضا.',
      'A nod to the film "Stand by Me", kept as a scene description.'),
    T('PalletTown_PlayersHouse_1F_Text_MovieOnTVGirlOnBrickRoad', H1, 'TV (girl player)',
      'يعرض التلفاز فيلما.\nفتاة بضفيرتين تمشي على طريق\nمرصوف بالطوب الأصفر.\n\n…حان وقت انطلاقي أنا أيضا.',
      'A nod to "The Wizard of Oz": "yellow brick road" made explicit so the reference lands.'),
    T('PalletTown_PlayersHouse_1F_Text_OopsWrongSide', H1, 'Back of the TV', 'عفوا، هذا ظهر التلفاز…'),

    # ---- Pallet Town ------------------------------------------------------------------
    T('PalletTown_Text_OakDontGoOut', PT, 'Oak stops you at the tall grass', 'أوك: مهلا! انتظر!\nلا تخرج!'),
    T('PalletTown_Text_OakGrassUnsafeNeedMon', PT, 'Oak stops you at the tall grass',
      'أوك: هذا خطر!\nالبوكيمون البرية تعيش في الأعشاب الطويلة!\n\nتحتاج إلى بوكيمون خاص بك\nليحميك.\n\nوجدتها!\nتعال معي!'),
    T('PalletTown_Text_RaisingMonsToo', PT, 'Girl in town',
      'أنا أيضا أربّي البوكيمون.\n\nحين تشتد قوتها،\nتستطيع أن تحميني.'),
    T('PalletTown_Text_CanStoreItemsAndMonsInPC', PT, 'Man in town',
      'التقنية مدهشة حقا!\n\nصار بإمكانك حفظ الأدوات والبوكيمون\nواستعادتها كبيانات عبر الحاسوب.'),
    T('PalletTown_Text_OakPokemonResearchLab', PT, 'Sign: the lab', 'مختبر أوك لأبحاث البوكيمون'),
    T('PalletTown_Text_PlayersHouse', PT, 'Sign: your house', 'بيت {PLAYER}'),
    T('PalletTown_Text_RivalsHouse', PT, 'Sign: rival\'s house', 'بيت {RIVAL}'),
    T('PalletTown_Text_TownSign', PT, 'Town sign', 'بلدة باليت\nألوان رحلتك تنتظرك!',
      '"Shades of your journey await!" -> "ألوان رحلتك تنتظرك!" (pallet/palette = colours).'),
    T('PalletTown_Text_OakLetMeSeePokedex', PT, 'Later: Oak asks to see your Pokédex',
      'أوك: آه، {PLAYER}!\nلقد عدت إذن؟\n\nكم ملأت من البوكيديكس؟\n\nهل تسمح لي بإلقاء نظرة؟\n\nلنرَ…'),
    T('PalletTown_Text_CaughtXPuttingInHonestEffort', PT, 'Later: Pokédex check (not enough yet)',
      'لقد أمسكت {STR_VAR_2}…\n\nهممم، يبدو أنك تبذل جهدا صادقا.\n\nحين تملأ المزيد منه،\nتعال وأرني إياه من فضلك.'),
    T('PalletTown_Text_CaughtXImpressiveFollowMe', PT, 'Later: Pokédex check (enough)',
      'لقد أمسكت… {STR_VAR_2}؟!\nهذا مذهل حقا!\n\nهناك أمر كنت أود أن أطلبه منك\nيا {PLAYER}.\n\nتعال.\nاتبعني.'),
    T('PalletTown_Text_OakYouEnjoyingTraveling', PT, 'Later: Oak in town',
      'أوك: آه، {PLAYER}!\nيبدو أنك تستمتع بالسفر.\n\nأعرفك جيدا يا {PLAYER}، ولن أستغرب\nأن تذهب إلى أماكن أبعد وأغرب.\n\nأحسنت، أحسنت.\nهوهوهو.'),

    # ---- Rival's house ------------------------------------------------------------------
    T(R + 'HiBrothersAtLab', RH, 'Daisy at the start',
      'ديزي: أهلا، {PLAYER}!\n\nأخي {RIVAL} في مختبر جدي.'),
    T(R + 'HeardYouBattledRival', RH, 'Daisy after the first battle',
      'ديزي: {PLAYER}، سمعت أنك خضت\nنزالا ضد {RIVAL}.\n\nليتني شاهدته!'),
    T(R + 'ErrandForGrandpaThisWillHelp', RH, 'Daisy gives the Town Map',
      'طلب منك جدي أن تقضي له حاجة؟\n\nيا له من كسول!\nخذ، هذه ستساعدك.'),
    T(R + 'ReceivedTownMapFromDaisy', RH, 'Item received',
      'حصل {PLAYER} على خريطة البلدات\nمن ديزي.',
      'TOWN MAP -> "خريطة البلدات" (the item name in the bag stays Latin until the names batch).'),
    T(R + 'DontHaveSpaceForThis', RH, 'Bag full', 'لا يوجد مكان لهذه في حقيبتك.'),
    T(R + 'ExplainTownMap', RH, 'Daisy explains the map',
      'يمكنك استخدام خريطة البلدات لتعرف\nأين أنت، أو لتتعرف على أسماء الأماكن.'),
    T(R + 'PleaseGiveMonsRest', RH, 'Daisy, later',
      'ديزي: البوكيمون كائنات حية\nمثلنا تماما.\n\nحين تتعب، أرجوك امنحها\nقسطا من الراحة.'),
    T(R + 'ItsBigMapOfKanto', RH, 'Wall map', 'خريطة كبيرة لمنطقة كانتو…\nكل مغامرة تبدأ بنظرة كهذه!'),
    T(R + 'ShelvesCrammedFullOfBooks', RH, 'Bookshelf', 'رفوف تفيض بكتب البوكيمون…\nتكفي لسنوات من القراءة!'),
    T(R + 'LikeMeToGroomMon', RH, 'Daisy grooming (postgame)',
      'ديزي: أهلا، {PLAYER}!\nجئت في الوقت المناسب.\n\nكنت على وشك أن أشرب الشاي.\nهل تشاركني؟\n\nلكن انظر!\nبوكيمونك متسخة قليلا.\n\nهل تريد أن أنظف واحدا منها؟'),
    T(R + 'DontNeedAnyGrooming', RH, 'Daisy grooming: no',
      'لا تحتاج إلى تنظيف؟\nحسنا، سنكتفي بالشاي إذن.'),
    T(R + 'GroomWhichOne', RH, 'Daisy grooming: pick', 'أيها تريد أن أنظف؟'),
    T(R + 'LookingNiceInNoTime', RH, 'Daisy grooming: start',
      'ديزي: حسنا، سأجعله يبدو جميلا\nفي لمح البصر.'),
    T(R + 'ThereYouGoAllDone', RH, 'Daisy grooming: done',
      '{X1}{STR_VAR_1} يبدو هانئا حالما…\n\n{X2}ديزي: [[تفضل!|تفضلي!]] انتهيت.\nأرأيت؟ أليس جميلا؟\n\nهيهي…\nيا له من بوكيمون لطيف.',
      '{X1} and {X2} are colour/font switches (narrator, then Daisy): keep them at the start of each part.',
      ifdef=[('{COLOR DARK_GRAY}', '{COLOR RED}'), ('{FONT_NORMAL}', '{FONT_FEMALE}')]),
    T(R + 'CantGroomAnEgg', RH, 'Daisy grooming: egg', 'آسفة، لا أستطيع حقا\nأن أنظف بيضة.'),
    T(R + 'MayISeeFirstMon', RH, 'Daisy checks friendship',
      'ديزي: البوكيمون تحبك إن ربيتها بحب.\n\nمثلا يا {PLAYER}، هل تسمح لي\nأن أرى أول بوكيمون لديك؟'),
    T(R + 'CouldntLoveYouMore', RH, 'Friendship: max',
      'لا يمكن أن يحبك أكثر مما يحبك الآن.\n\nبوكيمونك سعيد سعادة\nلا توصف.'),
    T(R + 'ItLooksVeryHappy', RH, 'Friendship: very high',
      'يبدو سعيدا جدا.\n\nليت {RIVAL} يرى هذا\nويتعلم منه شيئا.'),
    T(R + 'ItsQuiteFriendly', RH, 'Friendship: high', 'إنه ودود معك جدا.\nاستمر في معاملته بلطف!'),
    T(R + 'ItsWarmingUpToYou', RH, 'Friendship: medium', 'بدأ يألفك.\nلا بد أن الثقة بينكما تنمو.'),
    T(R + 'NotFamiliarWithYouYet', RH, 'Friendship: low',
      'لم يعتد عليك تماما بعد.\n\nكل البوكيمون تكون حذرة\nحين تحصل عليها أول مرة.'),
    T(R + 'DontLikeWayItGlaresAtYou', RH, 'Friendship: very low',
      '{PLAYER}، لا تعجبني طريقة\nتحديقه بك.\n\nهلا حاولت أن تكون ألطف معه قليلا؟'),
    T(R + 'WhyWouldMonHateYouSoMuch', RH, 'Friendship: lowest',
      '…ممم، ليس من السهل أن أقول هذا، لكن…\n\nهل هناك سبب يجعل بوكيمونك\nيكرهك إلى هذا الحد؟'),
    T(R + 'LovelyAndSweetClefairy', RH, 'Painting', '“كليفيري اللطيفة الجميلة”',
      'Title of a painting. Clefairy -> "كليفيري".'),

    # ---- Prof. Oak's lab -------------------------------------------------------------------
    T(L + 'RivalGrampsIsntAround', LAB, 'Rival, before you have a Pokémon',
      '{RIVAL}: ماذا؟ إنه أنت فقط يا {PLAYER}؟\nجدي ليس هنا.'),
    T(L + 'RivalFedUpWithWaiting', LAB, 'Rival when Oak arrives', '{RIVAL}: جدي!\nلقد سئمت الانتظار!'),
    T(L + 'RivalNoFairWhatAboutMe', LAB, 'Rival protests', '{RIVAL}: مهلا! جدي! هذا ليس عدلا!\nوماذا عني؟'),
    T(L + 'RivalGoChoosePlayer', LAB, 'Rival lets you pick first',
      '{RIVAL}: هه، لست طماعا مثلك.\nأنا ناضج!\n\nهيا، اختر يا {PLAYER}!'),
    T(L + 'RivalIllTakeThisOneThen', LAB, 'Rival picks', '{RIVAL}: سآخذ هذا إذن!'),
    T(L + 'RivalReceivedMonFromOak', LAB, 'Rival receives his Pokémon',
      'حصل {RIVAL} على {STR_VAR_1}\nمن البروفيسور أوك!'),
    T(L + 'RivalMyMonLooksTougher', LAB, 'Rival brags', '{RIVAL}: بوكيموني يبدو أقوى\nمن بوكيمونك بكثير.'),
    T(L + 'RivalLetsCheckOutMons', LAB, 'Rival challenges you',
      '{RIVAL}: انتظر يا {PLAYER}!\nلنختبر بوكيموناتنا!\n\nهيا، سأنازلك!',
      'Rival speaks with a cocky edge; "بوكيموناتنا" is a deliberate colloquial touch from him only.'),
    T(L + 'RivalDefeat', LAB, 'Rival loses (in battle)', 'ماذا؟!\nلا أصدق!\nلقد اخترت البوكيمون الخطأ!'),
    T('Text_RivalVictory', LAB, 'Rival wins (also Route 22)', '{RIVAL}: أجل!\nألست رائعا؟'),
    T(L + 'RivalGoToughenMyMon', LAB, 'Rival leaves the lab',
      '{RIVAL}: حسنا! سأجعل بوكيموني\nيخوض النزالات ليقوى!\n\n{PLAYER}! جدي!\nأراكما لاحقا… إن لحقتما بي!',
      '"Smell you later!" is the rival\'s catchphrase: rendered as a cocky Arabic jab rather than literally.'),
    T(L + 'RivalGramps', LAB, 'Rival returns', '{RIVAL}: جدي!'),
    T(L + 'RivalWhatDidYouCallMeFor', LAB, 'Rival returns', '{RIVAL}: كدت أنسى!\nلماذا استدعيتني؟'),
    T(L + 'RivalLeaveItToMeGramps', LAB, 'Rival accepts the Pokédex task', '{RIVAL}: حسنا يا جدي!\nاترك الأمر كله لي!'),
    T(L + 'RivalTellSisNotToGiveYouMap', LAB, 'Rival leaves for good',
      '{PLAYER}، يؤسفني أن أقولها، لكن\nلا حاجة إليك في هذه المهمة.\n\nوجدتها! سأستعير خريطة البلدات\nمن أختي!\n\nوسأطلب منها ألا تعيرك واحدة\nيا {PLAYER}! هاهاها!\n\nفلا تتعب نفسك وتأتِ إلى بيتي!'),
    T(L + 'OakThreeMonsChooseOne', LAB, 'Oak offers the three Pokémon',
      'أوك: {RIVAL}؟\nدعني أفكر…\n\nآه، صحيح! أنا من طلب منك المجيء!\nانتظر قليلا!\n\nتعال يا {PLAYER}.\n\nهنا ثلاثة بوكيمون.\n\nهاها!\n\nالبوكيمون موجودة داخل\nكرات البوكيمون هذه.\n\nحين كنت شابا، كنت مدرب\nبوكيمون محترفا.\n\nأما الآن، وقد كبرت في السن،\nفلم يبق لدي سوى هذه الثلاثة.\n\nيمكنك أن تأخذ واحدا.\nهيا، اختر!'),
    T(L + 'OakBePatientRival', LAB, 'Oak to the rival', 'أوك: صبرا يا {RIVAL}.\nستأخذ واحدا أنت أيضا!'),
    T(L + 'OakWhichOneWillYouChoose', LAB, 'Oak asks which one',
      'أوك: والآن يا {PLAYER}.\n\nفي كرات البوكيمون الثلاث هذه\nبوكيمون.\n\nأيها ستختار لنفسك؟'),
    T(L + 'OakHeyDontGoAwayYet', LAB, 'Leaving before choosing', 'أوك: مهلا!\nلا تذهب بعد!'),
    T(L + 'OakChoosingCharmander', LAB, 'Choosing Charmander',
      'آه! اخترت تشارماندر.\nعليك أن تربيه بصبر.\n\nأتختار تشارماندر يا {PLAYER}،\nبوكيمون النار؟',
      'Starter names follow the Arabic dub: تشارماندر، سكويرتل، بولباسور.'),
    T(L + 'OakChoosingSquirtle', LAB, 'Choosing Squirtle',
      'همم! اخترت سكويرتل.\nإنه يستحق التربية.\n\nأقررت أخذ سكويرتل يا {PLAYER}،\nبوكيمون الماء؟'),
    T(L + 'OakChoosingBulbasaur', LAB, 'Choosing Bulbasaur',
      'فهمت! اخترت بولباسور.\nتربيته سهلة جدا.\n\nأتنطلق مع بولباسور يا {PLAYER}،\nبوكيمون العشب؟'),
    T(L + 'OakThisMonIsEnergetic', LAB, 'After choosing', 'هذا البوكيمون مفعم بالحيوية حقا!'),
    T(L + 'ReceivedMonFromOak', LAB, 'You receive your Pokémon', 'حصل {PLAYER} على {STR_VAR_1}\nمن البروفيسور أوك!'),
    T(L + 'OakCanReachNextTownWithMon', LAB, 'Oak before you leave',
      'أوك: إن ظهر بوكيمون بري،\nيستطيع بوكيمونك أن ينازله.\n\nومعه إلى جانبك، ستتمكن من\nالوصول إلى البلدة التالية.'),
    T(L + 'OakBattleMonForItToGrow', LAB, 'Oak, later',
      'أوك: {PLAYER}، ربِّ بوكيمونك الصغير\nبأن تجعله يخوض النزالات.\n\nعليه أن ينازل لكي ينمو.'),
    T(L + 'OakHaveSomethingForMe', LAB, 'Oak, parcel delivery',
      'أوك: آه، {PLAYER}!\nكيف حال بوكيموني القديم؟\n\nيبدو أنه بدأ يتعلق بك أكثر.\n\nلا بد أنك موهوب\nكمدرب بوكيمون.\n\nما هذا؟\nأحضرت لي شيئا؟'),
    T(L + 'DeliveredOaksParcel', LAB, 'Parcel delivered', 'سلّم {PLAYER} طرد أوك.'),
    T(L + 'OakCustomBallIOrdered', LAB, 'Oak opens the parcel',
      'آه!\nإنها كرة البوكيمون الخاصة!\n\nكنت قد طلبتها.\nشكرا لك!'),
    T(L + 'OakHaveRequestForYouTwo', LAB, 'Oak to both of you', 'أوك: آه، صحيح!\nلدي طلب منكما أنتما الاثنين.'),
    T(L + 'OakPokedexOnDesk', LAB, 'Oak presents the Pokédex',
      'على المكتب يوجد اختراعي:\nالبوكيديكس!\n\nإنه يسجل تلقائيا بيانات البوكيمون\nالتي رأيتها أو أمسكتها.\n\nإنه موسوعة متطورة!'),
    T(L + 'OakTakeTheseWithYou', LAB, 'Oak gives the Pokédex', 'أوك: {PLAYER} و{RIVAL}.\nخذا هذين معكما.'),
    T(L + 'ReceivedPokedexFromOak', LAB, 'Item received', 'حصل {PLAYER} على البوكيديكس\nمن البروفيسور أوك.'),
    T(L + 'OakCatchMonsForDataTakeThese', LAB, 'Oak explains catching',
      'أوك: لا يمكنك الحصول على بيانات مفصلة\nعن البوكيمون بمجرد رؤيتها.\n\nعليك أن تمسكها لتحصل على\nبيانات كاملة.\n\nإذن، إليك بعض الأدوات\nلإمساك البوكيمون البرية.'),
    T(L + 'ReceivedFivePokeBalls', LAB, 'Item received', 'حصل {PLAYER} على خمس كرات بوكيمون.'),
    T(L + 'OakExplainCatching', LAB, 'Oak explains catching',
      'حين يظهر بوكيمون بري،\nيمكنك أن تحاول إمساكه.\n\nارمِ عليه كرة بوكيمون\nوحاول أن تمسكه!\n\nلكن هذا لن ينجح دائما.\n\nالبوكيمون الذي في كامل قوته قد يفلت.\nفلا تيأس، وحاول مرة بعد مرة!',
      '"You have to be lucky!" -> "فلا تيأس، وحاول مرة بعد مرة!": the lesson is perseverance, which suits the audience better than luck.'),
    T(L + 'OakCompleteMonGuideWasMyDream', LAB, 'Oak\'s dream',
      'أن أصنع دليلا كاملا لجميع\nالبوكيمون في العالم…\n\nكان ذلك حلمي!\n\nلكنني كبرت في السن،\nولم أعد قادرا على إنجازه.\n\nلذلك أريدكما أن تحققا\nحلمي هذا.\n\nهيا، انطلقا أنتما الاثنين.\n\nإنها مهمة عظيمة في تاريخ\nالبوكيمون!'),
    T(L + 'OakMonsAroundWorldWait', LAB, 'Oak, after', 'البوكيمون في كل أنحاء العالم\nتنتظرك يا {PLAYER}!'),
    T(L + 'OakAddedNothingToPokedex', LAB, 'Oak, no new Pokédex data',
      'آه، {PLAYER}!\nكيف حال البوكيديكس معك؟\n\nلقد أمسك {RIVAL} بعض البوكيمون\nوأضاف بياناتها.\n\nإذن يا {PLAYER}، لنلق نظرة\nعلى البوكيديكس الخاص بك.\n\n…ما الخطب؟\nلم تضف أي بيانات جديدة!\n\nسأعطيك هذه، فاجتهد أكثر\nقليلا.'),
    T(L + 'OakComeSeeMeSometime', LAB, 'Oak, later',
      'أوك: تعال لزيارتي من حين لآخر.\n\nفأنا أريد أن أعرف كيف\nيتقدم البوكيديكس معك.'),
    T(L + 'BlankEncyclopedia', LAB, 'Pokédex on the desk', 'إنه يشبه الموسوعة، لكن صفحاته\nفارغة.'),
    T(L + 'ThoseArePokeBalls', LAB, 'Poké Balls on the table', 'تلك كرات بوكيمون.\nفي داخلها بوكيمون!'),
    T(L + 'OaksLastMon', LAB, 'Last Poké Ball', 'هذا آخر بوكيمون لدى البروفيسور أوك.'),
    T(L + 'PressStartToOpenMenu', LAB, 'Poster', 'اضغط START لفتح القائمة!'),
    T(L + 'SaveOptionInMenu', LAB, 'Poster', 'خيار الحفظ موجود في القائمة.\nاستخدمه باستمرار.'),
    T(L + 'AllMonTypesHaveStrongAndWeakPoints', LAB, 'Poster',
      'لكل نوع من البوكيمون نقاط قوة\nونقاط ضعف أمام الأنواع الأخرى.'),
    T(L + 'EmailMessage', LAB, 'Oak\'s computer',
      'هناك رسالة بريد إلكتروني هنا.\n\n…\n\nأخيرا!\nأقوى مدربي دوري البوكيمون\nمستعدون لمواجهة كل المتحدين!\n\nأحضر أفضل بوكيموناتك، واكتشف\nمستواك كمدرب!\n\nمقر دوري البوكيمون\nهضبة إنديغو\n\nالبروفيسور أوك، نرجو زيارتك!\n…',
      'POKéMON LEAGUE -> "دوري البوكيمون"; INDIGO PLATEAU -> "هضبة إنديغو".'),
    T(L + 'StudyAsOaksAide', LAB, 'Aide', 'أدرس البوكيمون مساعدا\nللبروفيسور أوك.'),
    T(L + 'DaisyWillGroomMons', LAB, 'Aide (postgame)',
      'أهلا، {PLAYER}. أراهن أنك صرت صديقا\nمقربا لبوكيمونك.\n\nبالمناسبة، هل تعرف ديزي؟\n\nإن أريت ديزي بوكيمونك، تستطيع\nأن تعرف كم يحبك.\n\nوأحيانا قد تنظف لك\nأحد بوكيموناتك.\n\nهذا سر، فأرجوك\nلا تخبر أحدا.'),
    T(L + 'OakIsGoingToHaveRadioShow', LAB, 'Aide',
      'سيقدم البروفيسور أوك قريبا\nبرنامجه الإذاعي الخاص.\n\nواسمه: “ندوة أوك للبوكيمون”.'),
    T(L + 'OakIsAuthorityOnMons', LAB, 'Aide',
      'قد لا يبدو البروفيسور أوك مهما،\nلكنه المرجع الأول في البوكيمون.\n\nكثير من مدربي البوكيمون\nيكنّون له احتراما كبيرا.'),
    T(L + 'OakFavorToAskYouPlayer', LAB, 'Oak (postgame)',
      'آه، هذا رائع حقا!\n\n{PLAYER}، لدي طلب مهم آخر\nأريده منك.\n\nأريدك أن تصغي جيدا.'),
    T(L + 'OakSightingsOfRareMons', LAB, 'Oak (postgame)',
      'مؤخرا، شوهدت أنواع كثيرة\nمن البوكيمون النادرة.\n\nأقصد بوكيمون لم يرها أحد\nفي كانتو من قبل.\n\nكم أود أن أذهب وأراها بنفسي،\nلكنني كبرت كثيرا.\n\nوبما أنني لا أستطيع، يا {PLAYER}،\nأود أن تذهب أنت مكاني.'),
    T(L + 'RivalJustLetMeHandleEverything', LAB, 'Rival (postgame)',
      '{RIVAL}: مهلا، لقد سمعت ذلك!\n\nجدي، لماذا تفضّل {PLAYER} علي\nفي كل مرة؟\n\nلقد جمعت بوكيمون أكثر،\nوبسرعة أكبر أيضا.\n\nعليك أن تترك لي كل شيء.'),
    T(L + 'OakNeedYourHelpTooNeedToSeePokedexes', LAB, 'Oak (postgame)',
      'أوك: أعرف، أعرف.\nبالطبع أحتاج إلى عونك أيضا.\n\nوالآن، أريد أن أرى\nالبوكيديكس الخاص بكل منكما.'),
    T(L + 'OakTookBothPokedexUnits', LAB, 'Oak (postgame)', 'أخذ البروفيسور أوك جهازي\nالبوكيديكس.'),
    T(L + 'OakNowTheseUnitsCanRecordMoreData', LAB, 'Oak (postgame)',
      '… … …  … … …\n\n… … …  … … …\n\n…وانتهينا!\n\nالآن يسجل هذان الجهازان بيانات\nعدد أكبر بكثير من البوكيمون.'),
    T(L + 'PlayersPokedexWasUpgraded', LAB, 'Oak (postgame)', 'تمت ترقية البوكيديكس الخاص بـ{PLAYER}!'),
    T(L + 'OakMustReallyWorkToFillPokedex', LAB, 'Oak (postgame)',
      'والآن، يا {PLAYER} ويا {RIVAL}!\n\nهذه المرة، عليكما أن تجتهدا حقا\nفي ملء البوكيديكس.\n\nأحثكما على أن تجعلاه الأفضل\nوالأكمل على مر الزمان!\n\nإنها حقا مهمة عظيمة\nفي تاريخ البوكيمون!'),
    T(L + 'RivalIllCompleteThePokedex', LAB, 'Rival (postgame)',
      '{RIVAL}: اهدأ يا جدي.\nلا تتحمس هكذا.\n\nسأكمل البوكيديكس،\nفلا تقلق بشأن أي شيء.\n\nأظنني سأبدأ البحث\nفي الجزيرة الأولى…\n\nعلى أي حال، أنا راحل!'),
]

README = [
    ('Pokémon FireRed – Arabic translation – Batch 02: Pallet Town', 'title'),
    ('Every line in the player\'s house, Pallet Town, the rival\'s house and Prof. Oak\'s lab, including lines '
     'you only see later in the game (Pokédex checks, Daisy\'s grooming, the postgame Pokédex upgrade).', 'text'),
    ('', 'text'),
    ('What to edit', 'head'),
    ('Only the yellow cells: "Arabic" in Translation, and "Your decision" in Glossary. "Your comments" is free.', 'edit'),
    ('Same rules as batch 01: Alt+Enter = new line, empty line = new page, lines are wrapped automatically to the box '
     '(200 px per line, 2 lines per page). Keep {PLAYER}, {RIVAL}, {STR_VAR_1}, {STR_VAR_2} and {X1}/{X2} as they are.', 'text'),
    ('{STR_VAR_n} inserts a Pokémon or item name from the game\'s tables; the fit check assumes 10 Latin letters.', 'text'),
    ('', 'text'),
    ('Applying your changes', 'head'),
    ('1.  python3 tools/arabic/apply_translations.py pallet', 'text'),
    ('2.  make', 'text'),
    ('', 'text'),
    ('Names', 'head'),
    ('Pokémon, item and place names inside dialogue are in Arabic (dub forms where they exist). The game\'s name '
     'tables (bag, party, the names inserted by {STR_VAR_1}) are still Latin: they need the name-buffer work, '
     'planned as its own batch. Until then a line like "حصل AAAB على CHARMANDER" mixes both.', 'text'),
]

GLOSSARY = [
    ('MOM: / OAK: / DAISY: (speaker labels)', 'الأم: / أوك: / ديزي:', 'Daisy -> "ديزي" as in the dub.'),
    ('Gramps / Grandpa', 'جدي', 'The rival and Daisy both say "جدي".'),
    ('PALLET TOWN', 'بلدة باليت', 'Dub form. Sign line: "ألوان رحلتك تنتظرك!"'),
    ('KANTO', 'كانتو', ''),
    ('ONE ISLAND', 'الجزيرة الأولى', ''),
    ('INDIGO PLATEAU', 'هضبة إنديغو', ''),
    ('POKéMON LEAGUE', 'دوري البوكيمون', 'Alternative: "بطولة البوكيمون".'),
    ('POKéMON TRAINER', 'مدرب بوكيمون', ''),
    ('POKéDEX', 'البوكيديكس', 'Kept as a proper name; "موسوعة" is used when Oak describes it.'),
    ('POKé BALL', 'كرة البوكيمون / كرة بوكيمون', 'Plural "كرات البوكيمون".'),
    ('TOWN MAP', 'خريطة البلدات', ''),
    ('OAK\'S PARCEL', 'طرد أوك', ''),
    ('CHARMANDER / SQUIRTLE / BULBASAUR', 'تشارماندر / سكويرتل / بولباسور', 'Dub forms. The species table stays Latin for now.'),
    ('CLEFAIRY', 'كليفيري', ''),
    ('FIRE / WATER / GRASS POKéMON', 'بوكيمون النار / الماء / العشب', ''),
    ('battle (verb)', 'ينازل / يخوض النزالات', 'Consistent with batch 01.'),
    ('wild POKéMON', 'بوكيمون بري / البوكيمون البرية', ''),
    ('EGG', 'بيضة', ''),
    ('"Smell you later!"', 'أراكما لاحقا… إن لحقتما بي!', 'Rival catchphrase, adapted: "أراكما لاحقا… إن لحقتما بي!"'),
    ('"You have to be lucky!"', 'فلا تيأس، وحاول مرة بعد مرة!', 'Perseverance instead of luck.'),
]

# ---- Revision 2: livelier, dub-style wording -------------------------------------------
REVISED = {
    'PalletTown_PlayersHouse_2F_Text_PlayedWithNES': ('{PLAYER} يلعب بجهاز NES.\n\n…كفى لعبا!\nالمغامرة الحقيقية تنتظر!', ''),
    'PalletTown_PlayersHouse_2F_Text_PressLRForHelp': ('ورقة ملصقة على الحائط…\n\n“إن احترت في أمر، فاطلب المساعدة!\nاضغط زر L أو R!”', ''),
    'PalletTown_PlayersHouse_1F_Text_AllBoysLeaveOakLookingForYou': ('الأم: …نعم، أعرف يا بني.\nكل الأولاد يغادرون البيت يوما ما.\nهكذا قالوا في التلفاز.\n\nآه، صحيح! جارنا البروفيسور أوك\nكان يسأل عنك.',
        'Speaker label MOM -> "الأم:". "يا بني" adds a mother\'s warmth.'),
    'PalletTown_PlayersHouse_1F_Text_AllGirlsLeaveOakLookingForYou': ('الأم: …نعم، أعرف يا ابنتي.\nكل البنات يحلمن بالسفر يوما ما.\nهكذا قالوا في التلفاز.\n\nآه، صحيح! جارنا البروفيسور أوك\nكان يسأل عنك.', ''),
    'PalletTown_PlayersHouse_1F_Text_YouShouldTakeQuickRest': ('الأم: {PLAYER}!\nتبدو متعبا… خذ قسطا من الراحة.', ''),
    'PalletTown_PlayersHouse_1F_Text_LookingGreatTakeCare': ('الأم: ها أنت ذا! أنت وبوكيمونك\nفي أحسن حال.\nاعتنِ بنفسك جيدا!', ''),
    'PalletTown_PlayersHouse_1F_Text_MovieOnTVFourBoysOnRailroad': ('يعرض التلفاز فيلما…\nأربعة فتيان على سكة قطار.\n\n…يبدو أن وقت رحلتي قد حان أيضا.',
        'A nod to "Stand by Me".'),
    'PalletTown_PlayersHouse_1F_Text_MovieOnTVGirlOnBrickRoad': ('يعرض التلفاز فيلما…\nفتاة بضفيرتين تمشي على طريق\nمرصوف بالطوب الأصفر.\n\n…يبدو أن وقت رحلتي قد حان أيضا.',
        'A nod to "The Wizard of Oz".'),
    'PalletTown_PlayersHouse_1F_Text_OopsWrongSide': ('عفوا… هذا ظهر التلفاز!', ''),
    'PalletTown_Text_OakDontGoOut': ('أوك: انتظر! قف مكانك!\nلا تخرج!', ''),
    'PalletTown_Text_OakGrassUnsafeNeedMon': ('أوك: يا لك من متهور!\nالبوكيمون البرية تختبئ في الأعشاب!\n\nلا تخرج إليها دون بوكيمون\nيحميك.\n\nآه، وجدتها!\nتعال معي!', ''),
    'PalletTown_Text_RaisingMonsToo': ('أنا أيضا أربي البوكيمون.\n\nوحين تكبر وتقوى،\nستحميني من أي خطر!', ''),
    'PalletTown_Text_CanStoreItemsAndMonsInPC': ('التقنية مذهلة حقا!\n\nصار بإمكانك أن تحفظ أدواتك\nوبوكيمونك في الحاسوب كأنها بيانات!', ''),
    'PalletTown_Text_OakLetMeSeePokedex': ('أوك: آه، {PLAYER}!\nها قد عدت!\n\nإلى أين وصلت في ملء البوكيديكس؟\n\nهلا سمحت لي بإلقاء نظرة؟\n\nلنرَ…', ''),
    'PalletTown_Text_CaughtXImpressiveFollowMe': ('أمسكت… {STR_VAR_2}؟!\nهذا مذهل حقا!\n\nهناك أمر طالما أردت أن أطلبه\nمنك يا {PLAYER}.\n\nتعال.\nاتبعني.', ''),
    'PalletTown_Text_OakYouEnjoyingTraveling': ('أوك: آه، {PLAYER}!\nيبدو أن السفر يروق لك.\n\nأعرفك جيدا، ولن أستغرب أبدا\nأن تبلغ أماكن أبعد وأغرب.\n\nأحسنت، أحسنت.\nهوهوهو.', ''),
    'PalletTown_RivalsHouse_Text_HiBrothersAtLab': ('ديزي: أهلا {PLAYER}!\n\nأخي {RIVAL}؟ إنه في مختبر جدي.', ''),
    'PalletTown_RivalsHouse_Text_HeardYouBattledRival': ('ديزي: سمعت أنك نازلت أخي {RIVAL}.\n\nيا ليتني كنت هناك!', ''),
    'PalletTown_RivalsHouse_Text_ErrandForGrandpaThisWillHelp': ('جدي كلفك بمهمة؟\n\nيا له من كسول!\nخذ هذه، ستنفعك في طريقك.', ''),
    'PalletTown_RivalsHouse_Text_ExplainTownMap': ('بخريطة البلدات تعرف أين أنت،\nوتتعرف على أسماء الأماكن.', ''),
    'PalletTown_RivalsHouse_Text_PleaseGiveMonsRest': ('ديزي: البوكيمون كائنات حية،\nتتعب مثلنا تماما.\n\nفامنحها قسطا من الراحة\nحين تحتاج إليه.', ''),
    'PalletTown_RivalsHouse_Text_LikeMeToGroomMon': ('ديزي: أهلا {PLAYER}!\nجئت في الوقت المناسب.\n\nكنت على وشك أن أعد الشاي.\nهل تشاركني؟\n\nلكن انظر!\nبوكيمونك يحتاج إلى قليل من العناية.\n\nهل أنظف لك واحدا منها؟', ''),
    'PalletTown_RivalsHouse_Text_LookingNiceInNoTime': ('ديزي: سأجعله يتألق\nفي لمح البصر.', ''),
    'PalletTown_RivalsHouse_Text_CouldntLoveYouMore': ('إنه يحبك حبا لا مزيد عليه.\n\nبوكيمونك سعيد سعادة\nلا توصف.', ''),
    'PalletTown_RivalsHouse_Text_ItLooksVeryHappy': ('يبدو سعيدا جدا معك.\n\nليت {RIVAL} يرى هذا\nويتعلم منه شيئا!', ''),
    'PalletTown_RivalsHouse_Text_ItsWarmingUpToYou': ('بدأ يألفك ويرتاح إليك.\nالثقة بينكما تكبر يوما بعد يوم.', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalGrampsIsntAround': ('{RIVAL}: ماذا؟ هذا أنت يا {PLAYER}؟\nجدي ليس هنا.', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalFedUpWithWaiting': ('{RIVAL}: جدي!\nلقد مللت الانتظار!', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalNoFairWhatAboutMe': ('{RIVAL}: مهلا يا جدي! هذا ظلم!\nوأنا؟ ماذا عني؟', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalGoChoosePlayer': ('{RIVAL}: هه، أنا لست طماعا مثلك.\nأنا ناضج!\n\nاختر أنت أولا يا {PLAYER}!', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalIllTakeThisOneThen': ('{RIVAL}: وأنا آخذ هذا!', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalMyMonLooksTougher': ('{RIVAL}: بوكيموني يبدو أقوى\nمن بوكيمونك بكثير!', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalLetsCheckOutMons': ('{RIVAL}: مهلا يا {PLAYER}!\nلنجرب بوكيموناتنا!\n\nهيا، إلى النزال!',
        'The rival speaks with a cocky edge; "بوكيموناتنا" is his colloquial touch only.'),
    'PalletTown_ProfessorOaksLab_Text_RivalDefeat': ('ماذا؟!\nمستحيل!\nلقد اخترت البوكيمون الخطأ!', ''),
    'Text_RivalVictory': ('{RIVAL}: نعم!\nأنا عبقري، أليس كذلك؟', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalGoToughenMyMon': ('{RIVAL}: حسنا! سأدرب بوكيموني\nفي النزالات حتى يصير وحشا!\n\n{PLAYER}! جدي!\nأراكما لاحقا… إن لحقتما بي!',
        '"Smell you later!" -> a cocky Arabic jab.'),
    'PalletTown_ProfessorOaksLab_Text_RivalWhatDidYouCallMeFor': ('{RIVAL}: كدت أنسى!\nلماذا استدعيتني يا جدي؟', ''),
    'PalletTown_ProfessorOaksLab_Text_RivalLeaveItToMeGramps': ('{RIVAL}: حسنا يا جدي!\nاترك كل شيء لي!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakThreeMonsChooseOne': ('أوك: {RIVAL}؟\nدعني أتذكر…\n\nآه، نعم! أنا من استدعاك!\nانتظر قليلا!\n\nتعال يا {PLAYER}.\n\nهنا ثلاثة بوكيمون!\n\nهاها!\n\nإنها تنتظر داخل\nكرات البوكيمون هذه.\n\nفي شبابي، كنت مدرب بوكيمون\nلا يشق له غبار!\n\nأما الآن، وقد شاب شعري،\nفلم يبق لدي سوى هذه الثلاثة.\n\nاختر واحدا منها،\nهيا!',
        '"a serious POKéMON TRAINER" -> "لا يشق له غبار" (unrivalled), a classic Arabic idiom.'),
    'PalletTown_ProfessorOaksLab_Text_OakWhichOneWillYouChoose': ('أوك: والآن يا {PLAYER}…\n\nفي كل كرة من هذه الكرات الثلاث\nبوكيمون ينتظر صاحبه.\n\nأيها ستختار؟', ''),
    'PalletTown_ProfessorOaksLab_Text_OakThisMonIsEnergetic': ('هذا البوكيمون يتقد حيوية!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakCanReachNextTownWithMon': ('أوك: إن باغتك بوكيمون بري،\nفبوكيمونك سيتصدى له.\n\nومعه إلى جانبك، ستبلغ\nالبلدة التالية بأمان.', ''),
    'PalletTown_ProfessorOaksLab_Text_OakBattleMonForItToGrow': ('أوك: {PLAYER}، النزالات هي ما\nيجعل بوكيمونك ينمو.\n\nفلا تبخل عليه بها!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakHaveSomethingForMe': ('أوك: آه، {PLAYER}!\nكيف حال بوكيموني القديم؟\n\nأرى أنه صار يتعلق بك أكثر.\n\nفيك موهبة حقيقية\nكمدرب بوكيمون.\n\nما هذا؟\nأحضرت لي شيئا؟', ''),
    'PalletTown_ProfessorOaksLab_Text_OakCustomBallIOrdered': ('آه!\nإنها كرة البوكيمون الخاصة!\n\nكنت أنتظرها بفارغ الصبر.\nشكرا لك!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakPokedexOnDesk': ('على المكتب، أحدث اختراعاتي:\nالبوكيديكس!\n\nيسجل تلقائيا بيانات كل بوكيمون\nتراه أو تمسكه.\n\nإنه موسوعة تمشي معك أينما ذهبت!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakExplainCatching': ('حين يظهر بوكيمون بري،\nيمكنك أن تحاول إمساكه.\n\nارمِ عليه كرة بوكيمون\nوجرب حظك… أقصد مهارتك!\n\nلكنها لن تنجح دائما.\n\nفالبوكيمون في كامل قوته قد يفلت.\nفلا تيأس، وحاول مرة بعد مرة!',
        'Oak catches himself: "حظك… أقصد مهارتك!", then the lesson is perseverance.'),
    'PalletTown_ProfessorOaksLab_Text_OakCompleteMonGuideWasMyDream': ('موسوعة كاملة لكل بوكيمون\nفي هذا العالم…\n\nذلك كان حلم حياتي!\n\nلكن العمر لم يعد يسعفني\nلأحققه.\n\nلذلك أضعه أمانة بين أيديكما.\n\nهيا، انطلقا!\n\nإنها مهمة عظيمة ستُكتب في\nتاريخ البوكيمون!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakMonsAroundWorldWait': ('البوكيمون في كل أرجاء العالم\nتنتظرك يا {PLAYER}!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakComeSeeMeSometime': ('أوك: زرني من حين لآخر.\n\nأريد أن أرى كيف يكبر\nالبوكيديكس بين يديك.', ''),
    'PalletTown_ProfessorOaksLab_Text_BlankEncyclopedia': ('يبدو كموسوعة، لكن صفحاته\nبيضاء… تنتظر من يملؤها!', ''),
    'PalletTown_ProfessorOaksLab_Text_ThoseArePokeBalls': ('كرات بوكيمون…\nوفي داخلها بوكيمون ينتظر!', ''),
    'PalletTown_ProfessorOaksLab_Text_SaveOptionInMenu': ('خيار الحفظ موجود في القائمة.\nاحفظ تقدمك دائما!', ''),
    'PalletTown_ProfessorOaksLab_Text_OakIsAuthorityOnMons': ('قد لا يبدو عليه ذلك، لكن البروفيسور\nأوك هو المرجع الأول في البوكيمون.\n\nوكثير من المدربين يكنّون له\nكل الاحترام.', ''),
}
for _e in ENTRIES:
    if _e['id'] in REVISED:
        _e['ar'], _note = REVISED[_e['id']]
        if _note:
            _e['note'] = _note

# ---- Revision 2: line-fit fixes
_FIX = {'PalletTown_Text_OakGrassUnsafeNeedMon': 'أوك: يا لك من متهور!\nفي العشب بوكيمون برية!\n\nلا تخرج إليها دون بوكيمون\nيحميك.\n\nآه، وجدتها!\nتعال معي!', 'PalletTown_Text_CanStoreItemsAndMonsInPC': 'التقنية مذهلة حقا!\n\nأدواتك وبوكيمونك، كلها تُحفظ\nفي الحاسوب كبيانات!', 'PalletTown_RivalsHouse_Text_LikeMeToGroomMon': 'ديزي: أهلا {PLAYER}!\nجئت في الوقت المناسب.\n\nكنت على وشك أن أعد الشاي.\nهل تشاركني؟\n\nلكن انظر!\nبوكيمونك متسخ قليلا!\n\nهل أنظف لك واحدا منها؟', 'PalletTown_RivalsHouse_Text_ItsWarmingUpToYou': 'بدأ يألفك ويرتاح إليك.\nالثقة بينكما تكبر كل يوم.', 'PalletTown_ProfessorOaksLab_Text_RivalGoChoosePlayer': '{RIVAL}: هه، لست طماعا مثلك.\nأنا ناضج!\n\nاختر أنت أولا يا {PLAYER}!'}
for _e in ENTRIES:
    if _e['id'] in _FIX:
        _e['ar'] = _FIX[_e['id']]

# ---- Revision 3: plural «البوكيمونات» and player gender ([[masc|fem]]) -----------------
_P = 'PalletTown_'
_R3 = {
 _P+'PlayersHouse_1F_Text_YouShouldTakeQuickRest': 'الأم: {PLAYER}!\n[[تبدو|تبدين]] [[متعبا…|متعبة…]] [[خذ|خذي]] قسطا من الراحة.',
 _P+'PlayersHouse_1F_Text_LookingGreatTakeCare': 'الأم: ها أنت ذا! أنت وبوكيموناتك\nفي أحسن حال.\n[[اعتنِ|اعتني]] بنفسك جيدا!',
 _P+'Text_OakDontGoOut': 'أوك: [[انتظر|انتظري]]! [[قف|قفي]] مكانك!\nلا [[تخرج|تخرجي]]!',
 _P+'Text_OakGrassUnsafeNeedMon': 'أوك: يا لك من [[متهور|متهورة]]!\nفي العشب بوكيمونات برية!\n\nلا [[تخرج|تخرجي]] إليها دون بوكيمون\nيحميك.\n\nآه، وجدتها!\n[[تعال|تعالي]] معي!',
 _P+'Text_RaisingMonsToo': 'أنا أيضا أربي البوكيمونات.\n\nوحين تكبر وتقوى،\nستحميني من أي خطر!',
 _P+'Text_CanStoreItemsAndMonsInPC': 'التقنية مذهلة حقا!\n\nأدواتك وبوكيموناتك، كلها تُحفظ\nفي الحاسوب كبيانات!',
 _P+'Text_CaughtXPuttingInHonestEffort': 'لقد أمسكت {STR_VAR_2}…\n\nهممم، يبدو أنك [[تبذل|تبذلين]] جهدا صادقا.\n\nحين [[تملأ|تملئين]] المزيد منه،\n[[تعال|تعالي]] [[وأرني|وأريني]] إياه من فضلك.',
 _P+'Text_CaughtXImpressiveFollowMe': 'أمسكت… {STR_VAR_2}؟!\nهذا مذهل حقا!\n\nهناك أمر طالما أردت أن أطلبه\nمنك يا {PLAYER}.\n\n[[تعال.|تعالي.]]\n[[اتبعني.|اتبعيني.]]',
 _P+'Text_OakYouEnjoyingTraveling': 'أوك: آه، {PLAYER}!\nيبدو أن السفر يروق لك.\n\nأعرفك جيدا، ولن أستغرب أبدا\nأن [[تبلغ|تبلغي]] أماكن أبعد وأغرب.\n\nأحسنت، أحسنت.\nهوهوهو.',
 _P+'RivalsHouse_Text_ErrandForGrandpaThisWillHelp': 'جدي كلفك بمهمة؟\n\nيا له من كسول!\n[[خذ|خذي]] هذه، ستنفعك في طريقك.',
 _P+'RivalsHouse_Text_PleaseGiveMonsRest': 'ديزي: البوكيمونات كائنات حية،\nتتعب مثلنا تماما.\n\n[[فامنحها|فامنحيها]] قسطا من الراحة\nحين تحتاج إليه.',
 _P+'RivalsHouse_Text_LikeMeToGroomMon': 'ديزي: أهلا {PLAYER}!\nجئت في الوقت المناسب.\n\nكنت على وشك أن أعد الشاي.\nهل [[تشاركني؟|تشاركينني؟]]\n\nلكن انظر!\nبوكيموناتك متسخة قليلا!\n\nهل أنظف لك واحدا منها؟',
 _P+'RivalsHouse_Text_DontNeedAnyGrooming': 'لا [[تحتاج|تحتاجين]] إلى تنظيف؟\nحسنا، سنكتفي بالشاي إذن.',
 _P+'RivalsHouse_Text_GroomWhichOne': 'أيها [[تريد|تريدين]] أن أنظف؟',
 _P+'RivalsHouse_Text_MayISeeFirstMon': 'ديزي: البوكيمونات تحبك إن ربيتها بحب.\n\nمثلا يا {PLAYER}، هل [[تسمح|تسمحين]] لي\nأن أرى أول بوكيمون لديك؟',
 _P+'RivalsHouse_Text_ItsQuiteFriendly': 'إنه ودود معك جدا.\n[[استمر|استمري]] في معاملته بلطف!',
 _P+'RivalsHouse_Text_NotFamiliarWithYouYet': 'لم يعتد عليك تماما بعد.\n\nكل البوكيمونات تكون حذرة\nحين [[تحصل|تحصلين]] عليها أول مرة.',
 _P+'RivalsHouse_Text_DontLikeWayItGlaresAtYou': '{PLAYER}، لا تعجبني طريقة\nتحديقه بك.\n\nهلا حاولت أن [[تكون|تكوني]] ألطف معه قليلا؟',
 _P+'ProfessorOaksLab_Text_RivalGoChoosePlayer': '{RIVAL}: هه، لست طماعا مثلك.\nأنا ناضج!\n\n[[اختر|اختاري]] أنت أولا يا {PLAYER}!',
 _P+'ProfessorOaksLab_Text_RivalLetsCheckOutMons': '{RIVAL}: مهلا يا {PLAYER}!\nلنجرب بوكيمونينا!\n\nهيا، إلى النزال!',
 _P+'ProfessorOaksLab_Text_RivalTellSisNotToGiveYouMap': '{PLAYER}، يؤسفني أن أقولها، لكن\nلا حاجة إليك في هذه المهمة.\n\nوجدتها! سأستعير خريطة البلدات\nمن أختي!\n\nوسأطلب منها ألا تعيرك واحدة\nيا {PLAYER}! هاهاها!\n\nفلا [[تتعب|تتعبي]] نفسك [[وتأتِ|وتأتي]] إلى بيتي!',
 _P+'ProfessorOaksLab_Text_OakThreeMonsChooseOne': 'أوك: {RIVAL}؟\nدعني أتذكر…\n\nآه، نعم! أنا من استدعاك!\nانتظر قليلا!\n\n[[تعال|تعالي]] يا {PLAYER}.\n\nهنا ثلاثة بوكيمونات!\n\nهاها!\n\nإنها تنتظر داخل\nكرات البوكيمون هذه.\n\nفي شبابي، كنت مدرب بوكيمون\nلا يشق له غبار!\n\nأما الآن، وقد شاب شعري،\nفلم يبق لدي سوى هذه الثلاثة.\n\n[[اختر|اختاري]] واحدا منها،\nهيا!',
 _P+'ProfessorOaksLab_Text_OakWhichOneWillYouChoose': 'أوك: والآن يا {PLAYER}…\n\nفي كل كرة من هذه الكرات الثلاث\nبوكيمون ينتظر صاحبه.\n\nأيها [[ستختار؟|ستختارين؟]]',
 _P+'ProfessorOaksLab_Text_OakHeyDontGoAwayYet': 'أوك: مهلا!\nلا [[تذهب|تذهبي]] بعد!',
 _P+'ProfessorOaksLab_Text_OakChoosingCharmander': 'آه! اخترت تشارماندر.\nعليك أن تربيه بصبر.\n\n[[أتختار|أتختارين]] تشارماندر يا {PLAYER}،\nبوكيمون النار؟',
 _P+'ProfessorOaksLab_Text_OakChoosingBulbasaur': 'فهمت! اخترت بولباسور.\nتربيته سهلة جدا.\n\n[[أتنطلق|أتنطلقين]] مع بولباسور يا {PLAYER}،\nبوكيمون العشب؟',
 _P+'ProfessorOaksLab_Text_OakCanReachNextTownWithMon': 'أوك: إن باغتك بوكيمون بري،\nفبوكيمونك سيتصدى له.\n\nومعه إلى جانبك، [[ستبلغ|ستبلغين]]\nالبلدة التالية بأمان.',
 _P+'ProfessorOaksLab_Text_OakBattleMonForItToGrow': 'أوك: {PLAYER}، النزالات هي ما\nيجعل بوكيمونك ينمو.\n\nفلا [[تبخل|تبخلي]] عليه بها!',
 _P+'ProfessorOaksLab_Text_OakHaveSomethingForMe': 'أوك: آه، {PLAYER}!\nكيف حال بوكيموني القديم؟\n\nأرى أنه صار يتعلق بك أكثر.\n\nفيك موهبة حقيقية\n[[كمدرب|كمدربة]] بوكيمون.\n\nما هذا؟\nأحضرت لي شيئا؟',
 _P+'ProfessorOaksLab_Text_OakPokedexOnDesk': 'على المكتب، أحدث اختراعاتي:\nالبوكيديكس!\n\nيسجل تلقائيا بيانات كل بوكيمون\n[[تراه|ترينه]] أو [[تمسكه.|تمسكينه.]]\n\nإنه موسوعة تمشي معك أينما ذهبت!',
 _P+'ProfessorOaksLab_Text_OakCatchMonsForDataTakeThese': 'أوك: لا يمكنك الحصول على بيانات مفصلة\nعن البوكيمونات بمجرد رؤيتها.\n\nعليك أن [[تمسكها|تمسكيها]] لتحصل على\nبيانات كاملة.\n\nإذن، إليك بعض الأدوات\nلإمساك البوكيمونات البرية.',
 _P+'ProfessorOaksLab_Text_OakExplainCatching': 'حين يظهر بوكيمون بري،\nيمكنك أن [[تحاول|تحاولي]] إمساكه.\n\n[[ارمِ|ارمي]] عليه كرة بوكيمون\n[[وجرب|وجربي]] حظك… أقصد مهارتك!\n\nلكنها لن تنجح دائما.\n\nفالبوكيمون في كامل قوته قد يفلت.\nفلا [[تيأس،|تيأسي،]] [[وحاول|وحاولي]] مرة بعد مرة!',
 _P+'ProfessorOaksLab_Text_OakMonsAroundWorldWait': 'البوكيمونات في كل أرجاء العالم\nتنتظرك يا {PLAYER}!',
 _P+'ProfessorOaksLab_Text_OakAddedNothingToPokedex': 'آه، {PLAYER}!\nكيف حال البوكيديكس معك؟\n\nلقد أمسك {RIVAL} بعض البوكيمونات\nوأضاف بياناتها.\n\nإذن يا {PLAYER}، لنلق نظرة\nعلى البوكيديكس الخاص بك.\n\n…ما الخطب؟\nلم [[تضف|تضيفي]] أي بيانات جديدة!\n\nسأعطيك هذه، [[فاجتهد|فاجتهدي]] أكثر\nقليلا.',
 _P+'ProfessorOaksLab_Text_OakComeSeeMeSometime': 'أوك: [[زرني|زوريني]] من حين لآخر.\n\nأريد أن أرى كيف يكبر\nالبوكيديكس بين يديك.',
 _P+'ProfessorOaksLab_Text_DaisyWillGroomMons': 'أهلا، {PLAYER}. أراهن أنك صرت [[صديقا|صديقة]]\n[[مقربا|مقربة]] لبوكيموناتك.\n\nبالمناسبة، هل [[تعرف|تعرفين]] ديزي؟\n\nإن أريت ديزي بوكيموناتك، تستطيع\nأن تعرف كم تحبك.\n\nوأحيانا قد تنظف لك\nأحد بوكيموناتك.\n\nهذا سر، فأرجوك\nلا [[تخبر|تخبري]] أحدا.',
 _P+'ProfessorOaksLab_Text_OakSightingsOfRareMons': 'مؤخرا، شوهدت أنواع كثيرة\nمن البوكيمونات النادرة.\n\nأقصد بوكيمونات لم يرها أحد\nفي كانتو من قبل.\n\nكم أود أن أذهب وأراها بنفسي،\nلكنني كبرت كثيرا.\n\nوبما أنني لا أستطيع، يا {PLAYER}،\nأود أن [[تذهب|تذهبي]] أنت مكاني.',
 _P+'ProfessorOaksLab_Text_RivalJustLetMeHandleEverything': '{RIVAL}: مهلا، لقد سمعت ذلك!\n\nجدي، لماذا تفضّل {PLAYER} علي\nفي كل مرة؟\n\nلقد جمعت بوكيمونات أكثر،\nوبسرعة أكبر أيضا.\n\nعليك أن تترك لي كل شيء.',
 _P+'ProfessorOaksLab_Text_OakNowTheseUnitsCanRecordMoreData': '… … …  … … …\n\n… … …  … … …\n\n…وانتهينا!\n\nالآن يسجل هذان الجهازان بيانات\nعدد أكبر بكثير من البوكيمونات.',
}
for _e in ENTRIES:
    if _e['id'] in _R3:
        _e['ar'] = _R3[_e['id']]

# ---- Revision 4: Mom's first line uses a proverb instead of a literal rendering
_R4 = {
 'PalletTown_PlayersHouse_1F_Text_AllBoysLeaveOakLookingForYou': 'الأم: …أعرف يا بني، أعرف.\n\nلا بد للعصفور أن يغادر عشه\nيوما ما… هكذا قالوا في التلفاز!\n\nآه، صحيح! جارنا البروفيسور أوك\nكان يسأل عنك.',
 'PalletTown_PlayersHouse_1F_Text_AllGirlsLeaveOakLookingForYou': 'الأم: …أعرف يا ابنتي، أعرف.\n\nلا بد للعصفور أن يغادر عشه\nيوما ما… هكذا قالوا في التلفاز!\n\nآه، صحيح! جارنا البروفيسور أوك\nكان يسأل عنك.',
}
for _e in ENTRIES:
    if _e['id'] in _R4:
        _e['ar'] = _R4[_e['id']]
        _e['note'] = '"All boys/girls leave home someday" -> the proverb «لا بد للعصفور أن يغادر عشه يوما ما».'

# ---- Revision 5: verbs whose subject is the player are gendered
_R5 = {'PalletTown_PlayersHouse_2F_Text_PlayedWithNES': '{PLAYER} [[يلعب|تلعب]] بجهاز NES.\n\n…كفى لعبا!\nالمغامرة الحقيقية تنتظر!', 'PalletTown_RivalsHouse_Text_ReceivedTownMapFromDaisy': '[[حصل|حصلت]] {PLAYER} على خريطة البلدات\nمن ديزي.', 'PalletTown_ProfessorOaksLab_Text_ReceivedMonFromOak': '[[حصل|حصلت]] {PLAYER} على {STR_VAR_1}\nمن البروفيسور أوك!', 'PalletTown_ProfessorOaksLab_Text_DeliveredOaksParcel': '[[سلّم|سلّمت]] {PLAYER} طرد أوك.', 'PalletTown_ProfessorOaksLab_Text_ReceivedPokedexFromOak': '[[حصل|حصلت]] {PLAYER} على البوكيديكس\nمن البروفيسور أوك.', 'PalletTown_ProfessorOaksLab_Text_ReceivedFivePokeBalls': '[[حصل|حصلت]] {PLAYER} على خمس كرات بوكيمون.'}
for _e in ENTRIES:
    if _e['id'] in _R5:
        _e['ar'] = _R5[_e['id']]

# ---- Revision 6: Oak's lab lines that read like a translation
_R6 = {'PalletTown_ProfessorOaksLab_Text_OakHaveSomethingForMe': 'أوك: آه، {PLAYER}!\n\nكيف حال البوكيمون الذي أعطيتك إياه؟\n\nيبدو أنه صار يحبك ويتعلق بك أكثر فأكثر.\n\nلا شك أنك [[مدرب موهوب!|مدربة موهوبة!]]\n\nما هذا؟ [[أحضرت|أحضرتِ]] لي شيئا؟', 'PalletTown_ProfessorOaksLab_Text_OakChoosingCharmander': 'آه! اخترت تشارماندر.\nعليك أن تربيه بصبر.\n\n[[أتختار|أتختارين]] إذن تشارماندر، بوكيمون النار، يا {PLAYER}؟', 'PalletTown_ProfessorOaksLab_Text_OakChoosingSquirtle': 'همم! اخترت سكويرتل.\nإنه جدير بالعناية.\n\n[[أتختار|أتختارين]] إذن سكويرتل، بوكيمون الماء، يا {PLAYER}؟', 'PalletTown_ProfessorOaksLab_Text_OakChoosingBulbasaur': 'فهمت! اخترت بولباسور.\nتربيته سهلة جدا.\n\n[[أتختار|أتختارين]] إذن بولباسور، بوكيمون العشب، يا {PLAYER}؟', 'PalletTown_ProfessorOaksLab_Text_OakCatchMonsForDataTakeThese': 'أوك: رؤية البوكيمون وحدها لا تكفي لمعرفة كل شيء عنه.\n\nعليك أن [[تمسكه|تمسكيه]] لتكتمل بياناته.\n\nلذا، إليك بعض الأدوات لإمساك البوكيمونات البرية.', 'PalletTown_ProfessorOaksLab_Text_OakNeedYourHelpTooNeedToSeePokedexes': 'أوك: أعرف، أعرف. بالطبع أحتاج إلى عونك أنت أيضا.\n\nوالآن، أرياني جهازي البوكيديكس.', 'PalletTown_ProfessorOaksLab_Text_PlayersPokedexWasUpgraded': 'لقد طُوِّر بوكيديكس {PLAYER}!', 'PalletTown_ProfessorOaksLab_Text_OakFavorToAskYouPlayer': 'آه، هذا رائع حقا!\n\n{PLAYER}، عندي لك طلب مهم آخر.\n\n[[أصغ|أصغي]] إلي جيدا.'}
for _e in ENTRIES:
    if _e['id'] in _R6:
        _e['ar'] = _R6[_e['id']]
