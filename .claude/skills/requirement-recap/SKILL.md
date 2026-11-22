---
name: requirement-recap
description: Use when the user adds, corrects, or changes requirements across several turns ("아 그리고", "그게 아니라", "하나 더"), or a request arrives in pieces before the first full answer.
---

# Requirement recap

Source: ideas from Laban, Hayashi, Zhou, Neville, *LLMs Get Lost In Multi-Turn Conversation*, 2025 (arXiv:2505.06120). Ideas only, no text reused.

Why: when a task is revealed bit by bit, models answer too early, fill gaps with their own guesses, and then keep building on that first attempt. Errors from an early guess persist even after the user says otherwise. Performance drops sharply compared with getting the same request in one message.

## Rules

1. **Don't lock in early.** If the first message leaves out something that decides the result (audience, format, scope, numbers, constraints), ask about it or give a short draft clearly marked as provisional. Don't present a polished final version built on guesses.
2. **Keep one requirement list.** From the second requirement-bearing turn on, keep a numbered list of everything the user has asked for, each item tagged with where it came from:
   - `[사용자]` stated by the user (quote a few words)
   - `[가정]` your own assumption, not confirmed
   - `[변경]` an item the user replaced; strike the old one (~~old~~) and write the new one
3. **Rebuild, don't patch.** When requirements change, regenerate the answer from the whole list, not by editing the previous answer. Then check the new answer against every list item, including ones from early turns.
4. **Drop your own leftovers.** Delete content that came only from a `[가정]` the user has now contradicted or never confirmed and that no longer fits. Don't carry forward a detail just because an earlier answer had it.
5. **Show the list.** Put the current list above the answer (short, 1 line per item) whenever it changed this turn. End with any `[가정]` items still open, as questions.
6. **Offer a fresh start when it's tangled.** After many corrections, offer the list as one consolidated prompt the user can paste into a new chat (see `handoff` for bigger work).

## Done when

- The answer satisfies every non-struck list item, and you can point to where.
- No content rests on an assumption the user contradicted.
- Open assumptions are listed as questions, not silently kept.

Related: `grilling` (interviewing on a plan before work), `running-summary` (CONTEXT.md across tasks), `prompt-improver` (rewriting a prompt for someone else).
