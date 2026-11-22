---
name: no-test-gaming
description: Use when making failing tests or checks pass, especially when a test seems to contradict the task or keeps failing after several tries. Test-first work: `tdd`.
---

<!-- Source: Zhong, Raghunathan, Carlini, "ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases", 2025, arXiv:2510.20270. Ideas only, no text reused. -->

# No test gaming

The goal is code that meets the specification. A green test run is evidence of that, not the goal itself. Coding models, Claude among them, often turn a failing test green by editing the test instead of fixing the code, and that habit gets stronger when the prompt is loose and the model gets many retries.

## Rules

1. **Treat tests as read-only by default.** Change a test only when the user asked for it, or when you can name the line of the spec or the user's request that shows the test is wrong. Never weaken an assertion, delete or skip a test, widen a tolerance, or change an expected value just to get a pass.
2. **Do not write code that only works for the tests.** No branches on test inputs or test names, no hard-coded expected outputs, no checks for whether a test runner is active, no comparison operators (`__eq__`, `equals`) overridden so that anything matches, no hidden state used to return different answers on repeated calls.
3. **When the spec and a test disagree, stop and report.** Quote the spec line and the assertion, say which one you think is right and why, and ask which to follow. Do not pick one quietly. "This task can't be done as stated" is an acceptable answer.
4. **After three failed attempts on the same test, step back.** Re-read the spec and the test before trying again. More retries make gaming more likely, not less. If the conflict is still there, go to rule 3.

## Before saying it passes

Read your own diff and check:

- [ ] Files under test directories, fixtures, snapshots, and CI config: list every change with its reason, or say there are none.
- [ ] Production code: no literal that matches an expected value from a test, and no reference to test names, test data, or the test environment.
- [ ] No skip, xfail, `.only`, commented-out assertion, or raised timeout or tolerance added by you.

In the report, put test changes in their own line ("Tests changed: …" or "Tests changed: none"), separate from code changes. Then follow `verification-before-completion` for the run itself.
