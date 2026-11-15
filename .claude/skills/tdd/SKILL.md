---
name: tdd
description: Use when building a feature or fixing a bug test-first, when the user mentions TDD or red-green-refactor, or when writing or reviewing tests and deciding what to test, where, and what to mock. Covers what makes a test worth keeping, test anti-patterns, and the rules of the red-green loop.
---

# Test-Driven Development

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) (`skills/engineering/tdd`, MIT, © 2026 Matt Pocock). Condensed and reworded; see `UPGRADES.md` for the adoption record.

## A good test

Checks behavior through the public interface and reads like a specification: "user can check out with a valid cart". The implementation can be rewritten entirely and the test still passes. Name tests for *what* the system does, not *how*.

## Where tests go

Test at **seams**: public boundaries where behavior can be observed without reaching inside. Before writing tests, list the seams you intend to test with a line each on what that catches and what it misses, and agree them with the user when the choice isn't obvious. Not everything can be tested; this puts the effort on critical paths and complex logic.

## Anti-patterns

- **Coupled to implementation.** Mocks internal collaborators, tests private methods, asserts on call counts or order, or verifies through a side channel (querying the database directly instead of reading back through the interface). Tell: a refactor with no behavior change breaks the test.
- **Tautological.** The expected value is computed the same way the code computes it (`expect(add(a, b)).toBe(a + b)`, or summing the same list in the test). It can never disagree with the code. Expected values come from an independent source: a literal, a worked example, the spec.
- **Horizontal slicing.** Writing all the tests first, then all the code. Bulk tests describe imagined behavior and lock in structure before anything is learned. Work in vertical slices instead: one test → make it pass → next test, each informed by the last.

## Mocking

Mock only at system boundaries: external APIs, time and randomness, sometimes the file system or database (prefer a real test database). Never mock your own modules or anything you control.

To make boundaries easy to replace:
- Pass external dependencies in as arguments rather than constructing them inside.
- Wrap each external operation in its own function (`getUser`, `createOrder`) rather than one generic fetcher, so each fake returns a single shape with no branching.

## Rules of the loop

1. **Red before green.** Write the failing test and watch it fail for the right reason. Then write only enough code to pass it — no speculative features.
2. **One slice per cycle.** One seam, one test, one minimal change.
3. **Refactor separately.** Clean up once tests are green, as its own step, not mixed into making a test pass.
