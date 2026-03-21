# Going UI -- .gud 파일 구조 레퍼런스

> **.gud 파일의 최상위 구조, 페이지/윈도우/바 레이아웃, 공통 속성 규칙, 테마 색상을 정의한다.**
> 컨트롤별 JSON 템플릿은 이 문서에 포함하지 않는다.

> **⚠ 컨트롤 JSON은 반드시 `controls/` 에서 로드하라.**
> **⚠ Enum 전체 목록은 `enums-reference.md` 를 참조하라.**

---

## 1. GoDesign JSON 최상위 구조

.gud 파일은 GoDesign 객체를 직접 직렬화한 **단일 JSON**이다. 배열이나 래퍼 객체로 감싸지 않는다.

```json
{
  "Name": "ProjectName",
  "DesignWidth": 1024,
  "DesignHeight": 600,
  "ProjectFolder": "None",
  "Pages": { },
  "Windows": { },
  "Images": {},
  "Fonts": {},
  "TitleBar": { ... },
  "LeftSideBar": { ... },
  "RightSideBar": { ... },
  "Footer": { ... },
  "UseTitleBar": false,
  "UseLeftSideBar": false,
  "UseRightSideBar": false,
  "UseFooter": false,
  "BarColor": "Base2",
  "OverlaySideBar": false,
  "ExpandLeftSideBar": false,
  "ExpandRightSideBar": false,
  "CustomTheme": null
}
```

### 최상위 속성 설명

| 속성 | 타입 | 설명 |
|------|------|------|
| `Name` | string | 프로젝트 이름. **유효한 C# 식별자** 필수 (영문+숫자+밑줄, 영문/밑줄로 시작, 한글/띄어쓰기 불가) |
| `DesignWidth` | int | 디자인 기준 너비 (px). 기본 1024 |
| `DesignHeight` | int | 디자인 기준 높이 (px). 기본 600 |
| `ProjectFolder` | string | 프로젝트 폴더 경로. 일반적으로 `"None"` |
| `Pages` | Dictionary | 페이지 컬렉션 (**Dictionary, NOT Array!**) |
| `Windows` | Dictionary | 윈도우 컬렉션 (**Dictionary, NOT Array!**) |
| `Images` | Dictionary | 이미지 리소스 딕셔너리 (Key=리소스명, Value=Base64 문자열) |
| `Fonts` | Dictionary | 커스텀 폰트 딕셔너리 (일반적으로 비어 있음 -- 나눔고딕 기본 내장) |
| `UseTitleBar` | bool | 타이틀바 사용 여부 |
| `UseLeftSideBar` | bool | 왼쪽 사이드바 사용 여부 |
| `UseRightSideBar` | bool | 오른쪽 사이드바 사용 여부 |
| `UseFooter` | bool | 푸터 사용 여부 |
| `BarColor` | string | 바 영역 색상. 기본 `"Base2"` |
| `OverlaySideBar` | bool | 사이드바 오버레이 모드 |
| `ExpandLeftSideBar` | bool | 왼쪽 사이드바 펼침 여부 |
| `ExpandRightSideBar` | bool | 오른쪽 사이드바 펼침 여부 |
| `CustomTheme` | object/null | 사용자 정의 테마. null이면 기본 DarkTheme 사용 |

> **Name 규칙**: `DataLogger` (O), `OilRecovery_V09` (O), `유증기 GUI` (X), `My Project` (X), `3DViewer` (X).
> 사용자가 한글/띄어쓰기가 포함된 이름을 요청하면 영문 PascalCase 이름을 제안할 것.

### Images / Fonts

```json
"Images": {
  "bg_off": "Base64 문자열",
  "bg_on": "Base64 문자열"
},
"Fonts": {}
```

- UIEditor의 이미지 관리 기능으로 추가/삭제하는 것을 권장
- .gud에서 수동으로 추가하려면 Key(리소스명)와 Value(Base64 문자열)을 직접 작성

### CustomTheme

null이면 기본 DarkTheme 사용. 커스텀 테마를 지정하려면 C# 코드에서 GoTheme을 상속하여 작성한다.

**색상 값 설정 방법 (C# 코드):**
- `SKColors.Red`, `SKColors.DarkOrange` — SkiaSharp 기본 색상명 사용
- `Util.FromArgb(50, 50, 50)` — RGB 직접 지정
- `Base1` — 같은 테마 내 다른 키 참조 가능

```csharp
// C# 코드에서 커스텀 테마 작성 예시
public class MyTheme : GoTheme
{
    public MyTheme()
    {
        Dark = true;
        Alpha = 60;

        // SKColors 색상명 사용
        Fore = SKColors.White;
        Point = SKColors.DarkRed;
        Good = SKColors.Green;
        Warning = SKColors.DarkOrange;
        Danger = SKColors.DarkRed;
        Error = SKColors.Red;
        Highlight = SKColors.Cyan;
        Select = SKColors.Teal;

        // Util.FromArgb(R, G, B)로 RGB 직접 지정
        Back = Util.FromArgb(50, 50, 50);
        Window = Util.FromArgb(32, 32, 32);
        WindowBorder = Util.FromArgb(90, 90, 90);
        Title = Util.FromArgb(70, 70, 70);

        // Base0~5: 밝기 단계별 배경색
        Base0 = Util.FromArgb(0, 0, 0);
        Base1 = Util.FromArgb(30, 30, 30);
        Base2 = Util.FromArgb(60, 60, 60);
        Base3 = Util.FromArgb(90, 90, 90);
        Base4 = Util.FromArgb(120, 120, 120);
        Base5 = Util.FromArgb(150, 150, 150);

        // 다른 키 참조
        ScrollBar = Base1;
        ScrollCursor = Base3;

        // 렌더링 파라미터
        Corner = 5;
        DownBrightness = -0.25F;
        BorderBrightness = -0.3F;
        HoverBorderBrightness = 0.5F;
        HoverFillBrightness = 0.15F;
        ShadowAlpha = 180;
    }
}
```

**적용 방법:** `MainWindow` 생성자에서 `GoTheme.Current = new MyTheme();` 호출.

> **.gud JSON 내부의 CustomTheme 필드**: UIEditor에서 테마를 설정하면 ARGB uint 값으로 직렬화된다.
> 이 숫자를 직접 편집하지 말고, C# 코드에서 테마 클래스를 작성하여 적용하라.

SKColor는 uint(ARGB). 예: White=4294967295, Black=4278190080.

---

## 2. Pages / Windows Dictionary 형식

> **⚠ 절대 규칙: Pages와 Windows는 Array `[]`가 아니라 Dictionary `{}` 형태!**

```
// 올바른 형식
"Pages": { "PageMain": { "Type": "GoPage", "Value": { ... } } }

// 틀린 형식 -- 절대 사용 금지!
"Pages": [{ "Type": "GoPage", "Name": "PageMain" }]
```

- Key = 페이지/윈도우의 Name
- Value = `{ "Type": "...", "Value": { ... } }` 래핑 객체
- `"Value"` 래핑이 **반드시** 있어야 함 (GoPagesConverter/GoWindowsConverter가 `Type` -> `Value` 순서로 역직렬화)
- 컨트롤 배열 프로퍼티명은 **`"Childrens"`** (`"Controls"` 아님!)

> **⚠ 컨트롤 JSON은 반드시 `controls/` 에서 로드하라.** 이 문서에는 컨트롤별 템플릿을 포함하지 않는다.

---

## 3. GoPage JSON 구조

```json
"Pages": {
  "PageMain": {
    "Type": "GoPage",
    "Value": {
      "Childrens": [],
      "BackgroundImage": null,
      "Id": "UUID",
      "Name": "PageMain",
      "Visible": true,
      "Enabled": true,
      "Selectable": false,
      "Bounds": "0,0,1024,600",
      "Dock": 0,
      "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
    }
  }
}
```

- `Bounds`는 `"0,0,DesignWidth,DesignHeight"` 로 설정
- `Childrens`에 자식 컨트롤 배열을 배치

### IcPage (ImageCanvas 페이지)

GoPage를 상속하며 추가 속성:

```json
"PageMain": {
  "Type": "IcPage",
  "Value": {
    "BackgroundColor": "white",
    "OffImage": null,
    "OnImage": null,
    "Childrens": [],
    "BackgroundImage": null,
    "Id": "UUID", "Name": "PageMain",
    "Visible": true, "Enabled": true, "Selectable": false,
    "Bounds": "0,0,1024,600", "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

---

## 4. GoWindow JSON 구조

```json
"Windows": {
  "Keypad": {
    "Type": "GoWindow",
    "Value": {
      "IconString": "fa-calculator",
      "IconSize": 12,
      "IconGap": 10,
      "Text": "Window",
      "FontName": "나눔고딕",
      "FontStyle": 0,
      "FontSize": 12,
      "TextColor": "Fore",
      "WindowColor": "Back",
      "BorderColor": "Base2",
      "Round": 1,
      "TitleHeight": 40,
      "Childrens": [],
      "Id": "UUID",
      "Name": "Keypad",
      "Visible": true,
      "Enabled": true,
      "Selectable": false,
      "Bounds": "0,0,400,500",
      "Dock": 0,
      "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
    }
  }
}
```

> GoWindow에는 `IconDirection` 속성이 **없다**. `IconGap`만 존재.

---

## 5. TitleBar / SideBar / Footer JSON 구조

### GoTitleBar

```json
"TitleBar": {
  "Visible": false,
  "BarSize": 50,
  "Title": "Title",
  "TitleImage": null,
  "LeftExpandIconString": "fa-bars",
  "LeftCollapseIconString": "fa-chevron-left",
  "RightExpandIconString": "fa-ellipsis-vertical",
  "RightCollapseIconString": "fa-chevron-right",
  "IconSize": 16,
  "TextColor": "Fore",
  "FontName": "나눔고딕",
  "FontStyle": 0,
  "FontSize": 16,
  "Childrens": [],
  "Id": "UUID",
  "Name": null,
  "Bounds": "0,0,0,0",
  "Dock": 0,
  "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
}
```

### GoSideBar (LeftSideBar / RightSideBar)

```json
"LeftSideBar": {
  "Visible": false,
  "BarSize": 150,
  "Fixed": false,
  "Childrens": [],
  "Id": "UUID",
  "Name": null,
  "Bounds": "0,0,0,0",
  "Dock": 0,
  "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
}
```

- `Fixed`: true면 접기/펴기 불가
- `Expand`는 런타임 전용 (JsonIgnore) -- .gud에 포함하지 않음

### GoFooter

```json
"Footer": {
  "Visible": false,
  "BarSize": 40,
  "Childrens": [],
  "Id": "UUID",
  "Name": null,
  "Bounds": "0,0,0,0",
  "Dock": 0,
  "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
}
```

---

## 6. 공통 속성 규칙 (GoControl)

모든 컨트롤에 포함되는 기본 속성:

```json
{
  "Id": "UUID",
  "Name": null,
  "Visible": true,
  "Enabled": true,
  "Selectable": false,
  "Bounds": "0,0,70,30",
  "Dock": 0,
  "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 },
  "UseLongClick": false,
  "LongClickTime": null
}
```

### Bounds -- `"Left,Top,Right,Bottom"` 형식

**`"L,T,R,B"` = 좌상 좌표(L,T)에서 우하 좌표(R,B)까지. Width/Height가 아님!**

```
"10,20,210,70" = 좌표(10,20)에서 좌표(210,70)까지 -> 폭 200, 높이 50
```

### Dock (GoDockStyle)

| 값 | 의미 |
|----|------|
| 0 | None (절대 좌표 배치) |
| 1 | Left |
| 2 | Top |
| 3 | Right |
| 4 | Bottom |
| 5 | Fill (부모 영역 전체 채우기) |

> **`Fill` 프로퍼티는 존재하지 않는다!** `"Dock": 5`가 Fill 역할.

### Margin

반드시 **객체** 형식. 문자열 `"0,0,0,0"` 불가!

```json
"Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
```

### 기타 공통 규칙

- `Selectable`은 `protected set` -- JSON에 포함되지만 직접 설정 불가 (컨트롤 타입에 따라 자동 결정)
- 기본 `FontSize`는 **12**. TitleBar 등 특수 영역만 16 이상
- 모든 컨트롤은 `{ "Type": "GoXxx", "Value": { ... } }` 래퍼로 감싸야 함
- 컨트롤 배열 프로퍼티명은 **`"Childrens"`** (`"Controls"` 아님)

> **⚠ 컨트롤별 고유 속성과 JSON 템플릿은 `controls/` 디렉토리의 개별 파일을 참조하라.**

---

## 7. 이미지 기반 좌표 계산 방법

레이아웃 이미지가 제공된 경우, 아래 절차를 따라 Bounds를 산출한다.

### Step 1 -- 화면 해상도 확인

프로젝트 해상도 (DesignWidth x DesignHeight)를 확인한다. 기본: 1024x600.

### Step 2 -- 이미지 내 영역 비율 추출

이미지에서 각 컨트롤이 차지하는 위치를 **비율(0.0~1.0)** 로 추정한다.

```
컨트롤이 이미지 가로의 약 10%~30%, 세로의 약 5%~15% 영역에 위치
-> xRatio=0.10, yRatio=0.05, wRatio=0.20, hRatio=0.10
```

### Step 3 -- 픽셀 좌표 변환

```
L = round(W x xRatio)               = round(1024 x 0.10) = 102
T = round(H x yRatio)               = round(600 x 0.05)  = 30
R = round(W x (xRatio + wRatio))    = round(1024 x 0.30) = 307
B = round(H x (yRatio + hRatio))    = round(600 x 0.15)  = 90
-> Bounds = "102,30,307,90"
```

### Step 4 -- 정렬/간격 보정

- 같은 행의 컨트롤은 T, B를 통일
- 같은 열의 컨트롤은 L, R을 통일
- 컨트롤 간 간격: 최소 5px, 권장 10px
- 화면 가장자리 여백: 최소 10px

### Step 5 -- 검증

- R > L, B > T 확인
- 컨트롤이 화면 밖으로 나가지 않는지 (R <= DesignWidth, B <= DesignHeight)
- 겹치는 컨트롤이 없는지

### 권장 크기 참고표

| 컨트롤 | 최소 (WxH) | 권장 (WxH) |
|--------|-----------|-----------|
| GoButton | 60x30 | 100x40 |
| GoLabel | 50x25 | 80x30 |
| GoLamp | 60x30 | 80x30 |
| GoValue* | 80x30 | 120x40 |
| GoInput* | 80x30 | 150x40 |
| GoSlider | 150x50 | 200x40 |
| GoGauge/GoMeter | 100x100 | 150x150 |
| GoDataGrid | 200x100 | 400x300 |
| GoProgress | 100x20 | 200x30 |
| GoKnob | 80x80 | 120x120 |

### 이미지 참조 규칙

- 이미지의 레이아웃을 **우선 참조** (텍스트와 충돌 시 이미지 우선)
- 이미지에서 읽기 어려운 컨트롤은 텍스트로 보완
- **이미지를 우선하되, 애매한 요소를 추측하지 말 것** -- 반드시 사용자에게 확인
- 레지스터 맵은 이미지만으로 판단 불가 -- 반드시 문의

---

## 8. 직렬화 규칙

| 규칙 | 올바른 예 | 흔한 실수 |
|------|----------|----------|
| 컨트롤 래퍼 | `{ "Type": "GoButton", "Value": { ... } }` | Value 없이 속성 직접 나열 |
| Bounds | `"10,10,210,60"` (L,T,R,B 문자열) | W,H로 착각 |
| Enum | 숫자 `0`, `1`, `5` | 문자열 `"Normal"`, `"Fill"` |
| Margin / TextPadding | `{"Left":0,...}` 객체 | 문자열 `"0,0,0,0"` |
| Dock=Fill | `"Dock": 5` | `"Fill": true` |
| Id | 고유 UUID 필수 | 누락 또는 중복 |
| 컨트롤 배열명 | `"Childrens"` | `"Controls"` |
| 색상 값 | 테마 키 `"Fore"` 또는 CSS 색상명 `"red"` | ARGB 숫자 직접 사용 (CustomTheme 내부 제외) |
| GoTableLayoutPanel Childrens | `{"indexes":{...},"ls":[...]}` 객체 | 일반 배열 |
| GoTableLayoutPanel 열 병합 | `"ColSpan"` | `"ColumnSpan"` |

> **Enum 값은 .gud JSON에서 반드시 숫자로 직렬화하라. 문자열 불가!**
> Enum 전체 목록은 `enums-reference.md`를 참조.

---

## 9. GoTheme 색상 키 목록

컨트롤의 색상 속성 (`TextColor`, `ButtonColor`, `BorderColor` 등)은 아래 문자열 키를 사용한다.

### 기본 색상

| 키 | 용도 |
|----|------|
| `Fore` | 기본 텍스트 (전경) 색상 |
| `Back` | 기본 배경 색상 |
| `Window` | 윈도우 배경 색상 |
| `WindowBorder` | 윈도우 테두리 색상 |
| `Point` | 포인트/강조 색상 |
| `Title` | 타이틀바 배경 색상 |

### 기본 팔레트 (Base0~Base5)

| 키 | 용도 |
|----|------|
| `Base0` | 가장 어두운 배경 |
| `Base1` | 어두운 배경 |
| `Base2` | 중간 어두운 배경 |
| `Base3` | 중간 밝은 배경 |
| `Base4` | 밝은 배경 |
| `Base5` | 가장 밝은 배경 |

> Base0(어두움) -> Base5(밝음) 순서. 컨트롤의 ButtonColor, BoxColor 등에 사용.

### 상태 색상

| 키 | 용도 |
|----|------|
| `Good` | 정상/OK (초록 계열) |
| `Warning` | 경고 (노랑 계열) |
| `Danger` | 위험 (빨강 계열) |
| `Error` | 에러 표시 |
| `Highlight` | 하이라이트 |
| `Select` | 선택 항목 |

### 사용자 정의 색상

| 키 | 용도 |
|----|------|
| `User1` ~ `User9` | 사용자 정의 색상 슬롯 |

### 기타

| 키 | 용도 |
|----|------|
| `ScrollBar` | 스크롤바 트랙 |
| `ScrollCursor` | 스크롤바 커서 |
| `Transparent` | 투명 |

### CSS 색상명 직접 사용

테마 키 외에 CSS 기본 색상명도 직접 사용 가능:
`"lime"`, `"red"`, `"gray"`, `"blue"`, `"white"`, `"black"` 등

---

## 10. GoTheme.ToColor() 메서드

```csharp
SKColor ToColor(string? color)
```

색상 이름 문자열을 SKColor로 변환한다.

- 테마 키 지원: `"Fore"`, `"Back"`, `"Base0"`~`"Base5"`, `"User1"`~`"User9"`, `"Good"`, `"Warning"`, `"Danger"`, `"Error"`, `"Highlight"`, `"Select"` 등
- CSS 색상명 지원: `"red"`, `"lime"`, `"blue"` 등
- .gud JSON에서 컨트롤 색상 속성에 지정하는 문자열은 모두 이 메서드를 통해 해석됨

### 렌더링 파라미터 (GoTheme)

| 속성 | 타입 | 설명 |
|------|------|------|
| `Corner` | int | 모서리 반지름 (px). 기본값 5 |
| `Alpha` | int | 전체 투명도 |
| `ShadowAlpha` | byte | 그림자 투명도 |
| `DownBrightness` | float | 눌림 상태 밝기 조정 |
| `BorderBrightness` | float | 테두리 밝기 조정 |
| `HoverBorderBrightness` | float | 마우스 오버 시 테두리 밝기 |
| `HoverFillBrightness` | float | 마우스 오버 시 채우기 밝기 |
| `GradientLightBrightness` | float | 그라데이션 밝은 끝. 기본 +0.2 |
| `GradientDarkBrightness` | float | 그라데이션 어두운 끝. 기본 -0.2 |
| `StageLineBrightness` | float | 스테이지 라인 밝기 조정 |

---

## 11. 검증 체크리스트

.gud 파일을 생성하거나 수정한 후, **Write/Edit 도구로 저장하기 전에** 아래 항목을 반드시 확인한다. 하나라도 위반하면 UIEditor에서 열리지 않거나 런타임 예외가 발생한다.

### 구조 검증

- [ ] **최상위가 GoDesign 단일 JSON** 인가 (배열이나 래퍼 객체 없음)
- [ ] **Name**이 유효한 C# 식별자인가 (영문+숫자+밑줄, 한글/띄어쓰기 불가)
- [ ] **Pages가 Dictionary `{}`** 인가 (Array `[]` 불가)
- [ ] **Windows가 Dictionary `{}`** 인가 (Array `[]` 불가)
- [ ] 각 Page/Window가 **`"Type"` + `"Value"` 래퍼**로 감싸져 있는가
- [ ] 컨트롤 배열 프로퍼티명이 **`"Childrens"`** 인가 (`"Controls"` 아님)

### 컨트롤 검증

- [ ] **모든 컨트롤**에 `{ "Type": "GoXxx", "Value": { ... } }` 래퍼가 있는가
- [ ] **모든 컨트롤**에 고유한 **Id (UUID)** 가 있는가 -- 중복 없음
- [ ] **Bounds**가 `"L,T,R,B"` 문자열인가 (R>L, B>T 확인, W/H 아님)
- [ ] **Enum 값**이 숫자인가 (문자열 `"Normal"`, `"Fill"` 등 불가)
- [ ] **Margin/TextPadding**이 객체 `{"Left":0,...}` 인가 (문자열 `"0,0,0,0"` 불가)
- [ ] **Dock=Fill** 시 `"Dock": 5` 인가 (`"Fill": true` 불가)
- [ ] **색상 값**이 테마 키(`"Fore"`, `"Base3"`) 또는 CSS 색상명(`"red"`) 인가

### 컨테이너 검증

- [ ] **GoTableLayoutPanel**의 Childrens가 `{"indexes":{...},"ls":[...]}` 객체 구조인가
- [ ] GoTableLayoutPanel에서 **ColSpan** 인가 (`ColumnSpan` 아님)
- [ ] **GoSwitchPanel**의 Pages가 배열 `[{"Name":"Sub1","Childrens":[...]}]` 인가

### 최종 확인

- [ ] 컨트롤이 화면 밖으로 나가지 않는가 (R <= DesignWidth, B <= DesignHeight)
- [ ] 같은 컨테이너 내 컨트롤이 겹치지 않는가
- [ ] Python/스크립트를 사용하지 않고 **Write/Edit 도구로 직접 작성**했는가

> 이 검증 목록은 eval 대신 사용하는 자체 검증이다. 검증을 건너뛰면 UIEditor에서 파일을 열 수 없거나, 런타임에 JsonException이 발생한다.

---

## 절대 규칙 (요약)

1. **Designer.cs / design.json 수정 금지** -- UIEditor 자동 생성 파일. 수정해도 MakeCode 시 덮어씀
2. **속성/메서드 추측 금지** -- 이 문서에 없으면 `controls/*.md` 또는 `comm/*.md` 확인 필수. 다른 프레임워크 지식으로 유추 금지
3. **코드 네이밍: 영문+숫자만** -- 한글 식별자 불가, 주석으로 한글 보완
4. **데이터 구조 임의 작성 금지** -- 레지스터 맵은 사용자 확인 필수
5. **Pages/Windows는 Dictionary** -- Array 불가. 컨버터가 Dictionary만 역직렬화 가능
6. **이미지 우선, 추측 금지** -- 이미지를 우선하되 애매한 요소는 반드시 사용자에게 확인
7. **.gud 생성/수정 시 스크립트 금지** -- Write/Edit 도구로 직접 작성

> **⚠ 컨트롤 JSON은 반드시 `controls/` 에서 로드하라.**
> **⚠ Enum 전체 목록은 `enums-reference.md` 를 참조하라.**

---

## 관련 문서

| 문서 | 용도 |
|------|------|
| `controls/*.md` | 개별 컨트롤 JSON 템플릿 + 속성 |
| `controls/_common.md` | 공통 속성/이벤트 + 데이터 클래스 JSON 형식 |
| `enums-reference.md` | Enum 숫자값 전체 매핑 |
| `image-to-gud.md` | 이미지 → .gud 변환 절차 |
| `troubleshooting.md` | .gud 부분 수정 가이드 |
