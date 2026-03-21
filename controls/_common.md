# GoControl 공통 레퍼런스

모든 Go* 컨트롤은 GoControl을 상속하며, 아래 속성과 이벤트를 공통으로 갖는다.
.gud JSON 작성 시 이 공통 속성을 반드시 포함해야 한다.

## 공통 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 | JSON 직렬화 |
|------|------|------|--------|-------------|
| Guid | Id | 고유 식별자 (init only) | Guid.NewGuid() | ✅ UUID 문자열 |
| string? | Name | 컨트롤 이름. C# 바인딩 키 | null | ✅ |
| bool | Visible | 표시 여부 | true | ✅ |
| bool | Enabled | 활성화 여부 | true | ✅ |
| bool | UseLongClick | 롱클릭 사용 | false | ✅ |
| int? | LongClickTime | 롱클릭 시간(ms) | null | ✅ |
| bool | Selectable | 선택 가능 여부 | false | ✅ (protected set) |
| SKRect | Bounds | 영역 "Left,Top,Right,Bottom" | "0,0,70,30" | ✅ |
| GoDockStyle | Dock | 도킹 방향 | 0 (None) | ✅ 숫자 |
| GoPadding | Margin | 여백 {Left,Top,Right,Bottom} | {3,3,3,3} | ✅ 객체 |

⚠ **Bounds는 "Left,Top,Right,Bottom" 형식!** Width/Height 아님!
- `"10,20,210,70"` = 위치(10,20)에서 위치(210,70)까지 → 200×50 픽셀
- Width = Right - Left, Height = Bottom - Top

⚠ **Selectable 기본값은 false.** GoButton, GoSlider 등 일부 컨트롤은 생성자에서 true로 변경.

⚠ **Dock 값은 숫자로 직렬화:**
- None=0, Left=1, Top=2, Right=3, Bottom=4, Fill=5

## 공통 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler\<GoMouseClickEventArgs\> | MouseClicked | 마우스 클릭 |
| EventHandler\<GoMouseClickEventArgs\> | MouseLongClicked | 롱클릭 |
| EventHandler\<GoMouseClickEventArgs\> | MouseLongClickCanceled | 롱클릭 취소 |
| EventHandler\<GoMouseClickEventArgs\> | MouseDown | 마우스 다운 |
| EventHandler\<GoMouseClickEventArgs\> | MouseUp | 마우스 업 |
| EventHandler\<GoMouseClickEventArgs\> | MouseDoubleClicked | 더블 클릭 |
| EventHandler\<GoMouseEventArgs\> | MouseMove | 마우스 이동 |
| EventHandler\<GoMouseEventArgs\> | MouseWheel | 마우스 휠 (실제 전달되는 인자는 GoMouseWheelEventArgs — Delta 접근 시 캐스팅 필요) |
| EventHandler\<GoDrawnEventArgs\> | Drawn | 렌더링 완료 |
| EventHandler\<GoDragEventArgs\> | DragDrop | 드래그 앤 드롭 |

## 공통 JSON 템플릿 (최소)

```json
{
  "Id": "{UUID}",
  "Name": null,
  "Visible": true,
  "Enabled": true,
  "Selectable": false,
  "Bounds": "0,0,70,30",
  "Dock": 0,
  "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
}
```

## 데이터 클래스

### GoPadding

```json
{ "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
```

| 타입 | 이름 | 설명 |
|------|------|------|
| float | Left | 좌측 여백 |
| float | Top | 상단 여백 |
| float | Right | 우측 여백 |
| float | Bottom | 하단 여백 |

### GoMouseEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| float | X | 마우스 X 좌표 |
| float | Y | 마우스 Y 좌표 |

### GoMouseClickEventArgs : GoMouseEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| GoMouseButton | Button | 클릭 버튼 (Left=0, Right=1, Middle=2) |

### GoMouseWheelEventArgs : GoMouseEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| float | Delta | 휠 이동량 |

### GoDrawnEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| GoTheme | Theme | 현재 테마 |
| SKCanvas | Canvas | SkiaSharp 캔버스 |

### GoDragEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| float | X | 드롭 X 좌표 |
| float | Y | 드롭 Y 좌표 |
| object | DragItem | 드래그 데이터 |

### GoCancelableEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| bool | Cancel | 취소 여부 (true로 설정 시 동작 취소) |

## 컨트롤 데이터 클래스 (JSON 직렬화 형식)

⚠ **아래 클래스들은 컨트롤의 배열 속성(Items, Buttons, Menus, Series 등)에 사용된다.**
⚠ **문자열 배열이 아닌 객체 배열이다!** `"항목"` (X) → `{ "Text": "항목" }` (O)

### GoListItem

GoInputCombo, GoInputSelector, GoListBox, GoToolBox의 Items에 사용.

```json
{ "IconString": null, "Text": "항목1" }
```

| 타입 | 이름 | 설명 | JSON |
|------|------|------|------|
| string? | IconString | 아이콘 | ✅ |
| string? | Text | 표시 텍스트 | ✅ |
| object? | Tag | 사용자 데이터 | ❌ (JsonIgnore) |

### GoButtonItem

GoPanel, GoGroupBox, GoValue의 Buttons에 사용.

```json
{ "Name": "btn1", "Text": "버튼", "IconString": null, "Size": "100%" }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | Name | 식별자 | — |
| string? | Text | 표시 텍스트 | null |
| string? | IconString | 아이콘 | null |
| string | Size | 크기 ("100%", "80px") | "100%" |

### GoButtonsItem : GoButtonItem

GoButtons의 Buttons에 사용. GoButtonItem + Selected.

```json
{ "Name": "btn1", "Text": "버튼", "IconString": null, "Size": "100%", "Selected": false }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| bool | Selected | 선택 상태 (Toggle/Radio) | false |

### GoGraphSeries

GoBarGraph, GoCircleGraph, GoTrendGraph의 Series에 사용.

```json
{ "Name": "temp", "Alias": "온도", "Color": "Red", "Visible": true }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | Name | 데이터 키 | "" |
| string | Alias | 표시 이름 | "" |
| string | Color | 색상 | "Red" |
| bool | Visible | 표시 여부 | true |

### GoLineGraphSeries

GoLineGraph, GoTimeGraph의 Series에 사용. GoGraphSeries와 동일 속성 + Minimum/Maximum 추가. (별도 클래스, 상속 아님)

```json
{ "Name": "temp", "Alias": "온도", "Color": "Red", "Visible": true, "Minimum": 0, "Maximum": 100 }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| double | Minimum | Y축 최솟값 | 0 |
| double | Maximum | Y축 최댓값 | 100 |

### GoMenuItem

GoNavigator의 Menus에 사용.

```json
{ "IconString": "fa-home", "Text": "홈", "PageName": "PageMain" }
```

| 타입 | 이름 | 설명 |
|------|------|------|
| string? | IconString | 아이콘 |
| string? | Text | 메뉴 텍스트 |
| string? | PageName | 자동 전환 대상 페이지명 |
| object? | Tag | 사용자 데이터 (JSON 미직렬화) |

### GoTreeNode

GoTreeView의 Nodes에 사용. 재귀 구조.

```json
{ "Text": "루트", "IconString": "fa-folder", "Expand": true, "Nodes": [
    { "Text": "자식1", "IconString": null, "Expand": true, "Nodes": [] }
] }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | Text | 노드 텍스트 | null |
| string? | IconString | 아이콘 | null |
| ObservableList\<GoTreeNode\> | Nodes | 자식 노드 | [] |
| bool | Expand | 펼침 여부 | true |
| object? | Tag | 사용자 데이터 (JSON 미직렬화) |

### GoTabPage

GoTabControl의 TabPages에 사용.

```json
{ "Name": "tab1", "IconString": null, "Text": "탭1", "Childrens": [] }
```

| 타입 | 이름 | 설명 |
|------|------|------|
| string | Name | 탭 식별자 |
| string? | IconString | 탭 아이콘 |
| string? | Text | 탭 텍스트 |
| List\<IGoControl\> | Childrens | 탭 내 자식 컨트롤 |

---

## C# dic 캐스팅 패턴

```csharp
// Designer.cs에서 자동 생성되는 패턴
var dic = Util.AllControls(this);
var btnStart = (GoButton)dic["btnStart"];
var lblTitle = (GoLabel)dic["lblTitle"];
var lampRun = (GoLamp)dic["lampRun"];
```

⚠ dic 키는 .gud의 Name 값이다. Name이 null인 컨트롤은 dic에 포함되지 않는다.
