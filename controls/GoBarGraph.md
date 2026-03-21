# GoBarGraph

막대 그래프 컨트롤. 카테고리별 데이터를 수직/수평 바로 표시.
상속: GoControl → GoBarGraph

⚠ **Mode** — Stack(0)=누적, List(1)=나란히. 기본값 List(1). JSON에 숫자로 입력.
⚠ **Direction** — Horizon(0)=수평 바, Vertical(1)=수직 바. 기본값 Vertical(1).
⚠ **Minimum/Maximum** — nullable. null이면 데이터 기반 자동 스케일.
⚠ **Series** — GoGraphSeries 사용 (GoLineGraphSeries 아님). Minimum/Maximum 없음.
⚠ Selectable 기본값: **true** (생성자에서 설정)
⚠ **SetDataSource** — XAxisName은 반드시 **string 타입** 프로퍼티.

## .gud JSON

```json
{
  "Type": "GoBarGraph",
  "Value": {
    "GridColor": "Base3",
    "TextColor": "Fore",
    "RemarkColor": "Base2",
    "GraphColor": "Back",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "GraduationCount": 10,
    "FormatString": null,
    "Mode": 1,
    "Direction": 1,
    "Series": [],
    "BarSize": 20,
    "BarGap": 20,
    "Minimum": null,
    "Maximum": null,
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

> `GoBarGraphMode` — Stack=0, List=1
> `GoDirectionHV` — Horizon=0, Vertical=1

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | GridColor | 격자선 색상 | "Base3" |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | RemarkColor | 범례 배경 색상 | "Base2" |
| string | GraphColor | 그래프 영역 배경 | "Back" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| int | GraduationCount | Y축 눈금 수 | 10 |
| string? | FormatString | 값 표시 형식 | null |
| GoBarGraphMode | Mode | 바 모드 (Stack=0, List=1) | 1 (List) |
| GoDirectionHV | Direction | 바 방향 (Horizon=0, Vertical=1) | 1 (Vertical) |
| List\<GoGraphSeries\> | Series | 시리즈 목록 | [] |
| int | BarSize | 바 너비(px) | 20 |
| int | BarGap | 바 간격(px) | 20 |
| double? | Minimum | Y축 최솟값 (null=자동) | null |
| double? | Maximum | Y축 최댓값 (null=자동) | null |

+ GoControl 공통 속성 → _common.md 참조

### GoGraphSeries 구조

| 타입 | 이름 | 설명 |
|------|------|------|
| string | Name | 데이터 프로퍼티명 (매칭 키) |
| string | Alias | 범례 표시명 |
| string | Color | 시리즈 색상 (테마키 또는 직접 지정) |
| bool | Visible | 표시 여부 |

## 이벤트 (Events)

없음 (GoControl 공통 이벤트만 사용)

## C# 사용

```csharp
var grpBar = (GoBarGraph)dic["grpBar"];

// SetDataSource<T>(XAxisPropertyName, data)
// - XAxisName: string 타입 프로퍼티 → X축 라벨
// - 숫자형 프로퍼티가 Series.Name과 매칭되어 자동 바인딩
grpBar.SetDataSource("Date", SampleData.Datas);
```

### 데이터 클래스 예시

```csharp
public class Data1
{
    public string Date { get; set; }    // X축 라벨 (string)
    public double Temp { get; set; }    // Series.Name="Temp"
    public double Hum { get; set; }     // Series.Name="Hum"
}
```

## 검증 완료

- 소스코드(GoBarGraph.cs): GoProperty 속성 16개, 이벤트 없음
- 생성자에서 Selectable = true
- Series는 GoGraphSeries (GoLineGraphSeries 아님)
