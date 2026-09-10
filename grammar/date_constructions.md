# Date Constructions — Time Expressions in Zolai
> Last updated: 2026-09-10

> Reference for how dates and time are expressed in Zolai, drawn from "Tedim Lai Siangtho Tangthu Tom."
> Source: zolai-wiki/grammar/article_analysis_tangthu.md

---

## Overview

Zolai expresses dates using a **number + postposition** system. The core postposition is `kumin` (year), with variants for temporal relationships.

---

## Core Pattern: `[number] + kumin`

| Pattern | Example | Translation | Function |
|---------|---------|-------------|----------|
| `[year] kumin` | `1914 kumin` | in 1914 | Simple date |
| `[year] kum ciangin` | `1967 kum ciangin` | after 1967 | Temporal (after) |
| `[year] kum panin` | `1972 kum panin` | from 1972 | Temporal (from) |
| `[year] kuma` | `1960 kuma` | in that year 1960 | Temporal (demonstrative) |
| `[year] leh [year] kumin` | `1948 leh 1951 kumin` | in 1948 and 1951 | Multiple dates |
| `[year] kum ah` | (not in article, but valid) | at (year) | Temporal (location) |

---

## 1. Simple Date: `[year] + kumin`

### Pattern

```
[number] + kumin = "in [year]"
```

### Examples

| # | Date | Full Sentence | Translation |
|---|------|---------------|-------------|
| 1 | `1914 kumin` | `Cope Topa in 1914 kumin Mate zo hi.` | Rev. Cope completed Matthew in 1914. |
| 2 | `1915 kumin` | `1915 kumin Rangoon khuapi... suakkhia hi.` | In 1915, it was printed in Rangoon. |
| 3 | `1929 kumin` | `1929 kumin Thuciam Thak bup zo hi.` | The Old Testament was combined in 1929. |
| 4 | `1932 kumin` | `1932 kumin suakkhia zo pan hi.` | It was published from 1932. |
| 5 | `1945 kumin` | `1945 kumin BFBS in... khenkik hi.` | In 1945, BFBS reprinted it. |
| 6 | `1974 kumin` | `1974 kumin zosiang hi.` | Completed in 1974. |
| 7 | `1977 kumin` | `1977 kumin Thuciam Lui leh Thuciam Thak a kigawm.` | In 1977, the Testaments were combined. |
| 8 | `1982 kumin` | `1982 kumin lehkhiatna leh etphatna zosiang a.` | In 1982, translation and editing were completed. |
| 9 | `1983 kumin` | `1983 kumin a laibu suakhia hi.` | In 1983, the book was published. |
| 10 | `2004 kumin` | `2004 kumin Lai Siangtho (Puahphatna) a bu-in suakkhia hi.` | In 2004, the Bible (Revision) was published. |
| 11 | `2005 kumin` | `2005 kumin etphatna committee kiseh a.` | In 2005, an editing committee was formed. |
| 12 | `2010 kumin` | `2010 kumin Rev. Dam Suan Mung... khenkik hi.` | In 2010, Rev. Dam Suan Mung reprinted it. |
| 13 | `2024 kumin` | `2024 kumin Bible Society of Myanmar... kibubawl hi.` | In 2024, Bible Society of Myanmar combined it. |

### Word-by-Word Analysis

```
1914 kumin Mate zo hi.
[1914] [kumin] [Mate] [zo] [hi]
[year-number] [year-POST] [Matthew] [complete] [DECL]
"In 1914, Matthew was completed."
```

```
1929 kumin Thuciam Thak bup zo hi.
[1929] [kumin] [Thuciam-Thak] [bup] [zo] [hi]
[year-number] [year-POST] [Old-Testament] [combine] [complete] [DECL]
"In 1929, the Old Testament was combined."
```

---

## 2. Temporal (After): `[year] + kum ciangin`

### Pattern

```
[number] + kum + ciangin = "after [year]"
```

### Examples

| # | Date | Full Sentence | Translation |
|---|------|---------------|-------------|
| 1 | `1967 kum ciangin` | `1967 kum ciangin Bible Society of Burma in bu 4,000 bawl leuleu a.` | After 1967, Bible Society of Burma kept making 4,000 copies. |

### Word-by-Word Analysis

```
1967 kum ciangin Bible Society of Burma in bu 4,000 bawl leuleu a.
[1967] [kum] [ciangin] [Bible-Society-of-Burma] [in] [bu] [4,000] [bawl] [leuleu] [a]
[year-number] [year] [after] [Bible-Society-of-Burma] [ERG] [book] [4,000] [make] [continuously] [3SG.AGR]
"After 1967, Bible Society of Burma kept making 4,000 copies."
```

---

## 3. Temporal (From): `[year] + kum panin`

### Pattern

```
[number] + kum + panin = "from [year]"
```

### Examples

| # | Date | Full Sentence | Translation |
|---|------|---------------|-------------|
| 1 | `1972 kum panin` | `1972 kum panin lehkhiatna ah...` | From 1972, in translation... |

### Word-by-Word Analysis

```
1972 kum panin lehkhiatna ah Rev. Hau Lian Kham in bu 2...
[1972] [kum] [panin] [lehkhiatna] [ah] [Rev. Hau-Lian-Kham] [in] [bu] [2]...
[year-number] [year] [from] [translation] [at] [Rev. Hau-Lian-Kham] [ERG] [book] [2]...
"From 1972, in translation, Rev. Hau Lian Kham did 2 books..."
```

---

## 4. Temporal (That Year): `[year] + kuma`

### Pattern

```
[number] + kuma = "in that year [year]" (demonstrative)
```

### Examples

| # | Date | Full Sentence | Translation |
|---|------|---------------|-------------|
| 1 | `1960 kuma` | `1960 kuma kipan Tedim Baptist Association...` | Beginning in that year 1960, Tedim Baptist Association... |
| 2 | `1967 kuma` | `1967 kuma kibawl pen mah` | The very one made in that year 1967 |

### Word-by-Word Analysis

```
1960 kuma kipan Tedim Baptist Association' vaihawmna tawh...
[1960] [kuma] [kipan] [Tedim-Baptist-Association] [vaihawmna-tawh]...
[year-number] [year-that] [begin] [Tedim-Baptist-Association] [management-with]...
"Beginning in that year 1960, with Tedim Baptist Association's management..."
```

---

## 5. Multiple Dates: `[year] + leh + [year] + kumin`

### Pattern

```
[number] + leh + [number] + kumin = "in [year] and [year]"
```

### Examples

| # | Date | Full Sentence | Translation |
|---|------|---------------|-------------|
| 1 | `1948 leh 1951 kumin` | `1948 leh 1951 kumin zong Rangoon ah kibawl.` | In 1948 and 1951 also, it was made in Rangoon. |

### Word-by-Word Analysis

```
1948 leh 1951 kumin zong Rangoon ah kibawl.
[1948] [leh] [1951] [kumin] [zong] [Rangoon] [ah] [kibawl]
[year-number] [and] [year-number] [year-POST] [also] [Rangoon] [at] [be-made]
"In 1948 and 1951 also, it was made in Rangoon."
```

---

## 6. Full Date with Day: `Zani + [day] + [month] + [year] + in`

### Pattern

```
Zani + [day] + [month] + [year] + in = "on [day] [month] [year]"
```

### Examples

| # | Date | Full Sentence | Translation |
|---|------|---------------|-------------|
| 1 | `Zani 1 September 2026 in` | `Zani 1 September 2026 in, Bible Society Myanmar Zum na pai thei ing.` | On 1 September 2026, Bible Society Myanmar can go toward [it]. |

### Word-by-Word Analysis

```
Zani 1 September 2026 in , Bible Society Myanmar Zum na pai thei ing.
[Zani] [1] [September] [2026] [in] , [Bible-Society-Myanmar] [Zum] [na] [pai] [thei] [ing]
[Day] [1] [September] [2026] [on] , [Bible-Society-Myanmar] [toward] [go] [can] [IMPF]
"On 1 September 2026, Bible Society Myanmar can go toward [it]."
```

---

## 7. Time Reference: `[time] + panin`

### Pattern

```
[time expression] + panin = "from [time]"
```

### Examples

| # | Time | Full Sentence | Translation |
|---|------|---------------|-------------|
| 1 | `huna kipan` | `Thuciam Lui a kizawh huna kipan` | From the time the New Testament was finished |

### Word-by-Word Analysis

```
Rev. Kam Khaw Thang in Thuciam Lui a kizawh huna kipan...
[Rev. Kam-Khaw-Thang] [in] [Thuciam-Lui] [a kizawh] [huna] [kipan]...
[Rev. Kam-Khaw-Thang] [ERG] [New-Testament] [3SG.AGR-finish] [time-from] [begin]...
"From the time Rev. Kam Khaw Thang finished the New Testament..."
```

---

## 8. Postposition Summary

| Postposition | Meaning | Example | Translation |
|--------------|---------|---------|-------------|
| `kumin` | in (year) | `1914 kumin` | in 1914 |
| `kum ciangin` | after (year) | `1967 kum ciangin` | after 1967 |
| `kum panin` | from (year) | `1972 kum panin` | from 1972 |
| `kuma` | (year)-that | `1960 kuma` | in that year 1960 |
| `kum ah` | at (year) | (valid, not in article) | at (year) |
| `in` | on (full date) | `Zani 1 September 2026 in` | on 1 September 2026 |
| `panin` | from (time) | `huna kipan` | from the time |
| `ah` | at (place) | `Rangoon ah` | in Rangoon |

---

## 9. Number System (Dates)

Zolai uses Arabic numerals for years in modern writing:

| Number | Zolai | Usage |
|--------|-------|-------|
| 1914 | `1914` | Year |
| 1929 | `1929` | Year |
| 1945 | `1945` | Year |
| 1967 | `1967` | Year |
| 2010 | `2010` | Year |
| 2024 | `2024` | Year |
| 2026 | `2026` | Year |
| 1,000 | `1,000` | Quantity |
| 3,500 | `3,500` | Quantity |
| 4,000 | `4,000` | Quantity |
| 10,000 | `10,000` | Quantity |

**Note:** In formal historical writing, Arabic numerals are standard. In traditional contexts, Zolai number words would be used (e.g., `khat-sawm-sa-le-nga` for 1914).

---

## 10. Full Date Timeline from Article

| Year | Event | Zolai Expression |
|------|-------|------------------|
| 1914 | Matthew completed | `1914 kumin Mate zo hi` |
| 1915 | First printing in Rangoon | `1915 kumin Rangoon... suakkhia hi` |
| 1929 | Old Testament combined | `1929 kumin Thuciam Thak bup zo hi` |
| 1932 | Published from ABM Press | `1932 kumin suakkhia zo pan hi` |
| 1945 | Reprinted from India | `1945 kumin BFBS in... khenkik hi` |
| 1948 | Made in Rangoon | `1948 leh 1951 kumin zong Rangoon ah kibawl` |
| 1951 | Made in Rangoon | `1948 leh 1951 kumin zong Rangoon ah kibawl` |
| 1960 | New Testament work began | `1960 kuma kipan` |
| 1964 | New Testament with Late | `1964 kumin Bible Society of Burma in... bawl hi` |
| 1967 | 4,000 copies made | `1967 kum ciangin Bible Society of Burma in bu 4,000 bawl` |
| 1972 | Translation work (Jeremiah, Jonah) | `1972 kum panin lehkhiatna ah...` |
| 1974 | Translation completed | `1974 kumin zosiang hi` |
| 1977 | First combined Bible | `1977 kumin Thuciam Lui leh Thuciam Thak a kigawm` |
| 1982 | Editing completed | `1982 kumin lehkhiatna leh etphatna zosiang a` |
| 1983 | 10,000 copies published | `1983 kumin a laibu suakhia hi` |
| 2004 | Revision published | `2004 kumin Lai Siangtho (Puahphatna) a bu-in suakkhia hi` |
| 2005 | Editing committee formed | `2005 kumin etphatna committee kiseh a` |
| 2010 | Anniversary reprint | `2010 kumin Rev. Dam Suan Mung... khenkik hi` |
| 2024 | New version combined | `2024 kumin Bible Society of Myanmar... kibubawl hi` |
| 2026 | Personal postscript | `Zani 1 September 2026 in` |

---

*Reference: Zolai-AI Wiki Project | Date constructions from "Tedim Lai Siangtho Tangthu Tom"*
