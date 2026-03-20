---
name: going-ui
description: "Going Library skill for industrial HMI/SCADA development. Use when: (1) generating/editing .gud UI design files (GoDesign/GoPage/GoWindow JSON), (2) writing C# code for Going.UI controls (GoButton, GoLamp, GoInput, GoDataGrid) with event binding and OnUpdate data sync, (3) implementing Modbus RTU/TCP, MQTT, LS CNet, Mitsubishi MC PLC communication via Going.Basis, (4) deploying to LauncherTouch devices via MCP/gtcli. Trigger keywords: Going, GoButton, GoLamp, GoSlider, GoInput, GoValue, GoDesign, .gud, Modbus, MasterRTU, SlaveRTU, MasterTCP, SlaveTCP, MQTT, MQClient, HMI, SCADA, PLC, LauncherTouch, gtcli, Going.UI, Going.Basis, Going.UI.OpenTK, OnUpdate, Designer.cs, design.json, project_brief. File patterns: *.gud, *.Designer.cs, csproj referencing Going.UI/Going.Basis."
---

# Going Library Skill

Going Library는 산업용 HMI/SCADA 화면을 만들기 위한 C# .NET 8.0 UI 프레임워크. SkiaSharp 기반 커스텀 렌더링으로 GoButton, GoLamp, GoDataGrid 등 40여 종의 산업용 컨트롤을 제공하며, Going.Basis로 Modbus RTU/TCP, LS Electric CNet, Mitsubishi MC, MQTT 통신을 지원한다. 주 타겟은 라즈베리파이(linux-arm64) 터치패널이며 Windows에서도 동작한다.

| 패키지 | 버전 |
|--------|------|
| Going.Basis | 1.1.1 |
| Going.UI | 1.1.1 |
| Going.UI.OpenTK | 1.1.1 |

> 스킬 최종 갱신: 2026-03-20

---

## 작업별 참조 파일

| 작업 | 참조 파일 | 설명 |
|------|----------|------|
| .gud 빠른 생성 (1파일) | `ui-json-quick.md` | .gud 전체 구조 + 전 컨트롤 속성 압축본. **이 파일만으로 .gud 생성 가능** |
| 이미지 → .gud 변환 절차 | `ui-image-to-gud.md` | HMI 캡처/스케치 이미지를 .gud로 변환하는 6단계 절차 (인벤토리→그루핑→컨테이너→도식→검증→생성) |
| .gud 파일 상세 참조 | `ui-json.md` | .gud 구조, GoDesign, Pages/Windows, 공통 속성, Enum, 테마 |
| ↳ 기본 컨트롤 JSON | `ui-json-controls.md` | GoLabel, GoButton, GoLamp, GoSlider, GoButtons 등 기본 15종 |
| ↳ 확장 컨트롤 JSON | `ui-json-controls-ext.md` | GoDataGrid, GoGauge, GoBarGraph, GoNavigator 등 확장 19종 |
| ↳ GoInput/GoValue JSON | `ui-json-input-value.md` | GoInputString, GoInputNumber 등 입력 7종 + GoValue 표시 3종 |
| ↳ 컨테이너 JSON | `ui-json-containers.md` | GoTableLayoutPanel, GoBoxPanel, GoTabControl 등 9종 |
| ↳ ImageCanvas JSON | `ui-json-imagecanvas.md` | IcButton, IcLabel, IcSlider 등 이미지 기반 7종 |
| C# 코드 작성 (Page/Window/Main) | `ui-code.md` | 코드 패턴, Designer.cs 규칙, MakePropCode |
| ↳ 복잡한 컨트롤 C# 코드 | `ui-control-sample.md` | GoBarGraph, GoLineGraph, GoTimeGraph, GoTrendGraph, GoGauge, GoMeter, GoKnob, GoSwitchPanel, GoButtons, GoDataGrid의 C# 바인딩·시리즈 설정·데이터 업데이트 예제. **로드 조건: 위 컨트롤 중 하나라도 C# 코드에서 다룰 때 읽을 것** |
| 통신 코드 작성 (Modbus/MQTT) | `basis.md` | 통신 패턴, DeviceManager, 데이터 모델 |
| 장치 배포/제어 (LauncherTouch MCP) | `ui-mcp.md` | gtcli CLI 도구, MCP 도구 25개, 빌드-배포 자동화, 네트워크, 키오스크 |
| project_brief.md 작성 가이드 | `ui-project-brief.md` | 템플릿, 이미지 네이밍, 섹션별 작성법 |
| 트러블슈팅 (빌드/통신/런타임/배포) | `troubleshooting.md` | 증상별 원인·해결 테이블 (에러 발생 시 참조) |
| 세션 간 컨텍스트 유지 | `session-context.md` | project_status.md 템플릿, 유지 규칙 (Claude Code 전용) |
| Getting Started (튜토리얼) | `getting-start.md` | 모터 제어 패널 예제로 브리프→.gud→MakeCode→C#→빌드 전체 과정 안내 |

**작업 시작 전 해당 파일을 반드시 `Read` 도구로 읽은 후 작업할 것.**

### 로드 순서 가이드

작업 유형에 따라 아래 순서로 파일을 읽는다. **SKILL.md는 항상 먼저 로드됨** (진입점).

| 작업 | 1순위 | 2순위 | 3순위 (필요 시) |
|------|-------|-------|----------------|
| .gud 파일 생성 | `ui-json-quick.md` (이것만) | 상세 확인 필요 시: `ui-json.md` / `ui-json-controls.md` 등 개별 파일 | — |
| C# 코드 작성 | `ui-code.md` | `basis.md` (통신 있을 때) | `ui-control-sample.md` (복잡한 컨트롤) |
| 통신만 구현 | `basis.md` | — | — |
| 장치 배포 | `ui-mcp.md` | — | — |
| 프로젝트 시작 | `ui-project-brief.md` | `ui-json.md` | `ui-code.md` |
| 처음 사용 (튜토리얼) | `getting-start.md` | — | — |
| 에러 해결 | `troubleshooting.md` | — | — |
| 세션 이어받기 | `session-context.md` | — | — |

> 모든 파일을 한꺼번에 로드하지 말 것. 작업에 필요한 파일만 순서대로 읽어 컨텍스트를 절약한다.

---

## API 문서 참조 방법

Going Library의 클래스·속성·메서드·이벤트 확인이 필요할 때는 `Read` 도구로 아래 HTML 파일을 직접 읽어 확인한다.
**코드 작성 전 반드시 해당 파일을 확인하고 정확한 속성명·타입·기본값을 사용할 것.**

> **경로 규칙**: 아래 경로는 **이 스킬 파일(.md) 기준 상대경로**. `Read` 도구 사용 시 이 스킬 파일이 위치한 디렉터리를 기준으로 경로를 해석할 것.

### Going.UI

| 경로 (스킬 파일 기준 상대경로) | 내용 |
|------|------|
| `api/ui/design.html` | GoDesign, GoPage, GoWindow, GoTitleBar, GoSideBar, GoFooter |
| `api/ui/controls.html` | 전체 컨트롤 (GoButton, GoLabel, GoInput*, GoValue*, GoDataGrid, GoSlider, GoKnob, GoStep, GoProgress 등 40여 종) |
| `api/ui/containers.html` | GoBoxPanel, GoPanel, GoGroupBox, GoScrollablePanel, GoScalePanel, GoTabControl, GoTableLayoutPanel, GoGridLayoutPanel, GoSwitchPanel |
| `api/ui/dialogs.html` | GoDialogs, GoMessageBox, GoInputBox, GoSelectorBox |
| `api/ui/themes.html` | GoTheme, 색상 팔레트, ToColor() |
| `api/ui/collections.html` | ObservableList\<T\> |
| `api/ui/datas.html` | GoListItem, GoPadding, GoButtonItem, GoMouseEventArgs, ButtonClickEventArgs, GoDrawnEventArgs 등 데이터/이벤트 클래스 |
| `api/ui/enums.html` | GoContentAlignment, GoRoundType, GoDockStyle, GoKeys 등 전체 열거형 |
| `api/ui/imagecanvas.html` | IcButton, IcLabel, IcOnOff, IcProgress, IcSlider, IcState |

### Going.Basis

| 경로 (스킬 파일 기준 상대경로) | 내용 |
|------|------|
| `api/basis/communications-modbus.html` | ModbusRTUMaster, ModbusRTUSlave, ModbusTCPMaster, ModbusTCPSlave |
| `api/basis/communications-mqtt.html` | MQClient, MQSubscribe, MQReceiveArgs |
| `api/basis/communications-ls.html` | CNet (LS Electric PLC), DataReadEventArgs, WriteEventArgs, TimeoutEventArgs 등 |
| `api/basis/communications-mitsubishi.html` | MC (Mitsubishi PLC), WordDataReadEventArgs, BitDataReadEventArgs, WriteEventArgs 등 |
| `api/basis/datas.html` | INI, Serialize, BitMemory, WordMemory, WordRef, BitAccessor |
| `api/basis/extensions.html` | Bits (비트/바이트 확장 메서드) |
| `api/basis/measure.html` | Chattering, Stable |
| `api/basis/tools.html` | CryptoTool, MathTool, NetworkTool, WindowsTool |
| `api/basis/utils.html` | EasyTask, HiResTimer, ExternalProgram, NaturalSortComparer, CompressionUtility |

### HTML 파일 내부 구조

각 API HTML 파일은 동일한 구조로 되어 있다:
- **클래스별 섹션**: `<div class="class-card" id="class-GoButton">` 형태로 클래스 구분, `<hr class="class-separator">`로 클래스 간 시각적 분리
- **속성 테이블**: `<table class="api-table">` — 타입(`col-type`), 이름(`col-name`, get/set 접근자 표시), 설명(`col-desc`) 컬럼
- **메서드 테이블**: 반환타입(`ret`), 이름(`col-method-name`), 파라미터(`params`), 설명(`col-desc`)
- **이벤트 테이블**: 이벤트 핸들러 타입(`event-args`), 이름(`col-method-name`), 설명(`col-desc`)
- **검색 팁**: `data-search` 속성에 키워드가 있으므로, `Grep`으로 컨트롤명 검색하면 해당 섹션을 빠르게 찾을 수 있음

### API HTML 로드 전략

| 상황 | 도구 | 이유 |
|------|------|------|
| 특정 속성/메서드/이벤트명 확인 | `Grep("속성명", path="api/...")` | 해당 섹션만 빠르게 찾음 — 컨텍스트 절약 |
| 처음 다루는 클래스의 전체 API 파악 | `Read("api/...")` | 속성·메서드·이벤트를 모두 봐야 올바른 코드 작성 가능 |
| 클래스명은 아는데 정확한 시그니처가 불확실 | `Grep("클래스명", path="api/...")` | 클래스 섹션 전체를 반환 |

> **원칙**: 이미 알고 있는 API를 재확인할 때는 `Grep`, 처음 접하는 클래스를 학습할 때는 `Read`.

```
// 예: GoDataGrid의 메서드만 찾기
Grep("GoDataGrid", path="./api/ui/controls.html")

// 예: MasterRTU의 GetWord 시그니처 확인
Grep("GetWord", path="./api/basis/communications-modbus.html")
```

### 사용 예시

```
// GoButton 속성 확인
Read("./api/ui/controls.html")

// MasterRTU/ModbusTCPMaster 메서드 확인
Read("./api/basis/communications-modbus.html")
```

> **API HTML 조회가 불가능한 환경**(채팅 등)에서는:
>   1. 이 스킬 MD 파일들에 기재된 패턴·속성명·예시 코드만 사용
>   2. MD 파일에 없는 속성/메서드는 **"이 API는 확인이 필요합니다 — Claude Code에서 `api/` HTML을 조회하거나, 공식 문서를 참고하세요"** 라고 안내
>   3. 절대 규칙 #2(속성/메서드 추측 금지)가 더 엄격하게 적용됨 — 확실하지 않으면 코드에 포함하지 말 것

---

## 전체 워크플로우

Going Library 프로젝트의 전형적인 작업 흐름:

### 환경별 작업 범위

| 작업 | Claude 채팅 | Claude Code |
|------|:-----------:|:-----------:|
| 1. project_brief.md 작성 | O | O |
| 2. .gud 파일(JSON) 생성 | O | O |
| 3. UIEditor 조정 + MakeCode | — (사용자) | — (사용자) |
| 4. C# 코드 구현 (*.cs 작성) | **X** | **O** |
| 5. 빌드 및 실행 | — (사용자) | O (`dotnet build`) |
| 6. 장치 배포 (gtcli) | **X** | **O** |

> **채팅 환경**은 파일 시스템 접근(`Read`/`Edit`/`Bash`)이 없으므로 코드 구현·빌드·배포가 불가능하다.
> project_brief.md 작성과 .gud JSON 생성은 대화만으로 완료 가능하므로 양쪽 환경 모두 지원.

```
1. project_brief.md 작성

   ⚠ project_brief.md는 임의로 작성하지 않는다.
   반드시 `ui-project-brief.md`를 Read로 읽고 인터뷰 절차·템플릿·체크리스트를
   확인한 뒤 해당 절차에 따라 진행할 것. (절대 규칙 #8 적용)

   | 경로 | 조건 | 설명 |
   |------|------|------|
   | A | 프로젝트 구상만 있고 자료가 없을 때 | Claude와 인터뷰로 brief 작성 |
   | B | 사용자가 brief 템플릿을 직접 채울 때 | 템플릿 제공 → 검증 |
   | C | 기존 자료(이미지, 엑셀 등)가 이미 있을 때 | 자료 분석 → 빠진 부분만 인터뷰 → brief 생성 |

   → 상세 절차: `ui-project-brief.md`의 "인터뷰 절차" 섹션 참조

   ★ Claude Code 진입 전 완비 확인:
     □ 페이지/윈도우 목록 + 레이아웃 이미지 (스케치 또는 레퍼런스)
     □ 통신 방식 및 파라미터
     □ 레지스터 맵 (Modbus 사용 시 필수 — 누락 시 Claude Code 작업 불가)
     □ 설정 파일 항목

   .gud 생성 시: project_brief.md + 이미지를 채팅에 함께 첨부
   플랫폼: Going.UI.OpenTK 고정 (linux-arm64)

2. .gud 파일 생성 (Claude — 채팅)
   └─ 사용자가 project_brief.md 내용을 Claude 채팅에 전달
   └─ Claude가 ui-json.md 참조하여 .gud 파일(JSON) 생성
   └─ 페이지/윈도우/컨테이너/컨트롤 배치, 테마 설정 포함
   └─ 주의: .gud = GoDesign 단일 JSON, SKRect는 좌표값(L,T,R,B 형식, Width/Height 아님)
   └─ 주의: Enum은 숫자, 모든 컨트롤에 UUID Id 필수

3. UIEditor에서 수정 및 코드 배포 (사용자)
   └─ 생성된 .gud 파일을 UIEditor에서 열기
   └─ 컨트롤 위치/크기 미세 조정, 디자인 확인
   └─ MakeCode 실행 → 아래 파일들 자동 생성:
       ├─ design.json          (GoDesign 직렬화, 런타임 로드용)
       ├─ Program.cs           (진입점, ExistsCheck=true)
       ├─ MainWindow.cs        (사용자 파일, ExistsCheck=true)
       ├─ MainWindow.Designer.cs (자동생성, 항상 덮어씀)
       ├─ Pages/*.cs           (사용자 파일, ExistsCheck=true)
       ├─ Pages/*.Designer.cs  (자동생성, 항상 덮어씀)
       ├─ Windows/*.cs         (사용자 파일, ExistsCheck=true)
       └─ Windows/*.Designer.cs (자동생성, 항상 덮어씀)

4. Claude Code에서 프로젝트 구현 ★핵심 단계★
   └─ 전제: 1~3단계는 이미 완료된 상태. 작업 디렉터리에 Designer.cs와 design.json이 존재함.
   └─ 사용자가 생성된 코드 폴더를 작업 디렉터리로 지정
   └─ project_brief.md를 Claude Code에 전달
   └─ Claude Code가 *.cs(사용자 파일)만 작업 (Designer.cs/design.json 절대 수정 금지)

   4-1. UI 코드 작성 (참조: ui-code.md)
        ├─ Program.cs: Main 싱글턴, DataManager/DeviceManager 초기화, Run/Stop
        ├─ MainWindow.cs: 전역 이벤트 바인딩, OnUpdateFrame에서 상태 갱신
        ├─ Pages/*.cs: 컨트롤 이벤트 바인딩(ButtonClicked 등), OnUpdate에서 데이터→UI 반영
        └─ Windows/*.cs: 팝업 동작, 콜백 패턴 (Show → 결과 → Close)

   4-2. 통신 코드 작성 (참조: basis.md)
        ├─ DeviceManager: MasterRTU/MasterTCP 기본 (GetWord/GetBit + IsOpen)
        │   └─ ModbusRTUMaster / ModbusTCPMaster는 수신 이벤트 직접 제어 시에만 사용
        ├─ DataManager: 설정 파일(JSON) 로드/저장
        └─ ⚠ project_brief.md에 장치 모델이 없으면 반드시 사용자에게 문의

5. 빌드 및 실행 (사용자)
   └─ dotnet build → dotnet run
   └─ design.json이 실행 디렉터리에 있어야 함

6. 장치 배포 (GoingTouchCLI — 참조: ui-mcp.md)
   └─ 6-1. gtcli scan으로 네트워크의 터치 장치 검색
   └─ 6-2. 사용자가 장치 웹 UI에서 MCP 토큰 확인 → Claude Code에 전달
   └─ 6-3. Claude Code가 gtcli로 빌드-배포 자동화:
       ├─ dotnet publish -r linux-arm64 → zip 압축
       ├─ gtcli deploy {host} App.zip "앱이름" AppName true --token {token}
       └─ gtcli hide-ui {host} --token {token}
```

> **역할 분담**: 1=사용자, 2=Claude(채팅), 3=사용자(UIEditor), **4=Claude Code(핵심)**, 5=사용자, 6=사용자(토큰 확인)+**Claude Code(gtcli로 검색→빌드→배포 자동화)**.
> Claude Code는 ***.Designer.cs와 design.json을 절대 수정하지 않으며**, *.cs(사용자 파일)만 작업한다.

### 단계 전환 안내 규칙

각 단계가 완료되면 **다음 단계에서 사용자가 해야 할 일**을 구체적으로 안내한다. 특히 사용자 액션이 필요한 전환점에서는 반드시 상세 안내를 출력할 것.

| 전환 | 안내 내용 |
|------|----------|
| 프로젝트 시작 시 (`project_brief.md` 없음) | "프로젝트 브리프가 없습니다. 새 HMI 프로젝트를 시작하려면 인터뷰를 진행합니다. 기존 자료(화면 이미지, 레지스터 맵 등)가 있으면 함께 전달해주세요." |
| Step 1 → 2 (브리프 완성) | "project_brief.md가 완성되었습니다. 이제 이 브리프를 기반으로 .gud 파일(UI 디자인)을 생성합니다." |
| Step 2 → 3 (.gud 생성 완료) | "{프로젝트명}.gud 파일이 생성되었습니다. 다음 단계는 사용자님이 직접 진행합니다:\n1. UIEditor에서 {프로젝트명}.gud 파일을 엽니다\n2. 컨트롤 위치/크기를 원하는 대로 조정합니다\n3. **MakeCode**를 실행하여 C# 프로젝트를 생성합니다\n4. 생성된 프로젝트 폴더를 Claude Code 작업 디렉터리로 지정하고 알려주세요." |
| Step 3 → 4 (MakeCode 완료 확인) | "MakeCode로 생성된 프로젝트를 확인했습니다. 이제 C# 코드를 구현합니다. Designer.cs와 design.json은 수정하지 않고 *.cs 사용자 파일만 작업합니다." |
| Step 4 → 5 (코드 구현 완료) | "코드 구현이 완료되었습니다. `dotnet build`로 빌드하고 `dotnet run`으로 실행하여 동작을 확인해주세요." |
| Step 5 → 6 (배포 요청 시) | "장치 배포를 진행합니다. 먼저 장치의 웹 UI에서 MCP 토큰을 확인하고 알려주세요. `gtcli scan`으로 네트워크의 터치 장치를 검색할 수 있습니다." |

> **핵심**: Step 2→3 전환이 가장 중요하다. 여기서 작업 주체가 Claude에서 사용자로 바뀌므로, 사용자가 무엇을 해야 하는지 빠짐없이 안내해야 한다. "MakeCode 후 프로젝트 폴더를 알려주세요"까지 명시하여 다음 전환을 자연스럽게 유도한다.

---

## 세션 간 컨텍스트 유지

> **Claude Code 환경 전용.** 채팅 환경에서는 해당 없음.

여러 세션에 걸쳐 작업할 때 `project_status.md`를 유지한다.
상세 절차와 템플릿은 `session-context.md`를 `Read`로 읽을 것.

**핵심 규칙:** 세션 시작 시 `project_status.md`가 있으면 반드시 읽고 현재 상태를 파악한 후 작업을 시작.

---

## 절대 규칙

### 1. Designer.cs / design.json 수정 금지

`*.Designer.cs`와 `design.json`은 UIEditor가 자동 생성하는 파일.
**절대 수정하지 말 것.** 작업 대상은 `*.cs` (사용자 파일)만.

> **Why:** 이 파일들은 UIEditor의 MakeCode가 매번 덮어쓴다. Claude가 수정해도 다음 MakeCode 실행 시 전부 날아간다. 또한 design.json은 GoDesign의 내부 직렬화 포맷이므로 수동 편집 시 역직렬화 예외(`JsonException: The JSON value could not be converted`)가 발생할 확률이 높다.

### 2. 속성/메서드 추측 금지 — API 문서 확인 필수

이 스킬 문서에 기재되지 않은 속성명, 메서드 시그니처, 이벤트명을 추측하여 사용하지 말 것.
확실하지 않으면 **반드시 `api/` 디렉터리의 HTML 파일을 `Read` 또는 `Grep`으로 확인** 후 사용한다.

- 컨트롤 속성/이벤트 → `api/ui/controls.html`
- 컨테이너 속성 → `api/ui/containers.html`
- 통신 클래스 메서드 → `api/basis/communications-*.html`
- 테마/다이얼로그/컬렉션 → `api/ui/themes.html`, `api/ui/dialogs.html`, `api/ui/collections.html`

> **Why:** Going Library는 독자적인 커스텀 프레임워크로, WPF/WinForms/Avalonia와 API가 완전히 다르다. AI가 다른 프레임워크 지식으로 유추한 속성명(예: BackColor, Click, Text 등)은 대부분 컴파일 에러를 일으킨다. API 문서가 `api/` 디렉터리에 전부 있으므로 확인 비용은 낮지만, 잘못된 속성을 쓰면 사용자가 디버깅에 시간을 낭비하게 된다.

### 3. 코드 네이밍 — 영문+숫자만 사용

변수명, 속성명, 메서드명, 클래스명 등 코드에서 사용하는 모든 식별자는 **반드시 영문+숫자**로 작성.
한글 식별자는 절대 사용 금지. 대신 **주석으로 한글 명칭을 기입**하여 가독성을 확보한다.

> **Why:** Going Library 프로젝트는 linux-arm64(라즈베리파이) 타겟으로 크로스 컴파일된다. 한글 식별자는 일부 빌드 환경에서 인코딩 문제를 일으키며, PLC 통신 프로토콜의 태그명/로그 출력에서 깨질 수 있다. 또한 산업 현장에서 유지보수하는 엔지니어가 코드를 읽을 때 영문 식별자 + 한글 주석 조합이 가장 범용적이다.

```csharp
// ✅ 올바른 예
public double CondTank1Inlet => ...;  // T01-유증기응축탱크1단유입
public void SetTargetTemp(double value) ...  // 설정-정상운전 가동 온도

// ❌ 잘못된 예
public double 응축탱크1단유입 => ...;
public void Set정상운전가동온도(double value) ...
```

### 4. 데이터 구조 / 레지스터 맵 임의 작성 금지

Modbus 레지스터 주소, 데이터 의미, 단위, 슬레이브 번호는 프로젝트마다 완전히 다르다.
사용자 확인 없이 DeviceManager, 데이터 모델을 임의로 설계하면 실제 장비와 맞지 않는 코드가 된다.

> **Why:** AI가 그럴듯하게 만든 레지스터 맵은 실제 장비와 100% 불일치한다. 잘못된 주소로 쓰기(FC6/FC16)를 실행하면 **산업 장비가 오동작하여 물리적 사고로 이어질 수 있다.** 이 규칙은 안전 관련 규칙이다.

**반드시 확인 후 작성:**
1. **장치 데이터 모델** — 사용자의 `project_brief.md`에 장치 데이터 모델(레지스터 맵, 데이터 구조)이 없으면 **반드시 사용자에게 문의**. 모델과 모드버스 영역(어떤 주소에 어떤 데이터가 있는지)을 확인해야 함
2. **레지스터 맵** — 시작 주소, 각 주소의 데이터 의미, 단위, 읽기/쓰기 구분
3. **슬레이브 구성** — 슬레이브 번호, 보드/채널 수량
4. **FC 코드** — FC3/FC1/FC6/FC16 등
5. **데이터 클래스 구조** — 사용자가 제공하거나 명시적으로 승인한 구조만 사용

> **필수 문의 규칙**: `project_brief.md`가 제공되었으나 장치 데이터 모델이 누락된 경우, 코드를 작성하기 전에 반드시 사용자에게 "장치의 데이터 모델과 모드버스 영역 정보를 알려주세요"라고 문의해야 한다. 모델 없이 DeviceData/DeviceManager를 임의 작성하면 실제 장비와 맞지 않는 코드가 생성된다.

**확인 없이 작성 가능:**
- UIEditor 코드 생성 후 컨트롤 이벤트 바인딩
- Page/Window UI 로직
- DataManager (단, 설정 파일 구조는 사용자 확인 후 작성)
- MainWindow 초기화, 페이지 전환 로직

**확인 없이 작성 불가:**
- DeviceManager (폴링 주소/영역, 수신 데이터 처리)
- 데이터 모델 클래스 (Board, Channel, DeviceData 등 레지스터 맵 의존)
- 쓰기 메서드 (WriteXxx — 주소가 확정되어야 함)

DeviceManager 작성 시 클래스 선택 규칙:
- MasterRTU / MasterTCP를 기본으로 사용할 것
- ModbusRTUMaster / ModbusTCPMaster는 수신 이벤트 직접 제어가
  명시적으로 필요한 경우에만 허용
- DeviceData 사용 시 MasterRTU / MasterTCP 기반을 권장
  (ID(slaveId) 필수, 읽기=GetWord/GetBit 래핑, 쓰기=Set{기능이름}()로 SetWord/SetBit 래핑)

### 5. .gud 파일 Pages/Windows는 반드시 Dictionary 형태

.gud Design 내부의 Pages와 Windows는 **Array `[]`가 아닌 Dictionary `{}` 형태**로 작성해야 한다.
각 항목은 `"Type"` + `"Value"` 래핑 객체로 감싸야 하며, Key는 페이지/윈도우의 Name이다.
컨트롤 배열 프로퍼티명은 `"Childrens"` (Controls 아님).

```
✅ "Pages": { "PageMain": { "Type": "GoPage", "Value": { "Childrens": [...], ... } } }
❌ "Pages": [{ "Type": "GoPage", "Name": "PageMain", "Controls": [...] }]

✅ "Windows": { "Keypad": { "Type": "GoWindow", "Value": { "Childrens": [...], ... } } }
❌ "Windows": [{ "Type": "GoWindow", "Name": "Keypad" }]
```

Array로 작성하면 GoPagesConverter/GoWindowsConverter에서 `Expected StartObject` 예외 발생.

> **Why:** GoDesign의 JSON 직렬화는 GoPagesConverter/GoWindowsConverter를 사용하며, 이 컨버터들은 Dictionary`<string, TypeValue>` 구조만 역직렬화할 수 있다. Array `[]`로 작성하면 .gud 파일 자체를 로드할 수 없고 UIEditor에서도 열리지 않으므로, 파일을 처음부터 다시 만들어야 한다.

### 6. 이미지 참조 처리

project_brief.md + 이미지가 함께 제공된 경우:
- 이미지의 레이아웃을 우선 참조
- 텍스트 설명과 이미지가 충돌하면 이미지 우선
- 이미지에서 읽기 어려운 컨트롤은 텍스트로 보완 후 작업
- 이미지만으로 판단 불가한 레지스터 맵은 반드시 문의
- **이미지를 우선하되, 애매한 요소를 추측하지 말 것** — 반드시 사용자에게 확인

> **Why:** 사용자가 텍스트로 의도를 정확히 전달하지 못하는 경우가 많아 이미지가 더 신뢰할 수 있다. 단, 이미지 우선이 "추측 허용"을 의미하지는 않는다. 예를 들어 "ON" 버튼이 보일 때 이것이 전동기 ON인지 유압 ON인지는 이미지만으로 판단할 수 없다. 잘못 해석하면 완전히 다른 동작의 코드가 만들어지므로, 용도/의미가 불분명한 요소는 반드시 사용자에게 물어야 한다.

### 7. .gud 파일 생성/수정 시 Python/스크립트 사용 금지

.gud 파일은 순수 JSON이다. `Write`/`Edit` 도구로 직접 JSON 텍스트를 생성하거나 수정하라.
Python, Node.js 등 스크립트를 작성하여 JSON을 생성하거나 수정하지 말 것.
UUID 생성도 스크립트를 사용하지 말고 직접 작성하라.

**.gud를 생성/수정하는 행위에 예외는 없다.** 다음은 예외 사유가 아니다:
- "파일이 크다" / "JSON이 한 줄이다" / "포맷팅이 필요하다"
- "수정이지 생성이 아니다"
- "UUID를 랜덤 생성해야 한다"
- "기존 파일을 파싱해서 일부만 바꿔야 한다"
- "검증/파싱을 위해 스크립트가 필요하다"

> **참고:** `eval_runner.py`는 .gud 파일을 **읽기 전용으로 검증**하는 도구이며, .gud를 생성하거나 수정하지 않는다. 이 규칙은 .gud의 생성/수정에 적용되므로 읽기 전용 검증은 적용 범위 밖이다.

> **Why:** .gud는 단순 JSON이므로 Write/Edit 도구로 직접 작성하는 것이 가장 빠르고 정확하다. 스크립트를 작성하면 ① 스크립트 자체의 버그 디버깅이 필요하고 ② JSON 문자열 이스케이프 문제가 발생하며 ③ 생성된 결과물을 다시 검증해야 하는 이중 작업이 된다. 실제로 스크립트로 생성한 .gud에서 이스케이프 오류, UUID 중복, SKRect 형식 오류가 반복 발생했다.

- .gud는 단일 GoDesign JSON — 이스케이프 처리 불필요
- AI가 JSON을 직접 작성하는 것이 스크립트 작성+실행보다 빠름
- 디버깅 불필요 — JSON 구조만 정확하면 됨
- UUID는 컨트롤마다 **고유하게 순차 생성** — 중복 금지 (예: `00000001-0000-0000-0000-000000000001`, `...-002`, `...-003` 순서도 허용)

### 8. 절차별 동의 후 진행 (Step-by-Step Confirmation)

작업은 절차 단위로 실행하며, 각 절차 완료 후 결과를 사용자에게 명시하고 동의를 받은 뒤 다음 절차로 진행한다.

**원칙:**
- 하나의 절차를 완료하면 **무엇을 했는지, 결과물이 무엇인지** 구체적으로 보고한다
- 사용자가 확인/승인한 후에만 다음 절차로 넘어간다
- 모든 절차는 **개별 실행이 가능**해야 한다 — 특정 절차만 단독으로 재실행하거나 수정할 수 있어야 함

**절차 단위 기준:**

| 절차 | 산출물 | 동의 시점 |
|------|--------|----------|
| project_brief.md 작성 (인터뷰) | project_brief.md | 인터뷰 단계별 + 최종 확인 |
| .gud 파일 생성/수정 | .gud JSON | 레이아웃·컨트롤 배치 확인 후 |
| C# 코드 작성 (Page/Window) | *.cs 파일 | 파일별 또는 기능 단위 확인 후 |
| 통신 코드 작성 | DeviceManager 등 | 데이터 모델·폴링 구조 확인 후 |
| 빌드/배포 | 빌드 결과, 배포 로그 | 빌드 성공 확인 후 |

**이유:**
HMI 프로젝트는 UI 수정이 빈번하게 발생한다. .gud → C# 코드 → 통신 코드는 앞 단계의 결과에 의존하므로, 동의 없이 여러 단계를 한꺼번에 진행하면 앞 단계 수정 시 뒤따르는 모든 산출물을 폐기해야 한다. 절차별 확인을 통해 각 단계의 완성도를 높인 뒤 다음으로 넘어가는 것이 재작업을 최소화하는 방법이다.

**예외:**
사용자가 명시적으로 "끝까지 진행해줘", "한번에 다 해줘" 등 일괄 진행을 요청한 경우에는 동의 절차를 생략할 수 있다. 단, 이 경우에도 각 절차의 결과는 최종 보고에서 구분하여 명시한다.

---

## .gud 직렬화 핵심 (요약)

> 상세 규칙은 `ui-json-quick.md` 또는 `ui-json.md`의 "자주 하는 실수" 섹션 참조.

```
.gud = GoDesign 단일 JSON → GoJsonConverter.Options로 직렬화
  컨트롤: { "Type": "GoButton", "Value": { ... } }
  Bounds: "L,T,R,B" 문자열 (W,H 아님)
  Enum: 숫자 (문자열 불가)
  Margin: {"Left":0,...} 객체 (문자열 불가)
  Dock=Fill: "Dock": 5 ("Fill": true 불가)
  Id: 고유 UUID 필수
  컨트롤 배열: "Childrens" ("Controls" 아님)
  Pages/Windows: Dictionary {} (Array [] 불가)
```

---

## 프로젝트 구조

```
Going.UI          - 플랫폼 독립 UI 코어 (컨트롤, 컨테이너, 테마, 디자인)
Going.UI.OpenTK   - OpenTK 어댑터 (임베디드/라즈베리파이)
Going.Basis       - 통신 및 유틸리티 (Modbus, MQTT, 메모리, 직렬화)
Going.UIEditor    - 비주얼 에디터 (.gud 파일 생성 도구)
```

---

## 트러블슈팅

에러 발생 시 `troubleshooting.md`를 `Read`로 읽고 증상별 해결 방법을 확인할 것.
빌드 에러, 통신 에러, 런타임 에러, 배포 에러(gtcli) 4개 카테고리로 구성.
