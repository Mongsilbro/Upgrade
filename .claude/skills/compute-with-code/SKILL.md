---
name: compute-with-code
description: 'Use when an answer needs numbers derived from given figures (합계, 증감률, 비율, 기간·날짜, 단위 환산). Sourcing figures: `gov-report`.'
---

# Compute with code, not in your head

Ideas from Gao et al., *PAL: Program-aided Language Models*, 2022 (arXiv:2211.10435); Chen et al., *Program of Thoughts Prompting*, 2022 (arXiv:2211.12588); Dziri et al., *Faith and Fate: Limits of Transformers on Compositionality*, 2023 (arXiv:2305.18654). Written from scratch; no text reused.

Why: language models set up a calculation correctly far more often than they carry it out correctly. Errors grow with the number of digits and steps, and they read as confident. Running the arithmetic in an interpreter removes that class of error.

## When it applies

Any number you would produce that is not copied verbatim from the source: sums, differences, 증감률, 비중, averages, per-capita figures, 집행률, date spans and deadlines (D-day, 영업일), unit or currency conversion, rounding to 천원/백만원/억원. A single one-digit step ("3 + 4") does not count.

## Steps

1. **Write the inputs down with their source** (표 2 row, page, cell). If an input is missing, stop and ask; don't estimate it.
2. **Compute in code** (Python with `-I`, or the spreadsheet itself). One short script for all derived figures in the answer, inputs as named variables, `Decimal` for money. Dates with `datetime`; 영업일 needs the holiday list stated, or say it was not applied.
3. **Cross-check what the source already states.** Recompute any total, subtotal, or percentage the source prints. A mismatch is a finding: report "표 합계 1,234 vs 계산 1,243" instead of silently using either.
4. **Report** each derived figure with its formula in words once (e.g. 증감률 = (금년 − 전년) ÷ 전년). Keep the distinction between % and %p, and state the rounding rule.
5. **No code tool available** (e.g. chat without code execution): show each step on its own line, check by a reverse operation (multiply back, add the parts), and tag the result `[미검산]` so the reader knows it was not machine-checked.

## Checks before sending

- Every derived number traces to a line of the script or a shown step.
- Rounded parts that don't sum to the rounded total are noted ("단수 차이").
- Inputs, script, and outputs agree with what the prose says (copying a result into text is a common slip; re-read it).
