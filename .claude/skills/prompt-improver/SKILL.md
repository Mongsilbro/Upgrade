---
name: prompt-improver
description: Use when the user asks to improve, rewrite, or review a prompt for an AI (프롬프트 다듬어 줘, 어떻게 시키면 돼). Advises only; does not do the task.
---

<!--
Adapted from affaan-m/ECC, skills/prompt-optimizer/SKILL.md (author YannJY02)
https://github.com/affaan-m/ECC — MIT License, Copyright (c) 2026 Affaan Mustafa.
The source maps prompts to ECC's own commands, agents, and tech stacks; this version
drops that catalogue, generalizes the missing-context check to non-code work
(reports, letters, research), and points to this library's skills. Rewritten, not copied.
Skills and CLAUDE.md files are not prompts in this sense: use `writing-for-agents`.
-->

# Prompt improver

Turn a draft prompt into one the user can paste and run, for Claude, Claude Code, or any other AI tool. **Do not carry out the task itself.** If the user says "just do it", stop advising and treat it as a normal request.

## Steps

1. **Read the context you already have.** In a repository, glance at `CLAUDE.md` and the main manifest so the prompt can name the real stack and conventions instead of asking. Note which tool the prompt is for; if unknown, write it tool-neutral.
2. **Name the intent** in one line: produce a document, change code, fix a bug, research, review, compare, plan, translate, summarize. A prompt that mixes two big intents should usually become two prompts.
3. **Check what is missing.** Mark each as present, inferable (say from where), or missing:
   - Goal and why it is needed, and who the output is for
   - Inputs: which files, data, or source documents; what to treat as authoritative
   - Output: format, length, language, register, file type, where it goes
   - Done criteria the AI can check (tests pass, every section has a source, ≤ 2 pages)
   - Constraints and scope limits: what not to touch, not invent, or not decide
   - Existing patterns to follow (a previous report, a file, a style guide)
   - For code: test expectations, security, data or schema changes
4. **Ask before rewriting only if three or more critical items are missing**, and then at most three questions, each with a suggested default. Otherwise fill gaps with stated assumptions.
5. **Size it.** One sitting → one prompt. Larger → a sequence: research/plan first, then one prompt per phase, each ending with a check.

## Output

Reply in the user's language.

1. **Diagnosis** — what the draft already does well (one or two lines), then a short table: problem → effect → fix.
2. **Improved prompt** — one fenced block, self-contained: context, task, inputs, output format, done criteria, out of scope, and "if something is unclear, ask before guessing" when stakes are high. Mark any assumption you made as `[가정: …]` / `[assumption: …]` so the user can edit it.
3. **Short version** — two or three lines for a user who already knows the context.
4. **Skills that help** — only if relevant and the prompt is for a session with this library, name them (e.g. `writing-plans`, `tdd`, `systematic-debugging`, `gov-report`, `korean-doc-style`, `literature-review`, `comparison-matrix`).

Keep the rationale to the diagnosis table; do not add a separate essay on prompting.

## Habits to fix in drafts

- Vague verbs ("정리해 줘", "make it better") → say what changes and how to judge it.
- Asking for facts the AI cannot know (figures, recent regulations) without supplying a source → add the source or tell it to mark unknowns rather than invent them.
- Persona lines that carry no information ("you are a world-class expert") → replace with the actual audience and standard.
- Everything in one prompt → split by intent or phase.
- No negative scope → add what must stay unchanged.
- Personal or confidential data pasted into a prompt meant for an outside tool → point it out and suggest placeholders.
