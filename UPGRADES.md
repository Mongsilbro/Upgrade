# Upgrade log

One open-source adoption per day. Newest first.

| Date | Skill | Source | License | What it adds |
|------|-------|--------|---------|--------------|
| 2026-11-14 | [`delegate-free-ai`](.claude/skills/delegate-free-ai/SKILL.md) | Original (user request); calls the [OpenRouter](https://openrouter.ai) API | — | Hand self-contained, low-stakes sub-tasks (drafts, translation, summaries, boilerplate) to free models during work; results verified before use. |
| 2026-11-14 | [`second-opinion`](.claude/skills/second-opinion/SKILL.md) | Original (user request); calls the [OpenRouter](https://openrouter.ai) API | — | Ask free models on OpenRouter to cross-check a conclusion; free-only, no sensitive content, replies verified before use. |
| 2026-11-14 | [`grilling`](.claude/skills/grilling/SKILL.md) | [mattpocock/skills](https://github.com/mattpocock/skills) `skills/productivity/grilling` (★324k) | MIT | Stress-test a plan by interview: treat it as a decision tree, ask every currently answerable question per round with a recommended answer, look up facts yourself, stop only when nothing is assumed. |
| 2026-11-14 | [`vulnerability-triage`](.claude/skills/vulnerability-triage/SKILL.md) | [trailofbits/skills](https://github.com/trailofbits/skills) `plugins/vulnerability-triage-brocards` (after W. Woodruff, vulnbrocards.com) | CC BY-SA 4.0 (skill file carries the same license) | Seven tests for deciding whether a CVE, scanner alert, or security report is real: threat model, capability vs. impact, reachability, standard and documented behavior, proportionality, evidence over labels. |
| 2026-11-13 | [`systematic-debugging`](.claude/skills/systematic-debugging/SKILL.md) | [obra/superpowers](https://github.com/obra/superpowers) `skills/systematic-debugging` | MIT | Root-cause-first debugging: investigate → compare → single hypothesis → fix with a failing test; rethink the design after three failed fixes. |

## Candidates considered but not adopted

| Date | Source | Reason |
|------|--------|--------|
| 2026-11-14 | trailofbits/skills `plugins/insecure-defaults`, `plugins/sharp-edges` | Not evaluated in full: 130–150 KB each including large JS harnesses; too big to read completely in one daily run. May be revisited. |
| 2026-11-14 | multica-ai/andrej-karpathy-skills (★233k), anthropics/skills (★194k) | GitHub reports no license. |
