---
name: handoff
description: Use when the user asks for a handoff, wants to continue this work in another chat or session, or the conversation is long and the work should move to a fresh context. Writes a compact document a new agent can pick up from without the conversation.
---

# Handoff

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) (`skills/productivity/handoff`, MIT, © 2026 Matt Pocock). Reworded and expanded; see `UPGRADES.md`.

Write a document that lets a fresh agent, with no access to this conversation, continue the work.

## Contents

```
# Handoff: <task>
Next session will: <what the user said it's for, or your best reading>

## Goal
<what the user ultimately wants, in their terms>

## Done so far
<outcomes, not a narrative; link commits, files, PRs instead of restating them>

## Decisions and constraints
<choices the user made and rules they set — the things a newcomer would otherwise re-ask or get wrong>

## Current state
<branch, what works, what's broken, what's uncommitted>

## Next steps
<ordered, concrete>

## Open questions
<anything waiting on the user>

## Suggested skills
<skills from .claude/skills the next agent should use, and when>
```

## Rules

- Reference existing artifacts (specs, plans, ADRs, issues, commits, diffs) by path or URL; don't copy them in.
- Remove secrets, tokens, passwords, and personal data.
- Keep it short enough to read in a minute.
- Save it outside the repository by default (a temp or scratch directory the user can open), and tell the user the full path. Commit it to the repo only if the user wants that.
- If the user said what the next session is for, tailor the document to that.
