# -*- coding: utf-8 -*-
"""Batch 01 - New game intro: controls guide, adventure intro, Prof. Oak's
speech, name/gender menus, naming screen titles and the L/R HELP screens that
can be opened during the intro.

Each entry: id (label in the source), file, screen, where, box, end, ar, note.
box = (mode, max_px, font, max_lines)
  dialog : 2-line pages; blank line in the Arabic = new page
  static : one screen; blank line = empty line (like the English)
  help   : HELP panel; lines drawn one under the other, no pages
  line   : one line, no wrapping (menus, buttons, titles)
end = 'p' when the English ends with a page prompt before the string ends.
The Arabic here is only the starting point: the review sheet is the source of
truth once it exists (apply_translations.py reads the sheet).
"""

INC_INTRO = 'data/text/new_game_intro.inc'
INC_HELP = 'data/text/help_system.inc'
STRINGS = 'src/strings.c'

DIALOG = ('dialog', 200, 'normal', 2)

ENTRIES = [
    # ---- Top bar (small font) ------------------------------------------------
    dict(id='gText_Controls', file=STRINGS, screen='Top bar', where='Top bar title on the controls guide',
         box=('line', 100, 'small', 1), ar='التحكم',
         note='Short title; the bar is small.'),
    dict(id='gText_ABUTTONNext', file=STRINGS, screen='Top bar', where='Top bar button hint (A)',
         box=('line', 90, 'small', 1), ar='{A_BUTTON}التالي',
         note='Shared with other menus in the game.'),
    dict(id='gText_ABUTTONNext_BBUTTONBack', file=STRINGS, screen='Top bar', where='Top bar button hints (A / B)',
         box=('line', 120, 'small', 1), ar='{A_BUTTON}التالي {B_BUTTON}رجوع',
         note='Shared with other menus in the game.'),

    # ---- Controls guide ------------------------------------------------------
    dict(id='gControlsGuide_Text_Intro', file=INC_INTRO, screen='Controls guide', where='Page 1',
         box=('static', 232, 'normal', 2),
         ar='سنعرّفك على الأزرار واحدا تلو الآخر،\nبحسب أهميتها.'),
    dict(id='gControlsGuide_Text_DPad', file=INC_INTRO, screen='Controls guide', where='Page 2, next to the + Control Pad',
         box=('static', 184, 'normal', 3),
         ar='يحرّك بطل القصة، ويُستخدم أيضا للتنقل بين الخيارات والقوائم.'),
    dict(id='gControlsGuide_Text_AButton', file=INC_INTRO, screen='Controls guide', where='Page 2, next to the A Button',
         box=('static', 184, 'normal', 2),
         ar='للتأكيد، والتفحص، والتحدث إلى الناس، ومتابعة النص.'),
    dict(id='gControlsGuide_Text_BButton', file=INC_INTRO, screen='Controls guide', where='Page 2, next to the B Button',
         box=('static', 184, 'normal', 2),
         ar='للخروج، والتراجع عن اختيارك، وإلغاء الوضع الحالي.'),
    dict(id='gControlsGuide_Text_StartButton', file=INC_INTRO, screen='Controls guide', where='Page 3, next to START',
         box=('static', 184, 'normal', 2),
         ar='اضغط هذا الزر لفتح القائمة.'),
    dict(id='gControlsGuide_Text_SelectButton', file=INC_INTRO, screen='Controls guide', where='Page 3, next to SELECT',
         box=('static', 184, 'normal', 2),
         ar='لترتيب الأدوات، ولاستخدام الأداة المسجّلة بسرعة.',
         note='"Registered item" = the item you assign to SELECT. "أداة مسجّلة" keeps it short; open to a better term.'),
    dict(id='gControlsGuide_Text_LRButtons', file=INC_INTRO, screen='Controls guide', where='Page 3, next to L and R',
         box=('static', 184, 'normal', 3),
         ar='إن احتجت إلى مساعدة في اللعب، أو لم تعرف كيف تقوم بأمر ما، فاضغط زر L أو R.'),

    # ---- Adventure intro (Pikachu pages) --------------------------------------
    dict(id='gPikachuIntro_Text_Page1', file=INC_INTRO, screen='Adventure intro', where='Page 1 (Pikachu)',
         box=('static', 216, 'normal', 7),
         ar='في العالم الذي توشك أن تدخله، تنتظرك مغامرة كبرى… بطلها أنت!\n\n'
            'تحدّث إلى الناس وتفحّص ما حولك في المدن والطرقات والكهوف، واجمع المعلومات من كل مصدر.'),
    dict(id='gPikachuIntro_Text_Page2', file=INC_INTRO, screen='Adventure intro', where='Page 2 (Pikachu)',
         box=('static', 216, 'normal', 7),
         ar='ستنفتح أمامك دروب جديدة كلما ساعدت المحتاجين، وتغلبت على التحديات، وكشفت الألغاز.\n\n'
            'وأحيانا سيتحداك الآخرون، وستهاجمك المخلوقات البرية. فكن شجاعا، وواصل طريقك!'),
    dict(id='gPikachuIntro_Text_Page3', file=INC_INTRO, screen='Adventure intro', where='Page 3 (Pikachu)',
         box=('static', 216, 'normal', 7),
         ar='نأمل أن تلتقي في مغامرتك بأناس من شتى المشارب، وأن تكبر وتنضج مع كل خطوة. فذلك هو هدفنا الأكبر.\n\n'
            'اضغط زر A… ولتبدأ مغامرتك!',
         note='7 lines max: the ▼ arrow sits at the bottom-left. "achieve personal growth" -> "أن تكبر وتنضج مع كل خطوة": warmer than a literal "تحقق نموا شخصيا".'),

    # ---- Prof. Oak -------------------------------------------------------------
    dict(id='gOakSpeech_Text_WelcomeToTheWorld', file=INC_INTRO, screen="Prof. Oak's speech", where='Opening lines',
         box=DIALOG, end='p',
         ar='أهلا وسهلا!\nيسعدني لقاؤك!\n\nمرحبا بك في عالم البوكيمون!\n\nاسمي أوك.\n\nوالناس يلقبونني بمحبة:\nبروفيسور البوكيمون!',
         note='"POKéMON PROFESSOR" -> "بروفيسور البوكيمون", as the Arabic dub calls him البروفيسور أوك.'),
    dict(id='gOakSpeech_Text_ThisWorld', file=INC_INTRO, screen="Prof. Oak's speech", where='Before the Nidorino appears',
         box=DIALOG, ar='هذا العالم…'),
    dict(id='gOakSpeech_Text_IsInhabitedFarAndWide', file=INC_INTRO, screen="Prof. Oak's speech", where='Nidorino on screen',
         box=DIALOG, end='p', ar='…تسكنه في كل أرجائه\nمخلوقات تُدعى البوكيمون!'),
    dict(id='gOakSpeech_Text_IStudyPokemon', file=INC_INTRO, screen="Prof. Oak's speech", where='Nidorino on screen',
         box=DIALOG, end='p',
         ar='للبعض، البوكيمون رفاق أوفياء،\nوللبعض الآخر، شركاء في النزالات.\n\nأما أنا…\n\nفقد كرّست حياتي لدراسة البوكيمون.',
         note='"pets" -> "رفاق أوفياء" (faithful companions) rather than "حيوانات أليفة", closer to how fans see Pokémon; "battling" -> "شركاء في النزالات". Built as a parallel pair (للبعض… وللبعض الآخر…) so each half fills one line.'),
    dict(id='gOakSpeech_Text_TellMeALittleAboutYourself', file=INC_INTRO, screen="Prof. Oak's speech", where='Before the gender question',
         box=DIALOG, end='p', ar='لكن قبل كل شيء،\nحدّثني قليلا عن نفسك.'),
    dict(id='gOakSpeech_Text_AskPlayerGender', file=INC_INTRO, screen="Prof. Oak's speech", where='Gender question (menu opens after)',
         box=DIALOG, ar='والآن أخبرني، هل أنت فتى؟\nأم أنت فتاة؟'),
    dict(id='gText_Boy', file=STRINGS, screen='Gender menu', where='Menu option', box=('line', 56, 'normal', 1), ar='فتى'),
    dict(id='gText_Girl', file=STRINGS, screen='Gender menu', where='Menu option', box=('line', 56, 'normal', 1), ar='فتاة'),
    dict(id='gOakSpeech_Text_YourNameWhatIsIt', file=INC_INTRO, screen="Prof. Oak's speech", where='Asks the player name',
         box=DIALOG, end='p', ar='لنبدأ باسمك.\nما اسمك؟'),
    dict(id='gOtherText_NewName', file=INC_INTRO, screen='Name menu', where='First option in the name list',
         box=('line', 80, 'normal', 1), ar='اسم جديد'),
    dict(id='gText_YourName', file=STRINGS, screen='Naming screen', where='Title when typing the player name',
         box=('line', 120, 'normal', 1), ar='ما اسمك؟'),
    dict(id='gText_RivalsName', file=STRINGS, screen='Naming screen', where='Title when typing the rival name',
         box=('line', 120, 'normal', 1), ar='ما اسم منافسك؟'),
    dict(id='gText_MoveOkBack', file=STRINGS, screen='Naming screen', where='Top bar button hints (shared by every naming screen)',
         box=('line', 150, 'small', 1), ar='{DPAD_ANY}تحريك {A_BUTTON}تم {B_BUTTON}رجوع'),
    dict(id='gOakSpeech_Text_SoYourNameIsPlayer', file=INC_INTRO, screen="Prof. Oak's speech", where='Confirms the player name (YES/NO after)',
         box=DIALOG, ar='حسنا…\nإذن، اسمك {PLAYER}.'),
    dict(id='gText_YesNo', file=STRINGS, screen='Yes/No menu', where='YES/NO menu (whole game)',
         box=('manual', 40, 'normal', 2), ar='نعم\nلا', note='Two lines: first YES, then NO.'),
    dict(id='gText_Yes', file=STRINGS, screen='Yes/No menu', where='YES (whole game)', box=('line', 40, 'normal', 1), ar='نعم'),
    dict(id='gText_No', file=STRINGS, screen='Yes/No menu', where='NO (whole game)', box=('line', 40, 'normal', 1), ar='لا'),
    dict(id='gOakSpeech_Text_WhatWasHisName', file=INC_INTRO, screen="Prof. Oak's speech", where='Introduces the rival',
         box=DIALOG,
         ar='هذا حفيدي.\n\nإنه منافسك منذ نعومة أظفاركما.\n\n…ممم، ما كان اسمه يا ترى؟',
         note='"since you were babies" -> "منذ نعومة أظفاركما", the classic Arabic idiom.'),
    dict(id='gOakSpeech_Text_YourRivalsNameWhatWasIt', file=INC_INTRO, screen="Prof. Oak's speech", where='Asks the rival name',
         box=DIALOG, ar='اسم منافسك… ما كان يا ترى؟'),
    dict(id='gOakSpeech_Text_ConfirmRivalName', file=INC_INTRO, screen="Prof. Oak's speech", where='Confirms the rival name (YES/NO after)',
         box=DIALOG, ar='…أكان اسمه {RIVAL}؟'),
    dict(id='gOakSpeech_Text_RememberRivalsName', file=INC_INTRO, screen="Prof. Oak's speech", where='Rival name chosen',
         box=DIALOG, end='p', ar='صحيح! تذكرت الآن!\nاسمه {RIVAL}!'),
    dict(id='gOakSpeech_Text_LetsGo', file=INC_INTRO, screen="Prof. Oak's speech", where='Last lines, then the player shrinks into the game',
         box=DIALOG,
         ar='{PLAYER}!\n\nأسطورتك مع البوكيمون\nعلى وشك أن تبدأ!\n\nعالم من الأحلام والمغامرات\nينتظرك مع البوكيمون! هيا بنا!',
         note='"Your very own POKéMON legend" -> "أسطورتك مع البوكيمون"; "Let\'s go!" -> "هيا بنا!"'),

    # ---- HELP system (L/R) -----------------------------------------------------
    dict(id='gString_Help', file=STRINGS, screen='Help (L/R)', where='Title, top corner', box=('line', 44, 'normal', 1), ar='مساعدة'),
    dict(id='Help_Text_Greetings', file=INC_HELP, screen='Help (L/R)', where='Welcome text when the help opens',
         box=('help', 204, 'normal', 6),
         ar='أهلا بك! معك نظام المساعدة. استدعني متى وأينما احتجت إليّ، بالضغط على زر L أو R. تتغير رسائل المساعدة لتناسب كل موقف، فلا تنس أن تتفقدها كثيرا!'),
    dict(id='Help_Text_WhatShouldIDo', file=INC_HELP, screen='Help (L/R)', where='Main menu topic', box=('line', 196, 'normal', 1), ar='ماذا أفعل في هذا الموقف؟'),
    dict(id='Help_Text_HowDoIDoThis', file=INC_HELP, screen='Help (L/R)', where='Main menu topic', box=('line', 196, 'normal', 1), ar='كيف أقوم بهذا؟'),
    dict(id='Help_Text_WhatDoesThisTermMean', file=INC_HELP, screen='Help (L/R)', where='Main menu topic', box=('line', 196, 'normal', 1), ar='ما معنى هذا المصطلح؟'),
    dict(id='Help_Text_AboutThisGame', file=INC_HELP, screen='Help (L/R)', where='Main menu topic', box=('line', 196, 'normal', 1), ar='عن هذه اللعبة'),
    dict(id='Help_Text_TypeMatchupList', file=INC_HELP, screen='Help (L/R)', where='Main menu topic', box=('line', 196, 'normal', 1), ar='جدول تفوّق الأنواع',
         note='"Type matchup" -> "تفوّق الأنواع". Alternative: "جدول قوة الأنواع وضعفها" (longer).'),
    dict(id='Help_Text_Exit', file=INC_HELP, screen='Help (L/R)', where='Main menu topic', box=('line', 196, 'normal', 1), ar='خروج'),
    dict(id='Help_Text_Cancel', file=INC_HELP, screen='Help (L/R)', where='List option', box=('line', 196, 'normal', 1), ar='إلغاء'),
    dict(id='Help_Text_DescWhatShouldIDo', file=INC_HELP, screen='Help (L/R)', where='Description under the topic list', box=('help', 204, 'normal', 2),
         ar='اختره لتحصل على تلميحات تعينك في المواقف الصعبة.'),
    dict(id='Help_Text_DescHowDoIDoThis', file=INC_HELP, screen='Help (L/R)', where='Description under the topic list', box=('help', 204, 'normal', 2),
         ar='شرح مفصّل لطريقة القيام بمختلف الأمور.'),
    dict(id='Help_Text_DescWhatDoesThisTermMean', file=INC_HELP, screen='Help (L/R)', where='Description under the topic list', box=('help', 204, 'normal', 2),
         ar='شرح مفصّل للمصطلحات التي تظهر في اللعبة.'),
    dict(id='Help_Text_DescAboutThisGame', file=INC_HELP, screen='Help (L/R)', where='Description under the topic list', box=('help', 204, 'normal', 2),
         ar='معلومات مفصّلة عن هذه اللعبة.'),
    dict(id='Help_Text_DescTypeMatchupList', file=INC_HELP, screen='Help (L/R)', where='Description under the topic list', box=('help', 204, 'normal', 2),
         ar='جدول يبيّن أي أنواع البوكيمون وحركاتها يتفوّق على غيره.'),
    dict(id='Help_Text_DescExit', file=INC_HELP, screen='Help (L/R)', where='Description under the topic list', box=('help', 204, 'normal', 2),
         ar='اختره للخروج من نظام المساعدة.'),
    dict(id='Help_Text_TheHelpSystem', file=INC_HELP, screen='Help (L/R)', where='"About this game" entry', box=('line', 196, 'normal', 1), ar='نظام المساعدة'),
    dict(id='Help_Text_TheGame', file=INC_HELP, screen='Help (L/R)', where='"About this game" entry', box=('line', 196, 'normal', 1), ar='اللعبة'),
    dict(id='Help_Text_WirelessAdapter', file=INC_HELP, screen='Help (L/R)', where='"About this game" entry', box=('line', 196, 'normal', 1), ar='المحوّل اللاسلكي'),
    dict(id='Help_Text_DescTheHelpSystem', file=INC_HELP, screen='Help (L/R)', where='Answer: The HELP System', box=('help', 204, 'normal', 6),
         ar='تتغيّر رسائل المساعدة بحسب تقدّمك في اللعبة، فهي مصممة لتساندك حين تحتاج إليها. وإن صعب عليك فهم أي شيء، فلا تتردد في الرجوع إلى نظام المساعدة!'),
    dict(id='Help_Text_DescTheGame', file=INC_HELP, screen='Help (L/R)', where='Answer: The game', box=('help', 204, 'normal', 6),
         ar='ستصبح بطل القصة، وتستكشف عالم البوكيمون! وكلما تحدثت إلى الناس وكشفت الألغاز، انفتحت أمامك دروب جديدة. فانطلق نحو هدفك برفقة بوكيمونك الرائعين!'),
    dict(id='Help_Text_DescWirelessAdapter', file=INC_HELP, screen='Help (L/R)', where='Answer: Wireless Adapter', box=('help', 204, 'normal', 6),
         ar='تتواصل هذه اللعبة لاسلكيا باستخدام المحوّل اللاسلكي.\n\nالعب لاسلكيا في أي مكان، وفي أي وقت، ومع أي أحد!\n\nجرّب أن تُبقي المحوّل اللاسلكي موصولا دائما أثناء اللعب!'),
    dict(id='Help_Text_EnteringName', file=INC_HELP, screen='Help (L/R)', where='Naming screen: "How do I do this?" entry', box=('line', 196, 'normal', 1), ar='إدخال الاسم'),
    dict(id='Help_Text_HowToEnterName', file=INC_HELP, screen='Help (L/R)', where='Naming screen: answer', box=('manual', 204, 'normal', 7),
         ar='{CIRCLE_1} اختر الحرف بلوحة الاتجاهات {PLUS}،\n   ثم اضغط زر A لإدخاله.\n{CIRCLE_2} اضغط زر B لحذف آخر حرف.\n'
            '{CIRCLE_3} اضغط SELECT للتبديل بين\n   الحروف الكبيرة والصغيرة.\n{CIRCLE_4} اضغط زر A على “OK”.',
         note='Kept line by line like the original (numbered steps). The keyboard and its OK button stay in Latin for now.'),
    dict(id='gText_HelpSystemControls_A_Next', file=STRINGS, screen='Help (L/R)', where='Button hint, bottom bar', box=('line', 120, 'small', 1), ar='{A_BUTTON}التالي'),
    dict(id='gText_HelpSystemControls_PickOkEnd', file=STRINGS, screen='Help (L/R)', where='Button hint, bottom bar', box=('line', 124, 'small', 1),
         ar='{DPAD_UPDOWN}اختيار {A_BUTTON}تم {B_BUTTON}إنهاء'),
    dict(id='gText_HelpSystemControls_AorBtoCancel', file=STRINGS, screen='Help (L/R)', where='Button hint, bottom bar', box=('line', 120, 'small', 1),
         ar='{A_BUTTON}{B_BUTTON}إلغاء'),
    dict(id='gText_HelpSystemControls_PickOkCancel', file=STRINGS, screen='Help (L/R)', where='Button hint, bottom bar', box=('line', 124, 'small', 1),
         ar='{DPAD_UPDOWN}اختيار {A_BUTTON}تم {B_BUTTON}إلغاء'),
]

README = [
    ('Pokémon FireRed – Arabic translation – Batch 01: the new game intro', 'title'),
    ('From pressing NEW GAME until the player lands in the bedroom: controls guide, adventure intro, Prof. Oak, '
     'gender and name menus, naming screen titles, and every L/R HELP screen reachable during the intro.', 'text'),
    ('', 'text'),
    ('What to edit', 'head'),
    ('Only the yellow cells: the "Arabic" column in Translation, and "Your decision" in Glossary. '
     '"Your comments" is free for notes to me.', 'edit'),
    ('Line breaks: Alt+Enter starts a new line. An empty line starts a new page in dialogue boxes '
     '(or leaves an empty line on fixed screens). You do not need to break lines yourself: long lines are '
     'wrapped automatically to the real width of each box.', 'text'),
    ('Keep tokens exactly as they are: {PLAYER}, {RIVAL}, {A_BUTTON}, {B_BUTTON}, {DPAD_UPDOWN}, {DPAD_ANY}, '
     '{PLUS}, {CIRCLE_1}…', 'text'),
    ('Harakat (fatha, damma, shadda, tanween…) are removed automatically: the font has no glyphs for them. '
     'Write normally; they do no harm.', 'text'),
    ('A, B, L, R, START and SELECT stay in Latin letters, as printed on the console. Latin words and numbers inside '
     'an Arabic line are shown left-to-right automatically.', 'text'),
    ('', 'text'),
    ('Columns', 'head'),
    ('Box: the space the text must fit in. On-screen preview: how the text will be split into lines '
     '(——— marks a new page). Fit: OK, or what is too long.', 'text'),
    ('Preview and Fit are refreshed each time you apply the sheet, so they always match your latest Arabic.', 'text'),
    ('', 'text'),
    ('Applying your changes', 'head'),
    ('1.  python3 tools/arabic/apply_translations.py intro', 'text'),
    ('     Wraps and checks every row, writes the Arabic into the source, and updates Preview and Fit here. '
     'A row that does not fit is skipped and listed (the game keeps the previous text).', 'text'),
    ('2.  make', 'text'),
    ('', 'text'),
    ('Open decision', 'head'),
    ('Player and rival names hold 7 bytes, and each Arabic letter takes 2, so an Arabic name could have only 3 letters. '
     'For now the preset names and the naming-screen keyboard stay in Latin; Arabic names need a larger name buffer later.', 'text'),
]

GLOSSARY = [
    ('POKéMON', 'البوكيمون', 'As in the Arabic dub. Same form for one and many; no plural "بوكيمونات".'),
    ('Professor Oak', 'البروفيسور أوك', 'The dub\'s name for him. "POKéMON PROFESSOR" -> "بروفيسور البوكيمون".'),
    ('rival', 'منافس', 'Neutral and friendly; "خصم" sounds hostile for a childhood friend.'),
    ('battle / battling', 'نزال / النزالات', 'A sporting duel, not a war: "معركة" is kept for war-like contexts.'),
    ('pets', 'رفاق أوفياء', 'Faithful companions: how fans see Pokémon, and avoids "حيوانات أليفة".'),
    ('wild creatures', 'المخلوقات البرية', 'Wild Pokémon in general.'),
    ('legend (your POKéMON legend)', 'أسطورة', 'Epic tone of the original.'),
    ('HELP System', 'نظام المساعدة', 'Title shortened to "مساعدة" in the corner label.'),
    ('Type matchup', 'تفوّق الأنواع', 'Short enough for menus. Longer option: "قوة الأنواع وضعفها".'),
    ('item / items', 'أداة / الأدوات', 'Common term among Arab players.'),
    ('registered item', 'الأداة المسجّلة', 'The item assigned to SELECT.'),
    ('MENU', 'القائمة', ''),
    ('+ Control Pad', 'لوحة الاتجاهات', ''),
    ('Wireless Adapter', 'المحوّل اللاسلكي', ''),
    ('NEXT / BACK / CANCEL / END', 'التالي / رجوع / إلغاء / إنهاء', 'Button hints (small font).'),
    ('PICK / OK / MOVE', 'اختيار / تم / تحريك', '"تم" for OK: short enough for the help bar, natural in Arabic menus.'),
    ('YES / NO', 'نعم / لا', 'Used across the whole game.'),
    ('BOY / GIRL', 'فتى / فتاة', 'Matches Oak\'s question "هل أنت فتى؟ أم أنت فتاة؟".'),
    ('A, B, L, R, START, SELECT', '(unchanged)', 'Kept in Latin, as printed on the console.'),
    ('Player / rival names', '(Latin for now)', 'See "Open decision" in Read me: 7-byte name limit.'),
]

# ---- Revision 2: livelier, dub-style wording (instructions stay clear) ------------
REVISED = {
    'gControlsGuide_Text_Intro': ('لنتعرف على الأزرار واحدا تلو الآخر،\nمن الأهم فالأهم.', ''),
    'gControlsGuide_Text_DPad': ('به تقود بطلك في كل اتجاه، وتتنقل بين القوائم والخيارات.', ''),
    'gControlsGuide_Text_AButton': ('زر الفعل: أكّد، تفحّص، تحدّث، وتابع القراءة!', ''),
    'gControlsGuide_Text_BButton': ('زر التراجع: للخروج، والإلغاء، والعودة خطوة إلى الوراء.', ''),
    'gControlsGuide_Text_StartButton': ('افتح به القائمة… ففيها كل ما تحتاجه!', ''),
    'gControlsGuide_Text_SelectButton': ('رتّب به أدواتك، أو استخدم الأداة المسجّلة في لمح البصر.',
        '"Registered item" = the item you assign to SELECT.'),
    'gControlsGuide_Text_LRButtons': ('تهت؟ احترت؟ اضغط زر L أو R، وستأتيك المساعدة في الحال!', ''),
    'gPikachuIntro_Text_Page1': ('العالم الذي توشك أن تدخله ينتظر بطله… وبطله أنت!\n\n'
        'تحدّث إلى كل من تلقاه، وفتّش كل زاوية في المدن والدروب والكهوف. فكل كلمة قد تكون مفتاحا!',
        '7 lines max: the ▼ arrow sits at the bottom-left.'),
    'gPikachuIntro_Text_Page2': ('كلما مددت يد العون لمحتاج، وتجاوزت تحديا، وحللت لغزا، انفتح أمامك درب جديد.\n\n'
        'سيتحداك المدربون، وتباغتك المخلوقات البرية… فتشجّع، ولا تتوقف!', ''),
    'gPikachuIntro_Text_Page3': ('نتمنى أن تلتقي في رحلتك أناسا من كل حدب وصوب، وأن تعود منها أقوى وأحكم. فذلك أجمل ما في المغامرة.\n\n'
        'اضغط زر A… ولتبدأ الحكاية!', '"personal growth" -> "أن تعود منها أقوى وأحكم".'),
    'gOakSpeech_Text_WelcomeToTheWorld': ('أهلا وسهلا!\nكم يسعدني لقاؤك!\n\nمرحبا بك في عالم البوكيمون!\n\nأنا أوك.\n\nوالناس هنا يحبون أن ينادوني:\nبروفيسور البوكيمون!',
        '"POKéMON PROFESSOR" -> "بروفيسور البوكيمون", as the dub calls him البروفيسور أوك.'),
    'gOakSpeech_Text_IsInhabitedFarAndWide': ('…تعيش في كل شبر منه\nمخلوقات مدهشة تدعى البوكيمون!', ''),
    'gOakSpeech_Text_IStudyPokemon': ('للبعض، البوكيمون رفاق أوفياء،\nوللبعض الآخر، شركاء في النزالات.\n\nأما أنا…\n\nفقد وهبت عمري كله لدراستها.',
        '"pets" -> "رفاق أوفياء"; "battling" -> "شركاء في النزالات".'),
    'gOakSpeech_Text_TellMeALittleAboutYourself': ('لكن دعنا مني الآن…\nحدّثني عن نفسك قليلا.', ''),
    'gOakSpeech_Text_AskPlayerGender': ('قل لي، هل أنت فتى؟\nأم أنت فتاة؟', ''),
    'gOakSpeech_Text_YourNameWhatIsIt': ('لنبدأ بالأهم:\nما اسمك؟', ''),
    'gOakSpeech_Text_SoYourNameIsPlayer': ('حسنا…\nإذن، اسمك {PLAYER}!', ''),
    'gOakSpeech_Text_WhatWasHisName': ('هذا حفيدي.\n\nتتنافسان منذ نعومة أظفاركما.\n\n…ممم، ما كان اسمه يا ترى؟',
        '"since you were babies" -> "منذ نعومة أظفاركما".'),
    'gOakSpeech_Text_YourRivalsNameWhatWasIt': ('اسمه… اسمه…\nإنه على طرف لساني!', 'Oak\'s forgetfulness played for a smile.'),
    'gOakSpeech_Text_RememberRivalsName': ('صحيح! تذكرته الآن!\nاسمه {RIVAL}!', ''),
    'gOakSpeech_Text_LetsGo': ('{PLAYER}!\n\nأسطورتك مع البوكيمون\nعلى وشك أن تُكتب!\n\nعالم من الأحلام والمغامرات\nينتظرك! هيا، انطلق!',
        '"is about to unfold" -> "على وشك أن تُكتب".'),
    'Help_Text_Greetings': ('أهلا! أنا نظام المساعدة، رفيقك في كل خطوة. ناديني متى شئت وأينما كنت بزر L أو R. رسائلي تتبدل بحسب الموقف، فلا تتردد في زيارتي!', ''),
    'Help_Text_DescWhatShouldIDo': ('عالق في موقف صعب؟\nهنا تجد التلميح المناسب!', ''),
    'Help_Text_DescHowDoIDoThis': ('شرح خطوة بخطوة لكل ما تريد فعله.', ''),
    'Help_Text_DescWhatDoesThisTermMean': ('كلمة غريبة؟ هنا تجد معناها بالتفصيل.', ''),
    'Help_Text_DescAboutThisGame': ('كل ما تود معرفته عن هذه اللعبة.', ''),
    'Help_Text_DescTypeMatchupList': ('من يغلب من؟\nجدول قوة الأنواع وضعفها.', ''),
    'Help_Text_DescExit': ('للخروج من نظام المساعدة.', ''),
    'Help_Text_DescTheHelpSystem': ('رسائلي تتغير مع تقدمك في القصة، لأقدم لك العون في اللحظة المناسبة. وإن استعصى عليك شيء، فأنا هنا دائما!', ''),
    'Help_Text_DescTheGame': ('أنت بطل هذه الحكاية! جُب عالم البوكيمون، وحدّث أهله، واكشف أسراره، فتنفتح لك الدروب. وانطلق نحو حلمك مع بوكيمونك الرائعين!', ''),
    'Help_Text_DescWirelessAdapter': ('تتواصل هذه اللعبة لاسلكيا عبر المحوّل اللاسلكي.\n\nالعب مع من تشاء، أينما كنت، ومتى شئت!\n\nأبقِ المحوّل موصولا… فالمغامرة أجمل مع الأصدقاء!', ''),
}
for _e in ENTRIES:
    if _e['id'] in REVISED:
        _e['ar'], _note = REVISED[_e['id']]
        if _note:
            _e['note'] = _note

# ---- Revision 2: line-fit fixes
_FIX = {'gOakSpeech_Text_IsInhabitedFarAndWide': '…تعيش في كل شبر منه\nمخلوقات تدعى البوكيمون!'}
for _e in ENTRIES:
    if _e['id'] in _FIX:
        _e['ar'] = _FIX[_e['id']]
