# Going UI Skill

**Going Library**용 Claude Code 스킬 — C# .NET 8.0 산업용 HMI/SCADA UI 프레임워크를 AI로 개발합니다.

## 설치

```
/install going-kr/going-ui-skill
```

## 개발 절차

Going Library로 HMI 애플리케이션을 만드는 전체 흐름입니다.

### Step 1. 프로젝트 브리프 작성

> 환경: Claude 채팅 / Claude Code

프로젝트의 요구사항을 정리한 `project_brief.md`를 작성합니다.
화면 구성, 사용할 컨트롤, 통신 장비, 해상도 등을 대화로 정리하면 Claude가 문서를 생성합니다.

```
"1024x600 해상도의 데이터 로거를 만들거야.
 메인 페이지에 실시간 차트, 모니터링 페이지에 GoLamp 8개와 GoValue 16개.
 Modbus RTU로 슬레이브 1번과 통신."
```

### Step 2. .gud 파일 생성

> 환경: Claude 채팅 / Claude Code

브리프를 기반으로 `.gud` 파일(GoDesign JSON)을 생성합니다.
40개 이상의 산업용 컨트롤(GoButton, GoLamp, GoDataGrid, GoSlider 등)을 배치할 수 있습니다.

```
"브리프 기반으로 .gud 파일 만들어줘."
```

이미지를 첨부하면 화면 레이아웃을 분석하여 .gud로 변환할 수도 있습니다.

```
"이 이미지를 참고해서 .gud 파일 만들어줘."
(HMI 화면 스크린샷 첨부)
```

### Step 3. UIEditor에서 편집 + MakeCode

> 환경: 사용자 (Going UI Editor)

생성된 .gud 파일을 UI Editor에서 열어 컨트롤 위치와 속성을 미세 조정합니다.
편집이 완료되면 **MakeCode** 버튼으로 C# 코드(Designer.cs)를 자동 생성합니다.

### Step 4. C# 코드 구현

> 환경: Claude Code

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

> 환경: Claude Code

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
| [Going.UI.Forms](https://www.nuget.org/packages/Going.UI.Forms) | WinForms 어댑터 |
| [Going.Basis](https://www.nuget.org/packages/Going.Basis) | 통신 및 유틸리티 |

## 스킬 파일 구조

| 파일 | 용도 |
|------|------|
| `SKILL.md` | 진입점 — 워크플로우, 규칙, 참조 테이블 |
| `ui-json-quick.md` | .gud 생성 가이드 (전체 컨트롤) |
| `ui-json.md` | .gud 구조 상세, Enum, 테마 |
| `ui-image-to-gud.md` | 이미지→.gud 변환 절차 |
| `ui-code.md` | C# 코드 패턴, Designer.cs 규칙 |
| `basis.md` | 통신 패턴 (Modbus, MQTT, CNet, MC) |
| `ui-mcp.md` | gtcli 배포 가이드 |
| `api/` | 21개 HTML API 레퍼런스 |

## 라이선스

MIT
