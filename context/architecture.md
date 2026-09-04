# Zolai Wiki — Architecture

- Content: `wiki/` markdown tree (grammar, vocabulary, curriculum, culture,
  biblical, architecture, concepts).
- Consumed by: zolai-core (RAG/embeddings), zolai-web (curriculum).
- Bulk data: `../data/` (container shared, 6.3G, not a git repo).
- Enrichment: see `docs/WIKI_ENRICHMENT_GUIDE.md` (repo-local).
- Invariants: no secrets; no origin-point personal content; ZVS 2018.
