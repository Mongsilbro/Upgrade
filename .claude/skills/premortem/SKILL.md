---
name: premortem
description: "Use for a premortem of a plan or policy about to be committed. Unformed ideas: `grilling`; code: `change-impact`."
---

# Premortem

Adapted from [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) `skills/premortem-assassin/SKILL.md` (MIT, © 2026 Mohit Aggarwal). Rewritten and condensed; public-sector failure modes added.

A postmortem explains a failure after it happens. A premortem assumes the plan is already dead a year from now and asks how it died. Running every plan through the same fixed list of failure modes stops the team's shared blind spot from hiding itself.

## Inputs

- **The plan itself** (the document, not a summary). Attack what it says, and treat what it leaves out as evidence.
- **What success means**, with a number and a date. If the plan has none, say so first: a plan that cannot visibly fail cannot be managed, and that is the first finding.
- Optional: known limits (budget, staff, deadline) and who is lukewarm or opposed.

If the plan isn't written down yet, ask for it or offer `grilling` first; don't premortem a guess.

## The twelve failure modes

Check every one against this plan's specifics and give each a verdict: **likely fatal**, **damaging**, or **survives**.

1. **Overpromised dependency.** Another team, vendor, agency, or system said yes too easily.
2. **Compounding estimate.** One task slips and drags everything after it.
3. **Silent stakeholder.** Someone who approved it without commitment and withdraws support midway.
4. **Imagined demand.** Interest, need, or uptake that was politeness or assumption, not evidence.
5. **Key person.** One resignation, transfer, or sick leave away from collapse (in government: the routine rotation of the person in charge).
6. **Integration cliff.** Each part works; the whole doesn't.
7. **Legal or procedural tripwire.** A law, regulation, budget rule, procurement step, approval, or consultation nobody checked.
8. **Incentive misfire.** The plan asks people to act against how they are measured or rewarded.
9. **Cheap counter-move.** A competitor's response, public backlash, media story, or rule change that cancels months of work.
10. **Success catastrophe.** It works, and the load, cost, complaints, or support burden then sinks it.
11. **Narrative collapse.** One bad week and leadership or the public stops believing in it.
12. **Zombie outcome.** It neither fails nor succeeds and keeps consuming people and budget. The most common death and the least planned for; never skip it.

## Output

1. **Obituary** (under 150 words): one year on, the plan is dead; a sober summary of how, written like a real postmortem, not satire.
2. **Attack table**: failure mode | verdict | the concrete mechanism in this plan, quoting the plan where possible, or naming what it omits.
3. **Three most likely causes of death**, no more. For each: the earliest visible symptom, the point (week or milestone) after which it can no longer be reversed, and the cheapest way to prevent it now.
4. **Tripwires**: 3–5 observable, dated checks someone can put in a calendar today, e.g. "If the vendor contract is not signed by 15 March, mode 1 is live."

## Rules

- Be specific to this plan. A line that could apply to any project is boilerplate; replace it or drop it.
- Verdicts must be honest. If nearly every mode comes out fatal, the attack was theatrical; recheck and mark what genuinely survives.
- Don't soften the top three into "considerations", and don't rank a dozen risks equally; an unranked risk list is where warnings go to be ignored.
- Don't invent facts about the plan. Mark assumptions as assumptions, and absences as absences.
- Route every mechanism through structure, incentives, or process, never "person X is incompetent".
- Write in the language of the plan. For a Korean public-sector plan, keep the output in Korean and follow `korean-doc-style`; if the tripwires should go back into the plan, suggest adding them to its 세부 추진계획 (`gov-report`).
