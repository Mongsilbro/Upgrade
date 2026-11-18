---
name: regex-first-extraction
description: Use when designing code that extracts structured data from text — forms, invoices, receipts, quizzes, logs, tables, documents — and choosing between regular expressions, an LLM, or both. Regex for consistent formats, a confidence check to flag doubtful items, and an LLM only for those.
---

# Regex-First Extraction

Adapted from [affaan-m/ECC](https://github.com/affaan-m/ECC) (`skills/regex-vs-llm-structured-text`, MIT, © 2026 Affaan Mustafa). Condensed and reworded; see `UPGRADES.md`.

## Choose

- **Format mostly consistent and repeating** → start with regex (or a real parser for structured formats like CSV, JSON, HTML). If it covers nearly everything, stop there.
- **Mostly consistent, with a tail of oddities** → regex plus an LLM for the flagged tail only.
- **Free-form and highly variable** → LLM directly.

## Hybrid pipeline

```
text → regex parse → clean (strip page numbers, markers, artifacts)
     → score confidence per item
         ├─ high → output
         └─ low  → LLM fix-up (item + its source text) → output
```

- **Confidence scoring** is a set of cheap checks for the specific format: expected fields present, counts in range (e.g. 3–5 choices), lengths plausible, values in an allowed set. Each failed check lowers the score and records a reason.
- **LLM fix-up** sends only the flagged item and its surrounding source text, asks for corrected structured output (or "CORRECT"), and validates the reply against the same schema before accepting it. Use the cheapest model that is accurate enough.
- Return new objects from cleaning and fix-up steps rather than mutating parsed ones; it keeps each stage testable.

## Practice

- Write tests from real samples first, including malformed input, missing fields, and encoding problems.
- Log the regex hit rate, how many items were flagged, and how many LLM calls were made, so drift in the input format shows up.
- Don't send everything to an LLM when a pattern covers almost all of it — slower, costlier, and less deterministic. Don't force regex onto free-form text either.
