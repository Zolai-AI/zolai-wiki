# Zolai Tone System (4 Tones like Chinese)

## Overview
Zolai is a tonal language with 4 tones, similar to Chinese. The same spelling can have different meanings depending on tone.

**Source**: `data/reference/grammar/lesson_02_Tone_Sandhi_Tedim_Zomi_Toponyms.md` by Taang Zomi

## The 4 Tones

| Tone | Name | Pitch | Description |
|------|------|-------|-------------|
| T1 | High | High level | High pitch |
| T2 | High Falling | Falls from high | Only appears via tone sandhi |
| T3 | Low | Low level | Low pitch |
| T4 | Creaky | Glottalized | Glottalized/creaky voice |

## Tone Sandhi Rules (19 Rules)

When tones combine in compounds, they change according to 19 rules:

### Unchanged Combinations (Section 1)
- T1 + T1 = T1.T1
- T1 + T3 = T1.T3
- T1 + T4 = T1.T4
- T3 + T1 = T3.T1
- T3 + T3 = T3.T3
- T4 + T1 = T4.T1
- T4 + T3 = T4.T3
- T4 + T4 = T4.T4

### Changed Combinations (Section 2 - Tone Sandhi)
- T1 + T3 → T2 + T3 (Rule 01)
- T1 + T4 → T1 + T2 (Rule 03)
- T3 + T1 → T2 + T1 (Rule 05)
- T3 + T3 → T2 + T3 (Rule 06)
- T3 + T4 → T3 + T2 (Rule 07)
- T4 + T1 → T4 + T1 (Rule 09, unchanged)
- T4 + T3 → T4 + T3 (Rule 10, unchanged)
- T4 + T4 → T4 + T4 (Rule 11, unchanged)

## Tone-Dependent Word Meanings

| Word | T1 (High) | T3 (Low) | T4 (Creaky) |
|------|-----------|----------|-------------|
| khem | lie/deceive | thin/weak (after illness) | — |
| nam | smell | odoriferous | — |
| zu | alcohol/distillate | — | rain (with guah-) |
| ta | completive aspect | beginning | — |
| ci | say/speak | — | — |
| ne | eat/drink | — | — |
| pai | go/move | — | — |
| om | exist/stay | — | — |

## Written Zolai

Written Zolai **does NOT mark tones**. Same spelling = different meanings.
Context determines meaning. Tone marks used in academic notation:
- Acute accent (´) = T1 (high)
- Grave accent (`) = T3 (low)
- Creaky marker (ː) = T4 (creaky)

## Implications for NLP

1. Morphology analyzer must list ALL possible meanings
2. Context is required to disambiguate tone
3. Tone sandhi affects compound pronunciation
4. Dictionary entries may need tone labels

## Source Document
`data/reference/grammar/lesson_02_Tone_Sandhi_Tedim_Zomi_Toponyms.md` - 58 pages by Taang Zomi
