# GoLineGraph

꺾은선 그래프 컨트롤. 카테고리(string) X축에 다중 시리즈 라인을 표시.
상속: GoControl → GoLineGraph

⚠ **Series** — GoLineGraphSeries 사용. 시리즈별 Minimum/Maximum으로 개별 Y축 스케일 설정.
⚠ **PointWidth** — 데이터 포인트 간 간격(px). 데이터가 많으면 스크롤 자동 생성.
⚠ Selectable 기본값: **true** (생성자에서 설정)
⚠ **SetDataSource** — XAxisName은 반드시 **string 타입** 프로퍼티.
⚠ GoLineGraph vs GoTimeGraph: LineGraph의 X축은 string(카테고리), TimeGraph의 X축은 DateTime.
⚠ 범례 영역 더블클릭 시 시리즈 표시/숨김 선택 다이얼로그 표시.

## .gud JSON

```json
{
  "Type": "GoLineGraph",
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
    "Series": [],
    "PointWidth": 70,
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
| List\<GoLineGraphSeries\> | Series | 시리즈 목록 | [] |
| int | PointWidth | 포인트 간 간격(px) | 70 |

+ GoControl 공통 속성 → _common.md 참조

### GoLineGraphSeries 구조 (GoGraphSeries 상속)

| 타입 | 이름 | 설명 |
|------|------|------|
| string | Name | 데이터 프로퍼티명 (매칭 키) |
| string | Alias | 범례 표시명 |
| string | Color | 시리즈 색상 |
| bool | Visible | 표시 여부 |
| double | Minimum | Y축 최솟값 (시리즈별 개별 설정) |
| double | Maximum | Y축 최댓값 (시리즈별 개별 설정) |

## 이벤트 (Events)

없음 (GoControl 공통 이벤트만 사용)

## C# 사용

```csharp
var grpLine = (GoLineGraph)dic["grpLine"];

// SetDataSource<T>(XAxisPropertyName, data)
// - XAxisName: string 타입 프로퍼티 → X축 카테고리 라벨
// - 숫자형 프로퍼티가 Series.Name과 매칭되어 자동 바인딩
grpLine.SetDataSource("Date", SampleData.Datas);
```

### 데이터 클래스 예시

```csharp
public class Data1
{
    public string Date { get; set; }    // X축 라벨 (string)
    public double Temp { get; set; }    // Series.Name="Temp", Minimum=0, Maximum=100
    public double Hum { get; set; }     // Series.Name="Hum"
}
```

## 검증 완료

- 소스코드(GoLineGraph.cs): GoProperty 속성 11개, 이벤트 없음
- 생성자에서 Selectable = true
- Series는 GoLineGraphSeries (Minimum/Maximum 포함)
