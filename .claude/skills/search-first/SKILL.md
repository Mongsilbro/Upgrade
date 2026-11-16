---
name: search-first
description: Use before writing a new utility, helper, abstraction, or integration, or when adding a dependency — check whether the repository, the package registry, or an existing tool already solves it, then decide to adopt, extend, compose, or build. Not for small one-off logic that is quicker to write than to look up.
---

# Search First

Adapted from [affaan-m/ECC](https://github.com/affaan-m/ECC) (`skills/search-first`, MIT, © 2026 Affaan Mustafa). Condensed and reworded; see `UPGRADES.md` for the adoption record.

Before writing code for a common problem, find out whether it already exists.

## 1. State the need

One or two sentences: what it must do, plus language, framework, runtime, and license constraints.

## 2. Search, nearest first

1. **This repository.** Grep the relevant modules and tests; the helper may already be there under another name.
2. **Dependencies already installed.** The framework or a current dependency often covers it.
3. **The standard library.**
4. **The package registry** (npm, PyPI, crates.io, …).
5. **Tools already connected to the session** — skills, MCP servers, CLIs.
6. **GitHub and the web** for maintained implementations or reference patterns.

Stop as soon as a good answer appears. If a channel isn't available (no network, no registry access), say which one was skipped — never report "nothing found" for a search that didn't run.

## 3. Evaluate candidates

Check: covers the need, maintained recently, widely used, documented, license compatible, small dependency footprint. For a new dependency also confirm the exact package name and publisher (typosquats exist) and prefer what the project's ecosystem already standardizes on.

## 4. Decide

| Finding | Action |
|---------|--------|
| Exact fit, maintained, compatible license | **Adopt** — use it directly |
| Partial fit, solid base | **Extend** — thin wrapper over it |
| Several small pieces each cover part | **Compose** — combine two or three |
| Nothing suitable | **Build** — custom code, informed by what was found |

Adding a new third-party dependency changes the project's supply chain: name the package and why, and get the user's agreement before installing unless they already asked for it.

## 5. Report

One or two lines in the summary: what was searched, what was chosen, and why. Example: "Dead-link checking: found an existing textlint rule — adopted, no custom code."

## Avoid

- Writing a utility without looking.
- Wrapping a library so heavily its benefits disappear.
- Pulling in a large package for one small function.
- Spending longer searching than the code would take to write and test.
