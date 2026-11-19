---
name: grilling
description: "Use when the user asks to be grilled, interviewed, or challenged on a plan or idea before work starts. Ready-to-commit plan documents: `premortem`."
---

# Grilling

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) (`skills/productivity/grilling`, MIT, © 2026 Matt Pocock). Reworded; see `UPGRADES.md` for the adoption record.

Interview the user until both sides hold the same picture of the plan. Do not start acting on the plan during the interview.

## Model: a decision tree

Every decision opens further decisions that depend on it. The **frontier** is the set of decisions whose prerequisites are already settled — the questions that can be asked now without guessing at an answer not yet given.

## Work in rounds

1. Ask the **whole frontier** in one message, numbered.
2. Give a recommended answer with each question, and phrase the question so that "yes" accepts the recommendation.
3. Wait for the answers.
4. Recompute the frontier — settled answers unlock the questions that hung off them — and ask the next round.

A question that depends on another question in the same round belongs in a later round.

Round format:

```
**Q1 — <short title>**: <the question; options if there are any>
→ Recommended: <answer and one-line reason>

---

**Q2 — <short title>**: ...
→ Recommended: ...
```

## Facts versus decisions

- **Facts are your job.** If a question can be answered from the codebase, files, tools, or documentation, look it up instead of asking. While a lookup is pending, hold back only the questions that depend on it and ask the rest.
- **Decisions are the user's.** Put each one to them, even when the recommendation seems obvious. Do not settle a branch silently.

## Finishing

The interview is over when the frontier is empty: every branch visited, nothing assumed. Summarize the settled decisions and ask the user to confirm the shared understanding before acting on it.
