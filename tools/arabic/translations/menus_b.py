# -*- coding: utf-8 -*-
"""Batch 13 - Menus B: the PCs (player's PC, Pokémon storage, mailbox, Hall of
Fame, PC dialogue), the shop, the Pokédex screens, the trainer card, badge names."""
import menus_a
from menus_a import DIALOG, LABEL, one, SMALL

menus_a.FILES += ['data/text/pc.inc', 'data/event_scripts.s', 'src/pokemon_storage_system_menu.c']
menus_a._CODES = menus_a._CODES[:-1] + '|COLOR|SHADOW)[^}]*\\}' if False else menus_a._CODES.replace('HIGHLIGHT)', 'HIGHLIGHT|COLOR|SHADOW)')
import os
from arabic_text import ROOT
for f in ['data/text/pc.inc', 'data/event_scripts.s', 'src/pokemon_storage_system_menu.c']:
    menus_a._src[f] = open(os.path.join(ROOT, f), encoding='utf-8').read()

def M(label, ar, box=DIALOG, where='', screen='', **kw):
    menus_a.SCREEN = screen
    return menus_a.M(label, ar, box, where, **kw)

X = dict(X1='{DYNAMIC 0x00}')
PCD = ('dialog', 200, 'normal', 2)
DESC = ('dialog', 216, 'normal', 2)
_E = []
S = 'PC'
_E += [
 M('gText_SomeoneSPc', 'حاسوب أحدهم', one(120), screen=S), M('gText_BillSPc', 'حاسوب بيل', one(120), screen=S),
 M('gText_SPc', 'حاسوب {PLAYER}', one(120), screen=S), M('gText_ProfOakSPc', 'حاسوب أوك', one(130), screen=S),
 M('gText_HallOfFame', 'قاعة المشاهير', one(120), screen=S), M('gText_HallOfFame_2', 'قاعة المشاهير', one(120), screen=S),
 M('gText_LogOff', 'خروج', LABEL, screen=S),
 M('Text_AccessWhichPC', 'أي حاسوب تريد أن تستخدم؟', screen=S),
 M('Text_AccessedSomeonesPC', 'تم الدخول إلى حاسوب أحدهم.', screen=S),
 M('Text_OpenedPkmnStorage', 'فُتح نظام تخزين البوكيمونات.', screen=S),
 M('Text_AccessedPlayersPC', 'تم الدخول إلى حاسوب {PLAYER}.', screen=S),
 M('Text_AccessedBillsPC', 'تم الدخول إلى حاسوب بيل.', screen=S),
 M('Text_AccessedProfOaksPC', 'تم الدخول إلى حاسوب البروفيسور أوك…\n\nتم الدخول إلى نظام تقييم\nالبوكيديكس…', screen=S),
 M('gText_ItemStorage', 'تخزين الأدوات', one(120), screen=S), M('gText_Mailbox', 'صندوق البريد', one(120), screen=S),
 M('gText_TurnOff', 'إطفاء', one(120), screen=S),
 M('gText_WithdrawItem', 'سحب\nأداة', ('manual', 64, 'normal', 2), screen=S), M('gText_WithdrawItem2', 'سحب أداة', one(100), screen=S),
 M('gText_DepositItem2', 'إيداع أداة', one(100), screen=S),
 M('gText_DepositItem', 'إيداع أداة', one(100), screen=S, note='Header tab of the bag when depositing into the PC.'),
 M('gText_TakeOutItemsFromThePC', 'أخرج الأدوات من الحاسوب.', DESC, screen=S),
 M('gText_StoreItemsInThePC', 'خزّن الأدوات في الحاسوب.', DESC, screen=S),
 M('gText_GoBackToThePreviousMenu', 'العودة إلى\nالقائمة السابقة.', DESC, screen=S),
 M('gText_WithdrawHowMany', 'كم تريد أن تسحب\nمن {STR_VAR_1}؟', screen=S),
 M('gText_WithdrewQuantItem', 'سحبت {STR_VAR_2}\nمن {STR_VAR_1}.', screen=S),
 M('gText_ThereAreNoItems', 'لا توجد أدوات.', screen=S),
 M('gText_TheresNoMailHere', 'لا يوجد بريد هنا.', screen=S),
 M('gText_WhatWouldYouLikeToDoWithPlayersMail', 'ماذا تريد أن تفعل ببريد\n{STR_VAR_1}؟', screen=S),
 M('gText_MessageWillBeLost', 'ستضيع الرسالة.\nهل أنت متأكد؟', screen=S),
 M('gText_MailReturnedToBagMessageErased', 'أعيد البريد إلى الحقيبة\nوقد مُحيت رسالته.', screen=S),
 M('gText_BagIsFull', 'الحقيبة ممتلئة.', screen=S), M('gText_BagIsFull2', 'الحقيبة ممتلئة.', screen=S),
 M('gOtherText_Read', 'قراءة', LABEL, screen=S), M('gOtherText_MoveToBag', 'إلى الحقيبة', one(80), screen=S),
 M('gOtherText_Give2', 'إعطاء', LABEL, screen=S),
]
S = 'Pokémon storage'
_E += [
 M('gText_WithdrawPokemon', 'سحب بوكيمون', one(110), screen=S), M('gText_DepositPokemon', 'إيداع بوكيمون', one(110), screen=S),
 M('gText_MovePokemon', 'نقل البوكيمونات', one(110), screen=S), M('gText_MoveItems', 'نقل الأدوات', one(110), screen=S),
 M('gText_SeeYa', 'إلى اللقاء!', one(110), screen=S),
 M('gText_WithdrawMonDescription', 'اسحب بوكيمونا إن كانت لديك\nبوكيمونات في الصناديق.', DESC, screen=S),
 M('gText_DepositMonDescription', 'أودع بوكيمونات فريقك في\nأي صندوق تشاء.', DESC, screen=S),
 M('gText_MoveMonDescription', 'انقل البوكيمونات المحفوظة\nفي أي صندوق.', DESC, screen=S),
 M('gText_MoveItemsDescription', 'انقل الأدوات التي تحملها بوكيمونات\nالصناديق أو فريقك.', DESC, screen=S),
 M('gText_SeeYaDescription', 'إلى اللقاء!', DESC, screen=S),
 M('gText_Box', 'الصندوق', LABEL, screen=S),
 M('gText_ExitFromBox', 'الخروج من الصندوق.', one(176), screen=S),
 M('gText_WhatDoYouWantToDo', 'ماذا تريد أن تفعل؟', one(176), screen=S),
 M('gText_WhatWouldYouLikeToDo', 'ماذا تريد أن تفعل؟', one(176), screen=S),
 M('gText_PleasePickATheme', 'اختر موضوعا.', one(176), screen=S),
 M('gText_PickTheWallpaper', 'اختر الخلفية.', one(176), screen=S),
 M('gText_PkmnIsSelected', 'تم اختيار {X1}.', one(176), screen=S, codes=X),
 M('gText_JumpToWhichBox', 'إلى أي صندوق تنتقل؟', one(176), screen=S),
 M('gText_DepositInWhichBox', 'في أي صندوق تودعه؟', one(176), screen=S),
 M('gText_PkmnWasDeposited', 'أُودع {X1}.', one(176), screen=S, codes=X),
 M('gText_BoxIsFull2', 'الصندوق ممتلئ.', one(176), screen=S),
 M('gText_ReleaseThisPokemon', 'أتطلق سراح هذا البوكيمون؟', one(176), screen=S),
 M('gText_PkmnWasReleased', 'أُطلق سراح {X1}.', one(176), screen=S, codes=X),
 M('gText_ByeByePkmn', 'وداعا يا {X1}!', one(176), screen=S, codes=X),
 M('gText_MarkYourPkmn', 'ضع علامة على بوكيمونك.', one(176), screen=S),
 M('gText_ThatsYourLastPkmn', 'هذا آخر بوكيمون لديك!', one(176), screen=S),
 M('gText_YourPartysFull', 'فريقك ممتلئ!', one(176), screen=S),
 M('gText_YoureHoldingAPkmn', 'أنت تحمل بوكيمونا!', one(176), screen=S),
 M('gText_WhichOneWillYouTake', 'أيها ستأخذ؟', one(176), screen=S),
 M('gText_YouCantReleaseAnEgg', 'لا يمكنك إطلاق بيضة.', one(176), screen=S),
 M('gText_ContinueBoxOperations', 'أتواصل عمليات الصندوق؟', one(176), screen=S),
 M('gText_PkmnCameBack', 'عاد {X1}!', one(176), screen=S, codes=X),
 M('gText_WasItWorriedAboutYou', 'هل كان قلقا عليك؟', one(176), screen=S),
 M('gText_FourEllipsesExclamation', '‥ ‥ ‥ ‥ ‥!', one(176), screen=S),
 M('gText_PleaseRemoveTheMail', 'انزع البريد من فضلك.', one(176), screen=S),
 M('gText_GiveToAPkmn', 'أتعطيه لبوكيمون؟', one(176), screen=S),
 M('gText_PlacedItemInBag', 'وُضعت الأداة في الحقيبة.', one(176), screen=S),
 M('gText_NoMoreRoomInBag', 'لا مكان آخر\nفي الحقيبة.', ('manual', 176, 'normal', 2), screen=S),
 M('gText_PutItemInBag', 'أتضع هذه الأداة في الحقيبة؟', one(176), screen=S),
 M('gText_ItemIsNowHeld', 'صار {X1} محمولا.', one(176), screen=S, codes=X),
 M('gText_ChangedToNewItem', 'تغيرت إلى {X1}.', one(176), screen=S, codes=X),
 M('gText_MailCantBeStored', 'لا يمكن تخزين البريد!', one(176), screen=S),
 M('gText_JustOnePkmn', 'لا يمكنك إيداع آخر بوكيمون!', one(176), screen=S),
 M('gText_PartyFull', 'لا يتسع الفريق للمزيد.', one(176), screen=S),
 M('gText_ReturnToPC', 'العودة إلى الحاسوب.', one(176), screen=S),
]
S = 'Shop'
_E += [
 M('gText_ShopBuy', 'شراء', LABEL, screen=S), M('gText_ShopSell', 'بيع', LABEL, screen=S), M('gText_ShopQuit', 'إلى اللقاء!', one(80), screen=S),
 M('gText_QuitShopping', 'إنهاء التسوق.', DESC, screen=S),
 M('gText_AnythingElseICanHelp', 'هل [[تحتاج|تحتاجين]] شيئا آخر؟', screen=S),
 M('gText_Var1CertainlyHowMany', '{STR_VAR_1}؟ بكل سرور.\nكم قطعة [[تريد؟|تريدين؟]]', screen=S),
 M('gText_Var1AndYouWantedVar2', '{STR_VAR_1}، [[وتريد|وتريدين]] {STR_VAR_2}.\nالمجموع ¥{STR_VAR_3}. موافق؟', screen=S),
 M('gText_HereYouGoThankYou', '[[تفضل!|تفضلي!]]\nشكرا لك!', screen=S),
 M('gText_YouDontHaveMoney', 'ليس لديك مال كاف.', screen=S),
 M('gText_NoMoreRoomForThis', 'لا مكان آخر لهذه\nالأداة.', screen=S),
 M('gText_InBagVar1', 'في الحقيبة:{FONT_SMALL} {STR_VAR_1}', one(150), screen=S),
]
S = 'Pokédex'
_E += [
 M('gText_PokedexTableOfContents', 'البوكيديكس   الفهرس', one(200), screen=S),
 M('gText_PokemonList', 'قائمة البوكيمونات', one(140), screen=S), M('gText_PokemonListNoColor', 'قائمة البوكيمونات', one(140), screen=S),
 M('gText_PokemonHabitats', 'مواطن البوكيمونات', one(140), screen=S), M('gText_Search', 'بحث', one(140), screen=S),
 M('gText_SearchNoColor', 'بحث', one(140), screen=S), M('gText_PokedexOther', 'أخرى', one(140), screen=S),
 M('gText_ClosePokedex', 'إغلاق البوكيديكس', one(140), screen=S),
 M('gText_NumericalModeKanto', 'ترتيب رقمي: كانتو', one(140), screen=S),
 M('gText_NumericalModeNational', 'ترتيب رقمي: شامل', one(140), screen=S),
 M('gText_NumericalMode', 'ترتيب رقمي', one(140), screen=S), M('gText_AToZMode', 'ترتيب أبجدي', one(140), screen=S),
 M('gText_TypeMode', 'حسب النوع', one(140), screen=S), M('gText_LightestMode', 'الأخف وزنا', one(140), screen=S),
 M('gText_SmallestMode', 'الأصغر حجما', one(140), screen=S),
 M('gText_DexCategory_GrasslandPkmn', 'بوكيمونات المراعي', one(140), screen=S),
 M('gText_DexCategory_ForestPkmn', 'بوكيمونات الغابات', one(140), screen=S),
 M('gText_DexCategory_WatersEdgePkmn', 'بوكيمونات الشواطئ', one(140), screen=S),
 M('gText_DexCategory_SeaPkmn', 'بوكيمونات البحر', one(140), screen=S),
 M('gText_DexCategory_CavePkmn', 'بوكيمونات الكهوف', one(140), screen=S),
 M('gText_DexCategory_MountainPkmn', 'بوكيمونات الجبال', one(140), screen=S),
 M('gText_DexCategory_RoughTerrainPkmn', 'بوكيمونات البراري', one(140), screen=S),
 M('gText_DexCategory_UrbanPkmn', 'بوكيمونات المدن', one(140), screen=S),
 M('gText_DexCategory_RarePkmn', 'بوكيمونات نادرة', one(140), screen=S),
 M('gText_Seen', 'المشاهدة:', LABEL, screen=S), M('gText_Owned', 'الممسوكة:', LABEL, screen=S),
 M('gText_Kanto', 'كانتو', LABEL, screen=S), M('gText_National', 'شامل', LABEL, screen=S),
 M('gText_Area', 'المنطقة', LABEL, screen=S), M('gText_AreaUnknown', 'منطقة مجهولة', one(100), screen=S),
 M('gText_Size', 'الحجم', LABEL, screen=S), M('gText_Page', 'الصفحة', LABEL, screen=S),
 M('gText_HT', 'الطول', one(40), screen=S), M('gText_WT', 'الوزن', one(40), screen=S), M('gText_Lbs', 'رطل', one(32), screen=S),
 M('gText_Cry', '{START_BUTTON}الصوت', SMALL, screen=S), M('gText_Next', '{A_BUTTON}التالي', SMALL, screen=S),
 M('gText_PickOK', '{DPAD_UPDOWN}اختيار {A_BUTTON}تم', ('line', 140, 'small', 1), screen=S),
 M('gText_PickOKExit', '{DPAD_UPDOWN}اختيار {A_BUTTON}تم {B_BUTTON}إلغاء', ('line', 200, 'small', 1), screen=S),
 M('gText_PickFlipPageCheckCancel', '{DPAD_LEFTRIGHT}اختيار{PLUS}الصفحة {A_BUTTON}تفقّد {B_BUTTON}إلغاء', ('line', 230, 'small', 1), screen=S),
 M('gText_NextDataCancel', '{A_BUTTON}البيانات التالية {B_BUTTON}إلغاء', ('line', 200, 'small', 1), screen=S),
 M('gText_CancelPreviousData', '{A_BUTTON}إلغاء {B_BUTTON}البيانات السابقة', ('line', 200, 'small', 1), screen=S),
]
S = 'Trainer card'
_E += [
 M('gText_TrainerCardName', 'الاسم: ', one(48), screen=S), M('gText_TrainerCardIDNo', 'الهوية', one(40), screen=S),
 M('gText_TrainerCardMoney', 'المال', LABEL, screen=S), M('gText_TrainerCardPokedex', 'البوكيديكس', one(72), screen=S),
 M('gText_TrainerCardTime', 'الوقت', LABEL, screen=S),
 M('gText_Var1sTrainerCard', ': بطاقة المدرب', one(110), screen=S, note='Printed after the name: «AAAB: بطاقة المدرب».'),
 M('gText_HallOfFameDebut', 'أول دخول للقاعة  ', one(120), screen=S),
 M('gText_LinkBattles', 'نزالات الربط', one(120), screen=S), M('gText_LinkCableBattles', 'نزالات الكابل', one(120), screen=S),
 M('gText_PokemonTrades', 'مبادلات البوكيمونات', one(120), screen=S), M('gText_BerryCrushes', 'سحق التوت', one(120), screen=S),
 M('gText_UnionRoomTradesBattles', 'مبادلات ونزالات الاتحاد', one(140), screen=S),
 M('gText_WaitingTrainerFinishReading', 'في انتظار أن ينهي المدرب الآخر\nقراءة بطاقتك.', screen=S),
]
S = 'Badges'
_B = dict(Boulderbadge='وسام الصخرة', Cascadebadge='وسام الشلال', Thunderbadge='وسام الرعد', Rainbowbadge='وسام قوس قزح',
          Soulbadge='وسام الروح', Marshbadge='وسام المستنقع', Volcanobadge='وسام البركان', Earthbadge='وسام الأرض')
_E += [M('gText_' + k, v, one(100), screen=S) for k, v in _B.items()]
ENTRIES = [e for e in _E if e]

README = [
    ('Pokémon FireRed – Arabic translation – Batch 13: menus B', 'title'),
    ('PCs (player\'s PC, Pokémon storage, mailbox, Hall of Fame and the PC dialogue), the shop, the Pokédex screens, '
     'the trainer card and the eight badge names.', 'text'),
    ('The shopkeeper\'s lines are gendered with [[m|f]]. In the storage messages {X1} is the Pokémon or item name.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py menus_b, then make.', 'text'),
    ('Left for later: «… POKéMON» after the Pokédex category (with the Pokédex entries), the trainer card W/L line.', 'text'),
]
GLOSSARY = [
    ('PC', 'الحاسوب', ''), ('POKéMON Storage System', 'نظام تخزين البوكيمونات', ''), ('BOX', 'الصندوق', ''),
    ('WITHDRAW / DEPOSIT / MOVE', 'سحب / إيداع / نقل', ''), ('release', 'أطلق سراح', ''),
    ('BUY / SELL / SEE YA!', 'شراء / بيع / إلى اللقاء!', ''), ('HALL OF FAME', 'قاعة المشاهير', ''),
    ('SEEN / OWNED', 'المشاهدة / الممسوكة', ''), ('NATIONAL (Pokédex)', 'شامل', ''),
    ('Badges', 'وسام الصخرة، الشلال، الرعد، قوس قزح، الروح، المستنقع، البركان، الأرض', 'As in the dialogue.'),
]
