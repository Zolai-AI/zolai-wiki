# Zomidaily Corpus Guide

> Comprehensive guide to the zomidaily.com corpus for language learning and research.
> Last updated: 2026-09-10

---

## Overview

| Metric | Value |
|--------|-------|
| Source | https://zomidaily.com/ |
| Articles scraped | 12,966 |
| Date range | 2008–2026 |
| Total words | 8,711,121 |
| Unique words | 208,495 |
| New words (not in dict) | 45,625 |
| Grammar sentences | 511,329 |
| Proverbs found | 500 |

## Category Breakdown

| Category | Articles | % | Description |
|----------|----------|---|-------------|
| News | 8,700 | 67% | General news, community updates |
| Article | 4,170 | 32% | Essays, opinion pieces, devotional |
| Zomi | 3,820 | 29% | Zomi-specific news and culture |
| World | 3,441 | 27% | International news in Zolai |
| Sawltak | 3,018 | 23% | Stories, narratives, personal accounts |
| Malaysia | 1,428 | 11% | Zomi diaspora in Malaysia |
| Biakna | 1,154 | 9% | Faith, devotional, church |
| Myanmar | 1,030 | 8% | Myanmar national news |
| Politics | 607 | 5% | Political analysis and commentary |
| Hauzacin | 533 | 4% | Health articles |
| Dahpihna | 499 | 4% | Refugees and displacement |
| Refugee | 426 | 3% | Refugee stories and issues |
| USA | 423 | 3% | Zomi diaspora in USA |
| Khawmpau | 401 | 3% | Community news |
| ZAM | 394 | 3% | Zomi Association of Malaysia |
| Health | 225 | 2% | Health and wellness |

## How to Use for Language Learning

### By Proficiency Level

| Level | Focus Areas | Recommended Articles |
|-------|-------------|---------------------|
| A1-A2 | Basic vocabulary, simple sentences | Short news items, health tips |
| B1-B2 | Grammar patterns, discourse markers | Articles, interviews, opinion pieces |
| B2-C1 | Complex syntax, register variation | Political analysis, editorials, stories |
| C1-C2 | Idiomatic expressions, proverbs | Sawltak, devotional, personal narratives |

### By Topic

| Topic | What You'll Learn |
|-------|-------------------|
| **Health** | Medical vocabulary, body parts, symptoms, advice |
| **Politics** | Political terms, formal register, diplomatic language |
| **Religion** | Spiritual vocabulary, devotional patterns, prayers |
| **Family** | Kinship terms, family dynamics, proverbs |
| **Community** | Social vocabulary, organizational names, events |
| **Diaspora** | Migration vocabulary, cultural adaptation, identity |
| **News** | Reporting style, passive constructions, dates |

### Grammar Patterns by Frequency

| Pattern | Count | Example |
|---------|-------|---------|
| Ergative `in` | 189,358 | `BSM in lai suakkhia hi.` |
| Future `ding` | 97,787 | `Ka pai ding hi.` |
| Negation `lo` | 30,908 | `Pai lo hi.` |
| Content question `bang` | 27,567 | `Bang hang pai na hiam?` |
| Quotative `ci` | 24,753 | `A gen hi ci-in...` |
| Negation `kei` | 22,128 | `Ka pai kei hi.` |
| Progressive `lai` | 20,878 | `A ne lai hi.` |
| Past `ta` | 15,548 | `A pai ta hi.` |
| Yes/no `hiam` | 13,260 | `Na pai hiam?` |
| Completive `zo` | 11,516 | `A pai zo hi.` |

### Key Differences: Bible Zolai vs Modern Zolai

| Feature | Bible Zolai | Modern Zolai |
|---------|-------------|--------------|
| Vocabulary | Classical, formal | Mixed with loan words |
| Sentence length | Short, poetic | Longer, complex |
| Loan words | Rare | Common (English, Malay) |
| Discourse markers | Simple | Rich (mahmah, peuhmah, inzong) |
| Negation | `kei` dominant | `lo` and `kei` balanced |
| Questions | `hiam` dominant | `hiam` + `bang` + `diam` |
| Register | Single (literary) | Multiple (formal/informal) |

## Data Files

| File | Location | Description |
|------|----------|-------------|
| Articles | `data/raw/zomidaily/articles/` | 12,966 JSON files |
| Word frequency | `data/raw/zomidaily/vocabulary/words_frequency.jsonl` | 208K words |
| Phrases | `data/raw/zomidaily/vocabulary/phrases.jsonl` | 7K bigrams |
| New words | `data/raw/zomidaily/vocabulary/new_words.jsonl` | 45K new words |
| Grammar patterns | `data/raw/zomidaily/vocabulary/grammar_patterns.jsonl` | 11 patterns |
| Proverbs | `data/raw/zomidaily/vocabulary/proverbs.jsonl` | 500 proverbs |
| Stats | `data/raw/zomidaily/metadata/extraction_stats.json` | Summary stats |
| Dictionary | `data/dictionary/processed/dict_zomidaily_new_words.jsonl` | 1,432 entries |
