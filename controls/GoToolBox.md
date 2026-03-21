# GoToolBox

도구 상자 컨트롤. 카테고리별로 아이콘 도구 항목을 표시하고 드래그앤드롭을 지원한다.
상속: GoControl → GoToolBox

⚠ **Categories** — ObservableList\<GoToolCategory\>. Items/Nodes가 아니라 Categories.
⚠ **DragMode** 기본값 **true** — GoTreeView의 DragMode(false)와 다름.
⚠ **CategoryColor** — 카테고리 헤더 전용 색상. GoToolBox에만 있는 속성.
⚠ Selectable 기본값: **true** (생성자에서 설정)

## .gud JSON

```json
{
  "Type": "GoToolBox",
  "Value": {
    "IconSize": 12,
    "IconGap": 5,
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "BoxColor": "Base1",
    "BorderColor": "Base3",
    "SelectColor": "Select",
    "CategoryColor": "Base2",
    "Round": 1,
    "BackgroundDraw": true,
    "ItemHeight": 30,
    "Categories": [
      {
        "Text": "Basic",
        "IconString": "fa-cube",
        "Expand": true,
        "Items": [
          { "Text": "Button", "IconString": "fa-square" },
          { "Text": "Label", "IconString": "fa-font" }
        ]
      }
    ],
    "DragMode": true,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,200,400",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| float | IconSize | 아이콘 크기 | 12 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BoxColor | 배경 색상 | "Base1" |
| string | BorderColor | 테두리 색상 | "Base3" |
| string | SelectColor | 선택 항목 강조 색상 | "Select" |
| string | CategoryColor | 카테고리 헤더 색상 | "Base2" |
| GoRoundType | Round | 모서리 스타일 | 1 (All) |
| bool | BackgroundDraw | 배경 그리기 여부 | true |
| float | ItemHeight | 항목 높이(px) | 30 |
| ObservableList\<GoToolCategory\> | Categories | 카테고리 목록 | [] |
| bool | DragMode | 드래그 모드 활성화 | true |

**GoToolCategory 구조**:

| 속성 | 타입 | 설명 |
|------|------|------|
| Text | string? | 카테고리 표시 텍스트 |
| IconString | string? | 아이콘 문자열 |
| Tag | object? | 사용자 정의 데이터 |
| Items | ObservableList\<GoToolItem\> | 도구 항목 목록 |
| Expand | bool | 펼침 상태 (기본값: true) |

**GoToolItem 구조**:

| 속성 | 타입 | 설명 |
|------|------|------|
| Text | string? | 항목 표시 텍스트 |
| IconString | string? | 아이콘 문자열 |
| Tag | object? | 사용자 정의 데이터 |

**런타임 전용 속성 (JsonIgnore)**:

| 타입 | 이름 | 설명 |
|------|------|------|
| double | ScrollPosition | 스크롤 위치 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler\<ToolItemEventArgs\> | DragStart | 드래그 시작 시 발생 (DragMode=true) |
| EventHandler\<ToolItemEventArgs\> | ItemClicked | 항목 클릭 시 발생 |
| EventHandler\<ToolItemEventArgs\> | ItemLongClicked | 항목 롱클릭 시 발생 |
| EventHandler\<ToolItemEventArgs\> | ItemDoubleClicked | 항목 더블클릭 시 발생 |

**ToolItemEventArgs**: `Item` 속성으로 대상 GoToolItem 접근.

## C# 사용

```csharp
var tb = (GoToolBox)dic["tbControls"];

// 카테고리 및 항목 추가
var cat = new GoToolCategory { Text = "Controls", IconString = "fa-th", Expand = true };
cat.Items.Add(new GoToolItem { Text = "Button", IconString = "fa-square" });
cat.Items.Add(new GoToolItem { Text = "Label", IconString = "fa-font" });
tb.Categories.Add(cat);

// 드래그 시작 감지
tb.DragStart += (s, e) =>
{
    Console.WriteLine($"Drag: {e.Item.Text}");
};

// 항목 클릭 이벤트
tb.ItemClicked += (s, e) =>
{
    Console.WriteLine($"Clicked: {e.Item.Text} in {e.Item.Category?.Text}");
};
```

## 검증 완료

- 소스코드(GoToolBox.cs): GoProperty 속성 15개 (IconSize, IconGap, FontName, FontStyle, FontSize, TextColor, BoxColor, BorderColor, SelectColor, CategoryColor, Round, BackgroundDraw, ItemHeight, Categories, DragMode)
- 이벤트 4개 (DragStart, ItemClicked, ItemLongClicked, ItemDoubleClicked)
- 생성자에서 Selectable = true 설정 확인
