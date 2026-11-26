---
name: dated-facts
description: "Use when stating facts that change over time (현직자, 최신 버전·통계, 현행 금액·제도) or dates counted from today."
---

# Dated Facts

Ideas from Dhingra et al., *Time-Aware Language Models as Temporal Knowledge Bases* (TACL 2022, arXiv:2106.15110); Cheng et al., *Dated Data: Tracing Knowledge Cutoffs in Large Language Models* (2024, arXiv:2403.12958); Vu et al., *FreshLLMs* (2023, arXiv:2310.03214). Written from scratch; no text reused. See `UPGRADES.md`.

Why: many facts expire (who holds a post, the latest release, this year's 기준 중위소득, a fee or rate). A model answers them from a training snapshot whose effective cutoff differs by topic and is often older than the stated one, and it states them in the present tense with no date. Related: `source-driven` (library versions), `korean-law-citation` (현행 법령), `grounded-answers` (facts from a supplied document).

## Steps

1. **Spot the perishable claims.** Before sending, list every claim whose truth depends on when it is read: office holders, organisation names and structure, "latest/current/최신/현행", prices, fees, rates, thresholds, budgets, statistics with a year, deadlines, rankings, product features. Stable facts (definitions, history, math) are not on the list.
2. **Anchor to today.** Take today's date from the context (system prompt, environment, file dates), not from memory. Compute "N년 전", "올해", "다음 달", ages, and elapsed periods from it, and say which date you used.
3. **Check or date each claim.**
   - If search, a supplied document, or a repository file can confirm it, check it and cite the source with its date.
   - If not, keep the claim but tag it inline with the year it reflects: "(2025년 기준 기억, 최신 확인 필요)". Never write an unchecked perishable claim in the bare present tense.
   - If the question is mostly about something that changes often (this week's news, today's price), say you cannot know the current value and give the last value you know with its date.
4. **Watch false premises.** If the question assumes something that may have changed ("올해 바뀐 제도에 따라…"), say what you know, its date, and that the premise needs checking, instead of answering as if it were confirmed.
5. **Report.** When step 1 found any perishable claims, end with one line: `시점 확인: N건 중 확인 M건, 미확인 K건(…)`, naming the unchecked ones.

## Done when

Every perishable claim in the answer is either sourced with a date or tagged with the year it reflects, relative dates were computed from a stated today, and the 시점 확인 line is present.
