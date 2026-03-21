# MakeCode 출력 참조 (UIEditor 자동 생성 코드)

> ⚠ **이 파일은 참고용. 일반 C# 작업 시 로드 불필요.**
> UIEditor의 MakeCode()가 생성하는 코드 템플릿을 기록한 레퍼런스입니다.
> 실제 작업 대상은 `*.cs` (사용자 파일)뿐이며, `*.Designer.cs`는 수정 금지입니다.

---

## Program.cs (자동생성 — ExistsCheck=true)

```csharp
using ProjectName;

using var view = new MainWindow();
view.Run();
```

> UIEditor는 최소한의 진입점만 생성. 사용자가 DataManager/DeviceManager 등을 추가.

---

## MainWindow.cs (자동생성 — ExistsCheck=true)

```csharp
using Going.UI.Containers;
using Going.UI.Controls;
using Going.UI.Datas;
using Going.UI.OpenTK.Windows;
using OpenTK.Windowing.Common;
using ProjectName.Pages;
using ProjectName.Windows;

namespace ProjectName
{
    public partial class MainWindow : GoViewWindow
    {
        public MainWindow() : base(1024, 600, WindowBorder.Hidden)
        {
            InitializeComponent();
        }
    }
}
```

> **GoViewWindow** 상속. 모든 프로젝트에서 `GoViewWindow`를 사용.

---

## MainWindow.Designer.cs (자동생성 — ExistsCheck=false, 항상 덮어씀)

```csharp
using System.Text;
using System.Text.Json;
using Going.UI.Containers;
using Going.UI.Controls;
using Going.UI.Datas;
using Going.UI.Design;
using Going.UI.Json;
using Going.UI.OpenTK.Windows;
using Going.UI.Utils;
using Going.UI.Themes;
using OpenTK.Windowing.Common;
using ProjectName.Pages;
using ProjectName.Windows;

namespace ProjectName
{
    public partial class MainWindow
    {
        #region declare
        internal GoDesign DS { get; private set; }
        // TitleBar/SideBar/Footer 안의 Name 있는 컨트롤들이 여기 선언됨
        GoButton btnSideMenu;

        public PageMain PageMain { get; private set; }
        public PageSetting PageSetting { get; private set; }

        public Keypad Keypad { get; private set; }
        #endregion

        #region static
        public static MainWindow Current { get; private set; }
        #endregion

        public void InitializeComponent()
        {
            #region Design Load
            if (!File.Exists("design.json")) throw new Exception("design.json 파일이 없습니다.");
            var json = File.ReadAllText("design.json");
            var ds = GoDesign.JsonDeserialize(json);
            DS = ds;
            #endregion

            #region Window Setting
            Current = this;
            Title = "ProjectName";
            Debug = false;
            VSync = VSyncMode.On;
            CenterWindow();
            #endregion

            #region Design Setting
            Design.UseTitleBar = ds.UseTitleBar;
            Design.UseLeftSideBar = ds.UseLeftSideBar;
            Design.UseRightSideBar = ds.UseRightSideBar;
            Design.UseFooter = ds.UseFooter;
            Design.OverlaySideBar = ds.OverlaySideBar;
            Design.BarColor = ds.BarColor;
            Design.ExpandLeftSideBar = ds.ExpandLeftSideBar;
            Design.ExpandRightSideBar = ds.ExpandRightSideBar;
            #endregion

            #region Theme Setting
            Design.CustomTheme = ds.CustomTheme;
            #endregion

            #region Resources
            foreach (var v in ds.GetImages()) Design.AddImage(v.name, v.images);
            foreach (var v in ds.GetFonts())
                foreach (var f in v.fonts)
                        Design.AddFont(v.name, f);
            #endregion

            #region TitleBar
            {
                var c = ds.TitleBar;
                // MakeDesignBarCode: [GoProperty] 속성 복사 → Childrens 복사 → 컨트롤 매핑
                Design.TitleBar.BarSize = c.BarSize;
                Design.TitleBar.Title = c.Title;
                // ... (모든 [GoProperty] 속성)
                Design.TitleBar.Childrens.AddRange(c.Childrens);

                var dic = Util.AllControls(Design.TitleBar).ToDictionary(x => x.Id.ToString(), y => y);
                btnSideMenu = (GoButton)dic["uuid-here"];
            }
            #endregion

            #region LeftSideBar
            {
                var c = ds.LeftSideBar;
                // ... MakeDesignBarCode 동일 패턴
            }
            #endregion

            // RightSideBar, Footer도 동일

            #region Pages
            PageMain = new PageMain();
            PageSetting = new PageSetting();

            Design.AddPage(PageMain);
            Design.AddPage(PageSetting);

            Design.SetPage("PageMain");  // 첫 번째 페이지가 기본
            #endregion

            #region Windows
            Keypad = new Keypad();

            Design.Windows.Add(Keypad.Name, Keypad);
            #endregion
        }
    }
}
```

---

## PageName.cs (자동생성 — ExistsCheck=true)

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Going.UI.Design;
using Going.UI.ImageCanvas;

namespace ProjectName.Pages
{
    public partial class PageMain : GoPage    // IcPage인 경우: IcPage
    {
        public PageMain()
        {
            InitializeComponent();
        }
    }
}
```

---

## PageName.Designer.cs (자동생성 — ExistsCheck=false, 항상 덮어씀)

```csharp
using System.Text;
using System.Text.Json;
using Going.UI.Containers;
using Going.UI.Controls;
using Going.UI.Datas;
using Going.UI.Design;
using Going.UI.Json;
using Going.UI.OpenTK.Windows;
using Going.UI.Utils;
using Going.UI.ImageCanvas;
using OpenTK.Windowing.Common;

namespace ProjectName.Pages
{
    partial class PageMain
    {
        #region declare
        GoButton btnStart;
        GoLabel lblStatus;
        GoLamp lampComm;
        #endregion

        public void InitializeComponent()
        {
            #region base
            var c = MainWindow.Current.DS.Pages["PageMain"];
            // IcPage인 경우: var c = MainWindow.Current.DS.Pages["PageMain"] as IcPage;

            // MakeDesignBarCode 패턴:
            // 1. [GoProperty] 속성 복사
            this.BackgroundImage = c.BackgroundImage;
            // ... (모든 [GoProperty] 속성)

            // 2. Childrens 복사
            this.Childrens.AddRange(c.Childrens);

            // 3. Name 있는 컨트롤 Id 기준 매핑
            var dic = Util.AllControls(this).ToDictionary(x => x.Id.ToString(), y => y);
            btnStart = (GoButton)dic["a5f8b62e-7135-4cda-86c5-3675b5eeeae1"];
            lblStatus = (GoLabel)dic["7adf6f04-d55c-4476-9eea-672314a2a431"];
            lampComm = (GoLamp)dic["60cc7c64-3502-49db-b64d-8690165dccb3"];
            #endregion
        }
    }
}
```

---

## WindowName.cs (자동생성 — ExistsCheck=true)

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Going.UI.Design;
using Going.UI.ImageCanvas;

namespace ProjectName.Windows
{
    public partial class Keypad : GoWindow
    {
        public Keypad()
        {
            InitializeComponent();
        }
    }
}
```

---

## WindowName.Designer.cs (자동생성 — ExistsCheck=false, 항상 덮어씀)

```csharp
namespace ProjectName.Windows
{
    partial class Keypad
    {
        #region declare
        GoLabel lblValue;
        GoButton btnOk;
        GoButton btnCancel;
        #endregion

        public void InitializeComponent()
        {
            #region base
            var c = MainWindow.Current.DS.Windows["Keypad"];

            // MakeDesignBarCode 동일 패턴
            this.IconString = c.IconString;
            this.Text = c.Text;
            // ... (모든 [GoProperty] 속성)
            this.Childrens.AddRange(c.Childrens);

            var dic = Util.AllControls(this).ToDictionary(x => x.Id.ToString(), y => y);
            lblValue = (GoLabel)dic["uuid-here"];
            btnOk = (GoButton)dic["uuid-here"];
            btnCancel = (GoButton)dic["uuid-here"];
            #endregion
        }
    }
}
```

---

## MakeDesignBarCode 동작 원리

모든 Page/Window/TitleBar/SideBar/Footer의 Designer.cs에서 사용되는 핵심 패턴.
3단계로 구성:

### 1단계: [GoProperty] 속성 복사

design.json에서 로드된 객체(`c`)의 `[GoProperty]` 속성을 `this`(또는 대상 변수)에 복사.

```csharp
{varname}.{PropertyName} = c.{PropertyName};  // 각 [GoProperty] 속성마다
```

대상: `[GoPropertyAttribute]`, `[GoSizePropertyAttribute]`, `[GoSizesPropertyAttribute]` 중 하나가 있고, `[JsonIgnore]`가 아닌 public get/set 프로퍼티.

### 2단계: Childrens 복사

자식 컨트롤 트리를 통째로 복사.

```csharp
{varname}.Childrens.AddRange(c.Childrens);
```

### 3단계: Id 기준 매핑

UIEditor에서 Name이 지정된 컨트롤을 UUID(Id) 기준으로 딕셔너리 검색하여 필드에 할당.

```csharp
var dic = Util.AllControls({varname}).ToDictionary(x => x.Id.ToString(), y => y);
{controlName} = ({TypeName})dic["{controlId}"];  // 각 Name 있는 컨트롤마다
```

> `Util.AllControls()`는 재귀적으로 모든 자식 컨트롤을 flat 리스트로 반환.
> Id는 UIEditor가 생성한 UUID 문자열.
> Name이 없는 컨트롤은 dic 매핑 대상에서 제외됨.
