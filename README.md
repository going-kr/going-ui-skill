<p align="center">
  <img src="https://raw.githubusercontent.com/going-kr/Going-Library/master/icon/Going_logo_blue.png" alt="Going Library" width="120">
</p>

<h1 align="center">Going UI Skill</h1>

<p align="center">
  <b>Going Library</b>용 Claude Code 스킬 — 산업용 HMI/SCADA UI를 AI로 개발합니다.
</p>

<p align="center">
  <a href="https://github.com/going-kr/Going-Library"><img src="https://img.shields.io/badge/Going_Library-.NET_8.0-blue" alt="Going Library"></a>
  <a href="https://www.nuget.org/packages/Going.UI"><img src="https://img.shields.io/nuget/v/Going.UI?label=Going.UI&color=blue" alt="NuGet"></a>
  <a href="https://www.nuget.org/packages/Going.Basis"><img src="https://img.shields.io/nuget/v/Going.Basis?label=Going.Basis&color=blue" alt="NuGet"></a>
</p>

---

## 개발 환경 구성

Claude Code에 이렇게 말하세요:

```
https://going-kr.github.io/Going-Library/setup.html 여기 보고 개발 환경 구성해줘
```

스킬 설치, UIEditor 다운로드, 바탕화면 바로가기 생성까지 자동으로 진행됩니다.

---

## 개발 절차

Going Library로 HMI 애플리케이션을 만드는 전체 흐름입니다.

### Step 1. 프로젝트 브리프 작성
> `Claude 채팅` / `Claude Code`

프로젝트의 요구사항을 정리한 `project_brief.md`를 작성합니다.
화면 구성, 사용할 컨트롤, 통신 장비, 해상도 등을 대화로 정리하면 Claude가 문서를 생성합니다.

```
"1024x600 해상도의 데이터 로거를 만들거야.
 메인 페이지에 실시간 차트, 모니터링 페이지에 GoLamp 8개와 GoValue 16개.
 Modbus RTU로 슬레이브 1번과 통신."
```

### Step 2. 디자인 파일(.gud) 생성
> `Claude 채팅` / `Claude Code`

브리프를 기반으로 디자인 파일(`.gud`)을 생성합니다.
50여 종의 산업용 컨트롤(GoButton, GoLamp, GoDataGrid, GoSlider 등)을 배치할 수 있습니다.

```
"브리프 기반으로 디자인 파일 만들어줘."
```

이미지를 첨부하면 화면 레이아웃을 분석하여 디자인 파일로 변환할 수도 있습니다.

```
"이 이미지를 참고해서 디자인 파일 만들어줘."
(HMI 화면 스크린샷 첨부)
```

### Step 3. UI Editor에서 편집 + MakeCode
> `사용자` — Going UI Editor

생성된 디자인 파일(.gud)을 UI Editor에서 열어 컨트롤 위치와 속성을 미세 조정합니다.
편집이 완료되면 **MakeCode** 버튼으로 C# 코드(Designer.cs)를 자동 생성합니다.

### Step 4. C# 코드 구현
> `Claude Code`

MakeCode가 생성한 Designer.cs를 기반으로 비즈니스 로직을 작성합니다.

- 이벤트 바인딩 (`ButtonClicked`, `MouseClicked`)
- OnUpdate 데이터 연동 (주기적 UI 갱신)
- 통신 코드 (Modbus RTU/TCP, MQTT, CNet, MC)
- 페이지/윈도우 전환

```
"PageMonitor에서 btnStart 클릭 시 RTU 통신 시작하는 코드 작성해줘."
```

```csharp
btnStart.ButtonClicked += (o, s) =>
{
    MainWindow.Current.DeviceManager.Start();
};
```

### Step 5. 빌드 및 장치 배포
> `Claude Code`

`dotnet publish`로 빌드 후, `gtcli`로 Raspberry Pi 터치 패널에 배포합니다.

```
"172.30.1.50 장치에 빌드해서 배포해줘."
```

---

## 지원 통신

| 프로토콜 | 클래스 |
|----------|--------|
| Modbus RTU | `MasterRTU`, `SlaveRTU` |
| Modbus TCP | `MasterTCP`, `SlaveTCP` |
| MQTT | `MQClient` |
| LS Electric CNet | `CNet` |
| Mitsubishi MC | `MC` |

## NuGet 패키지

| 패키지 | 설명 |
|--------|------|
| [Going.UI](https://www.nuget.org/packages/Going.UI) | 플랫폼 독립 UI 코어 |
| [Going.UI.OpenTK](https://www.nuget.org/packages/Going.UI.OpenTK) | OpenTK 어댑터 (임베디드/Raspberry Pi) |
| [Going.Basis](https://www.nuget.org/packages/Going.Basis) | 통신 및 유틸리티 |

## 스킬 파일 구조

```
going-ui-skill/
├── SKILL.md                  진입점 — 워크플로우, 규칙, 라우팅
│
├── gud-structure.md           .gud 최상위 구조, Pages/Windows, 테마
├── enums-reference.md         Enum 전체 목록 + 숫자값 매핑
├── image-to-gud.md            이미지 → .gud 변환 6단계 절차
│
├── controls/                  ★ 컨트롤 정본 (54개)
│   ├── _common.md             GoControl 공통 속성/이벤트
│   ├── GoButton.md ~ GoTrendGraph.md   기본 15 + 확장 19 + 입력/표시 2
│   ├── GoTableLayoutPanel.md ~ GoPicturePanel.md   컨테이너 10
│   └── IcContainer.md ~ IcSlider.md   ImageCanvas 7
│
├── code-pattern.md            C# 코드 패턴, using 참조, 페이지/윈도우
├── code-makecode-ref.md       MakeCode 출력 템플릿 (참고용)
│
├── comm-pattern.md            통신 패턴 (자주 하는 실수 19개 포함)
├── comm/                      통신 API 레퍼런스 (6개)
│   ├── modbus-api.md          Modbus RTU/TCP Master/Slave 전체
│   ├── mqtt-api.md            MQClient, MQSubscribe
│   ├── ls-api.md              CNet (LS Electric)
│   ├── mitsubishi-api.md      MC (Mitsubishi)
│   ├── data-utils-api.md      INI, Serialize, Memory
│   └── tools-api.md           Crypto, Math, EasyTask, Timer
│
├── project-brief.md           프로젝트 브리프 작성 가이드
├── deploy-cli.md              gtcli 배포 가이드
├── getting-started.md         튜토리얼 (모터 제어 예제)
├── troubleshooting.md         에러 해결 + .gud 부분 수정 가이드
├── session-context.md         세션 간 컨텍스트 유지
│
├── evals.json                 스킬 평가 테스트 (43개, core/extended)
├── eval_runner.py             평가 실행기
├── tools/gtcli.exe            배포 CLI 도구
└── sample/                    샘플 프로젝트 (2개)
    ├── sample1/               TspMonitor (Modbus RTU)
    └── sample2/               TemperatureMonitor (Modbus TCP)
```

## 라이선스

MIT
