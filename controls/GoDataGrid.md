# GoDataGrid

데이터 그리드 컨트롤. 열 정의, 스크롤, 행 선택, 요약행을 지원하는 테이블 컨트롤.
상속: GoControl → GoDataGrid

⚠ **ScrollMode** 소스코드 기본값은 `Vertical`(1)이지만, .gud JSON 기본값은 0(Horizon). 코드에서 반드시 설정하라!
⚠ **SelectionMode** 소스코드 기본값은 `Single`(2)이지만, .gud JSON 기본값은 0(None). 코드에서 반드시 설정하라!
⚠ **ColumnGroups**는 다중 헤더행(그룹 헤더)용. 일반 사용에서는 빈 배열로 두라.
⚠ **Columns/SummaryRows는 보통 코드에서 구성** — .gud JSON에서는 빈 배열로 두고 C#에서 정의하는 것이 일반적.
⚠ Selectable 기본값: **true** (생성자에서 변경)
⚠ **Column.Name은 데이터 객체 T의 프로퍼티명과 정확히 일치해야 한다!** 대소문자 구분.

## .gud JSON

```json
{
  "Type": "GoDataGrid",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "RowColor": "Base2",
    "SummaryRowColor": "Base1",
    "ColumnColor": "Base1",
    "SelectedRowColor": "Select",
    "BoxColor": "Base2",
    "ScrollBarColor": "Base1",
    "RowHeight": 30,
    "ColumnHeight": 30,
    "ScrollMode": 0,
    "SelectionMode": 0,
    "ColumnGroups": [],
    "Columns": [],
    "SummaryRows": [],
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,70,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

> `GoDataGridSelectionMode` — None=0, Selector=1, Single=2, Multi=3, MultiPC=4
> `ScrollMode` — Horizon=0, Vertical=1, Both=2

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | RowColor | 행 배경색 | "Base2" |
| string | SummaryRowColor | 요약행 배경색 | "Base1" |
| string | ColumnColor | 헤더행 배경색 | "Base1" |
| string | SelectedRowColor | 선택행 색상 | "Select" |
| string | BoxColor | 입력박스 색상 | "Base2" |
| string | ScrollBarColor | 스크롤바 색상 | "Base1" |
| float | RowHeight | 행 높이(px) | 30 |
| float | ColumnHeight | 컬럼 헤더 높이(px) | 30 |
| ScrollMode | ScrollMode | 스크롤 모드 | Vertical(1) |
| GoDataGridSelectionMode | SelectionMode | 행 선택 모드 | Single(2) |
| ObservableList\<GoDataGridColumn\> | Columns | 열 정의 목록 | [] |
| ObservableList\<GoDataGridColumn\> | ColumnGroups | 열 그룹 정의 | [] |
| List\<GoDataGridSummaryRow\> | SummaryRows | 요약행 목록 | [] |

런타임 전용 (JsonIgnore):

| 타입 | 이름 | 설명 |
|------|------|------|
| List\<GoDataGridRow\> | Rows | 데이터 행 목록 |
| Type? | DataType | SetDataSource로 설정된 T 타입 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | SelectedChanged | 행 선택 변경 시 |
| EventHandler | SortChanged | 정렬 변경 시 |
| EventHandler\<GoDataGridColumnMouseEventArgs\> | ColumnMouseClick | 컬럼 헤더 클릭 시 |
| EventHandler\<GoDataGridCellMouseEventArgs\> | CellMouseClick | 셀 클릭 시 |
| EventHandler\<GoDataGridCellMouseEventArgs\> | CellMouseDoubleClick | 셀 더블클릭 시 |
| EventHandler\<GoDataGridCellMouseEventArgs\> | CellMouseLongClick | 셀 롱클릭 시 |
| EventHandler\<GoDataGridCellButtonClickEventArgs\> | CellButtonClick | 셀 버튼 클릭 시 |
| EventHandler\<GoDataGridCellValueChangedEventArgs\> | ValueChanged | 셀 값 변경 시 |

⚠ 추가 이벤트: DateTimeDropDownOpening, ColorDropDownOpening, ComboDropDownOpening, GetDateTimeDropDownVisible, GetColorDropDownVisible, GetComboDropDownVisible — 드롭다운 관련 이벤트는 필요 시 소스코드 참조

## 메서드 (Methods)

| 반환 | 이름 | 설명 |
|------|------|------|
| void | SetDataSource\<T\>(IEnumerable\<T\>) | 데이터 바인딩 (리플렉션 기반) |
| void | RefreshRows() | 행 레이아웃 재계산 |

⚠ **SetDataSource는 인수 1개!** `gridProperty.SetDataSource<T>(items)` (O)
⚠ GoBarGraph/GoLineGraph의 `SetDataSource("XAxisName", data)` (인수 2개)와 혼동 금지!

---

## 컬럼 타입 (11종)

### 컬럼 공통 속성

모든 컬럼 공통:

```json
{
  "Type": "GoDataGridLabelColumn",
  "Name": "PropertyName",
  "HeaderText": "표시 텍스트",
  "Size": "100px",
  "UseFilter": false,
  "UseSort": false,
  "TextColor": null,
  "Fixed": false
}
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | Name | 데이터 객체 프로퍼티명 매칭 키 | null |
| string? | HeaderText | 헤더 표시 텍스트 | null |
| string? | Size | 너비 ("100px", "30%", "100%") | null |
| bool | UseFilter | 필터 사용 | false |
| bool | UseSort | 정렬 사용 | false |
| string? | TextColor | 텍스트 색상 (null이면 Grid.TextColor) | null |
| bool | Fixed | 수평 스크롤 시 고정 | false |
| string? | GroupName | 소속 ColumnGroup 이름 | null |

### 읽기 전용 컬럼

#### GoDataGridLabelColumn

텍스트 표시 (편집 불가).

```json
{ "Type": "GoDataGridLabelColumn", "Name": "Name", "HeaderText": "장치명", "Size": "100px",
  "FormatString": null }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | FormatString | 포맷 문자열 | null |

#### GoDataGridNumberColumn\<T\>

숫자 포맷 표시 (편집 불가). T: Int32, Int64, Single, Double, Decimal 등 CLR 타입명.

```json
{ "Type": "GoDataGridNumberColumn<Double>", "Name": "Temperature", "HeaderText": "온도", "Size": "80px",
  "FormatString": "0.0" }
```

⚠ **CLR 타입명 사용!** `GoDataGridNumberColumn<Double>` (O), `GoDataGridNumberColumn<double>` (X)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | FormatString | 포맷 문자열 | null |

#### GoDataGridLampColumn

bool 값을 램프(원형 표시등)로 표시.

```json
{ "Type": "GoDataGridLampColumn", "Name": "IsOnline", "HeaderText": "통신", "Size": "60px",
  "OnColor": "Good" }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | OnColor | ON 색상 (테마키 또는 직접 지정) | "Good" |

#### GoDataGridCheckBoxColumn

bool 값을 체크박스로 표시 (읽기 전용).

```json
{ "Type": "GoDataGridCheckBoxColumn", "Name": "UseFilter", "HeaderText": "필터", "Size": "60px" }
```

### 편집 가능 컬럼

#### GoDataGridInputTextColumn

텍스트 편집.

```json
{ "Type": "GoDataGridInputTextColumn", "Name": "Name", "HeaderText": "이름", "Size": "100px" }
```

#### GoDataGridInputNumberColumn\<T\>

숫자 편집. T: Int32, Int64, Single, Double 등 CLR 타입명.

```json
{ "Type": "GoDataGridInputNumberColumn<Int32>", "Name": "Count", "HeaderText": "수량", "Size": "80px",
  "Minimum": 0, "Maximum": 999, "FormatString": null }
```

⚠ **CLR 타입명 사용!** `GoDataGridInputNumberColumn<Int32>` (O), `GoDataGridInputNumberColumn<int>` (X)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| T? | Minimum | 최솟값 | null |
| T? | Maximum | 최댓값 | null |
| string? | FormatString | 포맷 문자열 | null |

#### GoDataGridInputBoolColumn

ON/OFF 토글.

```json
{ "Type": "GoDataGridInputBoolColumn", "Name": "IsOnline", "HeaderText": "상태", "Size": "80px",
  "OnText": "ON", "OffText": "OFF" }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | OnText | ON 표시 텍스트 | "ON" |
| string? | OffText | OFF 표시 텍스트 | "OFF" |

#### GoDataGridInputComboColumn

드롭다운 선택.

```json
{ "Type": "GoDataGridInputComboColumn", "Name": "State", "HeaderText": "상태", "Size": "100px",
  "MaximumViewCount": 8, "ItemHeight": 30,
  "Items": [
    { "Text": "Idle", "Value": "Idle" },
    { "Text": "Running", "Value": "Running" },
    { "Text": "Error", "Value": "Error" }
  ] }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| List\<GoDataGridInputComboItem\> | Items | 선택 항목 목록 | [] |
| int | MaximumViewCount | 최대 표시 항목 수 | 8 |
| float | ItemHeight | 항목 높이(px) | 30 |

GoDataGridInputComboItem:

| 타입 | 이름 | 설명 |
|------|------|------|
| string? | Text | 표시 텍스트 |
| string? | Value | 값 |

#### GoDataGridInputTimeColumn

DateTime 편집.

```json
{ "Type": "GoDataGridInputTimeColumn", "Name": "LastUpdate", "HeaderText": "최종갱신", "Size": "140px",
  "DateTimeStyle": 0, "DateFormat": "yyyy-MM-dd", "TimeFormat": "HH:mm:ss" }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| GoDateTimeKind | DateTimeStyle | DateTime=0, Date=1, Time=2 | 0 |
| string | DateFormat | 날짜 포맷 | "yyyy-MM-dd" |
| string | TimeFormat | 시간 포맷 | "HH:mm:ss" |

#### GoDataGridInputColorColumn

색상 선택.

```json
{ "Type": "GoDataGridInputColorColumn", "Name": "TagColor", "HeaderText": "색상", "Size": "80px" }
```

### 동작 컬럼

#### GoDataGridButtonColumn

행별 동작 버튼. Name 불필요 (데이터 바인딩 대상 아님).

```json
{ "Type": "GoDataGridButtonColumn", "HeaderText": "삭제", "Size": "60px",
  "Text": "DEL", "ButtonColor": "Danger", "SelectButtonColor": "Select-light",
  "IconString": null, "IconSize": 12, "IconGap": 5 }
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | Text | 버튼 텍스트 | null |
| string? | ButtonColor | 버튼 색상 | "Danger" |
| string? | SelectButtonColor | 선택행 버튼 색상 | "Select-light" |
| string? | IconString | 아이콘 | null |
| float | IconSize | 아이콘 크기 | 12 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |

---

## 요약행 (SummaryRows)

숫자형 컬럼(NumberColumn, InputNumberColumn)에 자동 적용됨.

### GoDataGridSumSummaryRow

합계 요약행.

```json
{ "Type": "GoDataGridSumSummaryRow", "Title": "합계", "TitleColumnIndex": 0, "TitleColSpan": 3 }
```

### GoDataGridAverageSummaryRow

평균 요약행.

```json
{ "Type": "GoDataGridAverageSummaryRow", "Title": "평균", "TitleColumnIndex": 0, "TitleColSpan": 3 }
```

| 타입 | 이름 | 설명 |
|------|------|------|
| string? | Title | 요약행 제목 텍스트 |
| int | TitleColumnIndex | 제목 표시 시작 컬럼 인덱스 |
| int | TitleColSpan | 제목이 차지하는 컬럼 수 |

---

## 컬럼 타입 요약표

| 타입 | 용도 | 편집 | 주요 추가 속성 |
|------|------|------|---------------|
| `GoDataGridLabelColumn` | 텍스트 표시 | X | FormatString |
| `GoDataGridNumberColumn<T>` | 숫자 포맷 표시 | X | FormatString |
| `GoDataGridLampColumn` | bool → 램프 | X | OnColor |
| `GoDataGridCheckBoxColumn` | bool → 체크박스 | X | — |
| `GoDataGridButtonColumn` | 행별 버튼 | — | Text, ButtonColor |
| `GoDataGridInputTextColumn` | 텍스트 편집 | O | — |
| `GoDataGridInputNumberColumn<T>` | 숫자 편집 | O | Minimum, Maximum, FormatString |
| `GoDataGridInputBoolColumn` | ON/OFF 토글 | O | OnText, OffText |
| `GoDataGridInputComboColumn` | 드롭다운 선택 | O | Items[], MaximumViewCount, ItemHeight |
| `GoDataGridInputTimeColumn` | DateTime 편집 | O | DateTimeStyle, DateFormat, TimeFormat |
| `GoDataGridInputColorColumn` | 색상 선택 | O | — |

---

## 데이터 바인딩 규칙

- `dg.SetDataSource<T>(IEnumerable<T>)` — 리플렉션 기반
- **Column.Name**이 **T의 프로퍼티명**과 정확히 일치해야 바인딩됨
- 하나의 프로퍼티를 여러 컬럼에서 참조 가능 (예: `IsOnline` → LampColumn + InputBoolColumn)
- ButtonColumn은 데이터 바인딩 대상이 아니므로 Name 불필요
- 모든 Column의 Name이 T의 프로퍼티에 매칭되어야 함 (ButtonColumn 제외). 매칭 실패 시 예외 발생

⚠ **제네릭 컬럼의 T 타입은 데이터 객체의 프로퍼티 타입과 일치해야 한다.**
예: 프로퍼티가 `double Temperature`이면 `GoDataGridNumberColumn<Double>` 사용.

---

## C# 사용

### 데이터 클래스

```csharp
public class DeviceData
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Temperature { get; set; }
    public bool IsOnline { get; set; }
    public string State { get; set; }
    public DateTime LastUpdate { get; set; }
    public string TagColor { get; set; }
}
```

### 컬럼 구성 + 데이터 바인딩

```csharp
public partial class PageDataGrid : GoPage
{
    public PageDataGrid()
    {
        InitializeComponent();

        dg.ScrollMode = ScrollMode.Both;
        dg.SelectionMode = GoDataGridSelectionMode.Single;
        dg.Columns.Clear();

        // 읽기 전용
        dg.Columns.Add(new GoDataGridLabelColumn { Name = "Id", HeaderText = "ID", Size = "60px" });
        dg.Columns.Add(new GoDataGridLabelColumn { Name = "Name", HeaderText = "장치명", Size = "100px" });
        dg.Columns.Add(new GoDataGridNumberColumn<double> { Name = "Temperature", HeaderText = "온도", Size = "80px", FormatString = "0.0" });
        dg.Columns.Add(new GoDataGridLampColumn { Name = "IsOnline", HeaderText = "통신", Size = "60px" });

        // 편집 가능
        dg.Columns.Add(new GoDataGridInputBoolColumn { Name = "IsOnline", HeaderText = "상태", Size = "80px", OnText = "ON", OffText = "OFF" });
        dg.Columns.Add(new GoDataGridInputComboColumn
        {
            Name = "State", HeaderText = "상태", Size = "100px",
            Items = [
                new GoDataGridInputComboItem { Text = "Idle", Value = "Idle" },
                new GoDataGridInputComboItem { Text = "Running", Value = "Running" },
                new GoDataGridInputComboItem { Text = "Error", Value = "Error" },
            ]
        });
        dg.Columns.Add(new GoDataGridInputTimeColumn { Name = "LastUpdate", HeaderText = "최종갱신", Size = "140px" });
        dg.Columns.Add(new GoDataGridInputColorColumn { Name = "TagColor", HeaderText = "태그색", Size = "80px" });

        // 버튼 (Name 불필요)
        dg.Columns.Add(new GoDataGridButtonColumn { HeaderText = "삭제", Size = "60px", Text = "DEL", ButtonColor = "Danger" });

        // 요약행
        dg.SummaryRows.Add(new GoDataGridSumSummaryRow { Title = "합계", TitleColumnIndex = 0, TitleColSpan = 2 });
        dg.SummaryRows.Add(new GoDataGridAverageSummaryRow { Title = "평균", TitleColumnIndex = 0, TitleColSpan = 2 });

        // 이벤트
        dg.CellButtonClick += (s, e) =>
        {
            if (e.Cell.Row.Source is DeviceData data)
            {
                // data 기반 삭제 처리
            }
        };

        dg.ValueChanged += (s, e) =>
        {
            // e.Cell.Row.Source로 변경된 행 데이터 접근
        };

        dg.SelectedChanged += (s, e) =>
        {
            // 선택된 행 처리
        };

        // 데이터 바인딩
        dg.SetDataSource(deviceList);
    }
}
```

## 검증 완료

- 소스코드(GoDataGrid.cs): 속성 14개 + 이벤트 8개 (+ DropDownOpening 계열 3개)
- 컬럼 타입: 11종 (ImageColumn은 소스코드에 미존재)
- 요약행: 2종 (Sum, Average)
- HTML API(controls.html)와 소스코드 교차 검증 완료
- ScrollMode 소스코드 기본값=Vertical(1), JSON 기본값=0(Horizon) 불일치 확인
- SelectionMode 소스코드 기본값=Single(2), JSON 기본값=0(None) 불일치 확인
