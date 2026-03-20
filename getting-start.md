# Getting Started — 모터 제어 패널

이 문서는 Going Library를 사용하여 **모터 제어 HMI**를 처음부터 완성하는 전체 과정을 안내합니다.

| 단계 | 작업 | 환경 |
|------|------|------|
| 1 | 프로젝트 브리프 작성 | Claude 채팅 또는 Claude Code |
| 2 | .gud 파일 생성 | Claude 채팅 또는 Claude Code |
| 3 | UIEditor에서 조정 + MakeCode | 사용자 (UIEditor) |
| 4 | C# 코드 구현 | Claude Code |
| 5 | 빌드 및 실행 | 사용자 / Claude Code |

---

## 시나리오 개요

**모터 제어 패널** — 2페이지 구성

| 페이지 | 역할 |
|--------|------|
| PageMain | 모터 상태 모니터링 + 운전/정지 제어 |
| PageSetting | 통신 파라미터(포트, 보드레이트, 타임아웃) 설정 |

**사용 컨트롤:**
- GoLamp × 2 — 운전/정지 상태 표시
- GoButton × 2 — 운전/정지 버튼
- GoValue — RPM 표시
- GoSlider — 속도 설정
- GoLabel — 상태 텍스트, 제목 등

**통신:** Modbus TCP (IP: 192.168.0.10, Port: 502)

---

## Step 1. 프로젝트 브리프 작성

> `ui-project-brief.md` 참조. 인터뷰 경로 A/B/C 중 택 1.

아래는 이 시나리오의 **완성된 브리프 예시**입니다.

### project_brief.md

```markdown
## 1. 프로젝트 개요

- **프로젝트명**: MotorControl
- **앱 이름**: MotorControl
- **목적**: 모터 운전/정지 제어 및 RPM 모니터링
- **해상도**: 1024x600
- **테마**: Dark

## 2. 화면 구성

### 페이지 목록

#### PageMain
- **역할**: 모터 상태 모니터링, 운전/정지 제어, 속도 조절
- **주요 컨트롤**:
  - GoLamp "lampRun" — 운전 상태 (녹색)
  - GoLamp "lampStop" — 정지 상태 (적색)
  - GoButton "btnStart" — 운전 버튼
  - GoButton "btnStop" — 정지 버튼
  - GoValue "valRPM" — 현재 RPM 표시
  - GoSlider "sldSpeed" — 목표 속도 설정 (0~3000)
  - GoLabel "lblStatus" — 상태 메시지
- **페이지 이동**: 설정 버튼 → PageSetting

#### PageSetting
- **역할**: 통신 파라미터 설정
- **주요 컨트롤**:
  - GoInputString "inpIP" — PLC IP 주소
  - GoInputNumber "inpPort" — 포트 번호
  - GoInputNumber "inpTimeout" — 타임아웃(ms)
  - GoButton "btnSave" — 설정 저장
  - GoButton "btnBack" — 메인으로 돌아가기

### 윈도우(팝업) 목록

없음.

## 3. 통신

### Modbus TCP

- **IP**: 192.168.0.10
- **포트**: 502
- **타임아웃(ms)**: 1000

**슬레이브 구성**

| 슬레이브 번호 | 역할 |
|-------------|------|
| 1 | 모터 드라이브 |

**레지스터 맵 (워드)**

| 주소 | 명칭 | 설명 | 단위 | R/W | FC |
|------|------|------|------|-----|-----|
| 0x0000 | RunState | 운전 상태 (0=정지, 1=운전) | - | R | FC3 |
| 0x0001 | CurrentRPM | 현재 RPM | rpm | R | FC3 |
| 0x0002 | ErrorCode | 에러 코드 | - | R | FC3 |
| 0x0010 | TargetSpeed | 목표 속도 | rpm | R/W | FC3/FC6 |

**비트 맵**

| 주소 | 명칭 | 설명 | R/W | FC |
|------|------|------|-----|-----|
| 0x0000 | RunCmd | 운전 명령 | R/W | FC1/FC5 |
| 0x0001 | StopCmd | 정지 명령 | R/W | FC1/FC5 |

## 4. 설정 파일 (DataManager)

| 항목명 | 타입 | 기본값 | 설명 |
|--------|------|--------|------|
| IP | string | "192.168.0.10" | PLC IP 주소 |
| Port | int | 502 | 포트 번호 |
| Timeout | int | 1000 | 통신 타임아웃 |

## 5. 배포

- **장치**: 라즈베리파이 (linux-arm64)
- **앱 이름**: MotorControl
- **자동실행**: Y
- **키오스크 모드**: Y
```

---

## Step 2. .gud 파일 생성

> `ui-json-quick.md` 참조. 브리프 기반으로 Claude가 JSON 생성.

아래는 이 시나리오의 .gud 골격입니다. (실제 작업 시 Claude가 전체 JSON을 생성)

```
MotorControl.gud 구조:
├── GoDesign (1024x600, Dark 테마)
├── Pages
│   ├── PageMain
│   │   └── GoTableLayoutPanel (2행: 상단 모니터링, 하단 제어)
│   │       ├── 상단: GoLamp×2, GoValue(RPM), GoLabel(상태)
│   │       └── 하단: GoButton×2(운전/정지), GoSlider(속도)
│   └── PageSetting
│       └── GoTableLayoutPanel
│           ├── GoInputString(IP), GoInputNumber(Port, Timeout)
│           └── GoButton×2(저장, 돌아가기)
└── Windows: {} (없음)
```

**핵심 규칙 확인:**
- Pages/Windows는 Dictionary `{}` 형태 (Array `[]` 불가)
- 모든 컨트롤에 `{ "Type": "GoButton", "Value": { ... } }` 래핑
- Bounds는 `"L,T,R,B"` 형식
- Enum은 숫자
- 모든 컨트롤에 고유 UUID `Id` 필수

---

## Step 3. UIEditor에서 조정 + MakeCode

사용자가 직접 수행하는 단계입니다.

1. UIEditor 실행
2. `MotorControl.gud` 파일 열기
3. 컨트롤 위치/크기 미세 조정
4. **MakeCode** 실행 → 아래 파일 자동 생성:

```
MotorControl/
├── MotorControl.csproj       ← NuGet 참조 포함
├── design.json               ← 런타임 로드용
├── Program.cs                ← 진입점
├── MainWindow.cs             ← 사용자 파일 (ExistsCheck=true)
├── MainWindow.Designer.cs    ← 자동생성
├── Pages/
│   ├── PageMain.cs           ← 사용자 파일
│   ├── PageMain.Designer.cs  ← 자동생성
│   ├── PageSetting.cs        ← 사용자 파일
│   └── PageSetting.Designer.cs ← 자동생성
```

> MakeCode 후 `*.Designer.cs`와 `design.json`은 **절대 수정 금지** (절대 규칙 #1).

---

## Step 4. C# 코드 구현

> `ui-code.md`, `basis.md` 참조.

MakeCode 완료 후, 생성된 프로젝트 폴더를 Claude Code 작업 디렉터리로 지정합니다.

### 4-1. Main (Program.cs)

```csharp
using MotorControl;

Main.Init();

using var view = new MainWindow();
view.Run();

Main.Stop();

public static class Main
{
    public static DataManager DataMgr { get; private set; } = new DataManager();
    public static DeviceManager DeviceMgr { get; private set; } = new DeviceManager();

    public static void Init()
    {
        DataMgr.Load();       // 설정 로드
        DeviceMgr.Start();    // 통신 시작
    }

    public static void Stop()
    {
        DeviceMgr.Stop();     // 통신 종료
    }
}
```

### 4-2. DataManager

```csharp
using Going.Basis.Datas;

namespace MotorControl
{
    public class SystemSetting
    {
        public string IP { get; set; } = "192.168.0.10";
        public int Port { get; set; } = 502;
        public int Timeout { get; set; } = 1000;
    }

    public class DataManager : DataManager<SystemSetting>
    {
        public DataManager() : base("setting.json") { }
    }
}
```

### 4-3. DeviceManager (Modbus TCP)

```csharp
using Going.Basis.Communications;

namespace MotorControl
{
    public class DeviceManager
    {
        public MasterTCP TCP { get; } = new MasterTCP();

        public DeviceManager()
        {
            // 영역 매핑
            TCP.WordAreas.Add(0x0000, "D");   // D0, D1, D2...
            TCP.BitAreas.Add(0x0000, "P");    // P0, P1, P2...
        }

        // 통신 상태
        public bool IsConnected => TCP.IsOpen;

        // 값 읽기 — 의미있는 프로퍼티로 래핑
        public bool IsRunning    => TCP.GetWord(1, "D0") == 1;   // RunState
        public int  CurrentRPM   => TCP.GetWord(1, "D1") ?? 0;   // CurrentRPM
        public int  ErrorCode    => TCP.GetWord(1, "D2") ?? 0;   // ErrorCode
        public int  TargetSpeed  => TCP.GetWord(1, "D16") ?? 0;  // 0x0010 = 16

        // 쓰기
        public void SetTargetSpeed(int rpm) => TCP.SetWord(1, "D16", rpm);
        public void SetRunCmd(bool on)      => TCP.SetBit(1, "P0", on);
        public void SetStopCmd(bool on)     => TCP.SetBit(1, "P1", on);

        public void Start()
        {
            var setting = Main.DataMgr.Setting;
            TCP.IP      = setting.IP;
            TCP.Port    = setting.Port;
            TCP.Timeout = setting.Timeout;

            // 주기 읽기 등록
            TCP.MonitorWord_F3(1, 0x0000, 3);   // D0~D2 (RunState, RPM, Error)
            TCP.MonitorWord_F3(1, 0x0010, 1);   // D16 (TargetSpeed)
            TCP.MonitorBit_F1(1, 0x0000, 2);    // P0~P1 (RunCmd, StopCmd)

            TCP.Start();
        }

        public void Stop()
        {
            TCP.Stop();
        }
    }
}
```

### 4-4. PageMain.cs — UI 이벤트 + 데이터 반영

```csharp
using Going.UI.Controls;
using Going.UI.Design;

namespace MotorControl.Pages
{
    public partial class PageMain : GoPage
    {
        public PageMain()
        {
            InitializeComponent();

            // 운전 버튼
            btnStart.ButtonClicked += (s, e) =>
            {
                Main.DeviceMgr.SetRunCmd(true);
            };

            // 정지 버튼
            btnStop.ButtonClicked += (s, e) =>
            {
                Main.DeviceMgr.SetStopCmd(true);
            };

            // 속도 슬라이더 변경
            sldSpeed.ValueChanged += (s, e) =>
            {
                Main.DeviceMgr.SetTargetSpeed((int)sldSpeed.Value);
            };

            // 설정 페이지로 이동 (설정 버튼이 있다면)
            // btnSetting.ButtonClicked += (s, e) =>
            // {
            //     MainWindow.Current.Design.SetPage("PageSetting");
            // };
        }

        // 매 프레임 호출 — 통신 데이터를 UI에 반영
        protected override void OnUpdate()
        {
            var dev = Main.DeviceMgr;

            lampRun.OnOff = dev.IsRunning;           // 운전 램프
            lampStop.OnOff = !dev.IsRunning;          // 정지 램프
            valRPM.Value = dev.CurrentRPM;            // RPM 표시
            sldSpeed.Value = dev.TargetSpeed;         // 슬라이더 현재값 동기화
            lblStatus.Text = dev.IsConnected
                ? (dev.IsRunning ? "운전 중" : "정지")
                : "통신 끊김";

            base.OnUpdate();
        }
    }
}
```

### 4-5. PageSetting.cs — 설정 저장/로드

```csharp
using Going.UI.Controls;
using Going.UI.Design;

namespace MotorControl.Pages
{
    public partial class PageSetting : GoPage
    {
        public PageSetting()
        {
            InitializeComponent();

            // 설정값 로드 → UI 반영
            var setting = Main.DataMgr.Setting;
            inpIP.Value = setting.IP;
            inpPort.Value = setting.Port;
            inpTimeout.Value = setting.Timeout;

            // 저장 버튼
            btnSave.ButtonClicked += (s, e) =>
            {
                setting.IP = inpIP.Value;
                setting.Port = (int)inpPort.Value;
                setting.Timeout = (int)inpTimeout.Value;
                Main.DataMgr.Save();
            };

            // 돌아가기 버튼
            btnBack.ButtonClicked += (s, e) =>
            {
                MainWindow.Current.Design.SetPage("PageMain");
            };
        }
    }
}
```

---

## Step 5. 빌드 및 실행

```bash
cd MotorControl
dotnet build
dotnet run
```

> `design.json`이 실행 디렉터리에 있어야 합니다. MakeCode가 `.csproj`에 빌드 복사 설정을 포함하므로 별도 작업 불필요.

---

## 전체 흐름 요약

```
브리프 작성 (project_brief.md)
    ↓ Claude가 인터뷰 진행
.gud 생성 (MotorControl.gud)
    ↓ Claude가 JSON 생성
UIEditor에서 조정 + MakeCode
    ↓ 사용자가 실행
C# 코드 구현
    ↓ Claude Code가 작성
      ├── Program.cs + Main 클래스
      ├── DataManager (설정 로드/저장)
      ├── DeviceManager (Modbus TCP 통신)
      ├── PageMain.cs (모터 제어 UI)
      └── PageSetting.cs (설정 화면)
빌드 + 실행
    ↓ dotnet build → dotnet run
장치 배포 (선택)
    ↓ gtcli deploy (ui-mcp.md 참조)
```
