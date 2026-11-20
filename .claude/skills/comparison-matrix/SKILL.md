---
name: comparison-matrix
description: Use when comparing several options, vendors, products, or other organizations' cases on the same criteria (비교표, 대안 비교, 벤치마킹, 타 기관 사례 비교), or scoring them.
---

<!--
Adapted from affaan-m/ECC, skills/benchmark-methodology/SKILL.md
https://github.com/affaan-m/ECC — MIT License, Copyright (c) 2026 Affaan Mustafa.
The source scores design-studio competitors; this version keeps its scoring discipline
(anchored rubrics, evidence per score, no composite, asserted vs proven, cross-set
calibration) and generalizes it to any side-by-side comparison. Rewritten, not copied.
-->

# Comparison matrix

A comparison is only useful if the same evidence would earn the same score for every option. Build it so a reader can check each cell.

## 1. Fix the frame before looking at options

- **Decision question**: what the comparison is for (choose one, rank, learn from cases). Ask the user if unclear.
- **Option set**: list what is in and why; say what was left out. Note strong but less visible options found in directories, reports, or other agencies, not only the well-marketed ones.
- **Criteria**: 4–8, each one sentence, non-overlapping. Mark any must-have (pass/fail) separately from scored criteria. If weights matter, agree them with the user now, not after scoring.
- **Key trade-off** (optional): if the real question is whether an option achieves two things at once (e.g. cost vs. quality, speed vs. legal safety), keep those as two separate axes.

## 2. Anchor the scale per criterion

Use 1–5 and write what 1, 3, and 5 mean *for that criterion* before scoring:

- 1 absent or a liability · 2 below par · 3 meets expectations, nothing special · 4 clearly better than peers · 5 sets the standard.

Example for "evidence of results": 1 no outcome stated · 3 outcomes stated by the provider · 5 independently measured outcomes with numbers and a named source.

## 3. Score with evidence

- Every cell: score, one-line reason, source (link, document, page). No source → write "확인 불가 / not verified", not a guessed score.
- Tag claims **proven** (third-party, measured, verifiable) or **asserted** (the option's own marketing, press release, self-report). Score asserted-only evidence lower.
- Collect cheapest reliable sources first: official documents and sites → independent reports, audits, reviews → news. Do not invent figures.

## 4. Check bias before reporting

- **No single composite as the headline.** Show per-criterion scores; a weighted total, if the user wants one, goes after the table with the weights stated. Never average the two trade-off axes; the gap between them is the finding.
- **Calibrate across the set**: re-read each column side by side so a "4" means the same for every option; fix outliers.
- **Taste and novelty**: don't let a polished or fashionable option score high on substance criteria without evidence.
- **Score once, then compare**: score each option on the rubric before forming an overall preference.

## 5. Output

1. One-line decision question and option set (with exclusions).
2. Table: options × criteria, each cell `score — reason [source, proven/asserted]`; must-have results as ✓/✗.
3. Trade-off view if used: each option's two axis scores and which quadrant it falls in; say who already occupies the target quadrant.
4. Per option, one line each: strength to learn from, weakness, risk.
5. Gaps: cells not verified and what would close them.

Recording the final choice: `architecture-decision-records` (technical) or `gov-report` (개선방안·대안 비교 보고서). Judging a single study's quality: `literature-review`.
