PewterCity_Gym_Text_BrockIntro::
    .string "ﺇﺫﻥ ﺃﻧﺖ ﻫﻨﺎ. ﺃﻧﺎ ﺑﺮﻭﻙ،\n"
    .string "ﻗﺎﺋﺪ ﺻﺎﻟﺔ ﺑﻴﻮﺗﺮ.\p"
    .string "ﺇﺭﺩﺗﻲ ﺼﻠﺒﺔ ﻛﺎﻟﺼﺨﺮ ﺗﻈﻬﺮ\n"
    .string "ﺣﺘﻰ ﻓﻲ ﺑﻮﻛﻴﻤﻮﻧﻲ.\p"
    .string "ﺑﻮﻛﻴﻤﻮﻧﻲ ﻛﻠﻬﺎ ﺻﻠﺒﺔ ﻛﺎﻟﺼﺨﺮ،\n"
    .string "ﻭﻋﺰﻳﻤﺘﻬﺎ ﻻ ﺗﻠﻴﻦ.\p"
    .string "ﻧﻌﻢ، ﺑﻮﻛﻴﻤﻮﻧﻲ ﻛﻠﻬﺎ ﻣﻦ\n"
    .string "ﻧﻮﻉ ﺼﺨﺮ!\p"
    .string "ﻓﻮﻫﺎﻫﺎ! ﺃﺗﺘﺤﺪﻧﻲ ﻭﻧﺖ ﺗﻌﻠﻢ\n"
    .string "ﺃﻧﻚ ﺳﺘﺨﺴﺮ؟\p"
    .string "ﺇﻧﻪ ﺷﺮﻑ ﻤﺪﺭﺏ ﻣﺎ ﻳﺪﻓﻌﻚ\n"
    .string "ﺇﻟﻰ ﺗﺤﺪﻳﻲ.\p"
    .string "ﺣﺴﻨﺎ ﺇﺫﻥ!\n"
    .string "ﺃﺭﻧﻲ ﺃﻓﻀﻞ ﻣﺎ ﻟﺪﻳﻚ!{PLAY_BGM}{MUS_ENCOUNTER_GYM_LEADER}$"

@ NOTE: This defeat text actually causes a buffer overflow. It's too long for the gDisplayedStringBattle
@ buffer that it's put into, and it stomps all over the gBattleTextBuffs after, as well as the otherwise
@ unused array after that, sFlickerArray. Perhaps that's the reason why said array exists.
PewterCity_Gym_Text_BrockDefeat::
    .string "ﺍﺳﺘﺨﻔﻔﺖ ﺑﻚ، ﻓﺨﺴﺮﺕ.\p"
    .string "ﻭﺛﺒﺎﺗﺎ ﻟﻔﻮﺯﻙ، ﺃﻣﻨﺤﻚ ﻫﺬ…\n"
    .string "ﻭﺳﺎﻡ ﺼﺨﺮﺓ ﺮﺳﻤﻲ ﻟﻠﺪﻭﺭﻱ.\p"
    .string "{FONT_NORMAL}ﺣﺼﻞ {PLAYER} ﻋﻠﻰ ﻭﺳﺎﻡ ﺼﺨﺮﺓ\n"
    .string "ﻣﻦ ﺑﺮﻭﻙ!{PAUSE_MUSIC}{PLAY_BGM}{MUS_OBTAIN_BADGE}{PAUSE 0xFE}{PAUSE 0x56}{RESUME_MUSIC}\p"
    .string "{FONT_MALE}ﻣﺠﺮﺩ ﺍﻣﺘﻼﻙ ﻭﺳﺎﻡ ﺼﺨﺮﺓ ﻳﺠﻌﻞ\n"
    .string "ﺑﻮﻛﻴﻤﻮﻧﻚ ﺃﻗﻮﻯ.\p"
    .string "ﻭﻫﻮ ﻳﺘﻴﺢ ﺃﻳﻀﺎ ﺍﺳﺘﺨﺪﻡ ﺣﺮﻛﺔ\n"
    .string "ﻮﻣﻴﺾ ﺧﺎﺭﺝ ﻨﺰﻝ.\p"
    .string "ﻃﺒﻌﺎ، ﻳﺠﺐ ﺃﻥ ﻳﻌﺮﻑ ﺒﻮﻛﻴﻤﻮﻥ\n"
    .string "ﺣﺮﻛﺔ ﻮﻣﻴﺾ ﻟﻴﺴﺘﺨﺪﻣﻬﺎ.$"

PewterCity_Gym_Text_TakeThisWithYou::
    .string "ﺍﻧﺘﻈﺮ!\n"
    .string "ﺧﺬ ﻫﺬ ﻣﻌﻚ.$"

PewterCity_Gym_Text_ReceivedTM39FromBrock::
    .string "ﺣﺼﻞ {PLAYER} ﻋﻠﻰ ﻘﺮﺹ ﺘﻘﻨﻲ\n"
    .string "39\p"
    .string "ﻣﻦ ﺑﺮﻭﻙ.$"

PewterCity_Gym_Text_ExplainTM39::
    .string "ﻘﺮﺹ ﺘﻘﻨﻲ ﻳﺤﻮﻱ ﺣﺮﻛﺔ\n"
    .string "ﻳﺘﻌﻠﻤﻬﺎ ﺒﻮﻛﻴﻤﻮﻥ.\p"
    .string "ﺍﺳﺘﺨﺪﻡ ﻘﺮﺹ ﻳﻌﻠﻢ ﺒﻮﻛﻴﻤﻮﻥ\n"
    .string "ﺤﺮﻛﺔ ﺘﻲ ﻓﻴﻪ.\p"
    .string "ﻟﻜﻦ ﻘﺮﺹ ﻳﺴﺘﺨﺪﻡ ﻣﺮﺓ ﻭﺣﺪﺓ\n"
    .string "ﻓﻘﻂ.\p"
    .string "ﻟﺬ ﺍﺧﺘﺮ ﺒﻮﻛﻴﻤﻮﻥ ﺑﻌﻨﺎﻳﺔ\n"
    .string "ﺣﻴﻦ ﺗﺴﺘﺨﺪﻣﻪ.\p"
    .string "ﻋﻠﻰ ﺃﻱ ﺣﺎﻝ…\n"
    .string "ﻓﻲ ﻘﺮﺹ ﺘﻘﻨﻲ 39 ﻗﺒﺮ ﺼﺨﻮﺭ.\p"
    .string "ﺗﺮﻣﻲ ﺼﺨﻮﺭ ﻋﻠﻰ ﺨﺼﻢ\n"
    .string "ﻭﺗﺨﻔﺾ ﺳﺮﻋﺘﻪ.$"

PewterCity_Gym_Text_BrockPostBattle::
    .string "ﻓﻲ ﻋﺎﻟﻤﻨﺎ ﻮﺳﻊ ﻫﺬ، ﻣﺪﺭﺑﻮﻥ\n"
    .string "ﻣﻦ ﻛﻞ ﻧﻮﻉ.\p"
    .string "ﻭﻳﺒﺪﻭ ﺃﻧﻚ ﻣﻮﻫﻮﺏ ﺟﺪ\n"
    .string "ﻛﻤﺪﺭﺏ ﺑﻮﻛﻴﻤﻮﻥ.\p"
    .string "ﻓﺎﺳﻤﺢ ﻟﻲ ﺑﺎﻗﺘﺮﺡ:\p"
    .string "ﺍﺫﻫﺐ ﺇﻟﻰ ﺻﺎﻟﺔ ﺳﻴﺮﻭﻟﻴﻦ\n"
    .string "ﻭﺧﺘﺒﺮ ﻗﺪﺭﺗﻚ.$"

PewterCity_Gym_Text_DontHaveRoomForThis::
    .string "ﻟﻴﺲ ﻟﺪﻳﻚ ﻣﻜﺎﻥ ﻟﻬﺬ.$"

PewterCity_Gym_Text_LiamIntro::
    .string "ﻗﻒ ﻣﻜﺎﻧﻚ ﻳﺎ ﺻﻐﻴﺮ!\p"
    .string "ﺃﻧﺖ ﻋﻠﻰ ﺑﻌﺪ ﻋﺸﺮﺓ ﺁﻻﻑ ﺳﻨﺔ\n"
    .string "ﺿﻮﺋﻴﺔ ﻣﻦ ﻣﻮﺟﻬﺔ ﺑﺮﻭﻙ!$"

PewterCity_Gym_Text_LiamDefeat::
    .string "ﺗﺒﺎ!\p"
    .string "ﺴﻨﺔ ﻀﻮﺋﻴﺔ ﻟﻴﺴﺖ ﺯﻣﻨﺎ…\n"
    .string "ﺇﻧﻬﺎ ﺗﻘﻴﺲ ﻤﺴﺎﻓﺔ!$"

PewterCity_Gym_Text_LiamPostBattle::
    .string "ﺃﻧﺖ ﻗﻮﻱ ﺟﺪ.\n"
    .string "…ﻟﻜﻦ ﻟﻴﺲ ﻣﺜﻞ ﺑﺮﻭﻙ!$"

PewterCity_Gym_Text_LetMeTakeYouToTheTop::
    .string "ﺃﻫﻼ!\n"
    .string "ﻫﻞ ﺗﺤﻠﻢ ﺃﺣﻼﻣﺎ ﻛﺒﻴﺮﺓ؟\p"
    .string "ﻫﻞ ﺗﺠﺮﺅ ﻋﻠﻰ ﺃﻥ ﺗﺤﻠﻢ ﺑﺄﻥ ﺗﺼﺒﺢ\n"
    .string "ﺑﻄﻞ ﺒﻮﻛﻴﻤﻮﻥ؟\p"
    .string "ﻟﺴﺖ ﻣﺪﺭﺑﺎ، ﻟﻜﻨﻨﻲ ﺃﺳﺘﻄﻴﻊ ﺃﻥ\n"
    .string "ﺃﻧﺼﺤﻚ ﻛﻴﻒ ﺗﻔﻮﺯ.\p"
    .string "ﺩﻋﻨﻲ ﺁﺧﺬﻙ ﺇﻟﻰ ﻘﻤﺔ!$"

PewterCity_Gym_Text_LetsGetHappening::
    .string "ﺭﺋﻊ!\n"
    .string "ﻟﻨﺒﺪ!$"

PewterCity_Gym_Text_TryDifferentPartyOrders::
    .string "ﺃﻭﻝ ﺑﻮﻛﻴﻤﻮﻥ ﻳﺪﺧﻞ ﻨﺰﻝ ﻫﻮ\n"
    .string "ﺍﻷﻭﻝ ﻓﻲ ﻗﺎﺋﻤﺔ ﺒﻮﻛﻴﻤﻮﻥ.\p"
    .string "ﺑﺘﻐﻴﻴﺮ ﺗﺮﺗﻴﺐ ﺑﻮﻛﻴﻤﻮﻧﻚ،\n"
    .string "ﻗﺪ ﺗﻜﺴﺐ ﺃﻓﻀﻠﻴﺔ.\p"
    .string "ﺟﺮﺏ ﺗﺮﺗﻴﺒﺎﺕ ﻣﺨﺘﻠﻔﺔ ﺗﻨﺎﺳﺐ\n"
    .string "ﻓﺮﻳﻖ ﺧﺼﻤﻚ.$"

PewterCity_Gym_Text_ItsFreeLetsGetHappening::
    .string "ﺇﻧﻬﺎ ﺧﺪﻣﺔ ﻣﺠﺎﻧﻴﺔ!\n"
    .string "ﻟﻨﺒﺪ!$"

PewterCity_Gym_Text_YoureChampMaterial::
    .string "ﺗﻤﺎﻣﺎ ﻛﻤﺎ ﺗﻮﻗﻌﺖ!\n"
    .string "ﺃﻧﺖ ﻣﺸﺮﻭﻉ ﺑﻄﻞ ﺑﻮﻛﻴﻤﻮﻥ!$"

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

