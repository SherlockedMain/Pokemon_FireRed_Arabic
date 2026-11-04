# -*- coding: utf-8 -*-
"""Batch 06 - Pokémon species names (src/data/text/species_names.h).

Arabic dub forms where they exist, a consistent transliteration otherwise.
Each name must fit POKEMON_NAME_LENGTH (10 letters: Arabic now takes one byte
per letter) and the HUD's small font (51 px: the 5 px gender symbol follows the name)."""
import os, re
from arabic_text import ROOT

FILE = 'src/data/text/species_names.h'
AR = {
 'BULBASAUR':'بولباسور','IVYSAUR':'أيفيسور','VENUSAUR':'فينوسور','CHARMANDER':'تشارماندر','CHARMELEON':'تشارملون',
 'CHARIZARD':'تشاريزارد','SQUIRTLE':'سكويرتل','WARTORTLE':'وارتورتل','BLASTOISE':'بلاستويز','CATERPIE':'كاتربي',
 'METAPOD':'ميتابود','BUTTERFREE':'بترفري','WEEDLE':'ويدل','KAKUNA':'كاكونا','BEEDRILL':'بيدريل','PIDGEY':'بيدجي',
 'PIDGEOTTO':'بيدجيوتو','PIDGEOT':'بيدجيوت','RATTATA':'راتاتا','RATICATE':'راتيكيت','SPEAROW':'سبيرو','FEAROW':'فيرو',
 'EKANS':'إيكانز','ARBOK':'أربوك','PIKACHU':'بيكاتشو','RAICHU':'رايتشو','SANDSHREW':'ساندشرو','SANDSLASH':'ساندسلاش',
 'NIDORAN♀':'نيدوران♀','NIDORINA':'نيدورينا','NIDOQUEEN':'نيدوكوين','NIDORAN♂':'نيدوران♂','NIDORINO':'نيدورينو',
 'NIDOKING':'نيدوكينغ','CLEFAIRY':'كليفيري','CLEFABLE':'كليفيبل','VULPIX':'فولبيكس','NINETALES':'نايتيلز',
 'JIGGLYPUFF':'جيغليباف','WIGGLYTUFF':'ويغليتاف','ZUBAT':'زوبات','GOLBAT':'غولبات','ODDISH':'أوديش','GLOOM':'غلوم',
 'VILEPLUME':'فايلبلوم','PARAS':'باراس','PARASECT':'باراسيكت','VENONAT':'فينونات','VENOMOTH':'فينوموث','DIGLETT':'ديغليت',
 'DUGTRIO':'دوغتريو','MEOWTH':'ميوث','PERSIAN':'بيرشن','PSYDUCK':'سايداك','GOLDUCK':'غولداك','MANKEY':'مانكي',
 'PRIMEAPE':'برايماب','GROWLITHE':'غرولايث','ARCANINE':'أركانين','POLIWAG':'بوليواغ','POLIWHIRL':'بوليويرل',
 'POLIWRATH':'بوليراث','ABRA':'أبرا','KADABRA':'كادابرا','ALAKAZAM':'ألاكازام','MACHOP':'ماتشوب','MACHOKE':'ماتشوك',
 'MACHAMP':'ماتشامب','BELLSPROUT':'بلسبراوت','WEEPINBELL':'ويبينبل','VICTREEBEL':'فيكتريبل','TENTACOOL':'تنتاكول',
 'TENTACRUEL':'تنتاكرول','GEODUDE':'جيوديود','GRAVELER':'غرافلر','GOLEM':'غولم','PONYTA':'بونيتا','RAPIDASH':'رابيداش',
 'SLOWPOKE':'سلوبوك','SLOWBRO':'سلوبرو','MAGNEMITE':'ماغنمايت','MAGNETON':'ماغنتون','FARFETCH\'D':'فارفتشد',
 'FARFETCH':'فارفتشد', 'DODUO':'دودو','DODRIO':'دودريو','SEEL':'سيل','DEWGONG':'دوغونغ','GRIMER':'غرايمر','MUK':'مك','SHELLDER':'شيلدر',
 'CLOYSTER':'كلويستر','GASTLY':'غاستلي','HAUNTER':'هونتر','GENGAR':'غينغار','ONIX':'أونيكس','DROWZEE':'دراوزي',
 'HYPNO':'هيبنو','KRABBY':'كرابي','KINGLER':'كينغلر','VOLTORB':'فولتورب','ELECTRODE':'إلكترود','EXEGGCUTE':'إكزكيوت',
 'EXEGGUTOR':'إكزكيوتر','CUBONE':'كيوبون','MAROWAK':'ماروك','HITMONLEE':'هتمونلي','HITMONCHAN':'هتمونشان',
 'LICKITUNG':'ليكتونغ','KOFFING':'كوفينغ','WEEZING':'ويزينغ','RHYHORN':'رايهورن','RHYDON':'رايدون','CHANSEY':'تشانسي',
 'TANGELA':'تانغيلا','KANGASKHAN':'كنغسخان','HORSEA':'هورسي','SEADRA':'سيدرا','GOLDEEN':'غولدين','SEAKING':'سيكينغ',
 'STARYU':'ستاريو','STARMIE':'ستارمي','MR. MIME':'مستر ميم','SCYTHER':'سايذر','JYNX':'جينكس','ELECTABUZZ':'إلكتابز',
 'MAGMAR':'ماغمار','PINSIR':'بنسير','TAUROS':'توروس','MAGIKARP':'ماجيكارب','GYARADOS':'غياردوس','LAPRAS':'لابراس',
 'DITTO':'ديتو','EEVEE':'إيفي','VAPOREON':'فابوريون','JOLTEON':'جولتيون','FLAREON':'فلاريون','PORYGON':'بوريغون',
 'OMANYTE':'أومانايت','OMASTAR':'أومستار','KABUTO':'كابوتو','KABUTOPS':'كابوتوبس','AERODACTYL':'إيرودكتل',
 'SNORLAX':'سنورلاكس','ARTICUNO':'أرتيكونو','ZAPDOS':'زابدوس','MOLTRES':'مولتريس','DRATINI':'دراتيني',
 'DRAGONAIR':'دراغونير','DRAGONITE':'دراغونايت','MEWTWO':'ميوتو','MEW':'ميو',
 'CHIKORITA':'تشكوريتا','BAYLEEF':'بايليف','MEGANIUM':'ميغانيوم','CYNDAQUIL':'سنداكويل','QUILAVA':'كويلافا',
 'TYPHLOSION':'تايفلوجن','TOTODILE':'توتودايل','CROCONAW':'كروكوناو','FERALIGATR':'فيرالغاتر','SENTRET':'سينتريت',
 'FURRET':'فوريت','HOOTHOOT':'هوتهوت','NOCTOWL':'نوكتاول','LEDYBA':'ليديبا','LEDIAN':'ليديان','SPINARAK':'سبيناراك',
 'ARIADOS':'أريادوس','CROBAT':'كروبات','CHINCHOU':'تشينتشو','LANTURN':'لانترن','PICHU':'بيتشو','CLEFFA':'كليفا',
 'IGGLYBUFF':'إغليباف','TOGEPI':'توغيبي','TOGETIC':'توغيتيك','NATU':'ناتو','XATU':'زاتو','MAREEP':'ماريب',
 'FLAAFFY':'فلافي','AMPHAROS':'أمفاروس','BELLOSSOM':'بيلوسوم','MARILL':'ماريل','AZUMARILL':'أزوماريل',
 'SUDOWOODO':'سودوودو','POLITOED':'بوليتود','HOPPIP':'هوبيب','SKIPLOOM':'سكيبلوم','JUMPLUFF':'جمبلاف','AIPOM':'أيبوم',
 'SUNKERN':'سنكيرن','SUNFLORA':'سنفلورا','YANMA':'يانما','WOOPER':'ووبر','QUAGSIRE':'كواغسير','ESPEON':'إيسبيون',
 'UMBREON':'أمبريون','MURKROW':'مركرو','SLOWKING':'سلوكينغ','MISDREAVUS':'مسدريفوس','UNOWN':'أنون',
 'WOBBUFFET':'ووبوفيت','GIRAFARIG':'جيرافاريغ','PINECO':'باينكو','FORRETRESS':'فوريتريس','DUNSPARCE':'دانسبارس',
 'GLIGAR':'غلايغار','STEELIX':'ستيليكس','SNUBBULL':'سنوبل','GRANBULL':'غرانبل','QWILFISH':'كويلفيش','SCIZOR':'سيزور',
 'SHUCKLE':'شاكل','HERACROSS':'هيراكروس','SNEASEL':'سنيزل','TEDDIURSA':'تيديورسا','URSARING':'أورساينغ',
 'SLUGMA':'سلاغما','MAGCARGO':'ماغكارغو','SWINUB':'سواينب','PILOSWINE':'بيلوسوين','CORSOLA':'كورسولا',
 'REMORAID':'ريموريد','OCTILLERY':'أوكتيلري','DELIBIRD':'ديليبرد','MANTINE':'مانتاين','SKARMORY':'سكارموري',
 'HOUNDOUR':'هاودور','HOUNDOOM':'هاندوم','KINGDRA':'كينغدرا','PHANPY':'فانبي','DONPHAN':'دونفان','PORYGON2':'بوريغون2',
 'STANTLER':'ستانتلر','SMEARGLE':'سميرغل','TYROGUE':'تايروغ','HITMONTOP':'هتمونتوب','SMOOCHUM':'سموتشم',
 'ELEKID':'إليكيد','MAGBY':'ماغبي','MILTANK':'ميلتانك','BLISSEY':'بليسي','RAIKOU':'رايكو','ENTEI':'إنتاي',
 'SUICUNE':'سويكون','LARVITAR':'لارفيتار','PUPITAR':'بوبيتار','TYRANITAR':'تيرانيتار','LUGIA':'لوغيا','HO-OH':'هوه',
 'CELEBI':'سيليبي',
 'TREECKO':'تريكو','GROVYLE':'غروفايل','SCEPTILE':'سيبتايل','TORCHIC':'تورتشيك','COMBUSKEN':'كمبوسكن',
 'BLAZIKEN':'بلازيكن','MUDKIP':'مدكيب','MARSHTOMP':'مارشتومب','SWAMPERT':'سوامبرت','POOCHYENA':'بوتشيينا',
 'MIGHTYENA':'مايتيينا','ZIGZAGOON':'زيغزاغون','LINOONE':'لينون','WURMPLE':'ورمبل','SILCOON':'سيلكون',
 'BEAUTIFLY':'بيوتيفلاي','CASCOON':'كاسكون','DUSTOX':'داستوكس','LOTAD':'لوتاد','LOMBRE':'لومبر','LUDICOLO':'لوديكولو',
 'SEEDOT':'سيدوت','NUZLEAF':'نوزليف','SHIFTRY':'شيفتري','NINCADA':'نينكادا','NINJASK':'نينجاسك','SHEDINJA':'شيدينجا',
 'TAILLOW':'تايلو','SWELLOW':'سويلو','SHROOMISH':'شروميش','BRELOOM':'بريلوم','SPINDA':'سبيندا','WINGULL':'وينغل',
 'PELIPPER':'بيليبر','SURSKIT':'سيرسكيت','MASQUERAIN':'ماسكرين','WAILMER':'ويلمر','WAILORD':'ويلورد','SKITTY':'سكيتي',
 'DELCATTY':'ديلكاتي','KECLEON':'كيكليون','BALTOY':'بالتوي','CLAYDOL':'كلايدول','NOSEPASS':'نوزباس','TORKOAL':'توركول',
 'SABLEYE':'سابلاي','BARBOACH':'باربوتش','WHISCASH':'ويسكاش','LUVDISC':'لوفديسك','CORPHISH':'كورفيش',
 'CRAWDAUNT':'كرودونت','FEEBAS':'فيباس','MILOTIC':'ميلوتيك','CARVANHA':'كارفانا','SHARPEDO':'شاربيدو',
 'TRAPINCH':'ترابينش','VIBRAVA':'فيبرافا','FLYGON':'فلايغون','MAKUHITA':'ماكوهيتا','HARIYAMA':'هاريياما',
 'ELECTRIKE':'إلكترايك','MANECTRIC':'مانكتريك','NUMEL':'نومل','CAMERUPT':'كاميربت','SPHEAL':'سفيل','SEALEO':'سيليو',
 'WALREIN':'والرين','CACNEA':'كاكنيا','CACTURNE':'كاكتورن','SNORUNT':'سنورنت','GLALIE':'غلالي','LUNATONE':'لوناتون',
 'SOLROCK':'سولروك','AZURILL':'أزوريل','SPOINK':'سبوينك','GRUMPIG':'غرامبيغ','PLUSLE':'بلاسل','MINUN':'مينون',
 'MAWILE':'ماويل','MEDITITE':'ميديتايت','MEDICHAM':'ميديشام','SWABLU':'سوابلو','ALTARIA':'ألتاريا','WYNAUT':'واينوت',
 'DUSKULL':'داسكل','DUSCLOPS':'داسكلوبس','ROSELIA':'روزيليا','SLAKOTH':'سلاكوث','VIGOROTH':'فيغوروث',
 'SLAKING':'سلاكينغ','GULPIN':'غولبين','SWALOT':'سوالوت','TROPIUS':'تروبيوس','WHISMUR':'ويسمر','LOUDRED':'لاودريد',
 'EXPLOUD':'إكسبلاود','CLAMPERL':'كلامبيرل','HUNTAIL':'هانتيل','GOREBYSS':'غوربيس','ABSOL':'أبسول','SHUPPET':'شوبيت',
 'BANETTE':'بانيت','SEVIPER':'سيفايبر','ZANGOOSE':'زانغوس','RELICANTH':'ريليكانث','ARON':'آرون','LAIRON':'لايرون',
 'AGGRON':'أغرون','CASTFORM':'كاستفورم','VOLBEAT':'فولبيت','ILLUMISE':'إليوميز','LILEEP':'ليليب','CRADILY':'كراديلي',
 'ANORITH':'أنوريث','ARMALDO':'أرمالدو','RALTS':'رالتس','KIRLIA':'كيرليا','GARDEVOIR':'غاردفوار','BAGON':'باغون',
 'SHELGON':'شيلغون','SALAMENCE':'سالامنس','BELDUM':'بيلدم','METANG':'ميتانغ','METAGROSS':'ميتاغروس',
 'REGIROCK':'ريجيروك','REGICE':'ريجايس','REGISTEEL':'ريجستيل','KYOGRE':'كايوغر','GROUDON':'غرودون',
 'RAYQUAZA':'ريكوازا','LATIAS':'لاتياس','LATIOS':'لاتيوس','JIRACHI':'جيراتشي','DEOXYS':'ديوكسيس','CHIMECHO':'تشايمكو',
}

_src = open(os.path.join(ROOT, FILE), encoding='utf-8').read()
ENTRIES = []
_missing = []
for key, en in re.findall(r'\[(SPECIES_\w+)\]\s*=\s*_\("(.*?)"\)', _src):
    pass
# match on the English names from the original table, kept in this file so the batch can be re-applied
_EN = dict(re.findall(r"\[(SPECIES_\w+)\] = '(.*?)'", open(os.path.join(os.path.dirname(__file__), 'names_species_en.txt'), encoding='utf-8').read())) \
      if os.path.exists(os.path.join(os.path.dirname(__file__), 'names_species_en.txt')) else {}
for key, en in _EN.items():
    if en in AR:
        ENTRIES.append(dict(id=key, key=key, file=FILE, screen='Pokémon names', where=en.title(),
                            box=('line', 70, 'normal', 1), max_bytes=10, small_px=51, ar=AR[en], note=''))
    elif en not in ('?', '??????????'):
        _missing.append(en)
if _missing:
    print('names_species.py: no Arabic for', _missing)

README = [
    ('Pokémon FireRed – Arabic translation – Batch 06: Pokémon names', 'title'),
    ('All 386 species names, as shown in battles, the party, the Pokédex and every {STR_VAR} that inserts a name. '
     'Arabic dub forms where they exist, a consistent transliteration otherwise.', 'text'),
    ('Limits: 10 letters (Arabic now takes one byte per letter) and 51 px in the small font used by the battle HUD (the gender symbol follows the name). '
     'The Fit column checks both.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py names_species, then make.', 'text'),
    ('Nicknames you type are still Latin: the naming keyboard has no Arabic page yet.', 'text'),
]
GLOSSARY = [
    ('Gen 1 names', 'as in the Arabic dub', 'بيكاتشو، تشاريزارد، ميوتو…'),
    ('-SAUR / -TORTLE / -CHU', 'سور / تورتل / تشو', ''),
    ('MR. MIME', 'مستر مايم', 'Two words, like the English.'),
    ('♀ / ♂ in NIDORAN', 'kept', 'نيدوران♀ / نيدوران♂'),
    ('PORYGON2', 'بوريغون2', 'Digit kept.'),
    ('HO-OH', 'هوه', ''),
]
