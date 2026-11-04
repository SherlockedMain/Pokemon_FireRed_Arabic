# Crystal Arabic names — moves, types, items

Taken from the finished Pokémon Crystal Arabic ROM (v1.0.2 as updated, SHA-1 7abd57e6…),
so these are the names the game actually shows, not the older review sheets
(which differ in 6 moves, e.g. SAND-ATTACK is now ذر الرمل).

| File | What |
|---|---|
| `crystal_arabic_names.xlsx` | Moves (251, with Japanese), Types (18), Items (222 real ones; the unused slots are left out) |
| `crystal_arabic_names.json` / `.csv` | The same, for scripts |
| `names_to_firered.py` | Matches by English name against a pokefirered checkout and writes patched copies + `report.csv` |
| `crystal_arabic_charmap.xlsx` | Crystal's letter-form table (for the shaped-tile encoding) |

Arabic is plain Unicode in reading order. "Tiles" is how many 8-pixel cells the name takes in
Crystal's font (a seen/sheen/sad/dad at word end counts 2). The longest names here are moves 12, items 12, types 5 tiles; check them
against your FireRed build's own name-length limits (pokefirered's are usually 12 / 14 / 6).

Not in Crystal, so still to translate for FireRed: moves 252–354, the Gen 3 items and berries,
and the Gen 3 item descriptions. The script lists every one of them in `report.csv`.
