# GoTableLayoutPanel

테이블 레이아웃 컨테이너. Columns/Rows에 크기 문자열을 지정하여 격자를 구성하고, 자식 컨트롤을 셀에 배치한다.
상속: GoContainer → GoTableLayoutPanel

⚠ **Childrens가 배열이 아닌 객체 `{ "indexes": {...}, "ls": [...] }` 형식!** 일반 컨테이너와 JSON 구조가 다르다.
⚠ **ColSpan**이지 ColumnSpan이 아님!
⚠ Columns/Rows 포맷: `"25%"` 또는 `"40px"`. **`"%"` 비율 우선 사용** — 고정 크기가 필요한 경우에만 `"40px"` 사용.

## .gud JSON

```json
{
  "Type": "GoTableLayoutPanel",
  "Value": {
    "Columns": ["25%", "25%", "25%", "25%"],
    "Rows": ["40px", "50px", "10%", "10%"],
    "Childrens": {
      "indexes": {
        "UUID-of-control": { "Row": 0, "Column": 0, "RowSpan": 1, "ColSpan": 2 }
      },
      "ls": [
        { "Type": "GoLabel", "Value": { "Id": "UUID-of-control", "..." : "..." } }
      ]
    },
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,1024,600",
    "Dock": 0,
    "Margin": { "Left": 0, "Top": 0, "Right": 0, "Bottom": 0 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| List\<string\> | Columns | 열 크기 목록. "50%", "100px" 등 | [] |
| List\<string\> | Rows | 행 크기 목록 | [] |
| GoTableLayoutControlCollection | Childrens | 자식 컨트롤 컬렉션 (Indexes + Controls) | [] |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

### GoTableIndex (indexes 항목)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| int | Row | 행 인덱스 | 0 |
| int | Column | 열 인덱스 | 0 |
| int | RowSpan | 행 병합 수 | 1 |
| int | ColSpan | 열 병합 수 | 1 |

### GoTableLayoutControlCollection 메서드

| 반환 | 메서드 | 설명 |
|------|--------|------|
| void | Add(IGoControl control, int col, int row, int colspan = 1, int rowspan = 1) | 셀에 컨트롤 추가 |
| bool | Remove(IGoControl control) | 컨트롤 제거 |
| void | Clear() | 모든 컨트롤 제거 |
| bool | Contains(IGoControl control) | 포함 여부 |

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var tbl = (GoTableLayoutPanel)dic["tblMain"];

// 코드로 컨트롤 추가
var lbl = new GoLabel { Text = "Hello" };
tbl.Childrens.Add(lbl, col: 0, row: 0, colspan: 2, rowspan: 1);
```

## 검증 완료

- 소스코드(GoTableLayoutPanel.cs): Columns, Rows, Childrens(GoTableLayoutControlCollection) 확인
- GoTableIndex: Row, Column, RowSpan, ColSpan 확인 (ColSpan이지 ColumnSpan 아님)
