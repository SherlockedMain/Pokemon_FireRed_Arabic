# -*- coding: utf-8 -*-
# L/R help system, part 4: fundamentals, last definitions, and the type matchup list
# (the 36 tables are built from the English ones with the Crystal type names).
import json, os, re
_T = dict(NORMAL='عادي', FIGHTING='مقاتل', FLYING='طائر', POISON='سام', GROUND='أرضي', ROCK='صخري', BUG='حشري',
          GHOST='شبحي', STEEL='فولاذي', FIRE='ناري', WATER='مائي', GRASS='عشبي', ELECTRIC='كهربي', PSYCHIC='نفسي',
          ICE='جليدي', DRAGON='تنيني', DARK='ظلامي')
H4 = {
 'DefinePokemon':'البوكيمون اسم يُطلق على كائنات عجيبة تسكن كل أركان هذا العالم، يربيها الناس رفاقا لهم، أو يخوضون بها النزالات، وغير ذلك.',
 'DefineIDNo2':'رقم الهوية رقم خاص بك وحدك كمدرب، يُعرف به المدرب الأصلي بدقة مع اسمه، ولا يتغير حتى لو بودل البوكيمون.',
 'DefineMoney2':'كلما فزت في نزال ضد مدرب نلت مكافأة مالية، فادخرها لتستمتع بالتسوق في متاجر البوكيمون!',
 'DefineBadges2':'يبين هذا عدد أوسمة دوري البوكيمون التي نلتها، وتنال الأوسمة بهزيمة قادة الصالات في المدن والبلدات.',
 'GameFundamentals1':'أساسيات اللعبة 1', 'GameFundamentals2':'أساسيات اللعبة 2', 'GameFundamentals3':'أساسيات اللعبة 3',
 'WhatArePokemon':'ما هي البوكيمونات؟',
 'DescGameFundamentals1':'زر كل مدينة وبلدة، واسلك كل طريق، واستكشف كل كهف، وواجه كل تحد، وأنت تسعى لتصبح أعظم مدربي البوكيمون!',
 'DescGameFundamentals2':'ستواجه في مغامرتك عقبات كثيرة، ولكل عقبة حل، بفعل شيء ما أو بكشف سر ما، وبعض العقبات يتأثر بأمر يحدث في مكان بعيد.',
 'DescGameFundamentals3':'بعض العقبات التي تعترض طريقك تزول حين تتعلم بوكيموناتك حركات معينة.',
 'DescWhatArePokemon':'البوكيمونات كائنات عجيبة يلفها الغموض، تلقاها في كل أنحاء العالم… في العشب الطويل والكهوف والبحر وغيرها، ويبدو أنها تطيع المدربين الذين أمسكوها.',
 'UsingTypeMatchupList':'استخدام جدول توافق الأنواع',
 'HowToUseTypeMatchupList':'تختلف فعالية الحركة بحسب نوعها ونوع البوكيمون المستهدف: {CIRCLE_DOT}: فعالة جدا! {TRIANGLE}: ليست فعالة كثيرا {BIG_MULT_X}: لا تأثير لها أبدا (ولا تغيير في غير ذلك).',
}
for en, ar in _T.items():
    k = en.title()
    H4['OwnMove' + k] = 'نوع حركتك: ' + ar
    H4['OwnPokemon' + k] = 'نوع بوكيمونك: ' + ar

_en = dict(json.load(open(os.path.join(os.path.dirname(__file__), 'help_en.json'), encoding='utf-8')))
for label, text in _en.items():
    m = re.match(r'Help_Text_TypeMatchupOwn(Move|Pokemon)(\w+)$', label)
    if not m:
        continue
    body = text.replace('\\p', '\n').replace('\\n', '\n').replace('\\l', ' ').rstrip('$')
    rows = []
    for marker in ('{CIRCLE_DOT}', '{TRIANGLE}', '{BIG_MULT_X}'):
        mm = re.search(re.escape(marker) + r':\s*([A-Z ,\n]+?)(?=\s*\{|\s*$)', body)
        if mm:
            types = [t.strip() for t in re.split(r'[,\n]', mm.group(1)) if t.strip()]
            rows.append(marker + ': ' + '، '.join(_T[t] for t in types))
    head = 'أثرها على البوكيمون الخصم:' if m.group(1) == 'Move' else 'أثر حركات الخصم على بوكيمونك:'
    H4[label[len('Help_Text_'):]] = '\n\n'.join([head] + rows)
