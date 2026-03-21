# GoGridLayoutPanel

가변 열 그리드 레이아웃 컨테이너. 각 행마다 다른 수의 열을 가질 수 있다.
상속: GoContainer → GoGridLayoutPanel

⚠ GoTableLayoutPanel과 유사하지만, **행마다 열 수가 다를 수 있다** (불균등 그리드).
⚠ Childrens도 GoTableLayoutPanel처럼 **객체 `{ "indexes": {...}, "ls": [...] }` 형식**이다.
⚠ GoGridIndex에는 ColSpan/RowSpan이 **없다** — 셀 병합 불가.

## .gud JSON

```json
{
  "Type": "GoGridLayoutPanel",
  "Value": {
    "Rows": [
      { "Height": "50px", "Columns": ["50%", "50%"] },
      { "Height": "10%", "Columns": ["33%", "33%", "34%"] }
    ],
    "Childrens": {
      "indexes": {
        "UUID": { "Row": 0, "Column": 0 }
      },
      "ls": [
        { "Type": "GoLabel", "Value": { "Id": "UUID", "..." : "..." } }
      ]
    },
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,800,600",
    "Dock": 0,
    "Margin": { "Left": 0, "Top": 0, "Right": 0, "Bottom": 0 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| List\<GoGridLayoutPanelRow\> | Rows | 행 정의 목록 | [] |
| GoGridLayoutControlCollection | Childrens | 자식 컨트롤 컬렉션 (Indexes + Controls) | [] |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

### GoGridLayoutPanelRow

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | Height | 행 높이. "50px", "100%" 등 | "100%" |
| List\<string\> | Columns | 이 행의 열 크기 목록 | [] |

### GoGridIndex (indexes 항목)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| int | Row | 행 인덱스 | 0 |
| int | Column | 열 인덱스 | 0 |

### 메서드

| 반환 | 메서드 | 설명 |
|------|--------|------|
| void | AddRow(string height, string[] columns) | 행 추가 |
| Dictionary\<int, Dictionary\<int, SKRect\>\> | GridBounds() | 각 셀의 영역 반환 |
| SKRect? | CellBounds(rts, int col, int row) | 특정 셀 영역 반환 |

### GoGridLayoutControlCollection 메서드

| 반환 | 메서드 | 설명 |
|------|--------|------|
| void | Add(IGoControl control, int col, int row) | 셀에 컨트롤 추가 |
| bool | Remove(IGoControl control) | 컨트롤 제거 |
| void | Clear() | 모든 컨트롤 제거 |
| bool | Contains(IGoControl control) | 포함 여부 |

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var grid = (GoGridLayoutPanel)dic["gridMain"];

// 코드로 행 추가
grid.AddRow("50px", new[] { "50%", "50%" });
grid.AddRow("100%", new[] { "33%", "33%", "34%" });

// 컨트롤 배치
var lbl = new GoLabel { Text = "Cell" };
grid.Childrens.Add(lbl, col: 0, row: 0);
```

## 검증 완료

- 소스코드(GoGridLayoutPanel.cs): Rows(GoGridLayoutPanelRow), Childrens(GoGridLayoutControlCollection) 확인
- GoGridIndex: Row, Column만 존재 (ColSpan/RowSpan 없음)
- GoGridLayoutPanelRow: Height="100%", Columns=[] 기본값 확인
