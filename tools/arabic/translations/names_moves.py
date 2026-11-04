# -*- coding: utf-8 -*-
"""Batch 08 - Move names (src/data/text/move_names.h).

Moves 1-251 come from the Pokémon Crystal Arabic translation
(tools/arabic/crystal_names/crystal_arabic_names.json), matched by English name.
The battle move menu prints names in the small font in 64 px windows; when a
Crystal name is wider, the first shorter candidate that fits is used and the
row is marked as a PROPOSAL for review. Moves 252-354 (Gen 3) are new."""
import json, os, re
from arabic_text import ROOT, measure, shape, tokens

FILE = 'src/data/text/move_names.h'
SMALL_PX, MAX_BYTES = 64, 12
_norm = lambda s: re.sub(r'[^A-Z0-9]', '', s.upper().replace('É', 'E').replace('é', 'E'))
_cr = {_norm(m['english']): m['arabic'] for m in json.load(open(os.path.join(os.path.dirname(__file__), '..', 'crystal_names',
       'crystal_arabic_names.json'), encoding='utf-8'))['moves']}

# Shorter candidates for the Crystal names that are too wide (closest to the original first)
SHORTER = {
 'DOUBLEEDGE': ['هجوم مستميت', 'هجمة يائسة', 'ضربة يائسة'],
 'SPIDERWEB': ['شبكة العنكب', 'نسيج عنكبوت', 'شبكة لزجة'],
 'SKULLBASH': ['نطحة صاروخ', 'نطحة ساحقة', 'نطحة قوية'],
 'BONEMERANG': ['بومرانغ', 'عظم مرتد'],
 'CROSSCHOP': ['ضربة متصالبة', 'قطع متقاطع', 'ضربة مزدوجة'],
 'FLAIL': ['تخبط', 'ضرب عشوائي'],
 'CRABHAMMER': ['مطرقة سلطع', 'كماشة ساحقة'],
 'KARATECHOP': ['ضربة كاراتي', 'حد الكف'],
 'ICEPUNCH': ['لكمة الجليد', 'لكمة ثلجية'],
 'SWEETKISS': ['قبلة ملاك', 'قبلة لطيفة', 'قبلة حلوة'],
 'SUBMISSION': ['رمية جحيمية', 'رمية مدمرة', 'إخضاع'],
 'DYNAMICPUNCH': ['لكمة مدوية', 'لكمة هائلة'],
 'BLIZZARD': ['عاصفة الثلج', 'إعصار ثلجي'],
 'ZAPCANNON': ['مدفع صاعق', 'مدفع البرق'],
 'SYNTHESIS': ['بناء ضوئي', 'تمثيل ضوئي'],
 'SKYATTACK': ['صولة السماء', 'هجوم سماوي', 'انقضاض'],
 'BUBBLEBEAM': ['شعاع فقاعي', 'وابل فقاعات'],
 'SURF': ['ركوب الموج', 'الموجة'],
 'SPIKECANNON': ['مدفع أشواك', 'رشق الأشواك'],
 'METALCLAW': ['مخلب فولاذي', 'مخلب حديدي'],
 'FUTURESIGHT': ['بصيرة مؤلمة', 'بصيرة'],
 'FURYATTACK': ['وابل طعنات', 'طعنات متتالية'],
 'DOUBLESLAP': ['وابل صفعات', 'صفعات متتالية'],
 'COMETPUNCH': ['وابل لكمات', 'لكمات متتالية'],
}

GEN3 = {
 'FAKE OUT':'مباغتة','UPROAR':'ضجيج','STOCKPILE':'تخزين','SPIT UP':'قذف','SWALLOW':'ابتلاع','HEAT WAVE':'موجة حر',
 'HAIL':'حبات البرد','TORMENT':'مضايقة','FLATTER':'تملق','WILL-O-WISP':'شعلة تائهة','MEMENTO':'تذكار','FACADE':'واجهة',
 'FOCUS PUNCH':'لكمة مركزة','SMELLINGSALT':'ملح الإفاقة','FOLLOW ME':'اتبعني','NATURE POWER':'قوة الطبيعة',
 'CHARGE':'شحن','TAUNT':'استفزاز','HELPING HAND':'يد العون','TRICK':'خدعة','ROLE PLAY':'تقمص','WISH':'أمنية',
 'ASSIST':'مساعدة','INGRAIN':'تجذر','SUPERPOWER':'قوة خارقة','MAGIC COAT':'درع عاكس','RECYCLE':'تدوير','REVENGE':'ثأر',
 'BRICK BREAK':'كاسر الطوب','YAWN':'تثاؤب','KNOCK OFF':'إسقاط','ENDEAVOR':'مثابرة','ERUPTION':'ثوران',
 'SKILL SWAP':'تبادل القدرة','IMPRISON':'حبس','REFRESH':'انتعاش','GRUDGE':'ضغينة','SNATCH':'خطف',
 'SECRET POWER':'قوة خفية','DIVE':'غوص','ARM THRUST':'دفع الذراع','CAMOUFLAGE':'تمويه','TAIL GLOW':'وهج الذيل',
 'LUSTER PURGE':'بريق مطهر','MIST BALL':'كرة الضباب','FEATHERDANCE':'رقصة الريش','TEETER DANCE':'رقصة الترنح',
 'BLAZE KICK':'ركلة اللهب','MUD SPORT':'لعب بالطين','ICE BALL':'كرة جليد','NEEDLE ARM':'ذراع الإبر','SLACK OFF':'تكاسل',
 'HYPER VOICE':'صوت خارق','POISON FANG':'ناب سام','CRUSH CLAW':'مخلب ساحق','BLAST BURN':'حريق مدمر',
 'HYDRO CANNON':'مدفع مائي','METEOR MASH':'نيزك ساحق','ASTONISH':'إفزاع','WEATHER BALL':'كرة الطقس',
 'AROMATHERAPY':'علاج بالعطر','FAKE TEARS':'دموع زائفة','AIR CUTTER':'قاطع الهواء','OVERHEAT':'احتراق مفرط',
 'ODOR SLEUTH':'تعقب الأثر','ROCK TOMB':'قبر الصخور','SILVER WIND':'ريح فضية','METAL SOUND':'صوت معدني',
 'GRASSWHISTLE':'صفير العشب','TICKLE':'دغدغة','COSMIC POWER':'قوة كونية','WATER SPOUT':'نافورة','SIGNAL BEAM':'شعاع الإشارة',
 'SHADOW PUNCH':'لكمة الظل','EXTRASENSORY':'حاسة خارقة','SKY UPPERCUT':'لكمة صاعدة','SAND TOMB':'قبر الرمل',
 'SHEER COLD':'برد قارس','MUDDY WATER':'ماء موحل','BULLET SEED':'بذور رصاصية','AERIAL ACE':'انقضاض جوي',
 'ICICLE SPEAR':'رمح جليدي','IRON DEFENSE':'دفاع حديدي','BLOCK':'سد','HOWL':'عواء','DRAGON CLAW':'مخلب التنين',
 'FRENZY PLANT':'نبات هائج','BULK UP':'تضخيم','BOUNCE':'قفزة','MUD SHOT':'رمية طين','POISON TAIL':'ذيل سام',
 'COVET':'طمع','VOLT TACKLE':'صدمة برقية','MAGICAL LEAF':'ورقة عجيبة','WATER SPORT':'لعب بالماء','CALM MIND':'صفاء الذهن',
 'LEAF BLADE':'نصل الورق','DRAGON DANCE':'رقصة التنين','ROCK BLAST':'وابل صخري','SHOCK WAVE':'موجة صدمة',
 'WATER PULSE':'نبضة مائية','DOOM DESIRE':'ضربة الهلاك','PSYCHO BOOST':'دفعة نفسية',
}
GEN3_NOTES = {'MAGIC COAT':'Avoids «سحر»: a reflecting shield.', 'MAGICAL LEAF':'Avoids «سحر»: «عجيبة».',
              'WILL-O-WISP':'Avoids spirits: «شعلة تائهة».', 'HAIL':'«حبات البرد» so it is not read as «البَرْد» (cold).'}

def _fits(a):
    s = shape(a)
    return measure(s, 'small') <= SMALL_PX and len(tokens(s)) <= MAX_BYTES

_EN = dict(re.findall(r"\[(MOVE_\w+)\] = '(.*?)'", open(os.path.join(os.path.dirname(__file__), 'names_moves_en.txt'),
           encoding='utf-8').read()))
ENTRIES, PROPOSALS = [], []
for key, en in _EN.items():
    n = _norm(en)
    if n in _cr:
        ar, note = _cr[n], 'From Pokémon Crystal Arabic.'
        if not _fits(ar):
            cand = next((c for c in SHORTER.get(n, []) if _fits(c)), None)
            if cand:
                note = 'PROPOSAL: Crystal «%s» is too wide for the 64 px move menu; shortened.' % ar
                PROPOSALS.append((en, ar, cand))
                ar = cand
    elif en in GEN3:
        ar, note = GEN3[en], GEN3_NOTES.get(en, 'Gen 3 move (not in Crystal).')
    else:
        continue
    ENTRIES.append(dict(id=key, key=key, file=FILE, screen='Move names', where=en.title(),
                        box=('line', 120, 'normal', 1), max_bytes=MAX_BYTES, small_px=SMALL_PX, ar=ar, note=note))

README = [
    ('Pokémon FireRed – Arabic translation – Batch 08: move names', 'title'),
    ('Moves 1-251 are your Pokémon Crystal names. The battle move menu gives each name 64 px in the small font: '
     'where a Crystal name is wider, a shorter form is used and the note says PROPOSAL (filter the Translation sheet on it). '
     'Moves 252-354 (Gen 3) are new.', 'text'),
    ('Limits: 12 letters and 64 px in the small font; the Fit column checks both.', 'edit'),
    ('Applying: python3 tools/arabic/apply_translations.py names_moves, then make.', 'text'),
]
GLOSSARY = [(en, b, 'Crystal: «%s» (too wide)' % a) for en, a, b in PROPOSALS] + [
    ('MAGIC COAT / MAGICAL LEAF', 'درع عاكس / ورقة عجيبة', 'No «سحر».'),
    ('FUTURE SIGHT', 'بصيرة مؤلمة', 'Crystal «نبوءة مؤلمة»: «بصيرة» is shorter and avoids «prophecy».'),
]
