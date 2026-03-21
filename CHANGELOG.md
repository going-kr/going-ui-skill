# Changelog

Going Library NuGet 패키지 버전에 맞춰 스킬 버전을 관리합니다.
하나의 버전 안에서 여러 날에 걸쳐 작업이 진행될 수 있으므로, 각 항목은 날짜별로 기록합니다.
라이브러리가 다음 버전으로 올라가면 새 버전 섹션을 상단에 추가합니다.

---

## v1.1.2

Going Library NuGet latest 대응. 스킬 구조 리팩토링.

### 2026-03-21 — 평가 피드백 반영 (93/100 감점 5건 해소)
- **session-context.md 보강** — 세션 전환 판단 흐름 (판단 트리 + 채팅/Code 분기 테이블 + 현재 단계 체크리스트)
- **sample2 완전 구현** — .gud + MakeCode + C# 코드 전체 (SensorData/DeviceManager/DataManager/PageMain/PageHistory/SettingWindow)
- **comm-pattern.md 역할 경계 명시** — 상단에 "패턴은 여기, API 시그니처는 comm/*.md" 사용 흐름 추가
- **CustomTheme 색상 안내** — gud-structure.md에 SKColors + Util.FromArgb() C# 코드 예시 + 적용 방법
- **문서 간 연결성 보강** — 6개 핵심 문서에 "관련 문서" 테이블 추가 (gud-structure, code-pattern, image-to-gud, project-brief, deploy-cli, getting-started)
- **SKILL.md 미니 JSON 제거** — 607→427줄, 라우팅을 controls/*.md로 통일 (다양한 컨트롤 선택 유도)

### 2026-03-21 — 구조 변경
- **API HTML 21개 → controls/ 53개 MD + comm/ 6개 MD로 전환** — 모든 컨트롤에 JSON 템플릿 + 속성 테이블 + C# 코드 예제 + Events 섹션 완비
- **_common.md 신설** — GoControl 공통 속성/이벤트 + 데이터 클래스 8종(GoListItem, GoButtonItem, GoGraphSeries 등) JSON 형식 통합
- **comm/ 폴더 신설** — 통신 API 레퍼런스 6개 (modbus, mqtt, ls, mitsubishi, data-utils, tools)
- **SKILL.md 슬림화** — 607줄 → 427줄 (30% 감소). 미니 JSON 5종 제거, 라우팅을 controls/*.md로 통일
- **배치 파일 3개 제거** (release.bat, push.bat, sync-api.bat) — Claude가 직접 처리
- **gtcli.exe → tools/ 폴더로 이동**

### 2026-03-21 — 절대 규칙
- **#7 보강** — Agent 위임도 스크립트 사용에 해당하므로 금지. 대형 .gud 페이지 단위 분할 생성 가이드 추가
- **#8 신설** — 절차별 동의 후 진행. C# 코드는 일괄 진행 + 결과만 보고. 비프로그래머 고객 배려 (코딩 질문 부담 방지)

### 2026-03-21 — 워크플로우
- **image-to-gud.md 보강** — Claude Vision 한계 명시, 비율 기반 좌표 계산, 원본 레이아웃 보존 절대 원칙
- **Step 2 이미지 분기** — 이미지 있으면 image-to-gud.md 6단계 적용, 없으면 brief 기반 설계
- **DeviceData 패턴 강제** — 1대 슬레이브도 DeviceData 패턴 적용 권장

### 2026-03-21 — 문서 보강
- **getting-started.md** — DeviceData 패턴 적용, MasterTCP RemoteIP/RemotePort 수정
- **troubleshooting.md** — GoListItem 오류, GetWord null, 엔디안 불일치 3건 추가 (총 20개 증상)
- **comm/ 6개 파일에 간단 사용 예 추가**
- **컨테이너 8개 파일 Events 섹션 "없음" 명시**
- **project-brief.md** — sample/ 경로를 sample/sample1/, sample/sample2/로 수정

### 2026-03-21 — 평가
- **eval 31개 → 42개** — ImageCanvas 2종, DataGrid 2종, project_brief, .gud 부분 수정, 배포 등 추가
- **eval 카테고리 정리** — 9개 카테고리 (절대규칙, 프로젝트 시작, .gud 생성, 이미지→.gud, .gud 수정, C#, 통신, 배포, 트러블슈팅)
- **SlaveRTU eval 검증값 수정** — PortName→Port, BaudRate→Baudrate

### 2026-03-21 — 샘플
- **sample2 추가** — TemperatureMonitor (MasterTCP + 다중 페이지 + GoNavigator)

---

## v1.1.1 — 2026-03-20

Going Library NuGet 1.1.1 대응.

### 변경
- 패키지 버전 1.1.0 → 1.1.1 일괄 업데이트
- Getting Started 튜토리얼 추가 (모터 제어 예제)
- 단계 전환 안내 규칙 추가
- GoBarGraphMode 버그 수정, GoButtons 추가
- Enum/문서 전수 검증 보강
- 패키지 버전 하드코딩 제거 — NuGet 최신 버전 자동 사용

---

## v1.1.0 — 2026-03-18

초기 공개 릴리스.

### 변경
- README.md 추가 — GitHub 공개 배포 준비
- .gitignore 추가
- .vs/ IDE 캐시 제거
- Going.UI.Forms 참조 제거
- 전체 패키지 버전 1.1.0 통일

---

## v1.0.0 — 2026-03-18

최초 버전. 13개 MD + 21개 API HTML + 샘플 프로젝트 + gtcli 구성.
