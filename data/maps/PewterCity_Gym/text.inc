PewterCity_Gym_Text_BrockIntro::
    .string "ﺇﺫﻥ ﺃﻧﺖ ﻫﻨﺎ. ﺃﻧﺎ ﺑﺮﻭﻙ،\n"
    .string "ﻗﺎﺋﺪ ﺻﺎﻟﺔ ﺑﻴﻮﺗﺮ.\p"
    .string "ﺇﺭﺩﺗﻲ ﺼﻠﺒﺔ ﻛﺎﻟﺼﺨﺮ ﺗﻈﻬﺮ\n"
    .string "ﺣﺘﻰ ﻓﻲ ﺑﻮﻛﻴﻤﻮﻧﺎﺗﻲ.\p"
    .string "ﺑﻮﻛﻴﻤﻮﻧﺎﺗﻲ ﻛﻠﻬﺎ ﺻﻠﺒﺔ ﻛﺎﻟﺼﺨﺮ،\n"
    .string "ﻭﻋﺰﻳﻤﺘﻬﺎ ﻻ ﺗﻠﻴﻦ.\p"
    .string "ﻧﻌﻢ، ﺑﻮﻛﻴﻤﻮﻧﺎﺗﻲ ﻛﻠﻬﺎ ﻣﻦ\n"
    .string "ﻧﻮﻉ ﺼﺨﺮ!\p"
    .string "ﻓﻮﻫﺎﻫﺎ! {GENDER_M}ﺃﺗﺘﺤﺪﻧﻲ{GENDER_F}ﺃﺗﺘﺤﺪﻳﻨﻨﻲ{GENDER_E} ﻭﻧﺖ\n"
    .string "{GENDER_M}ﺗﻌﻠﻢ{GENDER_F}ﺗﻌﻠﻤﻴﻦ{GENDER_E}\p"
    .string "ﺃﻧﻚ {GENDER_M}ﺳﺘﺨﺴﺮ؟{GENDER_F}ﺳﺘﺨﺴﺮﻳﻦ؟{GENDER_E}\p"
    .string "ﺇﻧﻪ ﺷﺮﻑ ﻤﺪﺭﺏ ﻣﺎ ﻳﺪﻓﻌﻚ\n"
    .string "ﺇﻟﻰ ﺗﺤﺪﻳﻲ.\p"
    .string "ﺣﺴﻨﺎ ﺇﺫﻥ!\n"
    .string "{GENDER_M}ﺃﺭﻧﻲ{GENDER_F}ﺃﺭﻳﻨﻲ{GENDER_E} ﺃﻓﻀﻞ ﻣﺎ ﻟﺪﻳﻚ!{PLAY_BGM}{MUS_ENCOUNTER_GYM_LEADER}$"

@ NOTE: This defeat text actually causes a buffer overflow. It's too long for the gDisplayedStringBattle
@ buffer that it's put into, and it stomps all over the gBattleTextBuffs after, as well as the otherwise
@ unused array after that, sFlickerArray. Perhaps that's the reason why said array exists.
PewterCity_Gym_Text_BrockDefeat::
    .string "ﺍﺳﺘﺨﻔﻔﺖ ﺑﻚ، ﻓﺨﺴﺮﺕ.\p"
    .string "ﻭﺛﺒﺎﺗﺎ ﻟﻔﻮﺯﻙ، ﺃﻣﻨﺤﻚ ﻫﺬ…\n"
    .string "ﻭﺳﺎﻡ ﺼﺨﺮﺓ ﺮﺳﻤﻲ ﻟﻠﺪﻭﺭﻱ.\p"
    .string "{FONT_NORMAL}{GENDER_M}ﺣﺼﻞ{GENDER_F}ﺣﺼﻠﺖ{GENDER_E} {PLAYER} ﻋﻠﻰ ﻭﺳﺎﻡ ﺼﺨﺮﺓ\n"
    .string "ﻣﻦ ﺑﺮﻭﻙ!{PAUSE_MUSIC}{PLAY_BGM}{MUS_OBTAIN_BADGE}{PAUSE 0xFE}{PAUSE 0x56}{RESUME_MUSIC}\p"
    .string "{FONT_MALE}ﻣﺠﺮﺩ ﺍﻣﺘﻼﻙ ﻭﺳﺎﻡ ﺼﺨﺮﺓ ﻳﺠﻌﻞ\n"
    .string "ﺑﻮﻛﻴﻤﻮﻧﺎﺗﻚ ﺃﻗﻮﻯ.\p"
    .string "ﻭﻫﻮ ﻳﺘﻴﺢ ﺃﻳﻀﺎ ﺍﺳﺘﺨﺪﻡ ﺣﺮﻛﺔ\n"
    .string "ﻮﻣﻴﺾ ﺧﺎﺭﺝ ﻨﺰﻝ.\p"
    .string "ﻃﺒﻌﺎ، ﻳﺠﺐ ﺃﻥ ﻳﻌﺮﻑ ﺒﻮﻛﻴﻤﻮﻥ\n"
    .string "ﺣﺮﻛﺔ ﻮﻣﻴﺾ ﻟﻴﺴﺘﺨﺪﻣﻬﺎ.$"

PewterCity_Gym_Text_TakeThisWithYou::
    .string "{GENDER_M}ﺍﻧﺘﻈﺮ!{GENDER_F}ﺍﻧﺘﻈﺮﻱ!{GENDER_E}\n"
    .string "{GENDER_M}ﺧﺬ{GENDER_F}ﺧﺬﻱ{GENDER_E} ﻫﺬ ﻣﻌﻚ.$"

PewterCity_Gym_Text_ReceivedTM39FromBrock::
    .string "{GENDER_M}ﺣﺼﻞ{GENDER_F}ﺣﺼﻠﺖ{GENDER_E} {PLAYER} ﻋﻠﻰ ﻘﺮﺹ ﺘﻘﻨﻲ\n"
    .string "39\p"
    .string "ﻣﻦ ﺑﺮﻭﻙ.$"

PewterCity_Gym_Text_ExplainTM39::
    .string "ﻘﺮﺹ ﺘﻘﻨﻲ ﻳﺤﻮﻱ ﺣﺮﻛﺔ\n"
    .string "ﻳﺘﻌﻠﻤﻬﺎ ﺒﻮﻛﻴﻤﻮﻥ.\p"
    .string "ﺍﺳﺘﺨﺪﻡ ﻘﺮﺹ ﻳﻌﻠﻢ ﺒﻮﻛﻴﻤﻮﻥ\n"
    .string "ﺤﺮﻛﺔ ﺘﻲ ﻓﻴﻪ.\p"
    .string "ﻟﻜﻦ ﻘﺮﺹ ﻳﺴﺘﺨﺪﻡ ﻣﺮﺓ ﻭﺣﺪﺓ\n"
    .string "ﻓﻘﻂ.\p"
    .string "ﻟﺬ {GENDER_M}ﺍﺧﺘﺮ{GENDER_F}ﺍﺧﺘﺎﺭﻱ{GENDER_E} ﺒﻮﻛﻴﻤﻮﻥ ﺑﻌﻨﺎﻳﺔ\n"
    .string "ﺣﻴﻦ {GENDER_M}ﺗﺴﺘﺨﺪﻣﻪ.{GENDER_F}ﺗﺴﺘﺨﺪﻣﻴﻨﻪ.{GENDER_E}\p"
    .string "ﻋﻠﻰ ﺃﻱ ﺣﺎﻝ…\n"
    .string "ﻓﻲ ﻘﺮﺹ ﺘﻘﻨﻲ 39 ﻗﺒﺮ ﺼﺨﻮﺭ.\p"
    .string "ﺗﺮﻣﻲ ﺼﺨﻮﺭ ﻋﻠﻰ ﺨﺼﻢ\n"
    .string "ﻭﺗﺨﻔﺾ ﺳﺮﻋﺘﻪ.$"

PewterCity_Gym_Text_BrockPostBattle::
    .string "ﻓﻲ ﻋﺎﻟﻤﻨﺎ ﻮﺳﻊ ﻫﺬ، ﻣﺪﺭﺑﻮﻥ\n"
    .string "ﻣﻦ ﻛﻞ ﻧﻮﻉ.\p"
    .string "ﻭﻳﺒﺪﻭ ﺃﻧﻚ {GENDER_M}ﻣﻮﻫﻮﺏ{GENDER_F}ﻣﻮﻫﻮﺑﺔ{GENDER_E} ﺟﺪ\n"
    .string "{GENDER_M}ﻛﻤﺪﺭﺏ{GENDER_F}ﻛﻤﺪﺭﺑﺔ{GENDER_E} ﺑﻮﻛﻴﻤﻮﻥ.\p"
    .string "{GENDER_M}ﻓﺎﺳﻤﺢ{GENDER_F}ﻓﺎﺳﻤﺤﻲ{GENDER_E} ﻟﻲ ﺑﺎﻗﺘﺮﺡ:\p"
    .string "{GENDER_M}ﺍﺫﻫﺐ{GENDER_F}ﺍﺫﻫﺒﻲ{GENDER_E} ﺇﻟﻰ ﺻﺎﻟﺔ ﺳﻴﺮﻭﻟﻴﻦ\n"
    .string "{GENDER_M}ﻭﺧﺘﺒﺮ{GENDER_F}ﻭﺧﺘﺒﺮﻱ{GENDER_E} ﻗﺪﺭﺗﻚ.$"

PewterCity_Gym_Text_DontHaveRoomForThis::
    .string "ﻟﻴﺲ ﻟﺪﻳﻚ ﻣﻜﺎﻥ ﻟﻬﺬ.$"

PewterCity_Gym_Text_LiamIntro::
    .string "{GENDER_M}ﻗﻒ{GENDER_F}ﻗﻔﻲ{GENDER_E} ﻣﻜﺎﻧﻚ ﻳﺎ {GENDER_M}ﺻﻐﻴﺮ!{GENDER_F}ﺻﻐﻴﺮﺓ!{GENDER_E}\p"
    .string "ﺃﻧﺖ ﻋﻠﻰ ﺑﻌﺪ ﻋﺸﺮﺓ ﺁﻻﻑ ﺳﻨﺔ\n"
    .string "ﺿﻮﺋﻴﺔ ﻣﻦ ﻣﻮﺟﻬﺔ ﺑﺮﻭﻙ!$"

PewterCity_Gym_Text_LiamDefeat::
    .string "ﺗﺒﺎ!\p"
    .string "ﺴﻨﺔ ﻀﻮﺋﻴﺔ ﻟﻴﺴﺖ ﺯﻣﻨﺎ…\n"
    .string "ﺇﻧﻬﺎ ﺗﻘﻴﺲ ﻤﺴﺎﻓﺔ!$"

PewterCity_Gym_Text_LiamPostBattle::
    .string "ﺃﻧﺖ {GENDER_M}ﻗﻮﻱ{GENDER_F}ﻗﻮﻳﺔ{GENDER_E} ﺟﺪ.\n"
    .string "…ﻟﻜﻦ ﻟﻴﺲ ﻣﺜﻞ ﺑﺮﻭﻙ!$"

PewterCity_Gym_Text_LetMeTakeYouToTheTop::
    .string "ﺃﻫﻼ!\n"
    .string "ﻫﻞ {GENDER_M}ﺗﺤﻠﻢ{GENDER_F}ﺗﺤﻠﻤﻴﻦ{GENDER_E} ﺃﺣﻼﻣﺎ ﻛﺒﻴﺮﺓ؟\p"
    .string "ﻫﻞ {GENDER_M}ﺗﺠﺮﺅ{GENDER_F}ﺗﺠﺮﺋﻴﻦ{GENDER_E} ﻋﻠﻰ ﺃﻥ ﺗﺤﻠﻢ ﺑﺄﻥ\n"
    .string "{GENDER_M}ﺗﺼﺒﺢ{GENDER_F}ﺗﺼﺒﺤﻲ{GENDER_E}\p"
    .string "{GENDER_M}ﺑﻄﻞ{GENDER_F}ﺑﻄﻠﺔ{GENDER_E} ﺒﻮﻛﻴﻤﻮﻥ؟\p"
    .string "ﻟﺴﺖ ﻣﺪﺭﺑﺎ، ﻟﻜﻨﻨﻲ ﺃﺳﺘﻄﻴﻊ ﺃﻥ\n"
    .string "ﺃﻧﺼﺤﻚ ﻛﻴﻒ {GENDER_M}ﺗﻔﻮﺯ.{GENDER_F}ﺗﻔﻮﺯﻳﻦ.{GENDER_E}.\p"
    .string "ﺩﻋﻨﻲ ﺁﺧﺬﻙ ﺇﻟﻰ ﻘﻤﺔ!$"

PewterCity_Gym_Text_LetsGetHappening::
    .string "ﺭﺋﻊ!\n"
    .string "ﻟﻨﺒﺪ!$"

PewterCity_Gym_Text_TryDifferentPartyOrders::
    .string "ﺃﻭﻝ ﺑﻮﻛﻴﻤﻮﻥ ﻳﺪﺧﻞ ﻨﺰﻝ ﻫﻮ\n"
    .string "ﺍﻷﻭﻝ ﻓﻲ ﻗﺎﺋﻤﺔ ﺒﻮﻛﻴﻤﻮﻥ.\p"
    .string "ﺑﺘﻐﻴﻴﺮ ﺗﺮﺗﻴﺐ ﺑﻮﻛﻴﻤﻮﻧﺎﺗﻚ،\n"
    .string "ﻗﺪ ﺗﻜﺴﺐ ﺃﻓﻀﻠﻴﺔ.\p"
    .string "{GENDER_M}ﺟﺮﺏ{GENDER_F}ﺟﺮﺑﻲ{GENDER_E} ﺗﺮﺗﻴﺒﺎﺕ ﻣﺨﺘﻠﻔﺔ ﺗﻨﺎﺳﺐ\n"
    .string "ﻓﺮﻳﻖ ﺧﺼﻤﻚ.$"

PewterCity_Gym_Text_ItsFreeLetsGetHappening::
    .string "ﺇﻧﻬﺎ ﺧﺪﻣﺔ ﻣﺠﺎﻧﻴﺔ!\n"
    .string "ﻟﻨﺒﺪ!$"

PewterCity_Gym_Text_YoureChampMaterial::
    .string "ﺗﻤﺎﻣﺎ ﻛﻤﺎ ﺗﻮﻗﻌﺖ!\n"
    .string "ﺃﻧﺖ ﻣﺸﺮﻭﻉ {GENDER_M}ﺑﻄﻞ{GENDER_F}ﺑﻄﻠﺔ{GENDER_E} ﺑﻮﻛﻴﻤﻮﻥ!$"

PewterCity_Gym_Text_GymStatue::
    .string "ﺻﺎﻟﺔ ﺒﻮﻛﻴﻤﻮﻥ ﻓﻲ ﺑﻴﻮﺗﺮ\n"
    .string "ﻘﺎﺋﺪ: ﺑﺮﻭﻙ\p"
    .string "ﻤﺪﺭﺑﻮﻥ ﻔﺎﺋﺰﻭﻥ:\n"
    .string "{RIVAL}$"

PewterCity_Gym_Text_GymStatuePlayerWon::
    .string "ﺻﺎﻟﺔ ﺒﻮﻛﻴﻤﻮﻥ ﻓﻲ ﺑﻴﻮﺗﺮ\n"
    .string "ﻘﺎﺋﺪ: ﺑﺮﻭﻙ\p"
    .string "ﻤﺪﺭﺑﻮﻥ ﻔﺎﺋﺰﻭﻥ:\n"
    .string "{RIVAL}، {PLAYER}$"

