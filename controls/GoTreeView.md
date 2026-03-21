# GoTreeView

트리 뷰 컨트롤. 계층 구조 항목을 펼치기/접기로 표시하고 드래그앤드롭을 지원한다.
상속: GoControl → GoTreeView

⚠ **Nodes** — ObservableList\<GoTreeNode\>. Items(ListBox)와 혼동 주의.
⚠ **GoTreeNode.Nodes** — 재귀 트리 구조. 자식 노드도 ObservableList\<GoTreeNode\>.
⚠ **DragMode** 기본값 **false** — GoToolBox의 DragMode(true)와 다름.
⚠ Selectable 기본값: **true** (생성자에서 설정)

## .gud JSON

```json
{
  "Type": "GoTreeView",
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
    "DragMode": false,
    "ItemHeight": 30,
    "Nodes": [
      {
        "Text": "Root",
        "IconString": "fa-folder",
        "Expand": true,
        "Nodes": [
          { "Text": "Child 1", "IconString": "fa-file", "Expand": true, "Nodes": [] }
        ]
      }
    ],
    "SelectionMode": 1,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,250,400",
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
| string | SelectColor | 선택 노드 강조 색상 | "Select" |
| GoRoundType | Round | 모서리 스타일 | 1 (All) |
| bool | BackgroundDraw | 배경 그리기 여부 | true |
| bool | DragMode | 드래그 모드 활성화 | false |
| float | ItemHeight | 노드 항목 높이(px) | 30 |
| ObservableList\<GoTreeNode\> | Nodes | 루트 노드 목록 | [] |
| GoItemSelectionMode | SelectionMode | 선택 모드 | 1 (Single) |

**GoItemSelectionMode**: None=0, Single=1, Multi=2, MultiPC=3

**GoTreeNode 구조**:

| 속성 | 타입 | 설명 |
|------|------|------|
| Text | string? | 노드 표시 텍스트 |
| IconString | string? | 아이콘 문자열 |
| Tag | object? | 사용자 정의 데이터 |
| Nodes | ObservableList\<GoTreeNode\> | 자식 노드 목록 (재귀) |
| Expand | bool | 펼침 상태 (기본값: true) |

**런타임 전용 속성 (JsonIgnore)**:

| 타입 | 이름 | 설명 |
|------|------|------|
| List\<GoTreeNode\> | SelectedNodes | 선택된 노드 목록 |
| double | ScrollPosition | 스크롤 위치 |
| int | Depth | 노드 깊이 (0=루트) |
| GoTreeNode? | Parent | 부모 노드 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | SelectedChanged | 선택 변경 시 발생 |
| EventHandler\<TreeNodeEventArgs\> | DragStart | 드래그 시작 시 발생 (DragMode=true) |
| EventHandler\<TreeNodeEventArgs\> | ItemClicked | 노드 클릭 시 발생 |
| EventHandler\<TreeNodeEventArgs\> | ItemLongClicked | 노드 롱클릭 시 발생 |
| EventHandler\<TreeNodeEventArgs\> | ItemDoubleClicked | 노드 더블클릭 시 발생 |

**TreeNodeEventArgs**: `Item` 속성으로 대상 GoTreeNode 접근.

## C# 사용

```csharp
var tv = (GoTreeView)dic["tvFiles"];

// 트리 구성
var root = new GoTreeNode { Text = "Project", IconString = "fa-folder", Expand = true };
root.Nodes.Add(new GoTreeNode { Text = "src", IconString = "fa-folder" });
root.Nodes.Add(new GoTreeNode { Text = "README.md", IconString = "fa-file" });
tv.Nodes.Add(root);

// 선택 변경 감지
tv.SelectedChanged += (s, e) =>
{
    foreach (var node in tv.SelectedNodes)
        Console.WriteLine($"Selected: {node.Text}");
};

// 항목 클릭
tv.ItemClicked += (s, e) =>
{
    Console.WriteLine($"Clicked: {e.Item.Text}, Depth: {e.Item.Depth}");
};

// 드래그 모드 활성화
tv.DragMode = true;
tv.DragStart += (s, e) =>
{
    Console.WriteLine($"Drag: {e.Item.Text}");
};
```

## 검증 완료

- 소스코드(GoTreeView.cs): GoProperty 속성 15개 (IconSize, IconGap, FontName, FontStyle, FontSize, TextColor, BoxColor, BorderColor, SelectColor, Round, BackgroundDraw, DragMode, ItemHeight, Nodes, SelectionMode)
- 이벤트 5개 (SelectedChanged, DragStart, ItemClicked, ItemLongClicked, ItemDoubleClicked)
- 생성자에서 Selectable = true 설정 확인
