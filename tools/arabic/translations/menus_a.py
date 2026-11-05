# -*- coding: utf-8 -*-
"""Batch 10 - Menus A: start menu (labels and help lines), party menu, summary
screen (labels, nature names, "Met in…" memo), bag, options, saving.

Sound/pause codes at the start or end of a string (PAUSE_UNTIL_PRESS…) are read
from the source and kept automatically. {X1}… stand for codes in the middle."""
import os, re
from arabic_text import ROOT

FILES = ['src/strings.c', 'data/text/save.inc', 'src/data/text/nature_names.h']
_CODES = r'\{(?:PLAY_SE|PAUSE|WAIT_SE|PLAY_BGM|PAUSE_UNTIL_PRESS|PALETTE|COLOR_HIGHLIGHT_SHADOW|HIGHLIGHT)[^}]*\}'
_src = {f: open(os.path.join(ROOT, f), encoding='utf-8').read() for f in FILES}

def _find(label):
    for f, s in _src.items():
        if f.endswith('.inc'):
            m = re.search(r'^%s::\n((?:[ \t]*\.string .*\n)+)' % re.escape(label), s, re.M)
            if m:
                return f, ''.join(re.findall(r'\.string "(.*)"', m.group(1))).rstrip('$')
        else:
            m = re.search(r'\b%s\[\] = _\("(.*?)"\);' % re.escape(label), s)
            if m:
                return f, m.group(1)
    return None, None

DIALOG = ('dialog', 200, 'normal', 2)
LABEL = ('line', 64, 'normal', 1)
def one(px): return ('line', px, 'normal', 1)
SMALL = ('line', 88, 'small', 1)
MEMO = ('static', 216, 'normal', 3)
DESC = ('dialog', 216, 'normal', 2)

def M(label, ar, box=DIALOG, where='', **kw):
    f, text = _find(label)
    if f is None:
        print('menus_a.py: %s not found, skipped' % label)
        return None
    end = 'p' if text.endswith('\\p') else ''
    body = text[:-2] if end else text
    pre = re.match(r'(?:%s)*' % _CODES, body).group(0)
    post = re.search(r'(?:%s)*$' % _CODES, body).group(0)
    d = dict(id=label, file=f, screen=SCREEN, where=where or label.replace('gText_', '').replace('_', ' '),
             box=box, ar=ar, note=kw.pop('note', ''), end=end, prefix=pre, suffix=post)
    d.update(kw)
    return d

_E = []
SCREEN = 'Start menu'
_E += [
 M('gText_MenuPokedex', 'البوكيديكس', one(84), note='The start menu window grows to fit its longest label.'), M('gText_MenuPokemon', 'الفريق', LABEL, note='Same word as the battle menu.'),
 M('gText_MenuBag', 'الحقيبة', LABEL), M('gText_MenuSave', 'حفظ', LABEL), M('gText_MenuOption', 'الإعدادات', LABEL),
 M('gText_MenuExit', 'خروج', LABEL), M('gText_MenuRetire', 'انسحاب', LABEL),
 M('gText_MenuSafariStats', '{STR_VAR_1}/{STR_VAR_2}\nالكرات {STR_VAR_3}', ('manual', 140, 'normal', 2)),
 M('gStartMenuDesc_Pokedex', 'جهاز يسجل أسرار البوكيمون\nكلما صادفتها أو أمسكتها.', DESC),
 M('gStartMenuDesc_Pokemon', 'تفقّد بوكيمون فريقك، رفاقك\nفي الرحلة، ونظّم صفوفها.', DESC),
 M('gStartMenuDesc_Bag', 'حقيبة بجيوب لحفظ ما اشتريته\nأو حصلت عليه أو وجدته.', DESC),
 M('gStartMenuDesc_Player', 'اطّلع على مالك وبيانات\nمغامرتك.', DESC),
 M('gStartMenuDesc_Save', 'احفظ تقدمك كاملا، وخذ\nقسطا من الراحة.', DESC),
 M('gStartMenuDesc_Option', 'اضبط إعدادات اللعبة، كسرعة\nالنص وأسلوب النزال.', DESC),
 M('gStartMenuDesc_Exit', 'أغلق نافذة القائمة.', DESC),
 M('gStartMenuDesc_Retire', 'انسحب من لعبة السفاري، وعد\nإلى مكتب التسجيل.', DESC),
]
SCREEN = 'Saving'
_E += [
 M('gText_WouldYouLikeToSaveTheGame', 'هل تريد حفظ اللعبة؟'),
 M('gText_AlreadySaveFile_WouldLikeToOverwrite', 'هناك ملف محفوظ بالفعل.\nهل تريد الحفظ فوقه؟'),
 M('gText_DifferentGameFile', 'تحذير!\n\nهناك ملف لعبة مختلف محفوظ\nبالفعل.\n\nإن حفظت الآن، فستضيع مغامرة\nالملف الآخر كاملة، بأدواتها وبوكيمونها.\n\nهل أنت متأكد أنك تريد الحفظ الآن\nفوق الملف الآخر؟'),
 M('gText_SavingDontTurnOffThePower', 'جار الحفظ…\nلا تطفئ الجهاز.'),
 M('gText_SavingDontTurnOffThePower2', 'جار الحفظ…\nلا تطفئ الجهاز.'),
 M('gText_PlayerSavedTheGame', 'حفظ {PLAYER} اللعبة.'),
 M('gText_SaveError_PleaseExchangeBackupMemory', 'خطأ في الحفظ.\n\nيرجى تبديل ذاكرة\nالحفظ الاحتياطية.'),
]
SCREEN = 'Summary'
N1, N2, N3 = '{DYNAMIC 0x00}', '{DYNAMIC 0x02}', '{DYNAMIC 0x01}'
C = dict(X1=N1, X2=N2, X3=N3)
_MEMO_NOTE = '{X1} = nature, {X2} = place, {X3} = level: keep them.'
def memo(label, ar): return M(label, ar, MEMO, codes=C, note=_MEMO_NOTE)
_E += [
 M('gText_PokeSum_PageName_PokemonInfo', 'المعلومات', one(100)), M('gText_PokeSum_PageName_PokemonSkills', 'قدرات البوكيمون', one(100)),
 M('gText_PokeSum_PageName_KnownMoves', 'الحركات', one(100)),
 M('gText_PokeSum_Controls_Cancel', '{A_BUTTON}إلغاء', SMALL), M('gText_PokeSum_Controls_Page', '{DPAD_LEFTRIGHT}الصفحة', SMALL),
 M('gText_PokeSum_Controls_PageCancel', '{DPAD_RIGHT}الصفحة {A_BUTTON}إلغاء', SMALL),
 M('gText_PokeSum_Controls_PageDetail', '{DPAD_LEFT}صفحة {A_BUTTON}تفاصيل', SMALL),
 M('gText_PokeSum_Controls_Pick', '{DPAD_UPDOWN}اختيار', SMALL),
 M('gText_PokeSum_Controls_PickDelete', '{DPAD_UPDOWN}اختيار {A_BUTTON}حذف', SMALL),
 M('gText_PokeSum_Controls_PickSwitch', '{DPAD_UPDOWN}اختيار {A_BUTTON}تبديل', SMALL),
 M('gText_PokeSum_ExpPoints', 'الخبرة', LABEL), M('gText_PokeSum_NextLv', 'للترقية', one(72), note='"NEXT LV." -> «للترقية» (to the next level): the label has 72 px.'),
 M('gText_PokeSum_Item_None', 'لا شيء', LABEL), M('gText_PokeSum_NoData', 'لا بيانات', LABEL),
 M('gText_PokeSum_ATrade', 'مبادلة', LABEL), M('gText_Somewhere', 'مكان ما', LABEL), M('gFameCheckerText_Cancel', 'إلغاء', LABEL),
 M('gText_PokeSum_HmMovesCantBeForgotten', 'لا يمكن نسيان حركات\nالأقراص الخاصة الآن.', ('static', 112, 'normal', 3)),
 memo('gText_PokeSum_Met', 'طبيعته: {X1}.\nقابلته في {X2}\nفي المستوى {X3}.'),
 memo('gText_PokeSum_Met_BoldGentleGrammar', 'طبيعته: {X1}.\nقابلته في {X2}\nفي المستوى {X3}.'),
 memo('gText_PokeSum_MetInATrade', 'طبيعته: {X1}.\nحصلت عليه بالمبادلة.'),
 memo('gText_PokeSum_MetInATrade_BoldGentleGrammar', 'طبيعته: {X1}.\nحصلت عليه بالمبادلة.'),
 memo('gText_PokeSum_Hatched', 'طبيعته: {X1}.\nفقس في {X2}\nفي المستوى {X3}.'),
 memo('gText_PokeSum_Hatched_BoldGentleGrammar', 'طبيعته: {X1}.\nفقس في {X2}\nفي المستوى {X3}.'),
 memo('gText_PokeSum_FatefulEncounterMet', 'طبيعته: {X1}.\nلقاء استثنائي\nفي المستوى {X3}.'),
 memo('gText_PokeSum_FatefulEncounterMet_BoldGentleGrammar', 'طبيعته: {X1}.\nلقاء استثنائي\nفي المستوى {X3}.'),
 memo('gText_PokeSum_FatefulEncounterHatched', 'طبيعته: {X1}. لقاء استثنائي\n(فقس في {X2}\nفي المستوى {X3}).'),
 memo('gText_PokeSum_FatefulEncounterHatched_BoldGentleGrammar', 'طبيعته: {X1}. لقاء استثنائي\n(فقس في {X2}\nفي المستوى {X3}).'),
 memo('gText_PokeSum_ApparentlyMet', 'طبيعته: {X1}.\nيبدو أنك قابلته في {X2}\nفي المستوى {X3}.'),
 memo('gText_PokeSum_ApparentlyMet_BoldGentleGrammar', 'طبيعته: {X1}.\nيبدو أنك قابلته في {X2}\nفي المستوى {X3}.'),
 memo('gText_PokeSum_ApparentlyFatefulEncounterHatched', 'طبيعته: {X1}. لقاء استثنائي\n(فقس في {X2}\nفي المستوى {X3}).'),
 memo('gText_PokeSum_ApparentlyFatefulEncounterHatched_BoldGentleGrammar', 'طبيعته: {X1}. لقاء استثنائي\n(فقس في {X2}\nفي المستوى {X3}).'),
 M('gText_PokeSum_EggHatch_AlmostReady', 'تصدر منها أصوات.\nتكاد تفقس!', ('static', 112, 'normal', 3)),
 M('gText_PokeSum_EggHatch_Soon', 'تتحرك أحيانا.\nستفقس قريبا.', ('static', 112, 'normal', 3)),
 M('gText_PokeSum_EggHatch_SomeTime', 'ماذا سيخرج منها؟\nسيستغرق ذلك\nبعض الوقت.', ('static', 112, 'normal', 3)),
 M('gText_PokeSum_EggHatch_LongTime', 'تحتاج هذه البيضة\nوقتا طويلا\nحتى تفقس.', ('static', 112, 'normal', 3)),
 M('gText_PokeSum_EggOrigin_DayCare', 'بيضة بوكيمون غريبة وجدها\nزوجا دار الرعاية.', MEMO),
 M('gText_PokeSum_EggOrigin_NicePlace', 'بيضة بوكيمون عجيبة حصلت\nعليها في مكان جميل.', MEMO),
 M('gText_PokeSum_EggOrigin_Spa', 'بيضة بوكيمون غريبة أهدتك\nإياها سيدة عجوز في المنتجع.', MEMO),
 M('gText_PokeSum_EggOrigin_Trade', 'بيضة بوكيمون غريبة حصلت\nعليها بالمبادلة.', MEMO),
 M('gText_PokeSum_EggOrigin_TravelingMan', 'بيضة بوكيمون غريبة أعطاك\nإياها الرجل الرحالة.', MEMO),
]
SCREEN = 'Natures'
_NAT = dict(Hardy='صلب', Lonely='وحيد', Brave='شجاع', Adamant='عنيد', Naughty='مشاغب', Bold='جريء', Docile='مطيع',
            Relaxed='مسترخ', Impish='شقي', Lax='متراخ', Timid='خجول', Hasty='متعجل', Serious='جاد', Jolly='مرح',
            Naive='ساذج', Modest='متواضع', Mild='لطيف', Quiet='هادئ', Bashful='حيي', Rash='متهور', Calm='رزين',
            Gentle='رقيق', Sassy='سليط', Careful='حذر', Quirky='غريب الأطوار')
_E += [M('s%sNatureName' % k, v, one(90), where=k) for k, v in _NAT.items()]
SCREEN = 'Options'
_E += [
 M('gText_Option', 'الإعدادات', one(100)), M('gText_TextSpeed', 'سرعة النص', one(100)), M('gText_TextSpeedSlow', 'بطيء', LABEL),
 M('gText_TextSpeedMid', 'متوسط', LABEL), M('gText_TextSpeedFast', 'سريع', LABEL), M('gText_BattleScene', 'مشاهد النزال', one(100)),
 M('gText_BattleSceneOn', 'تشغيل', LABEL), M('gText_BattleSceneOff', 'إيقاف', LABEL), M('gText_BattleStyle', 'أسلوب النزال', one(100)),
 M('gText_BattleStyleShift', 'تبديل', LABEL), M('gText_BattleStyleSet', 'ثابت', LABEL), M('gText_Sound', 'الصوت', one(100)),
 M('gText_SoundMono', 'أحادي', LABEL), M('gText_SoundStereo', 'مجسم', LABEL), M('gText_ButtonMode', 'وضع الأزرار', one(100)),
 M('gText_ButtonTypeHelp', 'مساعدة', LABEL), M('gText_Frame', 'الإطار', one(100)), M('gText_FrameType', 'نوع', LABEL),
 M('gText_OptionMenuCancel', 'إلغاء', one(100)),
 M('gText_PickSwitchCancel', '{DPAD_UPDOWN}اختيار {DPAD_LEFTRIGHT}تغيير {A_BUTTON}{B_BUTTON}إلغاء', ('line', 230, 'small', 1)),
]
SCREEN = 'Bag'
_E += [
 M('gText_Items2', 'الأدوات', LABEL), M('gText_KeyItems2', 'أدوات مهمة', LABEL), M('gText_PokeBalls2', 'الكرات', LABEL),
 M('gOtherText_Use', 'استخدام', LABEL), M('gOtherText_Give', 'إعطاء', LABEL), M('gOtherText_Toss', 'رمي', LABEL),
 M('gOtherText_Register', 'تسجيل', LABEL), M('gText_Register', 'تسجيل', LABEL), M('gOtherText_Deselect', 'فك التسجيل', one(80)),
 M('gOtherText_Check', 'تفقّد', LABEL), M('gOtherText_Open', 'فتح', LABEL), M('gOtherText_Walk', 'مشي', LABEL),
 M('gText_CloseBag', 'إغلاق الحقيبة', one(90)),
 M('gText_TossOutHowManyStrVar1s', 'كم تريد أن ترمي\nمن {STR_VAR_1}؟'),
 M('gText_ThrowAwayStrVar2OfThisItemQM', 'أترمي {STR_VAR_2} من\nهذه الأداة؟'),
 M('gText_ThrewAwayStrVar2StrVar1s', 'رميت {STR_VAR_2}\nمن {STR_VAR_1}.'),
 M('gText_DepositHowManyStrVars1', 'كم تريد أن تودع\nمن {STR_VAR_1}؟'),
 M('gText_DepositedStrVar2StrVar1s', 'أودعت {STR_VAR_2}\nمن {STR_VAR_1}.'),
 M('gText_HowManyWouldYouLikeToSell', '{STR_VAR_1}؟\nكم تريد أن تبيع؟'),
 M('gText_ICanPayThisMuch_WouldThatBeOkay', 'أستطيع أن أدفع ¥{STR_VAR_3}.\nهل يناسبك هذا؟'),
 M('gText_TurnedOverItemsWorthYen', 'بعت {STR_VAR_1}\nمقابل ¥{STR_VAR_3}.'),
 M('gText_OhNoICantBuyThat', '{STR_VAR_1}؟ لا، للأسف.\nلا أستطيع شراء هذا.'),
 M('gOtherText_WhereShouldTheStrVar1BePlaced', 'أين تريد أن تضع\n{STR_VAR_1}؟'),
 M('gText_Var1IsSelected', 'تم اختيار\n{STR_VAR_1}.'),
 M('gText_ItemCantBeHeld', 'لا يمكن حمل {STR_VAR_1}.'),
 M('gText_NoRoomToStoreItems', 'لا مكان لحفظ\nالأدوات.'),
 M('gText_ThereIsNoPokemon', 'لا يوجد\nبوكيمون.'),
 M('gText_BoxFull', 'الصندوق ممتلئ.'),
 M('gText_CantDismountBike', 'لا يمكنك النزول عن\nالدراجة هنا.'),
 M('gText_CantWriteMailHere', 'لا يمكنك كتابة\nالبريد هنا.'),
 M('gText_CoinCase', 'قطعك النقدية:\n{STR_VAR_1}'),
 M('gText_PowderQty', 'كمية المسحوق: {STR_VAR_1}'),
 M('gText_OakForbidsUseOfItemHere', 'أوك: {PLAYER}!\nليس هذا وقت استخدامه!'),
 M('gText_PlayerUsedVar2', 'استخدم {PLAYER}\n{STR_VAR_2}.'),
 M('gText_UsedVar2WildLured', 'استخدم {PLAYER}\n{STR_VAR_2}.\n\nستنجذب البوكيمون البرية.'),
 M('gText_UsedVar2WildRepelled', 'استخدم {PLAYER}\n{STR_VAR_2}.\n\nستبتعد البوكيمون البرية.'),
 M('gText_RepelEffectsLingered', 'لكن أثر الطارد السابق\nما زال قائما.'),
 M('gText_PlayedPokeFlute', 'عزفت على ناي البوكيمون.'),
 M('gText_PlayedPokeFluteCatchy', 'عزفت على ناي البوكيمون.\n\nيا له من لحن جميل!'),
 M('gText_PokeFluteAwakenedMon', 'أيقظ ناي البوكيمون\nالبوكيمون النائمة.'),
 M('gText_WontHaveEffect', 'لن يكون له أي أثر.'),
]
SCREEN = 'Party menu'
P1 = one(168)
_E += [
 M('gText_ChoosePokemon', 'اختر بوكيمون.', P1), M('gText_ChoosePokemon2', 'اختر بوكيمون.', P1),
 M('gText_ChoosePokemonCancel', 'اختر بوكيمون أو ألغِ.', P1), M('gText_ChoosePokemonConfirm', 'اختر بوكيمون وأكّد.', P1),
 M('gText_DoWhatWithPokemon', 'ماذا ستفعل به؟', one(128), note='One line in a 128 px box.'),
 M('gText_DoWhatWithItem', 'ماذا تفعل بالأداة؟', one(152)), M('gText_DoWhatWithMail', 'ماذا تفعل بالبريد؟', one(128)),
 M('gText_RestoreWhichMove', 'استعد PP أي حركة؟', one(120)), M('gText_BoostPp', 'ارفع PP أي حركة؟', one(120)),
 M('gText_MoveToWhere', 'إلى أين؟', P1), M('gText_GiveToWhichPokemon', 'لأي بوكيمون تعطيها؟', P1),
 M('gText_UseOnWhichPokemon', 'على أي بوكيمون؟', P1), M('gText_TeachWhichPokemon', 'علّم أي بوكيمون؟', P1),
 M('gText_Summary5', 'الملخص', LABEL), M('gText_Switch2', 'تبديل', LABEL), M('gText_Item', 'أداة', LABEL),
 M('gText_Mail', 'بريد', LABEL), M('gText_Take', 'أخذ', LABEL), M('gText_Take2', 'أخذ', LABEL), M('gText_Read2', 'قراءة', LABEL),
 M('gText_Shift', 'تبديل', LABEL), M('gText_SendOut', 'إرسال', LABEL), M('gText_Store', 'إيداع', LABEL),
 M('gText_Enter', 'دخول', LABEL), M('gText_NoEntry', 'لا دخول', LABEL), M('gText_Trade4', 'مبادلة', LABEL),
 M('gText_PartyMenu_OK', 'تم', one(40)), M('gOtherText_Exit', 'خروج', LABEL),
 M('gText_Able', 'يستطيع', LABEL), M('gText_Able2', 'يستطيع', LABEL), M('gText_Able3', 'يستطيع!', LABEL),
 M('gText_NotAble', 'لا يستطيع', LABEL), M('gText_NotAble2', 'لا يستطيع', LABEL), M('gText_Learned', 'تعلّمها', LABEL),
 M('gText_First_PM', 'الأول', LABEL), M('gText_Second_PM', 'الثاني', LABEL), M('gText_Third_PM', 'الثالث', LABEL),
 M('gText_ItemEffect_HP', 'HP', LABEL), M('gText_ItemEffect_Attack', 'الهجوم', LABEL), M('gText_ItemEffect_Defense', 'الدفاع', LABEL),
 M('gText_ItemEffect_SpAtk', 'الهجوم الخاص', one(80)), M('gText_ItemEffect_SpDef', 'الدفاع الخاص', one(80)),
 M('gText_ItemEffect_Speed', 'السرعة', LABEL),
 M('gText_CutATreeOrGrass', 'اقطع شجرة أو عشبا.', one(144)), M('gText_FlyToAKnownTown', 'طر إلى بلدة تعرفها.', one(144)),
 M('gText_TravelOnWater', 'اعبر الماء.', one(144)), M('gText_MoveHeavyBoulders', 'حرّك الصخور الثقيلة.', one(144)),
 M('gText_LightUpDarkness', 'أضئ الظلام.', one(144)), M('gText_ShatterACrackedRock', 'حطّم صخرة متشققة.', one(144)),
 M('gText_ClimbAWaterfall', 'تسلّق شلالا.', one(144)), M('gText_EscapeFromHere', 'اهرب من هنا.', one(144)),
 M('gText_ReturnToAHealingSpot', 'عد إلى مكان علاج.', one(144)), M('gText_ShareHp', 'شارك HP.', one(144)),
 M('gText_LureWildPokemon', 'اجذب البوكيمون البرية.', one(144)),
 M('gText_NoUse', 'لا فائدة.'), M('gText_NotEnoughHp', 'HP غير كافية‥'), M('gText_CantUseHere', 'لا يمكن استخدام ذلك هنا.'),
 M('gText_AlreadySurfing', 'أنت تركب الموج بالفعل.'), M('gText_CantSurfHere', 'لا ركوب للموج هنا!'),
 M('gText_CurrentIsTooFast', 'التيار سريع جدا!'), M('gText_NothingToCut', 'لا شيء هنا لتقطعه.'),
 M('gText_EnjoyCycling', 'لنستمتع بركوب الدراجة!'), M('gText_InUseAlready_PM', 'هذا مستخدم بالفعل.'),
 M('gText_NoIdenticalHoldItems', 'لا أدوات محمولة متطابقة!'), M('gText_PokemonCantBeSame', 'لا يمكن أن يتكرر البوكيمون.'),
 M('gText_ThatIsntAnEgg', 'هذه ليست بيضة.'), M('gText_TwoPokemonAreNeeded', 'يلزم بوكيمونان.'),
 M('gText_ThreePkmnAreNeeded', 'يلزم ثلاثة بوكيمون.'), M('gText_CancelBattle', 'أتلغي النزال؟'),
 M('gText_CancelParticipation', 'أتلغي المشاركة؟'), M('gText_NoPokemonForBattle', 'لا نزال بهذه الطريقة!'),
 M('gText_EggCantBattle', 'البيضة لا تستطيع النزال!'), M('gText_EggCantBeTradedNow', 'لا يمكن مبادلة البيضة الآن.'),
 M('gText_PkmnCantParticipate', 'هذا البوكيمون لا يستطيع\nالمشاركة.'),
 M('gText_NoMoreThanTwoMayEnter', 'لا يدخل أكثر من بوكيمونين.'),
 M('gText_NoMoreThanThreeMayEnter', 'لا يدخل أكثر من ثلاثة\nبوكيمون.'),
 M('gText_CantUseUntilNewBadge', 'لا يمكن استخدام هذا حتى\nتنال وساما جديدا.'),
 M('gText_CantSwitchWithAlly', 'لا يمكنك تبديل بوكيمون {STR_VAR_1}\nبأحد بوكيموناتك!'),
 M('gText_CantTradeWithTrainer', 'لا يمكنك المبادلة مع هذا\nالمدرب الآن.'),
 M('gText_NotPkmnOtherTrainerWants', 'هذا ليس البوكيمون الذي\nيريده المدرب الآخر.'),
 M('gText_OtherTrainerCantAcceptPkmn', 'لا يستطيع المدرب الآخر قبول\nهذا البوكيمون الآن.'),
 M('gText_OtherTrainersPkmnCantBeTraded', 'لا يمكن مبادلة بوكيمون\nالمدرب الآخر الآن.'),
 M('gText_PkmnCantBeTradedNow', 'لا يمكن مبادلة هذا\nالبوكيمون الآن.'),
 M('gText_EscapeFromHereAndReturnTo', 'أتريد الهرب من هنا والعودة\nإلى {STR_VAR_1}؟'),
 M('gText_ReturnToHealingSpot', 'أتريد العودة إلى آخر مكان\nعلاج في {STR_VAR_1}؟'),
 M('gText_MailMessageWillBeLost', 'إن نزعت البريد، ستضيع\nرسالته. موافق؟'),
 M('gText_SendMailToPC', 'أترسل البريد المنزوع\nإلى حاسوبك؟'),
 M('gText_MailSentToPC', 'أُرسل البريد إلى حاسوبك.'),
 M('gText_MailTakenFromPkmn', 'أُخذ البريد من\nالبوكيمون.'),
 M('gText_MailTransferredFromMailbox', 'نُقل البريد من\nصندوق البريد.'),
 M('gText_PCMailboxFull', 'صندوق بريد حاسوبك ممتلئ.'),
 M('gText_RemoveMailBeforeItem', 'يجب نزع البريد قبل\nحمل أداة.'),
 M('gText_PkmnHoldingItemCantHoldMail', 'هذا البوكيمون يحمل أداة.\nلا يستطيع حمل البريد.'),
 M('gText_BagFullCouldNotRemoveItem', '{STR_VAR_1} ممتلئ. تعذّر نزع\nأداة البوكيمون.'),
 M('gText_PkmnWasGivenItem', 'أُعطي {STR_VAR_1}\n{STR_VAR_2} ليحمله.'),
 M('gText_ReceivedItemFromPkmn', 'حصلت على {STR_VAR_2}\nمن {STR_VAR_1}.'),
 M('gText_PkmnNotHolding', '{STR_VAR_1} لا يحمل\nأي شيء.'),
 M('gText_PkmnAlreadyHoldingItemSwitch', '{STR_VAR_1} يحمل {STR_VAR_2}\nبالفعل.\n\nهل تريد تبديل الأداتين؟'),
 M('gText_SwitchedPkmnItem', 'أُخذ {STR_VAR_2} ووُضع\n{STR_VAR_1} مكانه.'),
 M('gText_PkmnAlreadyInBattle', '{STR_VAR_1} في النزال\nبالفعل!'),
 M('gText_PkmnAlreadySelected', 'تم اختيار {STR_VAR_1}\nبالفعل.'),
 M('gText_PkmnCantSwitchOut', 'لا يمكن تبديل {STR_VAR_1}!'),
 M('gText_PkmnHasNoEnergy', 'لم تبق لدى {STR_VAR_1} طاقة\nللنزال!'),
 M('gText_PkmnHPRestoredByVar2', 'استعاد {STR_VAR_1}\n{STR_VAR_2} نقطة من HP.'),
 M('gText_PkmnBecameHealthy', 'عاد {STR_VAR_1} سليما معافى.'),
 M('gText_PkmnBurnHealed', 'شُفي {STR_VAR_1} من الحروق.'),
 M('gText_PkmnCuredOfParalysis', 'شُفي {STR_VAR_1}\nمن الشلل.'),
 M('gText_PkmnCuredOfPoison', 'شُفي {STR_VAR_1}\nمن التسمم.'),
 M('gText_PkmnThawedOut', 'ذاب الجليد عن {STR_VAR_1}.'),
 M('gText_PkmnWokeUp2', 'استيقظ {STR_VAR_1}.'),
 M('gText_PkmnSnappedOutOfConfusion', 'استعاد {STR_VAR_1}\nصوابه.'),
 M('gText_PkmnGotOverInfatuation', 'تحرر {STR_VAR_1}\nمن الافتتان.'),
 M('gText_PPWasRestored', 'استُعيدت PP.'),
 M('gText_MovesPPIncreased', 'ازدادت PP لدى {STR_VAR_1}.'),
 M('gText_PkmnBaseVar2StatIncreased', 'ارتفعت قيمة {STR_VAR_2} الأساسية\nلدى {STR_VAR_1}.'),
 M('gText_PkmnElevatedToLvVar2', 'ارتقى {STR_VAR_1} إلى\nالمستوى {STR_VAR_2}.'),
 M('gText_PkmnLearnedMove3', 'تعلّم {STR_VAR_1}\n{STR_VAR_2}!'),
 M('gText_PkmnAlreadyKnows', '{STR_VAR_1} يعرف\n{STR_VAR_2} بالفعل.'),
 M('gText_PkmnCantLearnMove', '{STR_VAR_1} و{STR_VAR_2}\nغير متوافقين.\n\nلا يمكن تعلّم {STR_VAR_2}.'),
 M('gText_MoveNotLearned', 'لم يتعلّم {STR_VAR_1}\nحركة {STR_VAR_2}.'),
 M('gText_PkmnNeedsToReplaceMove', 'يريد {STR_VAR_1} أن يتعلّم\nحركة {STR_VAR_2}.\n\nلكن {STR_VAR_1} يعرف أربع\nحركات بالفعل.\n\nهل تحذف حركة وتضع مكانها\n{STR_VAR_2}؟'),
 M('gText_StopLearningMove2', 'أتتوقف عن تعليمه\n{STR_VAR_2}؟'),
 M('gText_WhichMoveToForget', 'أي حركة تريد أن يَنساها؟'),
 M('gText_12PoofForgotMove', '1، {X1}2، و{X1}‥ {X1}‥ {X1}‥ {X1}{X2}فوووف!\n\nنسي {STR_VAR_1} كيف\nيستخدم {STR_VAR_2}.\n\nو…',
   codes=dict(X1='{PAUSE 0x0F}', X2='{PLAY_SE SE_BALL_BOUNCE_1}'), note='{X1} pauses, {X2} the "poof" sound.'),
 M('gText_OakImportantToGetToKnowPokemonThroughly', 'أوك: من المهم أن تعرف\nبوكيمونك حق المعرفة.'),
 M('gText_OakThisIsListOfPokemon', 'هذه قائمة بوكيمونك\nيا {PLAYER}.\n\nافتحها لتتفقد قدرات بوكيمونك\nوحركاتها.\n\nومنها تختار البوكيمون أيضا\nإن أردت استخدام أداة عليه.'),
]
ENTRIES = [e for e in _E if e]

README = [
    ('Pokémon FireRed – Arabic translation – Batch 10: menus A', 'title'),
    ('Start menu and its help lines, saving, the summary screen (labels, page names, nature names, the "Met in…" memo), '
     'options, the bag, and the party menu (prompts, actions, field moves, item-use messages).', 'text'),
    ('Some prompts are ONE line in a narrow box (e.g. "Do what with this POKéMON?" has 128 px): the Box column says so.', 'edit'),
    ('In the memo lines {X1} = nature, {X2} = place, {X3} = level. Sound/pause codes are kept automatically.', 'text'),
    ('Applying: python3 tools/arabic/apply_translations.py menus_a, then make.', 'text'),
    ('Still English: map names in the memo (map-names batch), the summary\'s page graphics and type badges (graphics).', 'text'),
]
GLOSSARY = [
    ('POKéMON (start menu)', 'الفريق', 'Same as the battle menu.'),
    ('OPTION', 'الإعدادات', ''), ('SUMMARY', 'الملخص', ''), ('SWITCH / SHIFT', 'تبديل', ''),
    ('USE / GIVE / TOSS / REGISTER', 'استخدام / إعطاء / رمي / تسجيل', ''),
    ('KEY ITEMS / POKé BALLS (pockets)', 'أدوات مهمة / الكرات', ''),
    ('nature', 'طبيعته: …', 'Memo line: «طبيعته: جريء.»'),
    ('fateful encounter', 'لقاء استثنائي', 'Event Pokémon; avoids «قدر».'),
    ('DAY-CARE', 'دار الرعاية', ''), ('SPA', 'المنتجع', ''),
    ('Natures', 'صلب، وحيد، شجاع، عنيد، مشاغب، جريء، مطيع، مسترخ، شقي، متراخ، خجول، متعجل، جاد، مرح، ساذج، متواضع، لطيف، هادئ، حيي، متهور، رزين، رقيق، سليط، حذر، غريب الأطوار', ''),
]

# ---- Revision 3: plural «البوكيمونات» and player gender ([[masc|fem]]) -----------------
_R3 = {'gStartMenuDesc_Pokemon': 'تفقّد بوكيمونات فريقك، رفاقك\nفي الرحلة، ونظّم صفوفها.', 'gText_NoMoreThanThreeMayEnter': 'لا يدخل أكثر من ثلاثة\nبوكيمونات.', 'gText_ThreePkmnAreNeeded': 'يلزم ثلاثة بوكيمونات.', 'gText_PokeFluteAwakenedMon': 'أيقظ ناي البوكيمون\nالبوكيمونات النائمة.', 'gText_OakImportantToGetToKnowPokemonThroughly': 'أوك: من المهم أن [[تعرف|تعرفي]]\nبوكيموناتك حق المعرفة.', 'gText_OakThisIsListOfPokemon': 'هذه قائمة بوكيموناتك\nيا {PLAYER}.\n\nافتحها [[لتتفقد|لتتفقدي]] قدرات بوكيموناتك\nوحركاتها.\n\nومنها [[تختار|تختارين]] البوكيمون أيضا\nإن أردت استخدام أداة عليه.', 'gText_UsedVar2WildLured': 'استخدم {PLAYER}\n{STR_VAR_2}.\n\nستنجذب البوكيمونات البرية.', 'gText_UsedVar2WildRepelled': 'استخدم {PLAYER}\n{STR_VAR_2}.\n\nستبتعد البوكيمونات البرية.', 'gText_LureWildPokemon': 'اجذب البوكيمونات.'}
for _e in ENTRIES:
    if _e['id'] in _R3:
        _e['ar'] = _R3[_e['id']]

# ---- Revision 5: verbs whose subject is the player are gendered
_R5 = {'gText_PlayerSavedTheGame': '[[حفظ|حفظت]] {PLAYER} اللعبة.', 'gText_PlayerUsedVar2': '[[استخدم|استخدمت]] {PLAYER}\n{STR_VAR_2}.', 'gText_UsedVar2WildLured': '[[استخدم|استخدمت]] {PLAYER}\n{STR_VAR_2}.\n\nستنجذب البوكيمونات البرية.', 'gText_UsedVar2WildRepelled': '[[استخدم|استخدمت]] {PLAYER}\n{STR_VAR_2}.\n\nستبتعد البوكيمونات البرية.'}
for _e in ENTRIES:
    if _e['id'] in _R5:
        _e['ar'] = _R5[_e['id']]
