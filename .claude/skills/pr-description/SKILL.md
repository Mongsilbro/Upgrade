---
name: pr-description
description: Use when writing or rewriting a pull request description.
---

# PR Description

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) (`skills/engineering/pr`, MIT, © 2026 Matt Pocock), whose summary guidance credits Dex Horthy's `show-me` skill ([humanlayer](https://github.com/humanlayer)). Reworded; see `UPGRADES.md`.

If the repository has a PR template, fill in its headings instead and use the guidance below inside them.

## Template

```markdown
## Summary
<one visual + a sentence or two>

## Evidence
- **Before:** <failing test / output / screenshot>
- **After:** <passing test / output / screenshot>

## Merge risk
**Reversibility:** one-way or two-way door
**Blast radius:** <one word> — <what could break, for whom>
```

No preamble. Use the project's own vocabulary.

## Summary: pick the smallest view that makes the point

| The change is about | Show |
|---------------------|------|
| Logic or an algorithm | Pseudocode |
| Runtime control flow | Call tree (indented function names) |
| UI structure | Component tree, with the state and module boundaries that matter |
| File responsibilities or a broad refactor | Shallow file tree with a comment per entry |
| Interaction between parts | Mermaid sequence or flow diagram |
| What changed in an existing shape | A `diff` block of any of the above (`+`/`-` lines) |
| Mostly new code, or a target shape to copy | The full block |

Usually one view, occasionally two. Put each next to the sentence it supports and keep only the parts needed to understand the change.

## Evidence

Concrete proof the change works, before and after. Best: a screenshot when the change is visual and screenshots are possible. Next: test or command output — name the test that failed before and passes now. Only include evidence that was actually produced.

## Merge risk

- **Two-way door:** easy to revert. **One-way door:** hard or impossible to undo — data migrations, deletions, published APIs, external side effects.
- **Blast radius:** who and what could be affected — consumers of an API, layout on mobile, other services, performance. Think through the possibilities rather than defaulting to "low".
