---
name: verification-before-completion
description: Use right before claiming work is done, fixed, or passing, and before committing or pushing.
---

# Verification Before Completion

Adapted from [obra/superpowers](https://github.com/obra/superpowers) (`skills/verification-before-completion`, MIT, © 2025 Jesse Vincent). Condensed and reworded; see `UPGRADES.md`.

**No claim of success without fresh evidence from this turn.**

## Before any "done", "fixed", "passes", "works"

1. **Identify** the command or check that would prove it.
2. **Run** it in full, now — not a subset, not a result from earlier.
3. **Read** the whole output: exit code, failure count, warnings.
4. **Report** what the output shows. If it confirms the claim, say so with the evidence ("34/34 tests pass"). If not, report the actual state.

## What counts as proof

| Claim | Proof | Not proof |
|-------|-------|-----------|
| Tests pass | Test run with 0 failures | An earlier run; "should pass" |
| Build works | Build command exits 0 | Linter passing |
| Bug fixed | The original reproduction now passes | Code changed |
| Regression test is real | It fails with the fix reverted, passes with it | Passing once |
| Subagent / delegated work done | The diff or output, inspected | Its own success report |
| Requirements met | Each requirement checked off against the result | Tests passing |

## Warning signs

- Words like "should", "probably", "seems to", "looks correct".
- Celebrating before checking.
- About to commit or push without running anything.
- Trusting another agent's or tool's summary of its own work.
- A partial check standing in for the full one.

If the full check genuinely can't be run here (no hardware, no credentials, too slow), say exactly what was and wasn't verified instead of implying success.
