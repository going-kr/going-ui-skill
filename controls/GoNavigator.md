# GoNavigator

메뉴 네비게이터 컨트롤. GoMenuItem 목록을 수평/수직으로 표시하고 클릭 시 자동 페이지 전환.
상속: GoControl → GoNavigator

⚠ **PageName 자동 전환**: GoMenuItem에 `PageName`을 지정하면 클릭 시 `Design.SetPage(PageName)`이 자동 호출된다. 별도 이벤트 핸들러 불필요.
⚠ **Direction** — 메뉴 배치 방향. **IconDirection** — 아이콘-텍스트 배치 방향. 혼동 주의.
⚠ **Menus** — ObservableList\<GoMenuItem\>. Items가 아님.
⚠ Selectable 기본값: **false**

## .gud JSON

```json
{
  "Type": "GoNavigator",
  "Value": {
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "Indent": 20,
    "MenuGap": 30,
    "Menus": [
      { "IconString": "fa-home", "Text": "Home", "PageName": "Main" },
      { "IconString": "fa-cog", "Text": "Settings", "PageName": "Setting" }
    ],
    "Direction": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,400,40",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘-텍스트 배치 방향 | 0 (Horizon) |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| float | Indent | 시작 들여쓰기(px) | 20 |
| float | MenuGap | 메뉴 항목 간격(px) | 30 |
| ObservableList\<GoMenuItem\> | Menus | 메뉴 항목 목록 | [] |
| GoDirectionHV | Direction | 메뉴 배치 방향 | 0 (Horizon) |

**GoDirectionHV**: Horizon=0, Vertical=1

**GoMenuItem 구조**:

| 속성 | 타입 | 설명 |
|------|------|------|
| IconString | string? | 아이콘 문자열 (FontAwesome 등) |
| Text | string? | 메뉴 표시 텍스트 |
| Tag | object? | 사용자 정의 데이터 |
| PageName | string? | 연결할 페이지 이름 (자동 전환) |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

(이벤트 없음 — PageName으로 자동 페이지 전환)

## C# 사용

```csharp
var nav = (GoNavigator)dic["navMain"];

// 메뉴 항목 추가
nav.Menus.Add(new GoMenuItem
{
    IconString = "fa-home",
    Text = "Home",
    PageName = "Main"        // 클릭 시 자동 페이지 전환
});

nav.Menus.Add(new GoMenuItem
{
    IconString = "fa-chart-bar",
    Text = "Monitor",
    PageName = "MonitorPage"
});

// 수직 방향 전환
nav.Direction = GoDirectionHV.Vertical;
```

## 검증 완료

- 소스코드(GoNavigator.cs): GoProperty 속성 11개 (IconSize, IconDirection, IconGap, FontName, FontStyle, FontSize, TextColor, Indent, MenuGap, Menus, Direction)
- 이벤트 없음 (페이지 전환은 Design.SetPage() 내부 호출)
- 현재 페이지 표시: PageName == Design.CurrentPage.Name이면 완전 불투명 표시
- Selectable 기본값 false (생성자에서 설정하지 않음)
