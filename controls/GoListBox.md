# GoListBox

목록 박스 컨트롤. 스크롤 가능한 항목 목록과 단일/다중 선택 모드를 지원한다.
상속: GoControl → GoListBox

⚠ **SelectionMode** — GoItemSelectionMode 열거형. None=0, Single=1, Multi=2, MultiPC=3. JSON에서 숫자로 지정.
⚠ **Items** — ObservableList\<GoListItem\>. Nodes(TreeView)나 Menus(Navigator)와 혼동 주의.
⚠ **ItemAlignment** 기본값 4 = MiddleCenter. GoContentAlignment 열거형 참조.
⚠ Selectable 기본값: **true** (생성자에서 설정)

## .gud JSON

```json
{
  "Type": "GoListBox",
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
    "Round": 1,
    "BackgroundDraw": true,
    "ItemHeight": 30,
    "ItemAlignment": 4,
    "SelectionMode": 1,
    "Items": [
      { "IconString": null, "Text": "Item 1" },
      { "IconString": "fa-star", "Text": "Item 2" }
    ],
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,200,300",
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
| GoRoundType | Round | 모서리 스타일 | 1 (All) |
| bool | BackgroundDraw | 배경 그리기 여부 | true |
| float | ItemHeight | 항목 높이(px) | 30 |
| GoContentAlignment | ItemAlignment | 항목 텍스트 정렬 | 4 (MiddleCenter) |
| GoItemSelectionMode | SelectionMode | 선택 모드 | 1 (Single) |
| ObservableList\<GoListItem\> | Items | 항목 목록 | [] |

**GoItemSelectionMode**: None=0, Single=1, Multi=2, MultiPC=3

**GoListItem 구조**:

| 속성 | 타입 | 설명 |
|------|------|------|
| IconString | string? | 아이콘 문자열 |
| Text | string? | 표시 텍스트 |
| Tag | object? | 사용자 정의 데이터 |

**런타임 전용 속성 (JsonIgnore)**:

| 타입 | 이름 | 설명 |
|------|------|------|
| List\<GoListItem\> | SelectedItems | 선택된 항목 목록 |
| double | ScrollPosition | 스크롤 위치 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | SelectedChanged | 선택 변경 시 발생 |
| EventHandler\<ListItemEventArgs\> | ItemClicked | 항목 클릭 시 발생 |
| EventHandler\<ListItemEventArgs\> | ItemLongClicked | 항목 롱클릭 시 발생 |
| EventHandler\<ListItemEventArgs\> | ItemDoubleClicked | 항목 더블클릭 시 발생 |

**ListItemEventArgs**: `Item` 속성으로 클릭된 GoListItem 접근.

## C# 사용

```csharp
var lb = (GoListBox)dic["lbItems"];

// 항목 추가
lb.Items.Add(new GoListItem { Text = "Apple", IconString = "fa-apple-alt" });
lb.Items.Add(new GoListItem { Text = "Banana" });

// 선택 변경 감지
lb.SelectedChanged += (s, e) =>
{
    foreach (var item in lb.SelectedItems)
        Console.WriteLine($"Selected: {item.Text}");
};

// 항목 클릭 이벤트
lb.ItemClicked += (s, e) =>
{
    Console.WriteLine($"Clicked: {e.Item.Text}");
};

// 다중 선택(PC 방식: Ctrl/Shift 지원)
lb.SelectionMode = GoItemSelectionMode.MultiPC;
```

## 검증 완료

- 소스코드(GoListBox.cs): GoProperty 속성 15개 (IconSize, IconGap, FontName, FontStyle, FontSize, TextColor, BoxColor, BorderColor, SelectColor, Round, BackgroundDraw, ItemHeight, ItemAlignment, SelectionMode, Items)
- 이벤트 4개 (SelectedChanged, ItemClicked, ItemLongClicked, ItemDoubleClicked)
- 생성자에서 Selectable = true 설정 확인
