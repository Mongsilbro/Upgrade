---
name: scoped-summaries
description: "Use when summarizing study or report findings or writing 시사점. Quoting long documents: `grounded-answers`."
---

# Scoped summaries of findings

Ideas (not text) from: U. Peters and B. Chin-Yee, "Generalization Bias in Large Language Model Summarization of Scientific Research", 2025 (arXiv:2504.00025). Written from scratch; see `UPGRADES.md`.

Why: in that study most of ten LLMs, Claude included, wrote summaries that claimed more than the source did: a result from one sample, place, or period became a general present-tense rule ("X reduces Y"). LLM summaries were about five times as likely as human-written ones to generalize broadly, and asking for accuracy did not stop it. The words that get lost are small (in this sample, was associated with, may), so a fluent summary hides the drift.

Related: `grounded-answers` covers finding and quoting passages in long documents; `literature-review` covers grading evidence across many studies. This skill governs how each finding is restated.

## Steps

1. **List each finding with its frame before writing.** For every result you will mention, note from the source: who or what was studied (population, sample size, region), when, the design (experiment, survey, case, model estimate), the claim's strength (cause, association, description, prediction), and any hedge or limit the authors state.
2. **Restate within that frame.** Keep:
   - **Scope**: name the population, place, or period (`2023년 서울 3개 구 시범사업 참여자 120명에서`), not "시민들은" or "people".
   - **Tense**: past tense for what was observed (`감소했다`); general present tense (`감소시킨다`) only if the source itself makes a general claim.
   - **Strength**: "associated with" stays `관련이 있었다`, not `효과가 있다`; "may" stays `~일 수 있다`; a model estimate stays an estimate.
   - **Quantity**: keep the figure, its unit and comparison base instead of turning it into "크게", "대부분", "significantly".
3. **Keep the authors' limits.** If the source names a limitation (small sample, one site, self-report, short follow-up), carry one line of it into any summary longer than two sentences.
4. **Separate your inference.** Policy implications (시사점) and extrapolations to other places are yours, not the study's. Label them (`시사점(작성자 판단):`) and phrase them as conditional (`~에도 적용된다면`).
5. **Check sentence by sentence.** Before finishing, set each summary sentence beside its source sentence and ask: is the claim broader, more causal, more certain, or more present-tense than the source? Fix any that is.

## Output

End the summary with one line: `범위 점검: 요약 N문장 중 원문 범위 유지 N, 수정 M`. For a one-sentence summary, skip the line but still do step 5.

Shortening is fine; widening is not. When space forces a choice, drop a finding rather than drop its scope.
