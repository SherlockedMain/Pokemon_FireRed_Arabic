# -*- coding: utf-8 -*-
# Batch 17, part 3: the rest of the Nugget Bridge, Route 25 and Bill's Sea Cottage.
from mtmoon import G, MV, SP, IT
import names_maps
_maps = {e.get('where', ''): e['ar'] for e in names_maps.ENTRIES}
ANNE = next((v for k, v in _maps.items() if 'ANNE' in k.upper()), 'السفينة آن')
VER = 'مدينة فيرميليون'
NO_REGRETS = 'بذلت قصارى جهدي، ولا أندم على شيء!'
def BILL_INTRO(girl):
    who = 'آنسة' if girl else 'صديقي'
    return ('أهلا! أنا بوكيمون…\n\n…لا، لست كذلك!\n\n' + ('ناديني' if girl else 'نادني') + ' بيل! أنا عاشق بوكيمونات حتى النخاع!\n\n'
            'مهلا! ما هذه النظرة المرتابة؟\n\nأنا لا أمزح معك يا ' + who + '.\n\nأفسدت تجربة، فاندمجت مع بوكيمون!\n\n'
            'فما رأيك؟ ' + ('ساعديني!' if girl else 'ساعدني!'))

def BILL_PLEASE(girl):
    if girl:
        return 'لا؟! لا تكوني قاسية هكذا!\n\nهيا، يجب أن تساعدي رجلا في ورطة كبيرة جدا!\n\nما قولك يا آنسة؟ أرجوك؟ اتفقنا؟ رائع!'
    return 'لا؟! لا تكن قاسيا هكذا!\n\nهيا، يجب أن تساعد رجلا في ورطة كبيرة جدا!\n\nما قولك يا زعيم؟ أرجوك؟ اتفقنا؟ رائع!'

def BILL_THANKS(girl):
    return ('بيل: ياهو! شكرا يا ' + ('آنسة' if girl else 'صديقي') + '! أنا مدين لك!\n\nإذن، هل ' + ('جئتِ لتري' if girl else 'جئت لترى') +
            ' مجموعة بوكيموناتي؟\n\nلا؟ يا للخسارة!\n\nعلي أن أشكرك… آه، ' + ('خذي' if girl else 'خذ') + '، لعل هذا يفي بالغرض.')

P3 = {
 'Route24_Text_ReliPostBattle': NO_REGRETS,
 'Route24_Text_TimmyIntro': 'وهذا رقم 3! لن أكون سهلا!',
 'Route24_Text_TimmyDefeat': 'آخ! سُحقت تماما!',
 'Route24_Text_TimmyPostBattle': NO_REGRETS,
 'Route24_Text_AliIntro': 'أنا الثاني! الآن جد الجد!',
 'Route24_Text_AliDefeat': 'كيف خسرت؟',
 'Route24_Text_AliPostBattle': NO_REGRETS,
 'Route24_Text_CaleIntro': 'يسمي الناس هذا الجسر جسر الذهب!\n\n' + G('اهزم', 'اهزمي') + ' خمستنا ' + G('واربح', 'واربحي') + ' جائزة رائعة!\n\n' + G('أتظن', 'أتظنين') + ' أنك ' + G('قادر', 'قادرة') + ' على ذلك؟',
 'Route24_Text_CaleDefeat': 'ووه! أداء رائع!',
 'Route24_Text_CalePostBattle': NO_REGRETS,
 'Route25_Text_JoeyIntro': 'يأتي المدربون من هنا ليتدربوا.',
 'Route25_Text_JoeyDefeat': 'أنت ' + G('جيد', 'جيدة') + '.',
 'Route25_Text_JoeyPostBattle': 'لكل البوكيمونات نقاط ضعف، حتى أقواها.\n\nلذا من الأفضل أن تربي بوكيمونات من أنواع مختلفة.',
 'Route25_Text_DanIntro': 'أخذني أبي إلى حفلة رائعة على متن ' + ANNE + ' في ' + VER + '.',
 'Route25_Text_DanDefeat': 'لست غاضبا!',
 'Route25_Text_DanPostBattle': 'على متن ' + ANNE + '، رأيت مدربين من كل أنحاء العالم.',
 'Route25_Text_FlintIntro': 'أنا شاب رائع، ولدي خطيبة!',
 'Route25_Text_FlintDefeat': 'آه، تبا…',
 'Route25_Text_FlintPostBattle': 'لا بأس، خطيبتي ستواسيني.',
 'Route25_Text_KelseyIntro': 'مرحبا! خطيبي رائع!',
 'Route25_Text_KelseyDefeat': 'لست في أفضل حالاتي…',
 'Route25_Text_KelseyPostBattle': 'ليت خطيبي كان بارعا مثلك.',
 'Route25_Text_ChadIntro': 'كان لدي شعور… كنت أعلم أن علي منازلتك!',
 'Route25_Text_ChadDefeat': 'وكنت أعلم أنني سأخسر أيضا!',
 'Route25_Text_ChadPostBattle': 'إذا أصابت الحيرة بوكيمونك، ' + G('فبدّله', 'فبدّليه') + '.\n\nهذه خطة جيدة.',
 'Route25_Text_HaleyIntro': 'لدى صديقتي بوكيمونات لطيفة كثيرة. أنا أغار منها جدا!',
 'Route25_Text_HaleyDefeat': 'لم أعد أغار كثيرا!',
 'Route25_Text_HaleyPostBattle': 'جئت من جبل القمر؟ هلا أعطيتني ' + SP('CLEFAIRY') + '؟',
 'Route25_Text_FranklinIntro': 'نزلت للتو من جبل القمر، لكن ما زالت لدي طاقة!',
 'Route25_Text_FranklinDefeat': 'لقد اجتهدت!',
 'Route25_Text_FranklinPostBattle': 'تبا! عضني ' + SP('ZUBAT') + ' في ذلك الكهف.',
 'Route25_Text_NobIntro': 'أنا ذاهب لأرى مجموعة عاشق البوكيمونات عند الرأس.',
 'Route25_Text_NobDefeat': 'لقد أوقعت بي، وبجدارة أيضا!',
 'Route25_Text_NobPostBattle': 'عاشق البوكيمونات جدير بلقبه حقا.\n\nففي مجموعته أنواع نادرة كثيرة من البوكيمونات.',
 'Route25_Text_WayneIntro': G('أنت ذاهب', 'أنتِ ذاهبة') + ' لرؤية بيل؟ أولا، سنتنازل!',
 'Route25_Text_WayneDefeat': 'أنت ' + G('مدهش!', 'مدهشة!'),
 'Route25_Text_WaynePostBattle': 'الدرب الذي في الأسفل طريق مختصر إلى مدينة سيرولين.',
 'Route25_Text_SeaCottageSign': 'كوخ البحر\nهنا يعيش بيل!',
 'Route25_Text_MistyHighHopesAboutThisPlace': 'هذا الرأس مكان مشهور يحب الناس زيارته.\n\nوميستي، قائدة الصالة، تحب هذا المكان كثيرا.',
 'Route25_Text_AreYouHereAlone': 'مرحبا، هل أنت هنا ' + G('وحدك؟', 'وحدك؟') + '\n\nرأس سيرولين مكان يحلو قضاء الوقت فيه مع الأصدقاء.',
 'Route25_SeaCottage_Text_ImBillHelpMeOutPal': BILL_INTRO(False),
 'Route25_SeaCottage_Text_ImBillHelpMeOutLady': BILL_INTRO(True),
 'Route25_SeaCottage_Text_RunCellSeparationOnPC': G('انتظر', 'انتظري') + ' حتى أدخل آلة النقل.\n\nوحين أدخلها، ' + G('اذهب', 'اذهبي') + ' إلى حاسوبي ' + G('وشغّل', 'وشغّلي') + ' نظام فصل الخلايا.',
 'Route25_SeaCottage_Text_NoPleaseChief': BILL_PLEASE(False),
 'Route25_SeaCottage_Text_NoPleaseBeautiful': BILL_PLEASE(True),
 'Route25_SeaCottage_Text_ThanksBudTakeThis': BILL_THANKS(False),
 'Route25_SeaCottage_Text_ThanksLadyTakeThis': BILL_THANKS(True),
 'Route25_SeaCottage_Text_ReceivedSSTicketFromBill': G('حصل', 'حصلت') + ' {PLAYER} على ' + IT('SS_TICKET') + ' من بيل.',
 'Route25_SeaCottage_Text_YouveGotTooMuchStuff': 'معك أغراض كثيرة جدا!',
 'Route25_SeaCottage_Text_SSAnnePartyYouGoInstead': ANNE + ' السياحية راسية في ' + VER + '.\n\nوسمعت أن على متنها مدربين كثيرين أيضا.\n\nدعوني إلى حفلتهم، لكنني لا أطيق الحفلات الفاخرة.\n\nلم لا ' + G('تذهب', 'تذهبين') + ' بدلا مني؟ ' + G('اذهب', 'اذهبي') + ' ' + G('واستمتع', 'واستمتعي') + ' بوقتك.',
 'Route25_SeaCottage_Text_CheckOutRareMonsOnPC': 'بيل: ' + G('أتحب', 'أتحبين') + ' أن ' + G('ترى', 'تري') + ' بعض بوكيموناتي النادرة في حاسوبي؟\n\nهيا، ' + G('تفقد', 'تفقدي') + ' حاسوبي.',
 'Route25_SeaCottage_Text_TeleporterIsDisplayed': 'على شاشة الحاسوب: آلة النقل.',
 'Route25_SeaCottage_Text_InitiatedTeleportersCellSeparator': G('شغّل', 'شغّلت') + ' {PLAYER} فاصل الخلايا في آلة النقل.',
 'Route25_SeaCottage_Text_BillsFavoriteMonList': 'قائمة بوكيمونات بيل المفضلة!',
 'Route25_SeaCottage_Text_SeeWhichMon': 'أي بوكيمون ' + G('تريد', 'تريدين') + ' أن ' + G('ترى؟', 'تري؟'),
}
