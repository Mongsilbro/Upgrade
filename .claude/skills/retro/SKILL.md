---
name: retro
description: Use when asked for a retrospective on a session or how future agent runs in this repo could go better.
---

# Retro

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) (`skills/engineering/retro`, MIT, © 2026 Matt Pocock). Condensed and reworded; see `UPGRADES.md`.

Goal: change the **environment** so the next agent run in this repo goes better — not to critique the agent's prose.

## Steps

1. Use the session the user names; default to the current one. Work from what actually happened (the transcript, commits, failed commands), not memory.
2. Look for problems in these areas:

| Area | Signal | Typical fix |
|------|--------|-------------|
| Navigation | Took long to find a file or fact; hidden coupling between files | A short pointer in `CLAUDE.md` or the relevant README |
| Automated checks | A mistake a linter, type check, test, or hook could have caught; or the repo has no pre-commit hook or CI running its checks at all | Wire up the check — first see whether one already exists but isn't run |
| Standards | A recurring style or design violation | Mechanical rule → automated check; judgement call → a written standard read at review time |
| Instruction bloat | `CLAUDE.md`/`AGENTS.md` large, or holding lines that change nothing | Move detail to docs or skills, delete no-ops |
| Tool cost | Expensive or noisy tool calls repeated | A cheaper command, script, or narrower query |
| Missing information | A crucial fact wasn't reachable (logs, service state) | Give read access, tee logs to a file |

3. Present findings to the user, most severe first, each with the evidence from the session and the concrete change proposed. Make changes only after the user picks which ones.

## Principles

- Instruction files loaded into every session (`CLAUDE.md`, `AGENTS.md`) cost context on every run. Keep them to pointers and rules that really change behavior.
- Prefer a deterministic check over a written rule whenever the rule is mechanical.
- Standards that need judgement are best enforced at review time, where there is less context pressure than during implementation.
