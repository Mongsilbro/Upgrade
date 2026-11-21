---
name: grounded-answers
description: Use when answering questions from, or summarizing, a long document or several documents the user supplied (지침, 편람, 법령 전문, 보고서, PDF, 회의록). Law citations: `korean-law-citation`.
---

# Grounded answers from long documents

Ideas (not text) from: Anthropic, "Reduce hallucinations" and "Prompting best practices — Long context prompting" (platform.claude.com docs, read 2026-11-21); N. F. Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", TACL 2023 (arXiv:2307.03172); S. Dhuliawala et al., "Chain-of-Verification Reduces Hallucination in Large Language Models", 2023 (arXiv:2309.11495). Written from scratch; see `UPGRADES.md`.

Why: models miss facts placed in the middle of long inputs, and paraphrased answers drift from the source. Quoting first and checking each claim against a quote catches both.

## Steps

1. **Find before answering.** Search the whole document for every passage relevant to the question (use `grep`/text search on extracted text, not only what you remember reading). Look at the middle sections deliberately, not just the start and end.
2. **Quote.** List the relevant passages word for word, each with its location (page, 장·조·항, section heading, or line). Keep quotes short — only the sentence that carries the fact.
3. **Answer from the quotes only.** Each claim in the answer points to a quote number, e.g. `[인용 2]`. General knowledge that is not in the document is labelled `(문서 외 일반 지식)` or left out when the user wants document-only answers.
4. **Say what is missing.** If the document does not answer part of the question, write `문서에 해당 내용 없음` for that part instead of filling the gap.
5. **Check independently.** After drafting, take each factual claim (number, date, deadline, amount, condition, exception) and re-find it in the source text without looking at your draft. Remove or correct any claim whose quote you cannot find; note conflicts between passages (e.g. 본문 vs 별표) rather than picking one silently.

## Output shape

- 답변 (근거 번호 표시)
- 근거 인용: 번호 · 위치 · 원문
- 문서에 없는 부분 / 상충하는 부분 (있을 때만)

Short questions about a short text (under a page or two) don't need the full shape: answer, then give the one supporting quote and its location.
