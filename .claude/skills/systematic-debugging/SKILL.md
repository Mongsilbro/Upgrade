---
name: systematic-debugging
description: Use when hitting any bug, test failure, or unexpected behavior, before proposing a fix.
---

# Systematic Debugging

Adapted from [obra/superpowers](https://github.com/obra/superpowers) (`skills/systematic-debugging`, MIT, © 2025 Jesse Vincent). Condensed and reworded; see `UPGRADES.md` for the adoption record.

**Rule: no fix until the root cause is understood.** A change that makes the symptom disappear without explaining it is not a fix.

## Phase 1 — Investigate

1. **Read the whole error.** Full stack trace, warnings, file paths, line numbers, error codes. The answer is often in the text that gets skimmed.
2. **Reproduce it.** Find exact steps that trigger it reliably. If it is intermittent, collect more data instead of guessing.
3. **Check what changed.** `git diff`, recent commits, dependency bumps, config and environment differences.
4. **In multi-component systems, instrument the boundaries first.** At every hand-off (CI → build → deploy, API → service → DB) log what goes in, what comes out, and whether config/env actually arrived. Run once, find *which* boundary breaks, then dig only there.
5. **Trace bad values backward.** Where did the wrong value originate? Who passed it in? Keep going up the call chain and fix at the source, not where it finally blew up.

## Phase 2 — Compare

- Find similar code in the same codebase that works.
- If following a reference implementation, read all of it, not a skim.
- List every difference between working and broken, including ones that "can't matter".
- Note the dependencies and assumptions the broken code relies on.

## Phase 3 — Hypothesize and test

- State one hypothesis: "X is the root cause because Y."
- Test it with the smallest possible change, one variable at a time.
- Confirmed → Phase 4. Refuted → form a new hypothesis; do not stack another fix on top.
- If something isn't understood, say so and research it rather than pretending.

## Phase 4 — Fix

1. Write a failing reproduction first (automated test if possible, a one-off script otherwise).
2. Make one change that addresses the root cause. No drive-by refactoring.
3. Verify: the reproduction passes, nothing else broke, the original problem is actually gone.
4. If the fix fails, go back to Phase 1 with the new information.
5. **After three failed fixes, stop.** Each fix surfacing a new problem somewhere else means the design is wrong, not the hypothesis. Raise it with the user before trying a fourth.

## Stop signs

Any of these thoughts means return to Phase 1:

- "Quick fix now, investigate later."
- "Just change X and see."
- "It's probably X."
- "I don't fully get it, but this might work."
- Bundling several changes into one test run.
- Listing fixes before tracing the data flow.
- "One more attempt" after two have already failed.

## When there is no root cause

If the investigation genuinely shows an environmental, timing, or external cause: document what was checked, add appropriate handling (retry, timeout, clear error), and add logging for next time. Be suspicious of this conclusion — it usually means the investigation was incomplete.

## Related techniques

- **Condition-based waiting:** replace fixed sleeps in flaky tests with polling for the actual condition.
- **Defense in depth:** once the root cause is fixed, add validation at the other layers the bad data passed through.
