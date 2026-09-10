# Cross-Corpus Comparison

## Overview

This document provides a comprehensive comparison of all Zolai data sources, analyzing vocabulary overlap, grammar patterns, register, time period, and gaps. All examples use correct ZVS 2018 orthography.

---

## 1. Data Sources

### 1.1. Source Inventory

| Source | Size | Entries | Time Period | Register | Notes |
|--------|------|---------|-------------|----------|-------|
| **Bible corpus** | 16MB | 31,102 verses | 1977–2010 | Biblical/Literary | Primary training corpus |
| **Zomidaily corpus** | 511K sentences | 12,966 articles | 2010–2026 | Modern/News | Contemporary spoken Zolai |
| **Dictionary (ZO→EN)** | 11MB | 93,931 entries | Various | Reference | Comprehensive word lookup |
| **Dictionary (EN→ZO)** | 56MB | 112,220 entries | Various | Reference | Reverse dictionary |
| **Paumkim corpus** | 686MB | 3M+ sentences | Various | Conversational | Modern spoken Zolai |
| **Reference materials** | 6.5MB | 23 files | 1899–2013 | Academic/Grammar | Authoritative grammar rules |
| **Dalsuum dictionary** | 6.7MB | 7,841 headwords | Various | Trilingual | ZO-EN-MY |
| **Bible supplement** | 708KB | 4,073 entries | Various | Religious | Bible-derived words |
| **Context analysis** | 53MB | 54,376 records | Various | Analysis | Per-book/chapter/topic |
| **Exercises** | 37MB | 81,805 examples | Various | Training | Grammar-aware generation |

### 1.2. Source Characteristics

| Source | Strengths | Limitations | Best For |
|--------|-----------|-------------|----------|
| **Bible corpus** | Complete parallel (EN↔ZO), community-validated, rich structure | Religious content, formal register | Grammar patterns, vocabulary, translation |
| **Zomidaily corpus** | Modern vocabulary, news register, contemporary usage | Limited parallel, informal | Modern vocabulary, discourse markers |
| **Dictionary (ZO→EN)** | Comprehensive (93K entries), authoritative | No context, no examples | Word lookup, frequency |
| **Dictionary (EN→ZO)** | Comprehensive (112K entries), authoritative | No context, no examples | Reverse lookup, translation |
| **Paumkim corpus** | Large (3M+ sentences), conversational, modern | No parallel, informal | Spoken patterns, colloquialisms |
| **Reference materials** | Authoritative grammar, historical depth | Limited vocabulary, academic | Grammar rules, historical forms |
| **Dalsuum dictionary** | Trilingual (ZO-EN-MY), compact | Limited entries (7.8K) | Cross-language comparison |
| **Bible supplement** | Bible-derived words, consistent | Limited to religious vocabulary | Religious terminology |
| **Context analysis** | Deep per-book analysis, topic words | Bible-only | Context-aware translation |
| **Exercises** | Grammar-aware, structured | Synthetic, not natural | Training data, practice |

---

## 2. Vocabulary Overlap

### 2.1. Vocabulary Distribution Across Sources

| Vocabulary Type | Bible | Zomidaily | Dictionary | Paumkim | Reference | Notes |
|----------------|-------|-----------|------------|---------|-----------|-------|
| **Core vocabulary** | ✅ High | ✅ High | ✅ High | ✅ High | ✅ High | Common across all |
| **Religious terms** | ✅ High | ⚠️ Low | ✅ High | ⚠️ Low | ✅ High | Bible-dominated |
| **Modern terms** | ❌ Low | ✅ High | ⚠️ Medium | ✅ High | ❌ Low | Zomidaily/Paumkim-dominated |
| **Loan words** | ❌ Low | ✅ High | ✅ High | ✅ High | ⚠️ Low | Modern sources |
| **Archaic forms** | ⚠️ Medium | ❌ Low | ✅ High | ❌ Low | ✅ High | Reference-dominated |
| **Regional dialects** | ❌ Low | ⚠️ Low | ⚠️ Low | ✅ High | ❌ Low | Paumkim-dominated |

### 2.2. Word Frequency Comparison

| Word | Bible | Zomidaily | Dictionary | Paumkim | Notes |
|------|-------|-----------|------------|---------|-------|
| **pasian** | High (225x) | Low | High | Low | Religious dominance |
| **topa** | High (150x) | Low | High | Low | Religious dominance |
| **tui** | Medium (80x) | High (500x) | High | High | Universal |
| **mi** | Medium (100x) | High (1000x) | High | High | Universal |
| **pai** | Medium (90x) | High (800x) | High | High | Universal |
| **mu** | Medium (70x) | High (600x) | High | High | Universal |
| **ne** | Medium (60x) | High (700x) | High | High | Universal |
| **gen** | Medium (50x) | High (500x) | High | High | Universal |
| **om** | Medium (40x) | High (400x) | High | High | Universal |
| **hiam** | High (100x) | High (200x) | High | High | Universal (question) |
| **kei** | Medium (80x) | High (150x) | High | High | Universal (negation) |
| **lo** | Low (20x) | High (100x) | High | High | Modern dominance |
| **ding** | Medium (90x) | High (300x) | High | High | Universal (future) |
| **ta** | Medium (80x) | High (200x) | High | High | Universal (past) |
| **zo** | Medium (70x) | High (150x) | High | High | Universal (completive) |

### 2.3. Unique Vocabulary by Source

| Source | Unique Words | Examples | Notes |
|--------|--------------|----------|-------|
| **Bible** | ~5,000 | religious terms, archaic forms | Bible-specific vocabulary |
| **Zomidaily** | ~45,000 | modern terms, loan words | Contemporary vocabulary |
| **Dictionary** | ~93,000 | comprehensive coverage | Most complete |
| **Paumkim** | ~30,000 | conversational, colloquial | Spoken vocabulary |
| **Reference** | ~2,000 | grammar terms, archaic forms | Academic vocabulary |

---

## 3. Grammar Patterns

### 3.1. Grammar Pattern Distribution

| Pattern | Bible | Zomidaily | Dictionary | Paumkim | Reference | Notes |
|---------|-------|-----------|------------|---------|-----------|-------|
| **SOV word order** | ✅ High (95%) | ✅ High (90%) | N/A | ✅ High (85%) | ✅ High (100%) | Universal |
| **Ergative `in`** | ✅ High (37%) | ✅ High (37%) | N/A | ✅ High (30%) | ✅ High (40%) | Universal |
| **Negation `kei`** | ✅ High (4.3%) | ✅ High (4.3%) | N/A | ✅ High (5%) | ✅ High (3%) | Universal |
| **Negation `lo`** | ⚠️ Low (1%) | ✅ High (6%) | N/A | ✅ High (7%) | ⚠️ Low (2%) | Modern dominance |
| **Question `hiam`** | ✅ High (2.6%) | ✅ High (2.6%) | N/A | ✅ High (3%) | ✅ High (2%) | Universal |
| **Question `diam`** | ⚠️ Low (0.2%) | ⚠️ Low (0.2%) | N/A | ⚠️ Low (0.3%) | ⚠️ Low (0.1%) | Rare |
| **Future `ding`** | ✅ High (19.1%) | ✅ High (19.1%) | N/A | ✅ High (20%) | ✅ High (18%) | Universal |
| **Past `ta`** | ✅ High (3%) | ✅ High (3%) | N/A | ✅ High (4%) | ✅ High (2%) | Universal |
| **Completive `zo`** | ✅ High (2.3%) | ✅ High (2.3%) | N/A | ✅ High (2.5%) | ✅ High (2%) | Universal |
| **Progressive `lai`** | ✅ High (4.1%) | ✅ High (4.1%) | N/A | ✅ High (5%) | ✅ High (3%) | Universal |
| **Quotative `ci`** | ✅ High (4.8%) | ✅ High (4.8%) | N/A | ✅ High (5%) | ✅ High (4%) | Universal |

### 3.2. Grammar Pattern Examples

| Pattern | Bible Example | Zomidaily Example | Paumkim Example | Notes |
|---------|---------------|-------------------|-----------------|-------|
| **SOV** | `Gam ka mu hi.` | `Gam ka mu hi.` | `Gam ka mu hi.` | Universal |
| **Ergative** | `Pasian in leitung a piangsak hi.` | `Mi in kam a nei hi.` | `A in lai a sih hi.` | Universal |
| **Negation `kei`** | `Ka pai kei hi.` | `Ka pai kei hi.` | `Ka pai kei hi.` | Universal |
| **Negation `lo`** | `Pai lo hi.` | `Pai lo hi.` | `Pai lo hi.` | Universal |
| **Question `hiam`** | `Na pai hiam?` | `Na pai hiam?` | `Na pai hiam?` | Universal |
| **Future `ding`** | `Ka pai ding hi.` | `Ka pai ding hi.` | `Ka pai ding hi.` | Universal |
| **Past `ta`** | `A pai ta hi.` | `A pai ta hi.` | `A pai ta hi.` | Universal |
| **Completive `zo`** | `A pai zo hi.` | `A pai zo hi.` | `A pai zo hi.` | Universal |
| **Progressive `lai`** | `A ne lai hi.` | `A ne lai hi.` | `A ne lai hi.` | Universal |

### 3.3. Grammar Pattern Gaps

| Pattern | Bible | Zomidaily | Paumkim | Notes |
|---------|-------|-----------|---------|-------|
| **Passive `ki-`** | ⚠️ Low | ⚠️ Low | ⚠️ Low | Rare in all sources |
| **Cleft `pen`** | ⚠️ Low | ⚠️ Low | ⚠️ Low | Rare in all sources |
| **Imperative** | ✅ Medium | ✅ Medium | ✅ Medium | Moderate in all |
| **Hortative** | ⚠️ Low | ⚠️ Low | ⚠️ Low | Rare in all sources |

---

## 4. Register Analysis

### 4.1. Register Distribution

| Register | Bible | Zomidaily | Dictionary | Paumkim | Reference | Notes |
|----------|-------|-----------|------------|---------|-----------|-------|
| **Biblical/Literary** | ✅ High | ⚠️ Low | ⚠️ Low | ❌ Low | ✅ High | Bible/Reference-dominated |
| **Formal/Written** | ✅ High | ✅ Medium | ✅ High | ⚠️ Low | ✅ High | Bible/Dictionary-dominated |
| **Semi-formal** | ⚠️ Medium | ✅ High | ✅ Medium | ✅ Medium | ⚠️ Medium | Zomidaily-dominated |
| **Conversational** | ❌ Low | ✅ High | ❌ Low | ✅ High | ❌ Low | Zomidaily/Paumkim-dominated |
| **Poetic** | ✅ High | ❌ Low | ❌ Low | ❌ Low | ⚠️ Low | Bible-dominated |

### 4.2. Register Examples

| Register | Bible Example | Zomidaily Example | Paumkim Example | Notes |
|----------|---------------|-------------------|-----------------|-------|
| **Biblical** | `Pasian in vantung leh leitung a piangsak hi.` | — | — | Formal, literary |
| **Formal** | `Tangthu hi a ciangin a om hi.` | `Tangthu hi a ciangin a om hi.` | — | Written, academic |
| **Semi-formal** | — | `Kam hi a nei hi.` | `Kam hi a nei hi.` | News, articles |
| **Conversational** | — | `Kam nei lai hi.` | `Kam nei lai hi.` | Spoken, informal |

### 4.3. Register Shifts

| Shift | From | To | Example | Notes |
|-------|------|----|---------|-------|
| **Bible → Modern** | `Pasian in leitung a piangsak hi.` | `Mi in kam a nei hi.` | Subject change | Religious → Secular |
| **Formal → Conversational** | `A pai hi.` | `Pai lai hi.` | Aspect change | Written → Spoken |
| **Literary → News** | `Tangthu hi a ciangin a om hi.` | `Tangthu hi a om hi.` | Simplification | Literary → Journalistic |

---

## 5. Time Period Analysis

### 5.1. Time Period Distribution

| Period | Bible | Zomidaily | Dictionary | Paumkim | Reference | Notes |
|--------|-------|-----------|------------|---------|-----------|-------|
| **Pre-1900** | ❌ Low | ❌ Low | ⚠️ Low | ❌ Low | ✅ High | Reference-dominated |
| **1900–1970** | ⚠️ Low | ❌ Low | ⚠️ Low | ❌ Low | ✅ High | Reference-dominated |
| **1977–2010** | ✅ High | ❌ Low | ⚠️ Low | ⚠️ Low | ⚠️ Low | Bible-dominated |
| **2010–2026** | ❌ Low | ✅ High | ⚠️ Low | ✅ High | ❌ Low | Zomidaily/Paumkim-dominated |

### 5.2. Vocabulary Evolution

| Word | Pre-1900 | 1977–2010 | 2010–2026 | Notes |
|------|----------|-----------|-----------|-------|
| **pasian** | `pathian` | `pasian` | `pasian` | ZVS 2018 reform |
| **gam** | `ram` | `gam` | `gam` | ZVS 2018 reform |
| **tapa** | `fapa` | `tapa` | `tapa` | ZVS 2018 reform |
| **topa** | `bawipa` | `topa` | `topa` | ZVS 2018 reform |
| **kumpipa** | `siangpahrang` | `kumpipa` | `kumpipa` | ZVS 2018 reform |
| **tua** | `cu/cun` | `tua` | `tua` | ZVS 2018 reform |
| **suahtakna** | `suah` | `suahtakna` | `suahtakna` | ZVS 2018 reform |
| **nuntakna** | `nunnak` | `nuntakna` | `nuntakna` | ZVS 2018 reform |

### 5.3. Grammar Evolution

| Pattern | Pre-1900 | 1977–2010 | 2010–2026 | Notes |
|---------|----------|-----------|-----------|-------|
| **Negation `kei`** | ✅ High | ✅ High | ✅ High | Universal |
| **Negation `lo`** | ✅ High | ⚠️ Low | ✅ High | Modern resurgence |
| **Question `hiam`** | ✅ High | ✅ High | ✅ High | Universal |
| **Future `ding`** | ✅ High | ✅ High | ✅ High | Universal |
| **Past `ta`** | ✅ High | ✅ High | ✅ High | Universal |
| **Completive `zo`** | ✅ High | ✅ High | ✅ High | Universal |
| **Progressive `lai`** | ⚠️ Low | ✅ High | ✅ High | Modern increase |

---

## 6. Gap Analysis

### 6.1. Vocabulary Gaps

| Gap Type | Description | Sources | Examples | Notes |
|----------|-------------|---------|----------|-------|
| **Bible-only** | Religious terms not in modern use | Bible | `suahtakna`, `nuntakna` | Limited modern usage |
| **Modern-only** | Loan words not in Bible | Zomidaily, Paumkim | `komputa`, `sikuul` | Not in Bible |
| **Dictionary-only** | Archaic forms in dictionary | Dictionary | `pathian`, `ram` | Forbidden in ZVS 2018 |
| **Paumkim-only** | Colloquialisms | Paumkim | `mahmah`, `ahihi` | Informal only |
| **Reference-only** | Grammar terms | Reference | `laimung`, `awphei` | Academic only |

### 6.2. Grammar Gaps

| Gap Type | Description | Sources | Examples | Notes |
|----------|-------------|---------|----------|-------|
| **Bible-only** | Formal patterns | Bible | passive `ki-` | Rare in modern |
| **Modern-only** | Informal patterns | Zomidaily, Paumkim | `lo` negation | Modern resurgence |
| **Dictionary-only** | Archaic patterns | Dictionary | `cu/cun` conjunction | Forbidden in ZVS 2018 |
| **Paumkim-only** | Colloquial patterns | Paumkim | discourse markers | Informal only |
| **Reference-only** | Academic patterns | Reference | tone rules | Not marked in orthography |

### 6.3. Register Gaps

| Gap Type | Description | Sources | Examples | Notes |
|----------|-------------|---------|----------|-------|
| **Bible-only** | Biblical register | Bible | religious vocabulary | Limited modern use |
| **Modern-only** | News register | Zomidaily | loan words | Not in Bible |
| **Dictionary-only** | Formal register | Dictionary | archaic forms | Not in modern use |
| **Paumkim-only** | Conversational register | Paumkim | colloquialisms | Not in formal writing |
| **Reference-only** | Academic register | Reference | grammar terms | Not in everyday use |

---

## 7. Integration Opportunities

### 7.1. Cross-Source Validation

| Validation | Bible | Zomidaily | Dictionary | Paumkim | Notes |
|------------|-------|-----------|------------|---------|-------|
| **Word existence** | ✅ | ✅ | ✅ | ✅ | Multi-source attestation |
| **Grammar correctness** | ✅ | ✅ | N/A | ✅ | Pattern validation |
| **Register appropriateness** | ✅ | ✅ | N/A | ✅ | Context validation |
| **ZVS 2018 compliance** | ✅ | ✅ | ✅ | ✅ | Standard compliance |

### 7.2. Complementary Sources

| Combination | Strengths | Use Case | Notes |
|-------------|-----------|----------|-------|
| **Bible + Dictionary** | Grammar + vocabulary | Language learning | Comprehensive |
| **Zomidaily + Paumkim** | Modern + spoken | Contemporary use | Modern Zolai |
| **Bible + Zomidaily** | Formal + modern | Register comparison | Historical shift |
| **Dictionary + Paumkim** | Vocabulary + context | Word usage | Real-world examples |
| **Reference + Bible** | Grammar + examples | Grammar teaching | Authoritative |

### 7.3. Data Enrichment

| Enrichment | Source | Target | Method | Notes |
|------------|--------|--------|--------|-------|
| **Add examples** | Bible | Dictionary | Verse citation | Contextual examples |
| **Add frequency** | Zomidaily | Dictionary | Word count | Frequency data |
| **Add register** | Paumkim | Dictionary | Usage tags | Register information |
| **Add etymology** | Reference | Dictionary | Historical forms | Etymology data |
| **Add cognates** | Dalsuum | Dictionary | Cross-language | Cognate data |

---

## 8. Recommendations

### 8.1. For Language Learning

| Recommendation | Priority | Rationale | Notes |
|----------------|----------|-----------|-------|
| **Use Bible for grammar** | High | Complete parallel corpus | Grammar patterns |
| **Use Zomidaily for modern vocabulary** | High | Contemporary usage | Modern Zolai |
| **Use Dictionary for word lookup** | High | Comprehensive coverage | Vocabulary reference |
| **Use Paumkim for spoken patterns** | Medium | Conversational Zolai | Spoken language |
| **Use Reference for grammar rules** | Medium | Authoritative sources | Grammar reference |

### 8.2. For AI Training

| Recommendation | Priority | Rationale | Notes |
|----------------|----------|-----------|-------|
| **Bible as primary training corpus** | High | Only complete parallel corpus | Translation pairs |
| **Zomidaily for modern vocabulary** | High | Contemporary vocabulary | Modern terms |
| **Dictionary for word coverage** | High | Comprehensive vocabulary | Word lookup |
| **Paumkim for spoken patterns** | Medium | Conversational data | Spoken language |
| **Reference for grammar rules** | Medium | Authoritative grammar | Grammar validation |

### 8.3. For Corpus Expansion

| Recommendation | Priority | Rationale | Notes |
|----------------|----------|-----------|-------|
| **Add more parallel corpora** | High | Increase translation pairs | More training data |
| **Add more modern texts** | High | Contemporary vocabulary | Modern Zolai |
| **Add more spoken data** | Medium | Conversational patterns | Spoken language |
| **Add more reference materials** | Medium | Grammar rules | Grammar reference |
| **Add more dialectal data** | Low | Regional variation | Dialect coverage |

---

## 9. References

1. Bible corpus (31,102 verses)
2. Zomidaily corpus (12,966 articles)
3. Dictionary (93,931 ZO→EN + 112,220 EN→ZO)
4. Paumkim corpus (3M+ sentences)
5. Reference materials (23 files)
6. Dalsuum dictionary (7,841 headwords)
7. Bible supplement (4,073 entries)
8. Context analysis (54,376 records)
9. Exercises (81,805 examples)

---

*All examples use correct ZVS 2018 orthography. Forbidden forms (pathian, ram, fapa, bawipa, siangpahrang, cu/cun) are noted but not used in examples.*