---
name: writing-plans
description: Use when asked for an implementation plan, or before coding a multi-step task that has a spec.
---

# Writing Plans

Adapted from [obra/superpowers](https://github.com/obra/superpowers) (`skills/writing-plans`, MIT, © 2025 Jesse Vincent). Condensed and reworded; see `UPGRADES.md`.

Write for an engineer who knows the language but not this codebase or this spec. They can write good code once told the exact interface and the exact test. What they can't know is **what you decided** — files, names, signatures, values from the spec, which tests prove each task. The plan records those decisions and nothing else.

Save it where the user wants; otherwise ask, or put it under `docs/plans/YYYY-MM-DD-<feature>.md`.

## Before the tasks

- **Scope.** If the spec covers several independent subsystems, propose one plan per subsystem; each plan should produce working, testable software on its own.
- **File map.** List the files to create or change and what each is responsible for. One responsibility per file; things that change together live together; follow existing patterns in the codebase.

## Header

```
# <Feature> Implementation Plan
Goal: <one sentence>
Approach: <2–3 sentences>
Stack: <key technologies>
Spec: <path or link>

## Global constraints
<project-wide requirements with exact values copied from the spec>

## Review focus
<up to five inputs or failure modes the spec implies but no task's tests cover, most likely first — each then gets a test in the owning task>
```

## Each task

```
### Task N: <component>
Files: create / modify (with line ranges) / test paths
Consumes: <exact signatures from earlier tasks>
Produces: <exact signatures later tasks rely on>

- [ ] Write failing test `<name>` asserting <exact values>
- [ ] Run `<command>` — expect FAIL (<reason>)
- [ ] Implement `<signature>` in `<file>` (one line on approach if there's a real choice)
- [ ] Run `<command>` — expect PASS
- [ ] Commit
```

A task is the smallest unit with its own test cycle that a reviewer could accept or reject on its own. Fold setup and docs into the task that needs them.

## Right amount of detail

A step is done when the implementer can write exactly one reasonable thing from it.

- **Too little:** "handle edge cases", "add validation", "TBD", a function no task defines.
- **Too much:** full function bodies that the signature and test already determine. If the plan is several times longer than the spec, it has become the code — cut bodies back to signatures and assertions.

## Self-review before handing over

1. Every spec requirement maps to a task.
2. No step is vague; no step is a transcript of code.
3. Names and types match across tasks (`clearLayers` in task 3 is not `clearAllLayers` in task 7).
4. Each review-focus item has a test in some task.

Fix problems inline, then give the plan to the user to review before implementing.
