---
name: codebase-onboarding
description: Use when the user asks to understand, explore, or be walked through an unfamiliar repository, or asks to create or update a CLAUDE.md for a project. Surveys stack, structure, entry points, data flow, and conventions efficiently, then writes a short onboarding guide and/or CLAUDE.md.
---

# Codebase Onboarding

Adapted from [affaan-m/ECC](https://github.com/affaan-m/ECC) (`skills/codebase-onboarding`, MIT, © 2026 Affaan Mustafa). Condensed and reworded; see `UPGRADES.md`.

## 1. Survey (search, don't read everything)

In parallel where possible:
- **Manifests:** `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `pom.xml`, `Gemfile`, …
- **Framework and tooling config:** build, lint, format, type-check, Docker, CI workflows, `.env.example`.
- **Entry points:** `main.*`, `index.*`, `app.*`, `server.*`, `cmd/`.
- **Layout:** top two directory levels, skipping dependencies and build output.
- **Tests:** test directories, file naming, test runner config.
- **Git:** recent commit and branch naming — skip if history is empty or shallow, and say so.

Open files only where a signal is ambiguous. If config and code disagree, trust the code.

## 2. Map

- Stack: languages and versions, frameworks, database and ORM, build tool, CI.
- Shape: monolith / monorepo / services; API style.
- What each top-level directory is for (skip the obvious).
- One request traced end to end: entry → validation → business logic → storage → response.
- Conventions: naming, error handling, dependency wiring, async style, test patterns.

## 3. Produce what was asked

**Onboarding guide** (in the reply unless the user wants a file), scannable in two minutes: overview, stack table, architecture, key entry points, request lifecycle, conventions, common commands (dev, test, lint, build, migrate), and a "to do X, look at Y" table.

**CLAUDE.md**: under about 100 lines — stack, exact commands, structure pointers, conventions that change how code is written. If one exists, read it first, keep everything project-specific, and tell the user what was added or changed.

## Rules

- Say "couldn't determine X" rather than guessing.
- Don't list every dependency — only those that shape how code is written.
- Don't restate the README; add the structural insight it lacks.
