# Going UI — C# 코드 작성 패턴

UIEditor에서 코드 생성 후 Claude Code가 `*.cs` 파일을 작성할 때 따르는 패턴.

> **컨트롤별 이벤트**는 `controls/*.md` 참조.
> **MakeCode 출력 예시**(Designer.cs 템플릿 등)는 `code-makecode-ref.md` 참조.

## 목차

| # | 섹션 | 설명 |
|---|------|------|
| 1 | using 참조표 | 파일별 using 네임스페이스 화이트리스트 |
| 2 | UIEditor Code 생성 시스템 개요 | MakeCode, ExistsCheck 규칙, 작업 대상 |
| 3 | .csproj 패키지 참조 | NuGet 패키지 (Going.UI, Going.Basis, Going.UI.OpenTK) |
| 4 | 사용자 확장 패턴 | 싱글턴(Main), Program.cs, MainWindow |
| 5 | 페이지 전환 패턴 | Design.SetPage, GoNavigator |
| 6 | Window 표시/숨기기 패턴 | Design.ShowWindow / HideWindow |
| 7 | 설정 데이터 패턴 | INI, Serialize |
| 8 | DataManager 패턴 | JSON 설정 파일 로드/저장 |
| 9 | Page 패턴 | OnUpdate, OnShow, 이벤트 바인딩 |
| 10 | Window 콜백 패턴 | Action 필드, Show 헬퍼, Close |
| 11 | 컨트롤 묶음 패턴 | dic 캐스팅, ChannelUI |
| 12 | GoDialogs 패턴 | MessageBox, InputBox, SelectorBox |

---

## 1. using 참조표

> ⚠ **필요한 using만 선언할 것.** 아래 표에 없는 네임스페이스는 사용 금지 (절대 규칙 #2 — API 추측 금지).

| 네임스페이스 | 포함 내용 | 사용 위치 |
|-----------|---------|---------|
| `Going.UI.Controls` | GoButton, GoLabel, GoLamp, GoSlider, GoInput 등 기본 컨트롤 | Page/Window/MainWindow |
| `Going.UI.Containers` | GoTableLayoutPanel, GoBoxPanel, GoSwitchPanel 등 컨테이너 | Page/Window/MainWindow |
| `Going.UI.Datas` | GoDataGrid, DataGridColumn 관련 | DataGrid 사용 시 |
| `Going.UI.Design` | GoDesign, GoPage, GoWindow, IcPage | Page/Window/MainWindow |
| `Going.UI.Dialogs` | GoDialogs (MessageBox, InputBox, SelectorBox) | 대화상자 사용 시 |
| `Going.UI.Json` | GoJsonConverter | Designer.cs (자동생성) |
| `Going.UI.Utils` | Util.AllControls, Util.FromArgb 등 유틸리티 | Designer.cs (자동생성) |
| `Going.UI.Themes` | GoTheme 커스텀 테마 | Designer.cs (자동생성) |
| `Going.UI.ImageCanvas` | IcPage, IcButton, IcLabel 등 ImageCanvas | IcPage 사용 시 |
| `Going.UI.OpenTK.Windows` | GoViewWindow | MainWindow |
| `Going.Basis.Communications` | MasterRTU, MasterTCP, SlaveRTU, SlaveTCP 등 | DeviceManager |
| `Going.Basis.Datas` | DataManager, INI, Serialize | Program.cs / MainWindow / 설정 |
| `OpenTK.Windowing.Common` | WindowBorder, VSyncMode | MainWindow |

**파일별 using 패턴:**

```csharp
// Program.cs
using ProjectName;

// MainWindow.cs (사용자 파일)
using Going.UI.Containers;
using Going.UI.Controls;
using Going.UI.Datas;
using Going.UI.OpenTK.Windows;
using OpenTK.Windowing.Common;
using ProjectName.Pages;
using ProjectName.Windows;

// PageName.cs (사용자 파일)
using Going.UI.Design;
// + 필요한 것만 추가 (Controls, Containers, Dialogs 등)

// DeviceManager.cs
using Going.Basis.Communications;
```

---

## 2. UIEditor Code 생성 시스템 개요

### 생성 파일 구조

UIEditor에서 Code 생성(MakeCode()) 실행 시 아래 파일들이 자동 생성됨:

```
[프로젝트 루트]
├── ProjectName.sln          ← 솔루션 파일
├── ProjectName.csproj       ← 프로젝트 파일 (NuGet 참조, design.json 빌드 복사 설정 포함)
├── design.json              ← GoDesign 직렬화 (런타임 로드용, UIEditor 전용)
├── Program.cs               ← 진입점 (최소 구조)
├── MainWindow.cs            ← partial class, GoViewWindow 상속 (사용자 영역)
└── MainWindow.Designer.cs   ← InitializeComponent() 자동생성 (항상 덮어씀)

Pages/
├── PageName.cs              ← partial class, GoPage 또는 IcPage 상속 (사용자 로직 영역)
└── PageName.Designer.cs     ← 자동생성 (항상 덮어씀)

Windows/
├── WindowName.cs            ← partial class, GoWindow 상속 (사용자 로직 영역)
└── WindowName.Designer.cs   ← 자동생성 (항상 덮어씀)
```

> **design.json 자동 포함**: UIEditor의 MakeCode 실행 시 `design.json`이 프로젝트 루트에 자동 생성되며, `.csproj`에 빌드 출력 복사 설정이 포함됨. `dotnet publish` 시 자동으로 출력 디렉터리에 포함되므로 별도 복사 불필요.

### ExistsCheck 규칙

| 파일 | ExistsCheck | 동작 |
|------|------------|------|
| `*.cs` (사용자 파일) | `true` | 이미 존재하면 덮어쓰지 않음 → 사용자 코드 보호 |
| `*.Designer.cs` | `false` | 항상 덮어씀 → 수동 수정 무의미 |
| `design.json` | `true` | UIEditor 전용, 코드에서 수정 금지 |

### 클로드 코드 작업 규칙

> ⚠ `*.Designer.cs`, `design.json` 수정 금지 — 상세는 **SKILL.md "절대 규칙 #1"** 참조.
> **작업 대상**: `*.cs` (사용자 파일)만 수정

```
MainWindow.cs      → 서비스 초기화, 전역 이벤트 바인딩
Pages/PageName.cs  → 페이지별 비즈니스 로직, 컨트롤 이벤트
Windows/WndName.cs → 팝업 동작 로직
```

> MakeCode 출력 전체 템플릿(Program.cs, MainWindow.Designer.cs, Page.Designer.cs, Window.Designer.cs 등)은 **code-makecode-ref.md** 참조.

---

## 3. .csproj 패키지 참조

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Going.Basis" Version="*" />
    <PackageReference Include="Going.UI" Version="*" />
    <PackageReference Include="Going.UI.OpenTK" Version="*" />
  </ItemGroup>
</Project>
```

> `Version="*"`로 NuGet 최신 버전 자동 사용. 특정 버전 고정 불필요.

---

## 4. 사용자 확장 패턴

UIEditor가 생성하지 않지만 사용자가 프로젝트에 추가하는 표준 구조.

### 4-1. 전역 싱글턴 패턴 (Main.cs)

Going 프로젝트의 핵심 진입 패턴. `Main` 클래스는 프로젝트 전역에서 매니저와 윈도우에 접근하기 위한 정적 허브 역할.
UIEditor가 생성하지 않으므로 사용자가 직접 정의해야 하며, 프로젝트 전체에서 `Main.Window`, `Main.DevMgr`, `Main.DataMgr`로 참조.

**왜 필요한가**: Going 라이브러리는 DI 컨테이너 없이 경량 정적 접근 패턴을 사용. 이벤트 핸들러, 페이지 간 통신, DeviceManager 접근 등 모든 곳에서 `Main.XXX`로 참조하므로 이 클래스가 없으면 프로젝트가 동작하지 않음.

```csharp
public class Main
{
    public static MainWindow Window { get; set; }
    public static DeviceManager DevMgr { get; set; }
    public static DataManager DataMgr { get; set; }
}
```

> `Main`은 Going 프레임워크 클래스가 아닌 사용자 정의 클래스. 프로퍼티 구성은 프로젝트 요구에 따라 자유롭게 확장 가능 (예: `LogManager`, `AuthManager` 등 추가).

### 4-2. Program.cs 진입점

UIEditor 생성 후 통신 등 서비스를 추가할 때:

```csharp
using ProjectName;

var dataMgr = Main.DataMgr = new DataManager();
var devMgr  = Main.DevMgr  = new DeviceManager();
var wnd     = Main.Window  = new MainWindow();

devMgr.Start();   // 통신 시작
wnd.Run();        // 렌더 루프 (블로킹)
devMgr.Stop();    // 통신 종료

wnd.Dispose();
```

### 4-3. MainWindow 확장 패턴 (MainWindow.cs)

UIEditor가 생성한 `GoViewWindow` 기반에 사용자 로직 추가:

```csharp
public partial class MainWindow : GoViewWindow
{
    public MainWindow() : base(1024, 600, WindowBorder.Hidden)
    {
        InitializeComponent();

        // 컨트롤 이벤트 바인딩
        btnSomething.ButtonClicked += (o, s) => Main.DevMgr.DoSomething();
    }

    // 매 프레임 호출 — UI 상태 갱신
    protected override void OnUpdateFrame(FrameEventArgs args)
    {
        lblTitle.Text = Main.DataMgr.Setting.Title;
        lampComm.OnOff = Main.DevMgr.IsConnected;

        base.OnUpdateFrame(args);
    }

    // 커스텀 렌더링이 필요할 때만 오버라이드
    protected override void OnDraw(SKCanvas canvas, GoTheme thm)
    {
        base.OnDraw(canvas, thm);
    }
}
```

### 이벤트 바인딩 규칙

| 이벤트 | 소속 | 용도 | 예시 |
|--------|------|------|------|
| `ButtonClicked` | GoButton 전용 | 버튼 클릭 처리 | `btnStart.ButtonClicked += (o, s) => { };` |
| `MouseClicked` | GoControl 베이스 (모든 컨트롤) | 일반 클릭 — Keypad 호출, 팝업 등 | `lblValue.MouseClicked += (o, s) => { };` |
| `MouseDoubleClicked` | GoControl 베이스 | 더블클릭 | `ctrl.MouseDoubleClicked += (o, s) => { };` |
| `MouseLongClicked` | GoControl 베이스 | 롱클릭 (길게 누르기) | `ctrl.MouseLongClicked += (o, s) => { };` |

> **GoButton은 `ButtonClicked`를 사용하고, 다른 컨트롤(GoLabel, GoLamp 등)의 클릭은 `MouseClicked`를 사용한다.** `MouseClick`이나 `Click` 이벤트는 존재하지 않는다.

> ⚠ 컨트롤별 상세 이벤트(GoDataGrid, GoSlider, GoInput 등)는 `controls/*.md` 참조.

---

## 5. 페이지 전환 패턴

`Design.SetPage("PageName")`으로 현재 표시 페이지를 변경. Page 클래스명(= .gud에서 설정한 페이지 이름)을 문자열로 전달.

### 기본 전환 (버튼 클릭)

```csharp
// MainWindow.cs 또는 Page.cs 생성자에서
btnGoMain.ButtonClicked += (o, s) => Design.SetPage("PageMain");
btnGoSetting.ButtonClicked += (o, s) => Design.SetPage("PageSetting");
btnGoDetail.ButtonClicked += (o, s) => Design.SetPage("PageDetail");
```

### SideBar 메뉴 전환

```csharp
// MainWindow.cs 생성자 — SideBar 버튼으로 페이지 전환
btnMenuMain.ButtonClicked += (o, s) => Design.SetPage("PageMain");
btnMenuSetting.ButtonClicked += (o, s) => Design.SetPage("PageSetting");
```

### TitleBar 뒤로가기

```csharp
// MainWindow.cs 생성자 — TitleBar의 뒤로가기 버튼
btnBack.ButtonClicked += (o, s) => Design.SetPage("PageMain");  // 메인으로 복귀
```

### GoNavigator 자동 전환 (코드 불필요)

GoNavigator의 GoMenuItem에 `PageName`을 지정하면 메뉴 클릭 시 자동으로 페이지가 전환된다. 별도 이벤트 핸들러 코드가 필요 없다.

```json
// .gud 파일 — TitleBar에 GoNavigator 배치 (Dock: Fill)
"Menus": [
  { "Text": "모니터링", "IconString": "fa-tv", "PageName": "PageMonitor" },
  { "Text": "설정",     "IconString": "fa-cog", "PageName": "PageSetting" }
]
```

> GoNavigator를 TitleBar 컨테이너에 Dock: 5(Fill)로 배치하면 상단 네비게이션 바 역할을 한다.

> **주의**: `Design.SetPage()`의 인자는 Page 클래스명 문자열 (예: `"PageMain"`, `"PageSetting"`). Designer.cs에서 `Design.AddPage()`로 등록한 이름과 일치해야 함. GoMenuItem의 `PageName`도 동일 규칙.

---

## 6. Window 표시/숨기기 패턴

### Design.ShowWindow / HideWindow

GoDesign 인스턴스를 통해 등록된 윈도우를 표시/숨김.

```csharp
// 이름으로 윈도우 표시
Design.ShowWindow("Keypad");

// 인스턴스로 윈도우 표시
Design.ShowWindow(Main.Window.Keypad);

// 윈도우 숨기기
Design.HideWindow(Main.Window.Keypad);
```

> `ShowWindow()`는 `Design.Windows`와 `GoDialogs.SystemWindows` 양쪽을 자동 탐색하므로 시스템 다이얼로그도 이름으로 표시 가능.

### GoWindow의 Show() / Close()

GoWindow 자체 메서드로도 표시/닫기 가능:

```csharp
// Window 내부에서 자기 자신 닫기
Close();

// 외부에서 Window 인스턴스로 표시
Main.Window.Keypad.Show();
```

### 드롭다운 윈도우

```csharp
// 드롭다운 윈도우 (특정 컨트롤 아래에 표시)
Design.ShowDropDownWindow(dropDownWnd);
Design.HideDropDownWindow(dropDownWnd);
```

---

## 7. 설정 데이터 패턴

### 7-1. INI 파일 패턴

`Going.Basis.Datas.INI` 클래스로 Windows INI 파일 읽기/쓰기:

```csharp
using Going.Basis.Datas;

var ini = new INI("config.ini");

// 쓰기
ini.Write("Communication", "PortName", "COM3");
ini.Write("Communication", "Baudrate", "115200");

// 읽기
string port = ini.Read("Communication", "PortName");       // "COM3"
string baud = ini.Read("Communication", "Baudrate");       // "115200"

// 존재 여부 확인
if (ini.ExistsINI()) { /* ... */ }

// 섹션 삭제
ini.DeleteSection("Communication");
```

> INI는 단순 키-값 설정에 적합. 복잡한 구조는 JSON(Serialize 또는 DataManager 패턴) 사용 권장.

### 7-2. Serialize 유틸리티

`Going.Basis.Datas.Serialize` 정적 클래스로 JSON/XML/Binary 직렬화:

```csharp
using Going.Basis.Datas;

// JSON — 문자열
string json = Serialize.JsonSerialize(setting);
var obj = Serialize.JsonDeserialize<SystemSetting>(json);

// JSON — 파일
Serialize.JsonSerializeToFile("setting.json", setting);
var loaded = Serialize.JsonDeserializeFromFile<SystemSetting>("setting.json");

// XML — 파일
Serialize.XmlSerializeToFile("config.xml", setting, typeof(SystemSetting));
var xmlObj = Serialize.XmlDeserializeFromFile("config.xml", typeof(SystemSetting));

// Binary (구조체) — 바이트 배열
byte[] raw = Serialize.RawSerialize(myStruct);
var restored = Serialize.RawDeserialize<MyStruct>(raw);
```

> `Serialize`는 `System.Text.Json` / `System.Xml` 래퍼. `JsonSerializerOptions`를 옵션으로 전달 가능.

---

## 8. DataManager 패턴 (Managers/DataManager.cs)

설정 파일 로드/저장 담당. `System.Text.Json` 직접 사용 또는 `Serialize` 유틸리티 사용.

### 기본 패턴

```csharp
public class DataManager
{
    const string PATH = "setting.json";
    public SystemSetting Setting { get; set; }

    public DataManager()
    {
        Setting = new SystemSetting();
        if (File.Exists(PATH))
        {
            var obj = JsonSerializer.Deserialize<SystemSetting>(File.ReadAllText(PATH));
            if (obj != null) Setting = obj;
        }
    }

    public void Save()
    {
        File.WriteAllText(PATH, JsonSerializer.Serialize(Setting));
    }
}
```

### 설정 DTO (Datas/SystemSetting.cs)

JSON 직렬화 가능한 설정 클래스. 프로젝트 요구에 맞게 프로퍼티를 자유롭게 구성.

```csharp
public class SystemSetting
{
    public string PortName  { get; set; } = "COM1";
    public int    Baudrate  { get; set; } = 115200;
    public int    Timeout   { get; set; } = 500;
}
```

---

## 9. Page 패턴 (Pages/PageXxx.cs)

생성자에서 이벤트 바인딩, `OnUpdate()`에서 데이터 → 컨트롤 반영.

```csharp
public partial class PageMain : GoPage
{
    public PageMain()
    {
        InitializeComponent();

        // 버튼 이벤트
        btnStart.ButtonClicked += (o, s) =>
        {
            Main.DevMgr.SetOutput(0x0010, 1);
        };

        // 값 입력 — Keypad 팝업
        lblSetpoint.MouseClicked += (o, s) =>
        {
            Main.Window.Keypad.ShowKeypad(Main.DevMgr.Data.Setpoint, (value) =>
            {
                Main.DevMgr.SetSetpoint(value);
            });
        };
    }

    // OnUpdate — 매 프레임 컨트롤 상태 갱신 (Page 단위)
    protected override void OnUpdate()
    {
        var data = Main.DevMgr.Data;

        // 통신 상태에 따른 색상
        lampComm.OnOff       = data.CommState;
        lblTemp.Text         = data.CommState ? $"{data.Temperature:F1} °C" : "---";
        lblTemp.TextColor    = data.CommState ? "Fore" : "Base4";

        // 운전 상태에 따른 버튼 색상
        btnStart.ButtonColor = data.RunState ? "Good"  : "Base3";
        btnStop.ButtonColor  = data.RunState ? "Base3" : "Error";

        base.OnUpdate();
    }
}
```

### Page 라이프사이클

| 메서드 | 호출 시점 | 용도 |
|--------|---------|------|
| `OnUpdate()` | 매 프레임 (현재 페이지일 때) | 데이터 → 컨트롤 갱신 |
| `OnShow()` | 페이지가 표시될 때 (SetPage 직후) | 초기화, 데이터 새로고침 |
| 생성자 | 객체 생성 시 1회 | 이벤트 바인딩, 초기 설정 |

---

## 10. Window 콜백 패턴 (Windows/XxxWindow.cs)

`GoWindow` 상속. 헬퍼 메서드로 콜백 기반 표시.

### 기본 Keypad 패턴

```csharp
public partial class Keypad : GoWindow
{
    Action<int>? _callback;

    public Keypad()
    {
        InitializeComponent();

        btnOk.ButtonClicked += (o, s) =>
        {
            if (int.TryParse(lblValue.Text, out var v))
                _callback?.Invoke(v);
            Close();
        };

        btnCancel.ButtonClicked += (o, s) => Close();
    }

    // 외부에서 호출하는 헬퍼
    public void ShowKeypad(int current, Action<int> callback)
    {
        _callback = callback;
        lblValue.Text = current.ToString();
        Show();
    }
}
```

### 범용 설정 윈도우 패턴

여러 값을 입력받고 결과를 콜백으로 반환:

```csharp
public partial class SettingWindow : GoWindow
{
    Action<string, int>? _callback;

    public SettingWindow()
    {
        InitializeComponent();

        btnOk.ButtonClicked += (o, s) =>
        {
            _callback?.Invoke(inpName.Text, (int)inpTimeout.Value);
            Close();
        };

        btnCancel.ButtonClicked += (o, s) => Close();
    }

    public void ShowSetting(string name, int timeout, Action<string, int> callback)
    {
        _callback = callback;
        inpName.Text = name;
        inpTimeout.Value = timeout;
        Show();
    }
}

// 호출 측 (Page에서)
btnSetting.ButtonClicked += (o, s) =>
{
    var setting = Main.DataMgr.Setting;
    Main.Window.SettingWnd.ShowSetting(setting.Name, setting.Timeout, (name, timeout) =>
    {
        setting.Name = name;
        setting.Timeout = timeout;
        Main.DataMgr.Save();
    });
};
```

> **핵심 패턴**: Show 헬퍼에서 현재 값 세팅 + `Action` 콜백 저장 → `Show()` 호출 → OK 시 콜백 실행 + `Close()`. WinForms의 `ShowDialog()`/`DialogResult`와 다름 — Going은 **비동기 콜백** 방식.

---

## 11. 컨트롤 묶음 패턴

반복되는 컨트롤 그룹(채널, 슬롯 등)을 클래스로 묶어 관리.
Designer.cs에서 Name으로 컨트롤을 찾아 바인딩.

```csharp
// 컨트롤 묶음 클래스
public class ChannelUI(int idx, GoLabel name, GoLamp state, GoLabel value)
{
    public int     Index  => idx;
    public GoLabel Name   => name;
    public GoLamp  State  => state;
    public GoLabel Value  => value;

    public bool Visible
    {
        get => name.Visible;
        set => name.Visible = state.Visible = value.Visible = value;
    }

    public void SetTag()
    {
        name.Tag = state.Tag = value.Tag = this;
    }
}

// PageMain 생성자에서 Name 기반으로 컨트롤 묶음 초기화
var dic = tbl.Childrens.Where(x => x.Name != null).ToDictionary(x => x.Name!, y => y);
for (int i = 0; i < 16; i++)
{
    if (dic.TryGetValue($"lblName{i+1}",  out var vn) &&
        dic.TryGetValue($"lamp{i+1}",     out var vl) &&
        dic.TryGetValue($"lblValue{i+1}", out var vv) &&
        vn is GoLabel ln && vl is GoLamp ll && vv is GoLabel lv)
    {
        Channels[i] = new ChannelUI(i, ln, ll, lv);
        Channels[i].SetTag();
    }
}
```

> Designer.cs의 `dic`은 `Id`(UUID) 기준이지만, 사용자 코드에서 반복 컨트롤을 묶을 때는 `Name` 기준 딕셔너리가 편리하다.

---

## 12. GoDialogs 패턴 (시스템 다이얼로그)

`GoDialogs`는 전역 싱글턴 다이얼로그. 별도 Window 정의 없이 사용 가능.
콜백 기반 — 결과를 `Action`으로 수신.
네임스페이스: `Going.UI.Dialogs`

### 12-1. MessageBox

확인/취소/예/아니요 조합의 메시지 다이얼로그.

```csharp
using Going.UI.Dialogs;

// OK만
GoDialogs.MessageBox.ShowMessageBoxOk("알림", "작업이 완료되었습니다.", (result) =>
{
    // result: GoDialogResult.Ok
});

// OK + Cancel
GoDialogs.MessageBox.ShowMessageBoxOkCancel("확인", "저장하시겠습니까?", (result) =>
{
    if (result == GoDialogResult.Ok)
        Main.DataMgr.Save();
});

// Yes + No
GoDialogs.MessageBox.ShowMessageBoxYesNo("종료", "프로그램을 종료하시겠습니까?", (result) =>
{
    if (result == GoDialogResult.Yes)
        Environment.Exit(0);
});

// Yes + No + Cancel
GoDialogs.MessageBox.ShowMessageBoxYesNoCancel("변경", "변경사항을 저장하시겠습니까?", (result) =>
{
    if (result == GoDialogResult.Yes) Main.DataMgr.Save();
    else if (result == GoDialogResult.No) { /* 저장 안 함 */ }
    // Cancel이면 아무것도 안 함
});
```

버튼 텍스트 커스텀:

```csharp
GoDialogs.MessageBox.YesText = "저장";
GoDialogs.MessageBox.NoText = "버리기";
GoDialogs.MessageBox.OkText = "확인";
GoDialogs.MessageBox.CancelText = "취소";
```

### 12-2. InputBox

문자열/숫자/불리언/제네릭 타입 값 입력 다이얼로그.

```csharp
// 문자열 입력
GoDialogs.InputBox.ShowString("이름 입력", "홍길동", (value) =>
{
    if (value != null) Main.DataMgr.Setting.UserName = value;
});

// 숫자 입력 (범위 지정)
GoDialogs.InputBox.ShowNumber<int>("설정값", 100, 0, 1000, (value) =>
{
    if (value.HasValue) Main.DevMgr.SetOutput(1, "D100", value.Value);
});

// 불리언 입력 (텍스트 지정)
GoDialogs.InputBox.ShowBool("자동 모드", true, "자동", "수동", (value) =>
{
    if (value.HasValue) Main.DevMgr.SetBitOutput(1, "P0", value.Value);
});

// 제네릭 클래스 프로퍼티 기반 입력
GoDialogs.InputBox.Showinputbox<SystemSetting>("설정 편집", Main.DataMgr.Setting, (value) =>
{
    if (value != null) Main.DataMgr.Setting = value;
});
```

InputBox 레이아웃 설정:

```csharp
GoDialogs.InputBox.ItemHeight = 40;       // 각 항목 높이 (px)
GoDialogs.InputBox.ItemTitleWidth = 80;   // 타이틀 너비
GoDialogs.InputBox.ItemValueWidth = 150;  // 값 영역 너비
```

### 12-3. SelectorBox

체크박스(다중)/라디오(단일)/콤보(드롭다운) 선택 다이얼로그.

```csharp
// Enum 라디오 선택 (단일)
GoDialogs.SelectorBox.ShowRadio<MyEnum>("모드 선택", 2, MyEnum.Mode1, (value) =>
{
    if (value.HasValue) Main.DataMgr.Setting.Mode = value.Value;
});

// Enum 체크 선택 (다중)
GoDialogs.SelectorBox.ShowCheck<MyEnum>("항목 선택", 3, selectedList, (values) =>
{
    if (values != null) { /* values: List<MyEnum> */ }
});

// Enum 콤보 선택 (드롭다운)
GoDialogs.SelectorBox.ShowCombo<MyEnum>("선택", MyEnum.Option1, (value) =>
{
    if (value.HasValue) { /* ... */ }
});

// GoListItem 목록으로 라디오 선택
var items = new List<GoListItem>
{
    new GoListItem { Text = "항목1", Tag = "A" },
    new GoListItem { Text = "항목2", Tag = "B" },
};
GoDialogs.SelectorBox.ShowRadio("선택", 1, items, null, (selected) =>
{
    if (selected != null) { /* selected: GoListItem */ }
});
```

> GoDialogs.SystemWindows(MessageBox, SelectorBox, InputBox)는 프레임워크가 자동 관리함.
> `GoDesign.Init()`이 SystemWindows를 자동 초기화하고, `ShowWindow()`가 `Design.Windows`와 `GoDialogs.SystemWindows` 양쪽을 자동 탐색하므로 별도 등록 코드 불필요.

---

## 관련 문서

| 문서 | 용도 |
|------|------|
| `controls/*.md` | 컨트롤별 이벤트명 + C# 사용 예제 |
| `comm-pattern.md` | DeviceManager/DeviceData 통신 코드 패턴 |
| `code-makecode-ref.md` | MakeCode 출력 템플릿 (참고용) |
| `session-context.md` | 세션 간 컨텍스트 유지 |
