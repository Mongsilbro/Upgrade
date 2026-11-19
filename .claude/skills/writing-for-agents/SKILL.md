---
name: writing-for-agents
description: Use when creating or editing a skill, CLAUDE.md, AGENTS.md, or any document an agent will follow.
---

# Writing for agents

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) `skills/productivity/writing-for-agents/SKILL.md` and `SKILL-MECHANICS.md`, MIT License, Copyright (c) 2026 Matt Pocock. Rewritten and condensed.

The goal of a document an agent reads is not identical output but the same *process* every run. These levers make that predictable.

## 1. Pointers decide when material is reached

A **pointer** is any always-loaded line that names material elsewhere and says when to reach it: a skill's `description`, a line in CLAUDE.md naming a doc. Its wording, not the target, decides whether the agent goes there.

- Start with the word that does the triggering ("Use when …").
- One trigger per distinct case the document handles. Synonyms for the same case count once; cut them.
- Don't repeat in the pointer what the body already says. Always-loaded text costs tokens every turn.
- If an important document is being missed, sharpen the pointer first; inline the material only if that fails.
- A skill only ever typed by hand can use `disable-model-invocation: true`: no always-loaded cost, but the human must remember it exists.

## 2. Put each piece at the right depth

Content is either **steps** (ordered actions) or **reference** (rules and facts consulted on demand). Place each piece on this ladder:

1. Steps in the main file.
2. Reference in the main file.
3. Reference in a separate file, reached by a pointer.

Inline what every path through the document needs; move to a linked file what only some paths need. Too little moved out buries the steps; too much hides what's needed. Keep a concept's definition, rules, and caveats together under one heading. A file too long even when every line is live (**sprawl**) gets split by case or by sequence.

## 3. Every step ends on a completion criterion

- **Clear:** the agent can tell done from not done. "Every changed endpoint listed with file:line" beats "understand the change." Vague criteria invite stopping early, pulled by the steps that come next.
- **Demanding where it matters:** "every rule checked" forces thoroughness that "review the code" doesn't.
- If a step keeps getting rushed despite a sharp criterion, split the later steps into a separate document or a subagent hand-off; hiding them only works across a real context boundary.

## 4. Word choice

- Prefer a compact, well-known term the model already understands (*tracer bullet*, *red/green*, *premortem*) over a sentence restating it; reuse the same term throughout.
- State the behaviour you want ("write one-line comments"), not the one you don't. Naming the forbidden behaviour makes it more available. Keep prohibitions for hard guardrails, paired with the positive target.

## 5. Prune

- One meaning, one place. Duplicates drift and inflate importance.
- Don't restate what the environment already shows (package scripts, config, `--help`). Record only what can't be looked up: unwritten conventions, the reason behind a choice, gotchas.
- For each sentence ask: does it change behaviour compared with the default? If not, delete the whole sentence. A too-weak word ("be thorough") is also a no-op; use a stronger one or drop it.
- Remove stale lines when behaviour changes, instead of adding layers on top.

## Checklist before saving a skill

- [ ] `description` starts with the trigger, lists each distinct case once, and says when *not* to use it if a neighbouring skill exists.
- [ ] Steps have checkable completion criteria.
- [ ] Main file holds what every run needs; optional reference is linked.
- [ ] No sentence that only restates default behaviour.
- [ ] Positive phrasing, except named guardrails.
