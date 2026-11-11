# -*- coding: utf-8 -*-
"""Batch 05 - Battle text, core: everything an ordinary fight shows
(encounters, sending out, attacks, effectiveness, fainting, EXP and level-up,
learning moves, catching, running, money, status conditions, stat changes,
battle menus). Rarer effects (abilities, weather, double/link battles) are
batch 05b.

Sound/pause codes at the start or end of a string (PLAY_SE, PAUSE, WAIT_SE,
PLAY_BGM, PAUSE_UNTIL_PRESS, PALETTE/COLOR codes) are read from the source and
kept automatically, so the Arabic never needs them."""
import os, re
from arabic_text import ROOT

SRC = 'src/battle_message.c'
BATTLE = ('dialog', 216, 'normal', 2)          # battle message box: 28 tiles, text at x=2
_CODES = r'\{(?:PLAY_SE|PAUSE|WAIT_SE|PLAY_BGM|PAUSE_UNTIL_PRESS|PALETTE|COLOR_HIGHLIGHT_SHADOW|HIGHLIGHT)[^}]*\}'
_src = open(os.path.join(ROOT, SRC), encoding='utf-8').read()

def _codes(label):
    m = re.search(r'\b%s\[\] = _\("(.*?)"\);' % re.escape(label), _src)
    if not m:
        return None
    text = m.group(1)
    end = 'p' if text.endswith('\\p') else ''
    body = text[:-2] if end else text
    pre = re.match(r'(?:%s)*' % _CODES, body).group(0)
    post = re.search(r'(?:%s)*$' % _CODES, body).group(0)
    return pre, post, end

def B(label, where, ar, note='', box=BATTLE, raw=False, **kw):
    c = _codes(label)
    if c is None:
        print('battle.py: %s not in %s, skipped' % (label, SRC))
        return None
    pre, post, end = c
    d = dict(id=label, file=SRC, screen='Battle', where=where, box=box, ar=ar, note=note, end=end)
    if not raw:
        d.update(prefix=pre, suffix=post)
    d.update(kw)
    return d

PROMPT = ('manual', 104, 'normal', 2)          # "What will X do?" box: 14 tiles
MENU = ('manual', 96, 'normal', 2)             # FIGHT / BAG / POKéMON / RUN box: 12 tiles
WORD = ('line', 72, 'normal', 1)

_E = [
    # ---- Names inside messages -------------------------------------------------------
    B('sText_WildPkmnPrefix', 'After a wild Pokémon\'s name', ' البري', box=WORD,
      note='RTL: written AFTER the name («RATTATA البري»). Keep the leading space.'),
    B('sText_FoePkmnPrefix', 'After a trainer\'s Pokémon\'s name', ' الخصم', box=WORD,
      note='RTL: written AFTER the name («RATTATA الخصم»). Keep the leading space.'),
    B('sText_FoePkmnPrefix2', 'Foe (other uses)', 'الخصم', box=WORD),
    B('sText_FoePkmnPrefix3', 'Foe (other uses)', 'الخصم', box=WORD),
    B('sText_FoePkmnPrefix4', 'Foe (other uses)', 'الخصم', box=WORD),
    B('sText_Bills', 'PC owner (BILL)', 'بيل', box=WORD),
    B('sText_Someones', 'PC owner (someone)', 'أحدهم', box=WORD),
    B('sText_ABoosted', 'EXP: traded Pokémon bonus', ' بمكافأة', box=WORD, note='Keep the leading space.'),

    # ---- Encounters and sending out ------------------------------------------------------
    B('sText_Trainer1WantsToBattle', 'Trainer battle starts', '{B_TRAINER1_CLASS} {B_TRAINER1_NAME}\nيتحداك في نزال!'),
    B('sText_WildPkmnAppeared', 'Wild encounter', 'انتبه! ظهر {B_OPPONENT_MON1_NAME} البري!'),
    B('sText_WildPkmnAppeared2', 'Wild encounter', 'انتبه! ظهر {B_OPPONENT_MON1_NAME} البري!'),
    B('sText_WildPkmnAppearedPause', 'Wild encounter (tutorial)', 'انتبه! ظهر {B_OPPONENT_MON1_NAME} البري!'),
    B('sText_TwoWildPkmnAppeared', 'Two wild Pokémon', 'ظهر {B_OPPONENT_MON1_NAME} و{B_OPPONENT_MON2_NAME}\nالبريان!'),
    B('sText_GhostAppearedCantId', 'Ghost in the Pokémon Tower', 'ظهر الشبح!\n\nتبا!\nلا يمكن معرفة هوية الشبح!'),
    B('sText_TheGhostAppeared', 'Ghost', 'ظهر الشبح!'),
    B('sText_Trainer1SentOutPkmn', 'Trainer sends out', 'أرسل {B_TRAINER1_CLASS} {B_TRAINER1_NAME}\n{B_OPPONENT_MON1_NAME}!'),
    B('sText_Trainer1SentOutPkmn2', 'Trainer sends out', 'أرسل {B_TRAINER1_CLASS} {B_TRAINER1_NAME}\n{B_BUFF1}!'),
    B('sText_GoPkmn', 'You send out', 'انطلق يا {B_PLAYER_MON1_NAME}!'),
    B('sText_GoTwoPkmn', 'You send out two', 'انطلقا يا {B_PLAYER_MON1_NAME}\nو{B_PLAYER_MON2_NAME}!'),
    B('sText_GoPkmn2', 'You send out', 'انطلق يا {B_BUFF1}!'),
    B('sText_DoItPkmn', 'You send out', 'هيا يا {B_BUFF1}! أرهم قوتك!'),
    B('sText_GoForItPkmn', 'You send out', 'لا تتراجع يا {B_BUFF1}!'),
    B('sText_YourFoesWeakGetEmPkmn', 'You send out (foe weak)', 'خصمك يترنح!\nأجهز عليه يا {B_BUFF1}!'),
    B('sText_PkmnThatsEnough', 'Recall', 'يكفي هذا يا {B_BUFF1}!\nعد إلي!'),
    B('sText_PkmnComeBack', 'Recall', 'عد إلي يا {B_BUFF1}!'),
    B('sText_PkmnOkComeBack', 'Recall', 'حسنا يا {B_BUFF1}!\nعد إلي!'),
    B('sText_PkmnGoodComeBack', 'Recall', 'أحسنت يا {B_BUFF1}!\nعد إلي!'),

    # ---- Menus -------------------------------------------------------------------------------
    B('gText_WhatWillPkmnDo', 'Action prompt', 'ماذا سيفعل\n{B_ACTIVE_NAME_WITH_PREFIX}؟', box=PROMPT),
    B('gText_WhatWillPlayerThrow', 'Safari prompt', 'ماذا سيرمي\n{B_PLAYER_NAME}؟', box=PROMPT),
    B('gText_BattleMenu', 'FIGHT / BAG / POKéMON / RUN', '{CLEAR_TO 8}قتال{CLEAR_TO 56}حقيبة\n{CLEAR_TO 8}الفريق{CLEAR_TO 56}هروب', box=MENU,
      note='Each column holds at most 40 px: «بوكيمون» (53 px) does not fit, so POKéMON -> «الفريق» (your team). Keep {CLEAR_TO 8} (cursor room on the right) and {CLEAR_TO 56} (second column).'),
    B('gText_SafariZoneMenu', 'Safari: BALL / BAIT / ROCK / RUN', '{CLEAR_TO 8}كرة{CLEAR_TO 56}طُعم\n{CLEAR_TO 8}حجر{CLEAR_TO 56}هروب', box=MENU),

    # ---- Attacking -------------------------------------------------------------------------------
    B('sText_AttackerUsedX', 'X used MOVE!', 'استخدم {B_ATK_NAME_WITH_PREFIX}\n{B_BUFF2}',
      note='{B_BUFF2} is the move name with its "!".'),
    B('sText_PlayerUsedItem', 'You used an item', 'استخدم {B_PLAYER_NAME}\n{B_LAST_ITEM}!'),
    B('sText_OldManUsedItem', 'Old man tutorial', 'استخدم العجوز\n{B_LAST_ITEM}!'),
    B('sText_Trainer1UsedItem', 'Trainer used an item', 'استخدم {B_TRAINER1_CLASS} {B_TRAINER1_NAME}\n{B_LAST_ITEM}!'),
    B('sText_SuperEffective', 'Effectiveness', 'إنها ضربة فعالة جدا!'),
    B('sText_NotVeryEffective', 'Effectiveness', 'ليست فعالة كثيرا…'),
    B('sText_ItDoesntAffect', 'No effect', 'لا تؤثر أبدا في\n{B_DEF_NAME_WITH_PREFIX}…'),
    B('sText_CriticalHit', 'Critical hit', 'ضربة حاسمة!'),
    B('sText_OneHitKO', 'One-hit KO', 'ضربة واحدة كانت كافية!'),
    B('sText_AttackMissed', 'Miss', 'أخطأ هجوم\n{B_ATK_NAME_WITH_PREFIX}!'),
    B('sText_PkmnAvoidedAttack', 'Dodge', 'تفادى {B_DEF_NAME_WITH_PREFIX}\nالهجوم ببراعة!'),
    B('sText_ButItFailed', 'Fail', 'لكنها فشلت!'),
    B('sText_ButNothingHappened', 'Nothing', 'لكن لم يحدث شيء!'),
    B('sText_HitXTimes', 'Multi-hit', 'أصاب الهدف {B_BUFF1} مرات!'),
    B('sText_NoPPLeft', 'No PP', 'لم يبق PP لهذه\nالحركة!'),
    B('sText_ButNoPPLeft', 'No PP', 'لكن لم يبق PP\nلهذه الحركة!'),
    B('sText_AttackerFainted', 'Faint', 'سقط {B_ATK_NAME_WITH_PREFIX}\nمغمى عليه!'),
    B('sText_TargetFainted', 'Faint', 'سقط {B_DEF_NAME_WITH_PREFIX}\nمغمى عليه!'),

    # ---- EXP, level up, moves ------------------------------------------------------------------
    B('sText_PkmnGainedEXP', 'EXP', 'كسب {B_BUFF1}{B_BUFF2}\n{B_BUFF3} نقطة خبرة!',
      note='{B_BUFF2} is " بمكافأة" for traded Pokémon, otherwise empty.'),
    B('sText_PkmnGrewToLv', 'Level up', 'ارتقى {B_BUFF1} إلى\nالمستوى {B_BUFF2}!'),
    B('sText_PkmnLearnedMove', 'New move', 'تعلّم {B_BUFF1}\n{B_BUFF2}!'),
    B('sText_PkmnLearnedMove2', 'New move', 'تعلّم {B_ATK_NAME_WITH_PREFIX}\n{B_BUFF1}!'),
    B('sText_TryToLearnMove1', 'Move slots full', 'يحاول {B_BUFF1}\nتعلّم {B_BUFF2}.'),
    B('sText_TryToLearnMove2', 'Move slots full', 'لكن {B_BUFF1} لا يستطيع تعلّم\nأكثر من أربع حركات.'),
    B('sText_TryToLearnMove3', 'Move slots full', 'أتحذف حركة لتفسح المجال\nلـ{B_BUFF2}؟'),
    B('sText_123Poof', 'Forgetting a move', '{X1}1، {X2}2، و{X2}… {X2}… {X2}… {X2}{X3}فوووف!', raw=True,
      codes={'X1': '{PAUSE 32}', 'X2': '{PAUSE 15}', 'X3': '{PLAY_SE SE_BALL_BOUNCE_1}'},
      note='{X1}/{X2} are pauses, {X3} the "poof" sound: keep them.'),
    B('sText_PkmnForgotMove', 'Move forgotten', 'ونسي {B_BUFF1}\n{B_BUFF2}.'),
    B('sText_StopLearningMove', 'Give up the move?', 'أتتوقف عن تعلّم\n{B_BUFF2}؟'),
    B('sText_DidNotLearnMove', 'Move not learned', 'لم يتعلّم {B_BUFF1}\n{B_BUFF2}.'),
    B('gText_PkmnStoppedEvolving', 'Evolution cancelled', 'ماذا؟ توقف {STR_VAR_1}\nعن التطور!'),

    # ---- Catching ---------------------------------------------------------------------------------
    B('sText_TrainerBlockedBall', 'Ball at a trainer\'s Pokémon', 'صدّ المدرب الكرة!'),
    B('sText_DontBeAThief', 'Ball at a trainer\'s Pokémon', 'لا تكن لصا!'),
    B('sText_ItDodgedBall', 'Uncatchable', 'تفادى الكرة!\nهذا البوكيمون لا يمكن إمساكه!'),
    B('sText_ItAppearedCaught', 'Broke free (3 shakes)', 'آه!\nبدا وكأنه أُمسك!'),
    B('sText_AarghAlmostHadIt', 'Broke free (2 shakes)', 'آآه!\nكدت أمسكه!'),
    B('sText_ShootSoClose', 'Broke free (1 shake)', 'تبا!\nكان قريبا جدا!'),
    B('sText_GotchaPkmnCaught', 'Caught!', 'رائع!\nأمسكت {B_OPPONENT_MON1_NAME}!'),
    B('sText_GotchaPkmnCaught2', 'Caught! (tutorial)', 'رائع!\nأمسكت {B_OPPONENT_MON1_NAME}!'),
    B('sText_GiveNicknameCaptured', 'Nickname?', 'أتريد أن تمنح {B_OPPONENT_MON1_NAME}\nلقبا؟'),
    B('sText_PkmnSentToPC', 'Sent to the PC', 'أُرسل {B_OPPONENT_MON1_NAME} إلى\nحاسوب {B_PC_CREATOR_NAME}.'),
    B('sText_PkmnDataAddedToDex', 'Pokédex', 'أضيفت بيانات {B_OPPONENT_MON1_NAME}\nإلى البوكيديكس.'),
    B('sText_YouThrowABallNowRight', 'Catching tutorial', 'سترمي كرة الآن، صحيح؟\nسأ… سأبذل قصارى جهدي!'),

    # ---- Winning, losing, running ----------------------------------------------------------------------
    B('sText_PlayerDefeatedLinkTrainerTrainer1', 'Trainer defeated', 'لقد هزمت\n{B_TRAINER1_CLASS} {B_TRAINER1_NAME}!'),
    B('sText_PlayerLostAgainstTrainer1', 'Lost to a trainer', 'لقد خسرت أمام\n{B_TRAINER1_CLASS} {B_TRAINER1_NAME}!'),
    B('sText_PlayerGotMoney', 'Prize money', 'حصل {B_PLAYER_NAME} على ¥{B_BUFF1}\nمكافأة على الفوز!'),
    B('sText_PlayerWhiteout', 'No Pokémon left', 'لم يبق لدى {B_PLAYER_NAME}\nأي بوكيمون قادر على القتال!'),
    B('sText_PlayerWhiteoutAgainstTrainer', 'No Pokémon left (trainer)', 'لم يبق لدى {B_PLAYER_NAME}\nأي بوكيمون قادر على القتال!\n\nلقد خسرت أمام\n{B_TRAINER1_CLASS} {B_TRAINER1_NAME}!'),
    B('sText_PlayerWhiteout2', 'Blacked out', 'انهار {B_PLAYER_NAME} من التعب!'),
    B('sText_GotAwaySafely', 'Ran away', 'أطلقت ساقيك للريح!', note='Same spelling for a boy or a girl.'),
    B('sText_WildPkmnFled', 'Wild Pokémon fled', 'هرب {B_BUFF1} البري!'),
    B('sText_CantEscape', 'Can\'t run', 'لا مفر!'),
    B('sText_CantEscape2', 'Can\'t run', 'لا مفر!'),
    B('sText_AttackerCantEscape', 'Trapped', 'لا يستطيع {B_ATK_NAME_WITH_PREFIX}\nالهرب!'),

    # ---- Status conditions -------------------------------------------------------------------------------
    B('sText_PkmnFellAsleep', 'Sleep', 'غطّ {B_EFF_NAME_WITH_PREFIX}\nفي النوم!'),
    B('sText_PkmnFastAsleep', 'Sleep', '{B_ATK_NAME_WITH_PREFIX} يغط\nفي نوم عميق…'),
    B('sText_PkmnWokeUp', 'Sleep', 'استيقظ {B_ATK_NAME_WITH_PREFIX}!'),
    B('sText_PkmnWasPoisoned', 'Poison', 'تسمّم {B_EFF_NAME_WITH_PREFIX}!'),
    B('sText_PkmnHurtByPoison', 'Poison', 'السم ينهش\n{B_ATK_NAME_WITH_PREFIX}!'),
    B('sText_PkmnWasBurned', 'Burn', 'احترق {B_EFF_NAME_WITH_PREFIX}!'),
    B('sText_PkmnHurtByBurn', 'Burn', 'الحروق تؤلم\n{B_ATK_NAME_WITH_PREFIX}!'),
    B('sText_PkmnWasFrozen', 'Freeze', 'تجمّد {B_EFF_NAME_WITH_PREFIX}\nتماما!'),
    B('sText_PkmnIsFrozen', 'Freeze', '{B_ATK_NAME_WITH_PREFIX}\nمتجمد تماما!'),
    B('sText_PkmnWasDefrosted', 'Thaw', 'ذاب الجليد عن\n{B_DEF_NAME_WITH_PREFIX}!'),
    B('sText_PkmnWasDefrosted2', 'Thaw', 'ذاب الجليد عن\n{B_ATK_NAME_WITH_PREFIX}!'),
    B('sText_PkmnWasParalyzed', 'Paralysis', 'شُلّ {B_EFF_NAME_WITH_PREFIX}!\nقد يعجز عن الحركة!'),
    B('sText_PkmnIsParalyzed', 'Paralysis', '{B_ATK_NAME_WITH_PREFIX} مشلول!\nلا يستطيع الحركة!'),
    B('sText_PkmnHealedParalysis', 'Paralysis cured', 'شُفي {B_DEF_NAME_WITH_PREFIX}\nمن الشلل!'),
    B('sText_PkmnWasConfused', 'Confusion', 'اختلط الأمر على\n{B_EFF_NAME_WITH_PREFIX}!'),
    B('sText_PkmnIsConfused', 'Confusion', '{B_ATK_NAME_WITH_PREFIX}\nفي حيرة من أمره!'),
    B('sText_ItHurtConfusion', 'Confusion', 'ومن حيرته…\nآذى نفسه!'),
    B('sText_PkmnHealedConfusion', 'Confusion cured', 'استعاد {B_ATK_NAME_WITH_PREFIX}\nصوابه!'),

    # ---- Stats --------------------------------------------------------------------------------------------
    B('gBattleText_Rose', 'Stat change verb', 'ازداد', box=WORD),
    B('sText_StatVerbRiseM', 'Stat up verb (masculine stats)', 'ازداد', box=WORD),
    B('sText_StatVerbRiseF', 'Stat up verb (speed, accuracy, evasion)', 'ازدادت', box=WORD),
    B('sText_StatVerbFallM', 'Stat down verb (masculine stats)', 'انخفض', box=WORD),
    B('sText_StatVerbFallF', 'Stat down verb (speed, accuracy, evasion)', 'انخفضت', box=WORD),
    B('sText_StatFell', 'Stat change verb', 'انخفض', box=WORD),
    B('sText_StatSharply', 'Stat change adverb', ' بشدة', box=WORD, note='Keep the leading space.'),
    B('sText_StatHarshly', 'Stat change adverb', ' بشدة', box=WORD, note='Keep the leading space.'),
    B('sText_AttackersStatRose', 'Stat up', '{B_ATK_NAME_WITH_PREFIX}\n{B_BUFF2} {B_BUFF1}{B_BUFF3}!', note='«بولباسور الخصم / ازدادت سرعته بشدة!» {B_BUFF2} = the verb (agrees with the stat), {B_BUFF1} = the stat, {B_BUFF3} = « بشدة» or nothing.'),
    B('gText_DefendersStatRose', 'Stat up', '{B_DEF_NAME_WITH_PREFIX}\n{B_BUFF2} {B_BUFF1}{B_BUFF3}!'),
    B('sText_AttackersStatFell', 'Stat down', '{B_ATK_NAME_WITH_PREFIX}\n{B_BUFF2} {B_BUFF1}{B_BUFF3}!'),
    B('sText_DefendersStatFell', 'Stat down', '{B_DEF_NAME_WITH_PREFIX}\n{B_BUFF2} {B_BUFF1}{B_BUFF3}!'),
    B('sText_StatsWontIncrease', 'Stat maxed', '{B_ATK_NAME_WITH_PREFIX}\n{B_BUFF1} في أعلى مستوى!', note='Verbless, so it needs no gender agreement.'),
    B('sText_StatsWontDecrease', 'Stat at minimum', '{B_DEF_NAME_WITH_PREFIX}\n{B_BUFF1} في أدنى مستوى!'),
    B('sText_StatsWontIncrease2', 'Stats maxed', 'لن ترتفع قدرات\n{B_ATK_NAME_WITH_PREFIX} أكثر!'),
    B('sText_StatsWontDecrease2', 'Stats at minimum', 'لن تنخفض قدرات\n{B_DEF_NAME_WITH_PREFIX} أكثر!'),
    B('sText_HP2', 'Stat name', 'HP', box=WORD),
    B('sText_Attack2', 'Stat name', 'هجومه', box=WORD, note='Possessive: «ازداد هجومه». Speed, accuracy and evasion are feminine.'),
    B('sText_Defense2', 'Stat name', 'دفاعه', box=WORD),
    B('sText_Speed', 'Stat name', 'سرعته', box=WORD),
    B('sText_SpAtk2', 'Stat name', 'هجومه الخاص', box=('line', 90, 'normal', 1)),
    B('sText_SpDef2', 'Stat name', 'دفاعه الخاص', box=('line', 90, 'normal', 1)),
    B('sText_Accuracy', 'Stat name', 'دقته', box=WORD),
    B('sText_Evasiveness', 'Stat name', 'مراوغته', box=WORD),

    # ---- Healing ---------------------------------------------------------------------------------------------
    B('sText_PkmnRegainedHealth', 'HP restored', 'استعاد {B_DEF_NAME_WITH_PREFIX}\nعافيته!'),
    B('sText_PkmnsItemRestoredHealth', 'Held item heals', 'أعاد {B_LAST_ITEM} إلى\n{B_SCR_ACTIVE_NAME_WITH_PREFIX} عافيته!'),
    B('sText_PkmnsItemHealedBurn', 'Held item heals burn', 'عالج {B_LAST_ITEM} حروق\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}!'),
    B('sText_PkmnsItemSnappedOut', 'Held item cures confusion', 'أعاد {B_LAST_ITEM} إلى\n{B_SCR_ACTIVE_NAME_WITH_PREFIX} صوابه!'),
    B('sText_PkmnsItemRestoredPP', 'Held item restores PP', 'أعاد {B_LAST_ITEM} لدى {B_SCR_ACTIVE_NAME_WITH_PREFIX}\nنقاط PP لحركة {B_BUFF1}!'),
]
ENTRIES = [e for e in _E if e]

README = [
    ('Pokémon FireRed – Arabic translation – Batch 05: battle text (core)', 'title'),
    ('Everything an ordinary battle shows: encounters, sending out and recalling, attacks, effectiveness, critical '
     'hits, fainting, EXP and level-ups, learning moves, catching, running, prize money, status conditions, stat '
     'changes, and the battle menus. Rarer effects (abilities, weather, double and link battles) come in batch 05b.', 'text'),
    ('', 'text'),
    ('What to edit', 'head'),
    ('Only the yellow cells. Keep every {B_…} token: they insert names, moves, items and numbers during battle.', 'edit'),
    ('Wild/Foe: the game now writes them AFTER the name, so « البري» and « الخصم» start with a space.', 'text'),
    ('Stat changes are built from pieces: {B_BUFF2} becomes «ارتفع» / «ارتفع بشدة» / «انخفض» / «انخفض بشدة», '
     '{B_BUFF1} the stat name.', 'text'),
    ('Sound and pause codes are kept automatically; only «1، 2، و…» uses {X1}/{X2}/{X3} for its pauses and sound.', 'text'),
    ('', 'text'),
    ('Applying your changes', 'head'),
    ('1.  python3 tools/arabic/apply_translations.py battle', 'text'),
    ('2.  make', 'text'),
    ('', 'text'),
    ('Still Latin for now', 'head'),
    ('Pokémon, move, item and trainer-class names come from the game\'s tables (names batch). The move screen\'s '
     '"PP" and "TYPE/" labels stay as they are: the type window is too narrow for Arabic until the type names are done.', 'text'),
]

GLOSSARY = [
    ('Wild X / Foe X', 'X البري / X الخصم', 'Written after the name.'),
    ('FIGHT / BAG / POKéMON / RUN', 'قتال / حقيبة / الفريق / هروب', 'POKéMON -> «الفريق»: «بوكيمون» is too wide for the menu column.'),
    ('BALL / BAIT / ROCK (Safari)', 'كرة / طُعم / حجر', ''),
    ('It\'s super effective!', 'إنها ضربة فعالة جدا!', ''),
    ('It\'s not very effective…', 'ليست فعالة كثيرا…', ''),
    ('A critical hit!', 'ضربة حاسمة!', 'Alternative: "ضربة حرجة!".'),
    ('fainted', 'سقط مغمى عليه', ''),
    ('EXP. Points', 'نقطة خبرة', ''),
    ('grew to LV. X', 'ارتقى إلى المستوى X', ''),
    ('Gotcha!', 'رائع!', ''),
    ('Got away safely!', 'أطلقت ساقيك للريح!', 'Idiom: ran as fast as the wind.'),
    ('Can\'t escape!', 'لا مفر!', ''),
    ('whited out', 'انهار من التعب', ''),
    ('ATTACK / DEFENSE / SPEED', 'الهجوم / الدفاع / السرعة', ''),
    ('SP. ATK / SP. DEF', 'الهجوم الخاص / الدفاع الخاص', ''),
    ('accuracy / evasiveness', 'الدقة / المراوغة', ''),
    ('X\'s SPEED rose sharply!', 'X / ازدادت سرعته بشدة!', 'The verb agrees with the stat: ازداد هجومه / ازدادت سرعته.'),
    ('X\'s DEFENSE fell!', 'X / انخفض دفاعه!', ''),
    ('BILL\'s PC / someone\'s PC', 'حاسوب بيل / حاسوب أحدهم', ''),
    ('Poof!', 'فوووف!', 'The forgetting-a-move gag.'),
]

# ---- Prof. Oak's tutorial in the first battle, nickname prompts -----------------------
_E2 = [
    B('gText_ForPetesSake', 'First battle: Oak steps in', 'أوك: آه، يا له من متسرع…\nكعادته دائما.\n\n{B_PLAYER_NAME}.\n\nلم تخض نزال بوكيمون من قبل،\nأليس كذلك؟\n\nفي نزال البوكيمون، يواجه المدربون\nبعضهم بعضا بالبوكيمون.'),
    B('gText_TheTrainerThat', 'First battle: Oak', 'والفائز هو المدرب الذي يُسقط بوكيمون\nخصمه، بإنزال HP خاصته إلى “0”.'),
    B('gText_TryBattling', 'First battle: Oak', 'لكن دعك من الكلام…\nفالتجربة خير معلم.\n\nهيا، جرب النزال بنفسك!'),
    B('gText_InflictingDamageIsKey', 'First battle: Oak', 'أوك: إلحاق الضرر بالخصم\nهو مفتاح كل نزال.'),
    B('gText_LoweringStats', 'First battle: Oak', 'أوك: إضعاف قدرات الخصم\nيمنحك الأفضلية.'),
    B('gText_KeepAnEyeOnHP', 'First battle: Oak', 'أوك: لا ترفع عينيك عن HP\nبوكيمونك.\n\nفإن هبطت إلى “0”،\nسقط مغمى عليه.'),
    B('gText_OakNoRunningFromATrainer', 'Trying to run from a trainer', 'أوك: لا! لا هروب من نزال\nضد مدرب بوكيمون!'),
    B('gText_WinEarnsPrizeMoney', 'First battle won', 'أوك: همم! ممتاز!\n\nحين تفوز، تكسب مالا،\nويكبر بوكيمونك!\n\nنازل المدربين الآخرين،\nواجعل بوكيمونك قويا!'),
    B('gText_HowDissapointing', 'First battle lost', 'أوك: همم…\nيا للخيبة…\n\nحين تفوز، تكسب مالا،\nويكبر بوكيمونك.\n\nلكن إن خسرت يا {B_PLAYER_NAME}،\nفأنت من يدفع المال…\n\nومع ذلك، بما أنك لم تكن تعلم\nهذه المرة، سأدفع عنك.\n\nلكن الأمر سيختلف حين تخطو\nخارج هذا الباب.\n\nلذا قوِّ بوكيمونك بمنازلة\nالبوكيمون البرية.'),
]
ENTRIES += [e for e in _E2 if e]
ENTRIES += [
    dict(id='Text_GiveNicknameToReceivedMon', file='data/event_scripts.s', screen='Nickname', where='After receiving a Pokémon',
         box=BATTLE, ar='أتريد أن تمنح {STR_VAR_2}\nالذي حصلت عليه لقبا؟', note=''),
    dict(id='Text_GiveNicknameToThisMon', file='data/event_scripts.s', screen='Nickname', where='After catching / receiving',
         box=BATTLE, ar='أتريد أن تمنح {STR_VAR_1}\nهذا لقبا؟', note=''),
    dict(id='gText_PkmnsNickname', file='src/strings.c', screen='Naming screen', where='Title after the Pokémon\'s name',
         box=('line', 90, 'normal', 1), ar=': اختر لقبا',
         note='Printed after the name: "SQUIRTLE: اختر لقبا". Keep the colon and the space.'),
]

_E3 = [
    B('sText_Trainer1RecallPkmn1', 'Trainer recalls', '{B_TRAINER1_NAME}: عد إلي يا {B_OPPONENT_MON1_NAME}!'),
    B('sText_Trainer1RecallPkmn2', 'Trainer recalls', '{B_TRAINER1_NAME}: عد إلي يا {B_OPPONENT_MON2_NAME}!'),
    B('sText_Trainer1RecallBoth', 'Trainer recalls two', '{B_TRAINER1_NAME}: عودا إلي يا\n{B_OPPONENT_MON1_NAME} و{B_OPPONENT_MON2_NAME}!'),
]
ENTRIES += [e for e in _E3 if e]

# ---- Revision 3: plural «البوكيمونات» and player gender ([[masc|fem]]) -----------------
_R3 = {'gText_ForPetesSake': 'أوك: آه، يا له من متسرع…\nكعادته دائما.\n\n{B_PLAYER_NAME}.\n\nلم [[تخض|تخوضي]] نزال بوكيمون من قبل،\nأليس كذلك؟\n\nفي نزال البوكيمون، يواجه المدربون\nبعضهم بعضا بالبوكيمونات.', 'gText_TryBattling': 'لكن دعك من الكلام…\nفالتجربة خير معلم.\n\nهيا، [[جرب|جربي]] النزال بنفسك!', 'gText_KeepAnEyeOnHP': 'أوك: لا [[ترفع|ترفعي]] عينيك عن HP\nبوكيمونك.\n\nفإن هبطت إلى “0”،\nسقط مغمى عليه.', 'gText_WinEarnsPrizeMoney': 'أوك: همم! ممتاز!\n\nحين [[تفوز،|تفوزين،]] [[تكسب|تكسبين]] مالا،\nوتكبر بوكيموناتك!\n\n[[نازل|نازلي]] المدربين الآخرين،\n[[واجعل|واجعلي]] بوكيموناتك قوية!', 'gText_HowDissapointing': 'أوك: همم…\nيا للخيبة…\n\nحين [[تفوز،|تفوزين،]] [[تكسب|تكسبين]] مالا،\nوتكبر بوكيموناتك.\n\nلكن إن خسرت يا {B_PLAYER_NAME}،\nفأنت من يدفع المال…\n\nومع ذلك، بما أنك لم [[تكن|تكوني]] [[تعلم|تعلمين]]\nهذه المرة، سأدفع عنك.\n\nلكن الأمر سيختلف حين [[تخطو|تخطين]]\nخارج هذا الباب.\n\nلذا [[قوِّ|قوّي]] بوكيموناتك بمنازلة\nالبوكيمونات البرية.', 'Text_GiveNicknameToReceivedMon': '[[أتريد|أتريدين]] أن تمنح {STR_VAR_2}\nالذي حصلت عليه لقبا؟', 'Text_GiveNicknameToThisMon': '[[أتريد|أتريدين]] أن تمنح {STR_VAR_1}\nهذا لقبا؟'}
for _e in ENTRIES:
    if _e['id'] in _R3:
        _e['ar'] = _R3[_e['id']]

# ---- Revision 5: verbs whose subject is the player are gendered
_R5 = {'sText_PlayerUsedItem': '[[استخدم|استخدمت]] {B_PLAYER_NAME}\n{B_LAST_ITEM}!', 'sText_PlayerGotMoney': '[[حصل|حصلت]] {B_PLAYER_NAME} على ¥{B_BUFF1}\nمكافأة على الفوز!', 'sText_PlayerWhiteout2': '[[انهار|انهارت]] {B_PLAYER_NAME} من التعب!'}
for _e in ENTRIES:
    if _e['id'] in _R5:
        _e['ar'] = _R5[_e['id']]

# ---- Revision: the nickname prompt follows the species name
for _e in ENTRIES:
    if _e['id'] == 'gText_PkmnsNickname':
        _e['ar'] = '، ما لقبه؟'
        _e['box'] = ('line', 80, 'normal', 1)   # + the species name (60 px max): ~130 px in all
        _e['note'] = 'Printed after the species name: «تشارماندر، ما لقبه؟».'
