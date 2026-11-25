---
name: pairwise-judging
description: "Use when judging which of two or more drafts or answers is better, incl. your own (A안 vs B안). Scoring options: `comparison-matrix`."
---

<!--
Ideas only, no text reused. Written from scratch after:
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", 2023 (arXiv:2306.05685):
  LLM judges show position bias, verbosity bias, and self-enhancement bias; swapping order helps.
- Wang et al., "Large Language Models are not Fair Evaluators", 2023 (arXiv:2305.17926):
  verdicts flip when candidate order is swapped; writing evidence before the verdict and
  balancing positions reduce it.
- Panickssery, Bowman, Feng, "LLM Evaluators Recognize and Favor Their Own Generations", 2024
  (arXiv:2404.13076): models rate their own outputs higher, linked to recognizing them.
-->

# Pairwise judging

A model picking the better of two texts leans toward the one shown first, the longer one, and the one it wrote itself. None of these is a quality. Judge so that swapping order, trimming padding, or hiding authorship would not change the verdict.

## Steps

1. **Neutral labels.** Call the candidates A, B (C…). If one is yours (an earlier draft, your own answer), say so once in the report, then judge it by the same rules; do not let "I wrote this" or "the user wrote this" count either way.
2. **Criteria first.** Before reading for a verdict, write 3–6 criteria from the user's purpose (accuracy, 요청 충족, 근거, 읽는 사람에게 맞는가, 분량 제한…). Use the user's criteria if given.
3. **Evidence before verdict, per criterion.** For each criterion quote or point to the specific passage in each candidate, then give the winner of that criterion or "동등". Read the later candidate first on every other criterion so neither always goes first.
4. **Length check.** If one is notably longer, ask of each extra part: does it add something the purpose needs, or repeat, pad, or hedge? Extra length scores only for content that is needed.
5. **Swap check.** Before the final verdict, restate the comparison with the order reversed (B vs A) and see if any criterion flips. A flip means the difference is too small to call: mark that criterion "동등". For a decision that matters, have a subagent or a free model (`second-opinion`) judge with the order reversed and labels only, and report whether it agreed.
6. **Verdict.** Name the winner only if it wins on the criteria that matter most to the purpose; otherwise say "우열 없음" and describe the trade-off. Suggest a merge when each has parts the other lacks.

## Output

- Table: criterion × candidate, each cell a short quote or pointer, last column the criterion winner or 동등.
- One line: `판정: A / B / 우열 없음 — 이유` and whether the swap check changed anything.
- Optional: what to take from the losing candidate.

Scoring many options, vendors, or other agencies' cases on a rubric: `comparison-matrix`. Reviewing one draft alone: no comparison needed.
