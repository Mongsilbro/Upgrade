---
name: architecture-decision-records
description: Use when recording a decision or ADR, choosing between technical alternatives, or asked why code is built a certain way.
---

# Architecture Decision Records

Adapted from [affaan-m/ECC](https://github.com/affaan-m/ECC) (`skills/architecture-decision-records`, MIT, © 2026 Affaan Mustafa). Condensed and reworded; see `UPGRADES.md`.

An ADR records one significant decision: the situation, what was chosen, what was rejected and why, and what it costs. Readable in two minutes.

## When

- **Write one** when the user asks, or **offer** one (don't create it unprompted) when a conversation reaches a real decision between alternatives: technology, architecture pattern, API design, data model, infrastructure, security approach, testing strategy, process.
- **Not** for trivial choices like naming or formatting.
- **Read existing ones** when asked "why did we choose X?": check `docs/adr/README.md`, open the matching ADR, and summarize its context and decision. If none exists, say so and offer to record it.

## Format

```markdown
# ADR-NNNN: <decision title>

Date: YYYY-MM-DD (for a past decision, the original date, marked "recorded later")
Status: proposed | accepted | deprecated | superseded by ADR-NNNN
Deciders: <who>

## Context
<2–5 sentences: the problem, constraints, forces>

## Decision
<1–3 sentences, present tense: "We use X">

## Alternatives considered
- **<option>** — pros / cons / why not

## Consequences
- Positive: …
- Negative: …
- Risks and mitigations: …
```

## Steps

1. If `docs/adr/` doesn't exist, ask before creating it (with a `README.md` index).
2. Draft the ADR — be specific ("Use Prisma", not "use an ORM"), include rejected alternatives, state trade-offs honestly.
3. Number it one higher than the highest existing ADR.
4. Show the draft; write `docs/adr/NNNN-<slug>.md` only after the user approves.
5. Add a row to the index: `| [NNNN](NNNN-slug.md) | Title | Status | Date |`.
6. When a decision is replaced, mark the old ADR "superseded by ADR-NNNN" and link it.

If the project already keeps decisions somewhere else, use that location and format instead.
