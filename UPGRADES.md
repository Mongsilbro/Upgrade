# Upgrade log

One open-source adoption per day. Newest first.

| Date | Skill | Source | License | What it adds |
|------|-------|--------|---------|--------------|
| 2026-11-14 | [`vulnerability-triage`](.claude/skills/vulnerability-triage/SKILL.md) | [trailofbits/skills](https://github.com/trailofbits/skills) `plugins/vulnerability-triage-brocards` (after W. Woodruff, vulnbrocards.com) | CC BY-SA 4.0 (skill file carries the same license) | Seven tests for deciding whether a CVE, scanner alert, or security report is real: threat model, capability vs. impact, reachability, standard and documented behavior, proportionality, evidence over labels. |
| 2026-11-13 | [`systematic-debugging`](.claude/skills/systematic-debugging/SKILL.md) | [obra/superpowers](https://github.com/obra/superpowers) `skills/systematic-debugging` | MIT | Root-cause-first debugging: investigate → compare → single hypothesis → fix with a failing test; rethink the design after three failed fixes. |

## Candidates considered but not adopted

| Date | Source | Reason |
|------|--------|--------|
| 2026-11-14 | trailofbits/skills `plugins/insecure-defaults`, `plugins/sharp-edges` | Not evaluated in full: 130–150 KB each including large JS harnesses; too big to read completely in one daily run. May be revisited. |
