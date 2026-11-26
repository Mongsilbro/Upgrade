# 작업 요약 (CONTEXT)

새 대화나 /compact 뒤에는 이 파일만 읽고 이어서 작업한다. 작업이 하나 끝날 때마다 갱신한다(덮어써서 짧게 유지, 80줄 이내).

## 목표
- GitHub 오픈소스에서 쓸 만한 기법을 골라 Claude 스킬로 옮겨 `.claude/skills/`에 쌓는다. 다른 Claude Code 세션에서도 이 저장소를 연결해 쓴다.
- 사용자: 대한민국 공무원. 공무원 업무(보고서·공문·법령 인용)에 도움 되는 스킬 우선.

## 사용자 결정사항
- 후보는 별(star) 많은 저장소부터. 라이선스 없으면 제외. 스크립트·바이너리는 가져오지 않고 제 말로 재작성.
- 작업 중 적합한 하위 작업은 무료 OpenRouter 모델에 위임(`delegate-free-ai`). 키는 환경의 network secret(openrouter.ai), 무료 하루 50회.
- 사용량 절약: 매일 예약 작업은 실행마다 새 세션(trig_01Qmry1r55NMpc9gSLzgzZQt, 매일 01:17 UTC = 10:17 KST). 이 대화에 묶인 예전 작업(trig_016P5TtbS3BADtyyAeEPDvFd)은 꺼 둠(삭제 안 함).
- 예약 작업에 커넥터 연결 안 함(필요 없음, 위험만 늘어남).
- 모든 코드 채팅방: 작업마다 CONTEXT.md 갱신, 새 채팅은 이것만 읽고 시작(`running-summary` 스킬). 다른 저장소에는 처음 한 번 묻고 CONTEXT.md 생성.
- 후보 범위: AI 에이전트 스킬뿐 아니라 별 많은 일반 가이드·체크리스트(리뷰, 보안, 문서 작성, 공공 업무)도 포함.
- 검토 시 이미 읽은 원본의 번역본(README-xx.md)은 링크·지시성 문구만 검사(11-19 결정).
- 11-21 채팅용 zip 5개(gov-report, korean-doc-style, korean-law-citation, grounded-answers, hold-position) 전달. 채팅 업로드는 사용자가 직접(Customize → Skills), 설명 200자 이하 필요.
- 논문·공식 글(Anthropic 문서, arXiv)도 후보: 아이디어만 가져와 새로 쓰고 출처 표기, 라이선스 불요(11-21 CLAUDE.md 반영). 새 저장소는 만들지 않음.
- 정부 공개 자료도 후보: 공공누리 1·2유형만(3·4유형·표시 없음 제외), 기관·제목·연도·유형 표기.
- 더 나은 방향이 있으면 항상 짧게 제안(매일 보고 끝에도 한 줄). 11-20: 사용자가 제시한 방법도 그대로 하지 말고 대안과 비교해 더 나은 안을 먼저 제시.
- 브랜치: `claude/daily-opensource-learning-5d8y9d` (저장소 기본 브랜치). PR 만들지 않음.

## 현재 상태 (2026-11-26)
- 11-26 예약 실행: `dated-facts` 추가(시점 민감 사실 논문 3편; 현직자·최신 버전·현행 금액 등은 날짜 출처 확인 또는 "YYYY년 기준" 표시, `시점 확인` 보고). 설명 4개 축약해 합계 4,189자. 스킬 39개.
- 11-25 예약 실행: `pairwise-judging` 추가(LLM-as-judge 위치·길이·자기선호 편향 논문 3편; 초안 A/B 비교 시 기준 먼저, 기준별 인용 근거, 순서 바꿔 재확인, `판정: A/B/우열 없음`). 설명 5개 축약해 합계 4,172자. 스킬 38개.
- 11-24 예약 실행: `constraint-checklist` 추가(Curse of Instructions·IFScale·IFEval 논문, 요청 하나에 제약이 많을 때 목록화→항목별 검사→`제약 N개 중 N개 충족` 보고). 스킬 37개, 설명 합계 4,174자(한도 4,200 근접 → 다음 월요일 점검 때 축소 필요).
- 11-23(월) 점검: `commit-message`, `codebase-onboarding` 제거(X→Y 실패: 기본 동작·`/init`이 대신함), 설명 합계 약 4,050자로 축소, YAML 오류 3건 수정. 같은 날 `compute-with-code` 추가(PAL·PoT·Faith and Fate 논문, 파생 수치는 코드로 계산). 스킬 36개.
- 11-23 사용자 승인: `scripts/check-skills.py`(YAML·name·설명 200자·합계 4,200자 검사)를 만들고 CLAUDE.md 6단계에 커밋 전 실행으로 넣음.
- 이전: 스킬 36개(11-22 예약 실행: `no-test-gaming` 추가(ImpossibleBench 논문, 테스트 고쳐서 통과시키기 방지). 11-21 사용자 요청으로 논문·공식 문서 기반 `grounded-answers`(긴 문서 원문 인용 근거 답변), `hold-position`(근거 없는 반박에 답 바꾸지 않기) 추가. 같은 날 `source-driven` 라이브러리 버전·공식 문서 근거 코드 추가; addyosmani/agent-skills ★119k MIT, 다른 스킬은 아직 미검토). 목록과 출처는 `UPGRADES.md`.
- 11-19 스킬 설명(description) 전체 정리: 9,956자 → 3,791자(매 대화 상시 비용 절감). 매주 월요일 예약 실행 때 설명 길이·중복 점검(CLAUDE.md 9단계).
- 공무원용: `gov-report`, `korean-doc-style`, `korean-law-citation`, `questionnaire`(질의서·의견조회서).
- 한계: 국가법령정보센터 본문은 여기서 직접 못 읽음(JS 로딩, Open API는 고정 IP 필요). HWP/HWPX는 세션에 설치된 플러그인(hwpx, kordoc)으로 처리.

## 다음 할 일 / 열린 질문
- 11-20 결정: 채택 기준을 "없으면 X, 있으면 Y" 한 문장으로 검증, 못 적으면 탈락. 건너뛰는 날이 정상. 예약 작업 문구 수정은 사용자가 직접(문구 전달함).
- 사용자가 사용량을 보고 추가 스킬 개수를 정하면 진행.
