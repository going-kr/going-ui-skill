# Going UI Skill

**Going Library**용 Claude Code 스킬 — C# .NET 8.0 산업용 HMI/SCADA UI 프레임워크를 AI로 개발합니다.

## 주요 기능

- **.gud 파일 생성** — 40개 이상의 산업용 컨트롤(GoButton, GoLamp, GoDataGrid, GoSlider 등)을 포함한 UI 디자인 파일(JSON) 생성
- **C# 코드 작성** — 이벤트 바인딩, OnUpdate 데이터 연동, 페이지/윈도우 라이프사이클
- **통신 코드** — Modbus RTU/TCP, MQTT, LS Electric CNet, Mitsubishi MC PLC 연동
- **장치 배포** — LauncherTouch MCP를 통한 Raspberry Pi 터치 패널 배포

## 설치

```
/install going-kr/going-ui-skill
```

## 사용 예시

### .gud UI 파일 생성

```
"1024x600 해상도로 모니터링 페이지 하나 만들어줘.
 GoLabel 4개, GoLamp 2개, GoButton 3개 배치해줘."
```

### 이미지 → .gud 변환

```
"이 이미지를 참고해서 .gud 파일을 만들어줘."
(HMI 화면 스크린샷 또는 스케치 첨부)
```

6단계 프로세스(인벤토리 → 그룹핑 → 컨테이너 설계 → 배치 → 검증 → 생성)로 진행됩니다.

### C# 이벤트 코드 작성

```
"PageMonitor에서 btnStart 클릭 시 DeviceManager.Start() 호출하는 코드 작성해줘."
```

```csharp
btnStart.ButtonClicked += (o, s) =>
{
    MainWindow.Current.DeviceManager.Start();
};
```

### Modbus 통신 설정

```
"MasterRTU로 슬레이브1번, D0~D49 영역 모니터링 코드 작성해줘."
```

```csharp
RTU = new MasterRTU();
RTU.WordAreas.Add(0x0000, "D");
RTU.MonitorWord_F3(1, 0x0000, 50);
RTU.Start();

var value = RTU.GetWord("D0");
```

### Raspberry Pi 배포

```
"172.30.1.50 장치에 프로젝트 빌드해서 배포해줘."
```

`dotnet publish` → `gtcli deploy`로 대상 장치에 업로드 및 설치합니다.

## 작업 흐름

| 단계 | 작업 | 환경 |
|------|------|------|
| 1 | project_brief.md 작성 | Claude 채팅 / Claude Code |
| 2 | .gud 파일 생성 | Claude 채팅 / Claude Code |
| 3 | UIEditor에서 조정 + MakeCode | 사용자 |
| 4 | C# 코드 구현 | Claude Code |
| 5 | 빌드 및 실행 | 사용자 / Claude Code |
| 6 | 장치 배포 (gtcli) | Claude Code |

## 트리거 키워드

`Going`, `GoButton`, `GoLamp`, `GoSlider`, `GoInput`, `GoValue`, `GoDesign`, `.gud`, `Modbus`, `MasterRTU`, `SlaveRTU`, `MQTT`, `HMI`, `SCADA`, `PLC`, `LauncherTouch`, `gtcli`

## NuGet 패키지

| 패키지 | 설명 |
|--------|------|
| [Going.Basis](https://www.nuget.org/packages/Going.Basis) | 통신 및 유틸리티 (Modbus, MQTT, CNet, MC) |
| [Going.UI](https://www.nuget.org/packages/Going.UI) | 플랫폼 독립 UI 코어 (컨트롤, 테마, 디자인) |
| [Going.UI.OpenTK](https://www.nuget.org/packages/Going.UI.OpenTK) | OpenTK 어댑터 (임베디드/Raspberry Pi) |
| [Going.UI.Forms](https://www.nuget.org/packages/Going.UI.Forms) | WinForms 어댑터 |

## 스킬 파일 구조

| 파일 | 용도 |
|------|------|
| `SKILL.md` | 진입점 — 워크플로우, 규칙, 파일 참조 테이블 |
| `ui-json-quick.md` | 단일 파일 .gud 생성 가이드 (전체 컨트롤) |
| `ui-json.md` | .gud 구조 상세, Enum, 테마 |
| `ui-image-to-gud.md` | 6단계 이미지→.gud 변환 절차 |
| `ui-code.md` | C# 코드 패턴, Designer.cs 규칙 |
| `basis.md` | 통신 패턴 (Modbus, MQTT, CNet, MC) |
| `ui-mcp.md` | gtcli CLI를 통한 장치 배포 |
| `api/` | 21개 HTML API 레퍼런스 |

## 라이선스

MIT
