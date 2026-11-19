---
name: literature-review
description: Use when asked for a literature review, evidence summary, or 선행연구, or how strong the evidence behind a claim or study is. Not for a quick fact lookup.
---

# Literature review and evidence evaluation

Adapted from [affaan-m/ECC](https://github.com/affaan-m/ECC) `skills/scientific-thinking-literature-review` and `skills/scientific-thinking-scholar-evaluation` (MIT, © 2026 Affaan Mustafa). Rewritten and condensed; Korean public-sector sources and rules on unverified sources added.

The point: a review someone else could repeat and check. Every claim in the final text traces to a source that was actually read, and the reader can see how strong each claim is.

## 1. Fix the question and the rigor

- Turn the request into one answerable question. Health or social programs: population, intervention, comparison, outcome. Technical: domain, method, baseline, metric. Policy: target group, measure, alternative, intended effect.
- Pick the level and say it at the top of the output:
  - **narrative**: orientation, broad picture (default for background sections of reports);
  - **scoping**: map what exists, methods used, and gaps (default for exploratory work);
  - **systematic**: written protocol, reproducible search, logged exclusions (needed before claiming "the evidence shows" in anything published, clinical, or budget-deciding).
- Never call a review systematic without the protocol and logs below.

## 2. Plan the search before searching

Write down: sources to search, date range, languages, publication types, inclusion and exclusion criteria, and the exact query strings. Use at least two independent sources for any broad claim, or state that the scope is limited to one.

Typical sources: PubMed (biomedical), arXiv (CS, math, physics; preprints), OpenAlex / Semantic Scholar / Crossref (all fields), trial registries, standards bodies, official statistics. For Korean topics also: RISS, KCI, DBpia, 국회도서관, 국회입법조사처 보고서, 정책연구관리시스템(PRISM), KOSIS, and government-funded research institutes. Use only the sources this session can actually reach; name the ones skipped.

## 3. Log, deduplicate, screen

Keep a search log as you go:

| Source | Date searched | Query | Filters | Hits | Kept |
|---|---|---|---|---:|---:|

- Deduplicate by DOI → PMID/arXiv ID → exact title → normalized title + first author + year. Record how many were removed.
- Screen title → abstract → full text. For systematic work record each exclusion reason (wrong population, wrong outcome, not primary research, out of date range, full text unavailable, duplicate).
- A search snippet or abstract is not evidence for a specific finding. If only the abstract could be read, mark the source **[abstract only]** and do not quote numbers that are not in it.

## 4. Extract into one table

| Study | Type (RCT, cohort, survey, case, review, preprint, gov. report) | Data / sample | Method | Comparator | Outcome measure | Key finding | Limitations |
|---|---|---|---|---|---|---|---|

Technical papers add dataset, benchmark, baseline, and whether code or data is available.

## 5. Synthesize by theme, not paper by paper

Organize around questions: where sources agree, where they conflict and why (population, method, period), methodological weak spots, what is replicated, what is untested. Give each conclusion a confidence label:

- **High**: replicated across independent, sound studies.
- **Medium**: plausible but limited by sample, method, context, or age.
- **Low**: single source, early, preprint-only, or weakly measured.

Report null and contrary findings; leaving them out is the most common way a review misleads. Keep reviews, primary studies, preprints, and grey literature labeled as such.

## 6. Verify every citation before finishing

For each reference: the identifier (DOI, PMID, arXiv ID, official URL) resolves; authors and year match; the source actually says what it is cited for. Anything not checked gets **[확인 필요 / unverified]** in the text, never a guessed reference. Do not invent page numbers, sample sizes, or effect sizes.

## 7. Evaluating one study or report

When asked how good a particular paper, proposal, or research report is, score each dimension that applies 1–5 (5 ready as is, 3 usable with real gaps, 1 major validity problems; N/A if outside its scope), and give the evidence for each score:

1. Question: clear, specific, matched to the claimed contribution.
2. Context: prior work synthesized, gap stated accurately.
3. Method: answers the question, choices justified, reproducible.
4. Data: credible source, adequate sample, missing data and bias discussed.
5. Analysis: appropriate methods, fair baselines, uncertainty or robustness checked, alternative explanations considered.
6. Results: claims stay inside the evidence; null results reported.
7. Limitations: specific, not boilerplate; speculation separated from results.
8. Writing: argument easy to follow, terms defined.
9. Citations: cited sources support the attached claims; primary sources preferred.

Read abstract, figures, and conclusion first for what is claimed, then methods and results for whether it holds, then check the two or three strongest claims against their citations. Separate blocking problems from suggested revisions. Venue, citation count, or author reputation are not evidence of quality; neither is a claim appearing in the abstract.

## Output

```markdown
# Literature review: <topic>
Type: narrative | scoping | systematic   Searched: <date>   Window: <years>
Sources searched: <list>   Not reachable: <list>

## Question
## Search strategy and criteria
## Evidence table
## Synthesis by theme (with High / Medium / Low)
## Gaps and limits of this review
## References (unverified ones marked)
## Search log
```

For a single-study evaluation: overall view and confidence, the score table with evidence, blocking issues, recommended revisions, and the checks still needed.
