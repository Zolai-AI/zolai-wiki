# Zolai NLP Pipeline Reference

> Complete NLP pipeline for Tedim Zolai (ZVS 2018). All examples use correct ZVS 2018 orthography.
> Last updated: 2026-09-10

---

## Table of Contents

1. [Pipeline Overview](#1-pipeline-overview)
2. [Tokenization](#2-tokenization)
3. [Part-of-Speech Tagging](#3-part-of-speech-tagging)
4. [Named Entity Recognition](#4-named-entity-recognition)
5. [Dependency Parsing](#5-dependency-parsing)
6. [Machine Translation](#6-machine-translation)
7. [Text Classification](#7-text-classification)
8. [Sentiment Analysis](#8-sentiment-analysis)
9. [Spell Checking](#9-spell-checking)
10. [Code Examples](#10-code-examples)

---

## 1. Pipeline Overview

### Architecture

```
Input Text (ZO or EN)
    ↓
┌─────────────────────────────────────────┐
│           PREPROCESSING                 │
│  • Text normalization (ZVS 2018)       │
│  • Sentence segmentation               │
│  • Tokenization                         │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│           ANALYSIS                      │
│  • POS tagging                          │
│  • Named entity recognition             │
│  • Dependency parsing                   │
│  • Morphological analysis               │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│           SEMANTICS                     │
│  • Word sense disambiguation            │
│  • Semantic role labeling               │
│  • Coreference resolution               │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│           APPLICATION                   │
│  • Machine translation                  │
│  • Text classification                  │
│  • Sentiment analysis                   │
│  • Spell checking                       │
│  • Information extraction               │
└─────────────────────────────────────────┘
```

### Data Sources

| Source | Size | Purpose |
|--------|------|---------|
| Bible parallel corpus | 31,102 verses | Parallel training data |
| ZO→EN dictionary | 93,931 entries | Word translations |
| EN→ZO dictionary | 112,220 entries | Word translations |
| Grammar patterns | 4,205 patterns | Grammar rules |
| Vocabulary index | 20,929 words | Frequency data |
| Word usage profiles | 7,384 records | Context-aware translation |
| Paumkim corpus | 3M+ sentences | Modern spoken Zolai |
| Zomidaily corpus | 12,966 articles | Modern written Zolai |

---

## 2. Tokenization

### Word Boundaries

Zolai uses **spaces** as primary word boundaries. However, tokenization must handle:

1. **Compound words** (written as single tokens)
2. **Hyphenated words** (verb + directional particles)
3. **Clitic pronouns** (agreement markers)
4. **Multi-word expressions** (idioms, phrases)

### Tokenization Rules

#### Rule 1: Space-Separated Tokens

```python
# Simple space-based tokenization
tokens = text.split()
```

**Example:**
```
Input:  "Pasian in vantung leh leitung a piangsak hi."
Tokens: ["Pasian", "in", "vantung", "leh", "leitung", "a", "piangsak", "hi."]
```

#### Rule 2: Compound Words

Compound words are written as single tokens without spaces:

| Compound | Components | Meaning |
|----------|------------|---------|
| `vantung` | `van` + `tung` | heaven |
| `leitung` | `lei` + `tung` | earth |
| `pasian` | `pa` + `sian` | God |
| `laisiangtho` | `lai` + `siang` + `tho` | Bible |
| `hawmkhia` | `hawm` + `khia` | publish |

**Detection method:** Check against compound word dictionary.

```python
COMPOUNDS = {
    "vantung": ("van", "tung"),
    "leitung": ("lei", "tung"),
    "pasian": ("pa", "sian"),
    "laisiangtho": ("lai", "siang", "tho"),
    "hawmkhia": ("hawm", "khia"),
}

def tokenize_compound(word):
    if word in COMPOUNDS:
        return COMPOUNDS[word]
    return (word,)
```

#### Rule 3: Hyphenated Words

Hyphenated words are split at hyphens:

```
Input:  "pai-in"
Tokens: ["pai", "in"]
```

```python
def tokenize_hyphenated(word):
    if "-" in word:
        return word.split("-")
    return [word]
```

#### Rule 4: Clitic Pronouns

Agreement markers (ka, na, a, i, ko) are separate tokens:

```
Input:  "Pai ka hi."
Tokens: ["Pai", "ka", "hi"]
```

#### Rule 5: Sentence-Final Particles

Particles like `hi`, `hiam`, `hen`, `un` are separate tokens:

```
Input:  "Pai na hiam?"
Tokens: ["Pai", "na", "hiam", "?"]
```

### Tokenization Algorithm

```python
def tokenize_zolai(text):
    """
    Tokenize Zolai text with proper handling of compounds,
    hyphens, and clitics.
    """
    # Step 1: Remove punctuation (store separately)
    sentences = re.split(r'([.?!])', text)
    
    tokens = []
    for sent in sentences:
        if sent.strip() in ['.', '?', '!']:
            tokens.append(sent.strip())
            continue
        
        # Step 2: Split on spaces
        words = sent.split()
        
        for word in words:
            # Step 3: Handle hyphens
            if '-' in word:
                parts = word.split('-')
                tokens.extend(parts)
            # Step 4: Check compound dictionary
            elif word in COMPOUNDS:
                tokens.append(word)  # Keep as single token
            # Step 5: Default
            else:
                tokens.append(word)
    
    return tokens
```

### Special Cases

| Case | Example | Tokenization | Notes |
|------|---------|--------------|-------|
| Loan word | `copyright` | `["copyright"]` | Keep as single token |
| Abbreviation | `BFBS` | `["BFBS"]` | Keep as single token |
| Number | `1914` | `["1914"]` | Keep as single token |
| Multi-word EUP | `bang hang` | `["bang", "hang"]` | Two tokens, but functions as one unit |
| Idiom | `lung dam` | `["lung", "dam"]` | Two tokens, but functions as one unit |

---

## 3. Part-of-Speech Tagging

### Zolai POS Tagset

| Tag | Category | Description | Examples |
|-----|----------|-------------|----------|
| `NOUN` | Noun | Common noun | `gam`, `tui`, `mi`, `inn` |
| `PROPN` | Proper Noun | Named entity | `Pasian`, `David`, `Israel` |
| `PRON` | Pronoun | Personal pronoun | `kei`, `nang`, `amah`, `eite` |
| `AGRM` | Agreement Marker | Subject agreement | `ka`, `na`, `a`, `i`, `ko` |
| `POSS` | Possessive Marker | Possession | `ka`, `na`, `a`, `i`, `amau` |
| `VERB` | Verb | Action/state | `pai`, `mu`, `ne`, `om`, `hi` |
| `VCOMP` | Compound Verb | Multi-part verb | `hawmkhia`, `paikhia`, `pailut` |
| `ADV` | Adverb | Manner | `mahmah`, `limtak`, `taktek` |
| `ADJ` | Adjective | Quality | `hoih`, `lianzaw`, `sang` |
| `NUM` | Numeral | Number | `khat`, `nih`, `thum`, `sawm` |
| `DET` | Determiner | Demonstrative | `tua`, `hih`, `kua` |
| `POSTP` | Postposition | Location/Direction | `ah`, `sungah`, `tungah`, `panin` |
| `CONJ` | Conjunction | Connector | `leh`, `ahih leh`, `cih leh` |
| `PART` | Particle | Sentence-final | `hi`, `hiam`, `hen`, `un`, `vo` |
| `NEG` | Negation Particle | Negation | `kei`, `lo` |
| `QUOT` | Quotative Particle | Reported speech | `ci` |
| `ERG` | Ergative Marker | Agent marker | `in` |
| `FUT` | Future Marker | Future tense | `ding` |
| `ASP` | Aspect Marker | Tense/aspect | `ta`, `zo`, `khin`, `lai` |
| `DIR` | Directional Particle | Movement | `hong`, `va`, `khia`, `lut`, `kik` |
| `INTJ` | Interjection | Exclamation | `ai`, `oh`, `ung` |
| `PUNCT` | Punctuation | Sentence boundary | `.`, `?`, `!` |

### POS Rules

#### Rule 1: Verb Always Last

In Zolai, the verb always comes at the end of the clause:

```
Pasian in vantung leh leitung a piangsak hi.
[PROPN] [ERG] [NOUN] [CONJ] [NOUN] [AGRM] [VERB] [PART]
```

#### Rule 2: Agreement Marker Before Verb

The agreement marker directly precedes the verb:

```
Gam ka mu hi.
[NOUN] [AGRM] [VERB] [PART]
```

#### Rule 3: Postpositions Follow Nouns

Postpositions come after the noun they modify:

```
Inn sungah om hi.
[NOUN] [POSTP] [VERB] [PART]
```

#### Rule 4: Adjectives Precede Nouns

Adjectives typically precede the noun:

```
Hoih gam
[ADJ] [NOUN]
```

#### Rule 5: Negation Particle After Agreement

The negation particle comes after the agreement marker:

```
Pai ka kei hi.
[VERB] [AGRM] [NEG] [PART]
```

### POS Tagging Algorithm

```python
def pos_tag_zolai(tokens):
    """
    Rule-based POS tagger for Zolai.
    """
    tagged = []
    i = 0
    
    while i < len(tokens):
        token = tokens[i]
        
        # Check if it's a known word
        if token in DICTIONARY:
            pos = DICTIONARY[token].get('pos', 'NOUN')
            tagged.append((token, pos))
        
        # Check agreement markers
        elif token in ['ka', 'na', 'a', 'i', 'ko']:
            # Determine if possessive or agreement
            if i > 0 and is_noun(tokens[i-1]):
                tagged.append((token, 'POSS'))
            else:
                tagged.append((token, 'AGRM'))
        
        # Check particles
        elif token in ['hi', 'hiam', 'hen', 'un', 'vo']:
            tagged.append((token, 'PART'))
        
        # Check negation
        elif token in ['kei', 'lo']:
            tagged.append((token, 'NEG'))
        
        # Check postpositions
        elif token in ['ah', 'sungah', 'tungah', 'nuaiah', 'panin']:
            tagged.append((token, 'POSTP'))
        
        # Default to noun
        else:
            tagged.append((token, 'NOUN'))
        
        i += 1
    
    return tagged
```

### POS Examples

**Example 1: Simple Transitive**
```
Gam ka mu hi.
[NOUN] [AGRM] [VERB] [PART]
"I see the land."
```

**Example 2: Ergative Construction**
```
Pasian in vantung leh leitung a piangsak hi.
[PROPN] [ERG] [NOUN] [CONJ] [NOUN] [AGRM] [VERB] [PART]
"God created the heaven and earth."
```

**Example 3: Negation**
```
Pai ka kei hi.
[VERB] [AGRM] [NEG] [PART]
"I don't go."
```

**Example 4: Question**
```
Na pai hiam?
[AGRM] [VERB] [PART]
"Do you go?"
```

---

## 4. Named Entity Recognition

### Entity Types

| Type | Label | Description | Examples |
|------|-------|-------------|----------|
| Person | `PER` | Personal names | `Pasian`, `David`, `Moses` |
| Place | `LOC` | Locations | `Jerusalem`, `Israel`, `Zolai` |
| Organization | `ORG` | Organizations | `BFBS`, `TBA`, `ZCLS` |
| Date | `DATE` | Temporal expressions | `1914 kumin`, `Zani 1` |
| Number | `NUM` | Numerical values | `khat`, `nih`, `1000` |
| Title | `TITLE` | Honorifics | `Cope Topa`, `Pu Tual Khaw Mang` |
| Scripture | `SCRIPT` | Bible references | `GEN 1:1`, `Mate 5:3` |

### NER Rules

#### Rule 1: Capitalized Words

Proper nouns are capitalized in ZVS 2018:

```python
def is_capitalized(word):
    return word[0].isupper() and word[1:].islower()
```

#### Rule 2: Title Patterns

Titles follow patterns:

| Pattern | Example | Entity |
|---------|---------|--------|
| `Pu + Name` | `Pu Tual Khaw Mang` | `PER` |
| `Topa + Name` | `Cope Topa` | `PER` |
| `Rev. + Name` | `Rev. Cope` | `PER` |

#### Rule 3: Organization Patterns

Organizations often end in `Society`, `Association`, or use acronyms:

```python
ORG_PATTERNS = [
    r'[A-Z]{2,}',  # Acronyms: BFBS, TBA
    r'[^ ]+ Society',
    r'[^ ]+ Association',
]
```

#### Rule 4: Date Patterns

Dates follow specific patterns:

```python
DATE_PATTERNS = [
    r'\d{4} kumin',           # 1914 kumin
    r'\d{4} kum ciangin',     # 1967 kum ciangin
    r'\d{4} kum panin',       # 1972 kum panin
    r'Zani \d+',              # Zani 1
]
```

#### Rule 5: Scripture References

Bible references follow patterns:

```python
SCRIPT_PATTERNS = [
    r'[A-Z]{3} \d+:\d+',     # GEN 1:1
    r'[A-Z]{3} \d+',         # GEN 1
]
```

### NER Algorithm

```python
import re

def ner_zolai(text):
    """
    Named Entity Recognition for Zolai text.
    """
    entities = []
    tokens = tokenize_zolai(text)
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # Check capitalized words (proper nouns)
        if is_capitalized(token):
            # Look ahead for multi-word names
            name = [token]
            j = i + 1
            while j < len(tokens) and is_capitalized(tokens[j]):
                name.append(tokens[j])
                j += 1
            
            entity_text = ' '.join(name)
            entity_type = classify_entity(entity_text)
            entities.append((entity_text, entity_type, i, j-1))
            i = j
            continue
        
        # Check date patterns
        if re.match(r'\d{4} kumin', ' '.join(tokens[i:i+2])):
            entities.append((' '.join(tokens[i:i+2]), 'DATE', i, i+1))
            i += 2
            continue
        
        # Check scripture patterns
        if re.match(r'[A-Z]{3} \d+', token):
            entities.append((token, 'SCRIPT', i, i))
        
        i += 1
    
    return entities
```

### NER Examples

**Example 1: Person**
```
Cope Topa in 1914 kumin Mate zo hi.
[PER: Cope Topa] [DATE: 1914 kumin] [SCRIPT: Mate]
```

**Example 2: Organization**
```
BFBS in ABFMS' phalna tawh India pan khenkik hi.
[ORG: BFBS] [ORG: ABFMS] [LOC: India]
```

**Example 3: Title + Person**
```
Menzi Pu Tual Khaw Mang B.A, B.L, B.C.S thu tomno
[TITLE: Menzi] [PER: Pu Tual Khaw Mang] [NUM: B.A, B.L, B.C.S]
```

---

## 5. Dependency Parsing

### Dependency Relations

Zolai uses **SOV** (Subject-Object-Verb) word order. Dependencies follow head-final patterns.

| Relation | Label | Description | Example |
|----------|-------|-------------|---------|
| Subject | `nsubj` | Nominal subject | `Pasian` → `piangsak` |
| Object | `dobj` | Direct object | `vantung` → `piangsak` |
| Verb | `ROOT` | Main verb | `piangsak` |
| Agreement | `agrm` | Agreement marker | `a` → `piangsak` |
| Particle | `part` | Sentence particle | `hi` → `piangsak` |
| Ergative | `erg` | Ergative marker | `in` → `Pasian` |
| Postposition | `postp` | Postpositional phrase | `sungah` → `inn` |
| Conjunction | `conj` | Conjunction | `leh` → `vantung` |
| Modifier | `amod` | Adjectival modifier | `hoih` → `gam` |
| Compound | `compound` | Compound word | `tung` → `vantung` |
| Auxiliary | `aux` | Auxiliary verb | `ding` → `pai` |
| Negation | `neg` | Negation particle | `kei` → `pai` |
| Punctuation | `punct` | Punctuation | `.` → `hi` |

### Dependency Patterns

#### Pattern 1: Simple Transitive (SOV)

```
Gam ka mu hi.
      ↑    ↑
      nsubj ROOT

Tree:
ROOT (mu)
├── nsubj (ka)
├── dobj (gam)
└── part (hi)
```

#### Pattern 2: Ergative Construction

```
Pasian in vantung leh leitung a piangsak hi.
  ↑         ↑         ↑
  nsubj   dobj     agrm

Tree:
ROOT (piangsak)
├── nsubj (Pasian)
│   └── erg (in)
├── dobj (vantung)
│   └── conj (leh)
│       └── dobj (leitung)
├── agrm (a)
└── part (hi)
```

#### Pattern 3: Negation

```
Pai ka kei hi.
  ↑    ↑
 agrm neg

Tree:
ROOT (pai)
├── agrm (ka)
├── neg (kei)
└── part (hi)
```

#### Pattern 4: Question

```
Na pai hiam?
  ↑    ↑
agrm  part

Tree:
ROOT (pai)
├── agrm (na)
└── part (hiam)
```

#### Pattern 5: Postpositional Phrase

```
Inn sungah om hi.
  ↑    ↑
  ROOT postp

Tree:
ROOT (om)
├── obl (inn)
│   └── postp (sungah)
└── part (hi)
```

### Dependency Parsing Algorithm

```python
def parse_zolai(tokens, pos_tags):
    """
    Rule-based dependency parser for Zolai SOV structure.
    """
    dependencies = []
    
    # Find the main verb (always at the end)
    verb_idx = len(tokens) - 1
    for i, (token, pos) in enumerate(pos_tags):
        if pos == 'VERB':
            verb_idx = i
            break
    
    # Set verb as root
    dependencies.append(('ROOT', tokens[verb_idx]))
    
    # Find agreement marker (immediately before verb)
    if verb_idx > 0 and pos_tags[verb_idx-1][1] == 'AGRM':
        dependencies.append(('agrm', tokens[verb_idx-1]))
    
    # Find negation (after agreement marker)
    if verb_idx > 1 and pos_tags[verb_idx-2][1] == 'NEG':
        dependencies.append(('neg', tokens[verb_idx-2]))
    
    # Find sentence-final particle (after verb)
    if verb_idx < len(tokens) - 1 and pos_tags[verb_idx+1][1] == 'PART':
        dependencies.append(('part', tokens[verb_idx+1]))
    
    # Find subject (with optional ergative marker)
    subject_idx = None
    for i, (token, pos) in enumerate(pos_tags):
        if pos in ['NOUN', 'PROPN'] and i < verb_idx:
            subject_idx = i
            break
    
    if subject_idx is not None:
        dependencies.append(('nsubj', tokens[subject_idx]))
        # Check for ergative marker
        if subject_idx + 1 < len(tokens) and pos_tags[subject_idx+1][1] == 'ERG':
            dependencies.append(('erg', tokens[subject_idx+1]))
    
    # Find objects (between subject and verb)
    for i, (token, pos) in enumerate(pos_tags):
        if pos == 'NOUN' and i > (subject_idx or 0) and i < verb_idx:
            dependencies.append(('dobj', token))
    
    return dependencies
```

### Dependency Examples

**Example 1: Complex Sentence**
```
Pasian in vantung leh leitung a piangsak hi.
[PROPN] [ERG] [NOUN] [CONJ] [NOUN] [AGRM] [VERB] [PART]

Dependencies:
ROOT: piangsak
nsubj: Pasian (with erg: in)
dobj: vantung (with conj: leh)
dobj: leitung
agrm: a
part: hi
```

**Example 2: Negation with Future**
```
Pai ka kei ding hi.
[VERB] [AGRM] [NEG] [FUT] [PART]

Dependencies:
ROOT: pai
agrm: ka
neg: kei
aux: ding
part: hi
```

---

## 6. Machine Translation

### Translation Challenges

#### Challenge 1: SOV vs SVO Word Order

Zolai uses **SOV**, while English uses **SVO**:

```
Zolai:  Gam ka mu hi.
        [land] [I] [see] [DECL]
        "I see the land."

English: I see the land.
        [I] [see] [land]
```

**Solution:** Reorder words during translation.

#### Challenge 2: Ergative Construction

Zolai uses ergative `in` for transitive agents:

```
Zolai:  Pasian in vantung leh leitung a piangsak hi.
        [God] [ERG] [heaven] [and] [earth] [3SG] [create] [DECL]

English: God created the heaven and earth.
         [God] [created] [the] [heaven] [and] [earth]
```

**Solution:** Remove ergative marker, add determiners.

#### Challenge 3: Agreement Markers

Zolai uses agreement markers (ka, na, a, i, ko) that don't exist in English:

```
Zolai:  Pai ka hi.
        [go] [1SG] [DECL]
        "I go."

English: I go.
         [I] [go]
```

**Solution:** Map agreement markers to English pronouns.

#### Challenge 4: Particles

Zolai has sentence-final particles for mood/evidentiality:

```
Zolai:  Pai a hi.
        [go] [3SG] [DECL]
        "He goes."

English: He goes.
         [He] [goes] [s]
```

**Solution:** Map particles to English tense/aspect.

#### Challenge 5: Compound Words

Zolai compounds don't translate word-for-word:

```
Zolai:  Vantung
        [van] [tung]  (literally: sky + top)

English: heaven
```

**Solution:** Use compound dictionary for direct translation.

### Translation Strategy

```python
def translate_zolai_to_english(zolai_text):
    """
    Translate Zolai to English with proper word reordering.
    """
    # Step 1: Tokenize and POS tag
    tokens = tokenize_zolai(zolai_text)
    pos_tags = pos_tag_zolai(tokens)
    
    # Step 2: Extract components
    subject = extract_subject(tokens, pos_tags)
    object_ = extract_object(tokens, pos_tags)
    verb = extract_verb(tokens, pos_tags)
    particle = extract_particle(tokens, pos_tags)
    
    # Step 3: Map agreement markers to English pronouns
    subject = map_agrm_to_pronoun(subject)
    
    # Step 4: Map Zolai verb to English verb
    verb = translate_verb(verb, particle)
    
    # Step 5: Reorder to SVO
    english_tokens = [subject, verb, object_]
    
    return ' '.join(english_tokens)
```

### Translation Examples

| Zolai | English | Notes |
|-------|---------|-------|
| `Gam ka mu hi.` | I see the land. | SOV → SVO |
| `Pasian in vantung leh leitung a piangsak hi.` | God created the heaven and earth. | Ergative removed |
| `Pai ka kei hi.` | I don't go. | Negation mapped |
| `Na pai hiam?` | Do you go? | Question word added |
| `Pai ka ding hi.` | I will go. | Future mapped |

---

## 7. Text Classification

### Categories

| Category | Label | Description | Examples |
|----------|-------|-------------|----------|
| Biblical | `BIBLICAL` | Scripture text | Bible verses, religious text |
| News | `NEWS` | News articles | Zomidaily articles |
| Narrative | `NARRATIVE` | Stories, accounts | Biographies, histories |
| Formal | `FORMAL` | Formal writing | Official documents, reports |
| Conversational | `CONVERSATIONAL` | Spoken language | Dialogues, casual speech |
| Educational | `EDUCATIONAL` | Teaching material | Grammar guides, lessons |
| Literary | `LITERARY` | Poetry, prose | Songs, poems |

### Classification Features

#### Feature 1: Vocabulary Distribution

```python
BIBLICAL_WORDS = {'pasian', 'topa', 'vantung', 'leitung', 'laisiangtho'}
NEWS_WORDS = {'copyright', 'quality', 'proposal', 'vitamin'}
CONVERSATIONAL_WORDS = {'mahmah', 'ung', 'ei maw'}
```

#### Feature 2: Sentence Structure

```python
BIBLICAL_PATTERNS = [
    r'Pasian in .* a .* hi\.',  # God created...
    r'Tua ciangin .*',          # Then...
]
NEWS_PATTERNS = [
    r'\d{4} kumin .*',          # In year...
    r'[^ ] in .* khenkik hi',  # ...reprinted
]
```

#### Feature 3: Register Markers

```python
FORMAL_MARKERS = ['Tua ciangin', 'Tua ahih ciangin', 'ci-in']
CONVERSATIONAL_MARKERS = ['ung', 'ei maw', 'maw']
```

### Classification Algorithm

```python
def classify_zolai_text(text):
    """
    Classify Zolai text into categories.
    """
    tokens = tokenize_zolai(text.lower())
    
    scores = {
        'BIBLICAL': 0,
        'NEWS': 0,
        'NARRATIVE': 0,
        'FORMAL': 0,
        'CONVERSATIONAL': 0,
    }
    
    # Score based on vocabulary
    for token in tokens:
        if token in BIBLICAL_WORDS:
            scores['BIBLICAL'] += 1
        elif token in NEWS_WORDS:
            scores['NEWS'] += 1
        elif token in CONVERSATIONAL_WORDS:
            scores['CONVERSATIONAL'] += 1
    
    # Score based on patterns
    if re.search(r'Pasian in', text):
        scores['BIBLICAL'] += 3
    if re.search(r'\d{4} kumin', text):
        scores['NEWS'] += 2
    if re.search(r'Tua ciangin', text):
        scores['NARRATIVE'] += 2
    
    # Return highest scoring category
    return max(scores, key=scores.get)
```

---

## 8. Sentiment Analysis

### Sentiment Markers

#### Positive Markers

| Marker | Meaning | Example |
|--------|---------|---------|
| `hoih` | good | `Hoih a hi.` (It is good.) |
| `dam` | well/healthy | `Ka dam hi.` (I am well.) |
| `it` | love | `Ka it na uh hi.` (I love.) |
| `lungdam` | thank | `Lungdam.` (Thank you.) |
| `sangam` | grateful | `Sangam ta.` (Was grateful.) |

#### Negative Markers

| Marker | Meaning | Example |
|--------|---------|---------|
| `kei` | not | `Pai kei hi.` (Don't go.) |
| `lo` | not (literary) | `Pai lo hi.` (Goes not.) |
| `sang` | expensive/hard | `Sang hi.` (It's hard.) |
| `thei` | pain | `Ka thei hi.` (I hurt.) |

#### Intensifiers

| Marker | Meaning | Example |
|--------|---------|---------|
| `mahmah` | very | `Hoih mahmah hi.` (It's very good.) |
| `limtak` | truly | `Limtak hi.` (It's true.) |
| `sa` | very (literary) | `Hoih sa hi.` (It's very good.) |

### Sentiment Algorithm

```python
def sentiment_zolai(text):
    """
    Simple sentiment analysis for Zolai text.
    """
    tokens = tokenize_zolai(text.lower())
    
    positive = 0
    negative = 0
    
    for token in tokens:
        if token in ['hoih', 'dam', 'it', 'lungdam', 'sangam']:
            positive += 1
        elif token in ['kei', 'lo', 'sang', 'thei']:
            negative += 1
        elif token in ['mahmah', 'limtak', 'sa']:
            # Amplify existing sentiment
            if positive > 0:
                positive += 1
            elif negative > 0:
                negative += 1
    
    if positive > negative:
        return 'POSITIVE'
    elif negative > positive:
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'
```

### Sentiment Examples

| Text | Sentiment | Reasoning |
|------|-----------|-----------|
| `Hoih mahmah hi.` | POSITIVE | `hoih` (good) + `mahmah` (very) |
| `Pai ka kei hi.` | NEGATIVE | `kei` (not) |
| `Lungdam.` | POSITIVE | `lungdam` (thank) |
| `A sang hi.` | NEGATIVE | `sang` (expensive/hard) |

---

## 9. Spell Checking

### ZVS 2018 Compliance

Spell checking must enforce ZVS 2018 orthography rules.

### Forbidden Forms

| Forbidden | Correct | Meaning | Rule |
|-----------|---------|---------|------|
| `pathian` | `pasian` | God | ALWAYS use `pasian` |
| `ram` | `gam` | earth/land | ALWAYS use `gam` |
| `fapa` | `tapa` | life/son | ALWAYS use `tapa` |
| `bawipa` | `topa` | Lord | ALWAYS use `topa` |
| `siangpahrang` | `kumpipa` | Savior | ALWAYS use `kumpipa` |
| `cu/cun` | `tua` | that (conjunction) | ALWAYS use `tua` |
| `suah` | `suahtakna` | holiness | Context-dependent |
| `nunnak` | `nuntakna` | life | Context-dependent |

### Spell Checking Algorithm

```python
FORBIDDEN_FORMS = {
    'pathian': 'pasian',
    'ram': 'gam',
    'fapa': 'tapa',
    'bawipa': 'topa',
    'siangpahrang': 'kumpipa',
    'cu': 'tua',
    'cun': 'tua',
    'suah': 'suahtakna',
    'nunnak': 'nuntakna',
}

def spell_check_zolai(text):
    """
    Check Zolai text for ZVS 2018 violations.
    """
    tokens = tokenize_zolai(text)
    errors = []
    
    for token in tokens:
        token_lower = token.lower()
        if token_lower in FORBIDDEN_FORMS:
            errors.append({
                'word': token,
                'suggestion': FORBIDDEN_FORMS[token_lower],
                'rule': f'Use {FORBIDDEN_FORMS[token_lower]} instead of {token}',
            })
    
    return errors
```

### Spell Checking Examples

| Input | Errors | Suggestion |
|-------|--------|------------|
| `Pathian in...` | `Pathian` | Use `Pasian` |
| `Ram ka mu hi.` | `Ram` | Use `Gam` |
| `Fapa hi.` | `Fapa` | Use `Tapa` |
| `Bawipa in...` | `Bawipa` | Use `Topa` |

---

## 10. Code Examples

### Complete NLP Pipeline

```python
class ZolaiNLP:
    """
    Complete NLP pipeline for Zolai.
    """
    
    def __init__(self):
        self.tokenizer = ZolaiTokenizer()
        self.pos_tagger = ZolaiPOSTagger()
        self.ner = ZolaiNER()
        self.parser = ZolaiParser()
        self.translator = ZolaiTranslator()
        self.classifier = ZolaiClassifier()
        self.sentiment = ZolaiSentiment()
        self.spell_checker = ZolaiSpellChecker()
    
    def analyze(self, text):
        """
        Full analysis of Zolai text.
        """
        # Step 1: Tokenize
        tokens = self.tokenizer.tokenize(text)
        
        # Step 2: POS tag
        pos_tags = self.pos_tagger.tag(tokens)
        
        # Step 3: Named entities
        entities = self.ner.extract(text)
        
        # Step 4: Parse dependencies
        dependencies = self.parser.parse(tokens, pos_tags)
        
        # Step 5: Classify text
        category = self.classifier.classify(text)
        
        # Step 6: Sentiment
        sentiment = self.sentiment.analyze(text)
        
        # Step 7: Spell check
        errors = self.spell_checker.check(text)
        
        return {
            'tokens': tokens,
            'pos_tags': pos_tags,
            'entities': entities,
            'dependencies': dependencies,
            'category': category,
            'sentiment': sentiment,
            'spell_errors': errors,
        }
    
    def translate(self, text, direction='zo-en'):
        """
        Translate Zolai text.
        """
        if direction == 'zo-en':
            return self.translator.to_english(text)
        else:
            return self.translator.to_zolai(text)
```

### Usage Example

```python
# Initialize pipeline
nlp = ZolaiNLP()

# Analyze text
text = "Pasian in vantung leh leitung a piangsak hi."
analysis = nlp.analyze(text)

print("Tokens:", analysis['tokens'])
print("POS Tags:", analysis['pos_tags'])
print("Entities:", analysis['entities'])
print("Category:", analysis['category'])
print("Sentiment:", analysis['sentiment'])

# Translate
english = nlp.translate(text)
print("English:", english)

# Spell check
errors = nlp.spell_checker.check("Pathian in ram a piangsak hi.")
print("Errors:", errors)
```

---

## Appendix: Zolai NLP Resources

### Available Tools

| Tool | Purpose | Source |
|------|---------|--------|
| Bible Engine | Verse analysis, glossing | `zolai-datasets/scripts/bible/bible_engine.py` |
| ZVS Checker | ZVS 2018 compliance | `zolai-core/zolai/zvs/` |
| Dictionary Lookup | Word translations | `zolai-datasets/data/dictionary/` |
| Grammar Patterns | Grammar rules | `zolai-datasets/data/bible/grammar_patterns_v2.jsonl` |
| Word Attestation | Word verification | `zolai-core/zolai/learning/word_attestation.py` |
| Sentence Validation | Sentence checking | `zolai-core/zolai/learning/sentence_validator.py` |

### Data Files

| File | Size | Purpose |
|------|------|---------|
| `dict_zo_en_master_v1.jsonl` | 11MB | ZO→EN dictionary (93,931 entries) |
| `dict_canonical_clean.jsonl` | 56MB | EN→ZO dictionary (112,220 entries) |
| `parallel_corpus_v1.jsonl` | 16MB | Bible verses (31,102) |
| `vocab_index_full.jsonl` | — | Vocabulary (20,929 words) |
| `grammar_patterns_v2.jsonl` | — | Grammar patterns (4,205) |
| `phrases_v1.jsonl` | — | Multi-word phrases (5,000) |

---

*Reference: ZVS 2018, Zolai Sinna Bu, Zolai Khanggui, Bible Parallel Corpus*
