# Arabic 8x16 pixel font kit

From the Mega Man Battle Network 1 Arabic translation (glyph art based on the
Pokémon Crystal Arabic font). For reuse in Pokémon FireRed.

## Files

| File | What it is |
|---|---|
| `atlas_regular_8x16.png` | All 134 glyphs, 16 per row, 8x16 px cells, indexed colour |
| `atlas_bold_8x16.png` | Same order, bold variant (heavier strokes, outline = colour 2) |
| `glyphs/regular/`, `glyphs/bold/` | One PNG per glyph, named `U+XXXX_slot.png` |
| `glyph_map.json` | Per glyph: Unicode char, name, atlas index, ink columns, suggested advance width, the slot it had in BN1 |
| `arabic_shaping.py` | Text -> list of glyph keys in draw order (right to left). Needs `pip install arabic-reshaper python-bidi` |
| `preview_regular.png` | Labelled sheet to look up a glyph by its code |
| `source/` | The original BN1 font sheets and BN1's `arabic.py`, for reference |

## Colours (palette index)

- 0: transparent / outside
- 1: background
- 2: shadow (regular) or outline (bold)
- 3: ink

FireRed's text renderer uses background, foreground and shadow colours. Map 1 to
background, 3 to foreground and 2 to shadow.

## Glyph set

- **U+FE80 to U+FEFC:** every Arabic presentation form (isolated, final, initial
  and medial), including the lam-alef ligatures.
- **U+060C ، U+061B ؛ U+061F ؟:** Arabic punctuation. ؟ is drawn as a mirrored ?.
- **Private-use helpers that `arabic_shaping.py` emits:**
  - **U+E081, U+E083, U+E087, U+E08D:** آ أ إ ا used inside a word after a
    non-joining letter. The glyph sits at the right of its cell so the gap stays
    small.
  - **U+E090:** two alefs in one cell, for stretched words like واااه.
  - **U+E0A0:** the article ال packed into one cell.

Some forms share artwork. For example, beh isolated and final are the same, and
seen, sheen, sad and dad share one cell for isolated and final. `bn1_slot` in
glyph_map.json shows which forms share.

## Notes for FireRed

- **Text direction.** FireRed draws left to right with a proportional (variable
  width) font, so it needs an RTL patch, as we did for BN1 and Crystal. Either
  draw from the right edge moving left, or store each line reversed and
  right-align it. `shape_line()` returns glyphs in draw order (index 0 is the
  right-most).
- **Widths.** `advance_regular` is the ink width + 1, a starting point for
  FireRed's per-glyph width table. Joining forms (initial and medial) should
  touch their neighbour, so use the full 8 px for them if the joins show gaps.
- **Font slots.** FireRed's font sheet has unused slots (the Japanese
  characters). Put the glyphs there and build the charmap from glyph_map.json.
- **Stretched words.** Words like واااه look spaced out unless the alefs come in
  pairs, because alef doesn't join to the left. In BN1 we kept these runs to two
  or three letters.
