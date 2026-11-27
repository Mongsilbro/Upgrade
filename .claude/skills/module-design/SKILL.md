---
name: module-design
description: Use when designing a module's interface, adding an abstraction layer or wrapper, or placing a seam.
---

# Module design

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) (`skills/engineering/codebase-design/SKILL.md`, `DEEPENING.md`, `DESIGN-IT-TWICE.md`; MIT, © 2026 Matt Pocock), after Ousterhout's *A Philosophy of Software Design* and Feathers' seams. Condensed and reworded; parallel sub-agents replaced by in-line sketches. See `UPGRADES.md`.

Goal: **deep modules**, much behaviour behind a small interface. A module is anything with an interface (function, class, package). Its **interface** is everything a caller must know: types, but also invariants, call order, error modes, config, performance. A **seam** is where that interface sits; an **adapter** is something plugged in at a seam.

## Steps

1. **Sketch two or three radically different interfaces** before writing code, each under a different constraint: (a) fewest entry points, (b) the common caller's case is one call, (c) dependencies behind ports. For each: signature, one usage example, what it hides. Recommend one (or a hybrid) and say why, by depth, where future changes land, and seam placement. Don't present a menu without a pick.
2. **Deletion test** for every module, wrapper, or layer you propose or touch: if it were deleted, would complexity vanish (it was a pass-through: drop or merge it) or reappear in several callers (it earns its place)? Write the answer in one line.
3. **No single-adapter seams.** Add an interface/port only when at least two adapters exist now (typically production + test fake). One adapter is indirection; inline it.
4. **Classify each dependency** and test accordingly:
   - in-process (pure logic, memory): merge freely, test through the interface directly;
   - local stand-in exists (SQLite/PGLite, in-memory FS): use the stand-in in tests, no port;
   - own remote service: port at the seam, HTTP adapter in production, in-memory adapter in tests;
   - third-party service: injected port, mock adapter in tests.
5. **Replace, don't layer, tests.** After merging shallow modules, write tests at the new interface and delete the old per-piece tests. Internal seams used by the module's own tests stay out of its public interface.

## Done when

The design note or answer contains: the alternatives considered with the pick, a deletion-test line per new module/layer, and each new seam with its two adapters named. Writing tests across these seams: `tdd`. Recording the choice: `architecture-decision-records`.
