---
name: running-summary
description: Use in every coding session. At the start, if the repository has a CONTEXT.md, read it before anything else and continue from it instead of asking the user to repeat context. After finishing each task the user asked for, update it. Standing user instruction (2026-11-18) to keep chats short and cheap.
---

# Running Summary

Original to this repository. The user prefers short chats that restart from a summary over one long chat (cheaper on usage).

## At the start of a session

- If `CONTEXT.md` exists at the repository root, read it first and work from it.
- Don't re-read files or history it already summarizes unless the task needs the detail.

## After each finished task

Update `CONTEXT.md` (create it if missing — in a repository other than this one, ask once before adding the file):

```
# 작업 요약 (CONTEXT)
## 목표            — what the user is ultimately after
## 사용자 결정사항  — choices and rules the user set, so they are never re-asked
## 현재 상태        — what exists and works now, with dates; pointers to files instead of copies
## 다음 할 일 / 열린 질문
```

- Overwrite stale lines; don't append a diary. Under 80 lines.
- Write it in the user's language (Korean for this user).
- No secrets, tokens, or personal data.
- Commit it with the task's other changes when the task is committed.

## When the chat gets long

After a large task, or when the conversation has grown long, update `CONTEXT.md` and suggest in one line that the user continue in a new chat ("CONTEXT.md 읽고 이어서 해줘") or run `/compact`. Don't repeat the suggestion every turn.
