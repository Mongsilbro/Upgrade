---
name: teach
description: Use when the user asks to be taught or to learn a topic or skill over several sessions (e.g. "teach me X", "X 공부하고 싶어", "X 가르쳐 줘") — not for a one-off explanation. Sets up a learning workspace with the learner's goal, trusted sources, short lessons with retrieval practice, and records of what they have actually learned.
---

# Teach

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) `skills/productivity/teach/` (`SKILL.md`, `MISSION-FORMAT.md`, `RESOURCES-FORMAT.md`, `GLOSSARY-FORMAT.md`, `LEARNING-RECORD-FORMAT.md`), MIT License, Copyright (c) 2026 Matt Pocock. Rewritten and condensed.

Learning spans sessions, so its state lives in files in the current directory. Read them at the start of every session.

## Workspace files

| File | Holds |
|------|-------|
| `MISSION.md` | Why the learner wants this: concrete goal, "success looks like" (observable abilities), constraints, out of scope. Under one screen. |
| `RESOURCES.md` | Trusted sources, each with one line on what it covers and when to use it. Split into **Knowledge** (books, official docs, papers, 공공기관 자료) and **Wisdom** (communities, classes, practitioners). A `## Gaps` section for areas with no good source yet. |
| `GLOSSARY.md` | The workspace's terms: one- or two-sentence definitions, a preferred term with aliases to avoid. Add a term only once the learner uses it correctly. |
| `learning-records/NNNN-slug.md` | One short paragraph each: something the learner has shown they understand, prior knowledge they stated, a misconception corrected, or a change in goal. Not a session log. Mark replaced records `Status: superseded by NNNN`. |
| `lessons/NNNN-slug.html` | One lesson per file. |
| `reference/` | Cheat sheets distilled from lessons, for later lookup. |
| `NOTES.md` | The learner's stated preferences about how to be taught. |

Create files when first needed. Ask before changing the mission.

## Each session

1. **Mission first.** If `MISSION.md` is missing or vague, interview the learner until the goal is concrete ("pass 정보처리기사 필기 in March", not "learn IT"). Done when "success looks like" lists observable abilities.
2. **Sources before teaching.** Until `RESOURCES.md` has solid entries for the next topic, find them (primary and official sources first; no marketing). Cite them inside lessons rather than relying on memory.
3. **Pick the next lesson** from the mission and the learning records: the most useful thing just beyond what the learner has shown they can do. If they name a topic, teach that.
4. **Write one short lesson**: one concrete win, completable in minutes, tied to the mission.
   - Teach only the knowledge the skill needs, as plainly as possible.
   - Then practise with immediate feedback: quizzes (answer options of equal length, correct position varied, no formatting hints) or real-world steps to try.
   - Use retrieval (recall without looking), spacing (revisit earlier lessons' material), and, for skills, interleaving related problem types. Feeling fluent right after reading is not retention.
   - Link one best source to read or watch, related lessons and reference sheets, and remind the learner they can ask follow-up questions.
   - Reuse a shared stylesheet in `assets/` so lessons look like one course.
5. **Record evidence.** After the learner answers or practises, write a learning record only for demonstrated understanding, stated prior knowledge, a corrected misconception, or a goal change. Update the glossary for terms they now use correctly.
6. For questions that need practical judgement, give your best answer and point to a community or practitioner from `RESOURCES.md`, unless the learner declined communities (note that in `RESOURCES.md`).
