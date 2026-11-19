---
name: questionnaire
description: Use when the user needs answers from someone else and asks for a questionnaire, 질의서, 의견조회서, or questions to send to a colleague, department, expert, or vendor.
---

# Questionnaire for someone who knows what you don't

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) `skills/productivity/to-questionnaire/SKILL.md`, MIT License, Copyright (c) 2026 Matt Pocock. Rewritten; Korean public-sector usage added.

The recipient holds knowledge the user lacks. The questions target that gap. Ask the user only about the sending, which they can always answer, not about the subject itself.

## Steps

1. **Recipient.** In one message ask: who receives it (role, department, expertise), their relationship to the user (상급기관, 협조부서, 외부 전문가, 업체 …), and whether it will be answered in writing or in a meeting. Done when you know what they know that the user doesn't, and what tone fits.
2. **What the user needs back.** In one message ask which decisions or facts the user can't settle alone, and the deadline. Done when there is a concrete list of things the user must be able to decide or do afterwards.
3. **Write the document** to `questionnaire-<topic>.md` (or the format the user asks for) and give the path. Done when every item from step 2 is covered by at least one question.

## Document layout

```
# <제목 / Title>

목적: why this exists and what decision depends on it.
보내는 사람 / 받는 사람 / 회신 기한 / 답변 활용처

## 배경
One paragraph — enough for someone who wasn't in the user's head to answer well.

## 답변 방법
Rough effort and deadline. "모름"이나 부분 답변도 도움이 되니 확실하지 않은 부분은 표시해 달라.

## <주제 1>
### 1. <one question>
_왜 묻는지: <only where the question could be misread or get a throwaway answer>_
> (답변)

## 그 밖에
우리가 묻지 않았지만 알아야 할 것이 있는지.
```

## Rules for questions

- Most important first; the recipient may answer only once or only partly.
- One idea per question. Split "A and B?" into two.
- Ask for facts, numbers, or choices they can give, not their opinion of the whole project. Offer options where a choice is needed, plus "기타".
- Group under headings once there are more than about six questions.
- For official correspondence (협조 요청, 의견조회 공문), keep the attachment in this format and let the cover letter carry the formal request; use `korean-doc-style` for the wording.
