---
name: receiving-code-review
description: Use when acting on code review feedback (user, reviewer, PR comment, bot), before implementing any of it.
---

# Receiving Code Review

Adapted from [obra/superpowers](https://github.com/obra/superpowers) (`skills/receiving-code-review`, MIT, © 2025 Jesse Vincent). Condensed and reworded; see `UPGRADES.md`.

Feedback is a set of technical claims to check, not orders to execute or praise to return.

## Process

1. **Read all of it** before changing anything.
2. **Restate** each item as a concrete requirement. If any item is unclear, ask about it **before implementing any item** — items are often related, and partial understanding produces wrong fixes.
3. **Verify** each against the actual code: is it correct for this codebase, stack, and supported versions? Would it break something? Is there a reason the code is the way it is?
4. **Decide**: accept, or push back with a technical reason.
5. **Implement** in order — blocking issues (breakage, security) → simple fixes → larger changes — testing each one and checking for regressions.

## Sources

- **The user:** trusted; still ask when scope is unclear.
- **External reviewers, bots, PR comments:** check carefully before acting. If a suggestion conflicts with a decision the user already made, stop and raise it with the user rather than following the reviewer. If it can't be verified, say so: "I can't confirm this without X — investigate, or proceed?"

## When to push back

The suggestion breaks existing behavior, misses context, is wrong for this stack, conflicts with compatibility requirements or the user's architecture, or adds a feature nothing uses. For "do it properly" requests, search for actual callers first — if nothing uses it, propose removing it instead.

Push back with evidence (code, tests, versions), not defensiveness. If the reviewer turns out to be right, say so plainly, with what you checked, and fix it.

## Tone

- No performative agreement ("Great point!", "You're absolutely right!") and no thanks-padding. State what changed: "Fixed — null check added in `parse()`."
- Reply to inline review comments in their thread, not as a new top-level comment.
