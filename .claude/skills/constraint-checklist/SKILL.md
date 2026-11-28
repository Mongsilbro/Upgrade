---
name: constraint-checklist
description: "Use when one request sets many explicit constraints (형식, 분량, 필수 항목, 금지 표현). Changes across turns: `requirement-recap`."
---

# Constraint checklist

Source: ideas from Harada et al., *Curse of Instructions: Large Language Models Cannot Follow Multiple Instructions at Once*, OpenReview 2024 (id R6q67CDBCH); Jaroslawicz, Whiting, Shah, Maamari, *How Many Instructions Can LLMs Follow at Once?*, 2025 (arXiv:2507.11538); Zhou et al., *Instruction-Following Evaluation for Large Language Models*, 2023 (arXiv:2311.07911). Ideas only, no text reused.

Why: each added instruction is another chance to drop one. The chance of satisfying all of them falls roughly multiplicatively with their number, later instructions are dropped more often than early ones, and the misses are silent. Explicitly re-checking each instruction against the draft recovers much of the loss.

## When

One message (or attached 양식, 작성 지침, 공모 요강) sets about five or more checkable constraints on the output: length, format, headings or order, items that must appear, words or styles to avoid, numbers, dates, file type. Not for short casual requests.

## Steps

1. **Extract before drafting.** Write a numbered list of every constraint, each in the user's words or a close paraphrase with where it came from (문장, 양식 항목). Split compound ones ("A4 2쪽, 개조식" → two items). Include constraints that sit late in the message or in attachments; those are the ones most often missed.
2. **Flag conflicts now.** If two constraints cannot both hold (e.g. 1쪽 이내 + 항목 12개 각 설명), say so and ask, or state which one you prioritised and why.
3. **Draft.**
4. **Check item by item.** Go through the list against the finished draft, not from memory of writing it. Count what can be counted (글자 수, 쪽수, 항목 수, 문단 수) with a tool when one is available. Search the draft for every banned word or style.
5. **Fix, then re-check** only the items that failed and anything the fix touched.
6. **Report briefly** after the deliverable: `제약 N개 중 N개 충족` and, for any not met, which and why (conflict, missing information). Show the full list only if something failed or the user asks.

## Avoid

- Checking "in your head" while writing instead of against the final text.
- Silently dropping a constraint that turned out hard; say it was not met.
- Inventing constraints the user did not give; mark your own additions as 제안.
