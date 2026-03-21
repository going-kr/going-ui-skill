# GoTimeGraph

시간축 그래프 컨트롤. X축이 DateTime 기반으로 시계열 데이터를 표시.
상속: GoControl → GoTimeGraph

⚠ **SetDataSource** — XAxisName은 반드시 **DateTime 타입** 프로퍼티. (GoLineGraph는 string)
⚠ **XScale** — 화면에 표시되는 시간 범위. TimeSpan 형식 "HH:mm:ss". 기본 1시간.
⚠ **XAxisGraduationTime** — X축 눈금 간격. TimeSpan 형식. 기본 10분.
⚠ **Series** — GoLineGraphSeries 사용. 시리즈별 Minimum/Maximum으로 개별 Y축 스케일.
⚠ Selectable 기본값: **true** (생성자에서 설정)
⚠ GoLineGraph vs GoTimeGraph: LineGraph X축=string, TimeGraph X축=DateTime.
⚠ 범례 영역 더블클릭 시 시리즈 표시/숨김 선택 다이얼로그 표시.

## .gud JSON

```json
{
  "Type": "GoTimeGraph",
  "Value": {
    "GridColor": "Base3",
    "TextColor": "Fore",
    "RemarkColor": "Base2",
    "GraphColor": "Back",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "XScale": "01:00:00",
    "XAxisGraduationTime": "00:10:00",
    "YAxisGraduationCount": 10,
    "TimeFormatString": null,
    "ValueFormatString": null,
    "Series": [],
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
| TimeSpan | XScale | X축 표시 범위 | "01:00:00" (1시간) |
| TimeSpan | XAxisGraduationTime | X축 눈금 간격 | "00:10:00" (10분) |
| int | YAxisGraduationCount | Y축 눈금 수 | 10 |
| string? | TimeFormatString | X축 시간 포맷 | null |
| string? | ValueFormatString | Y축 값 포맷 | null |
| List\<GoLineGraphSeries\> | Series | 시리즈 목록 | [] |

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
var grpTime = (GoTimeGraph)dic["grpTime"];

// SetDataSource<T>(XAxisPropertyName, data, start?, end?)
// - XAxisName: DateTime 타입 프로퍼티 → X축 시간
// - 숫자형 프로퍼티가 Series.Name과 매칭되어 자동 바인딩
// - start/end: 선택적 표시 범위 제한
grpTime.SetDataSource("Date", SampleData.Datas2);
```

### 데이터 클래스 예시

```csharp
public class Data2
{
    public DateTime Date { get; set; }  // X축 시간 (DateTime)
    public double Temp { get; set; }    // Series.Name="Temp"
    public double Hum { get; set; }     // Series.Name="Hum"
}
```

### TimeFormatString 예시

```
"M/d\r\nHH:mm"        // 줄바꿈으로 날짜/시간 분리
"yyyy.MM.dd HH:mm:ss" // 한 줄 전체 표시
"HH:mm:ss"            // 시간만 표시
```

## 검증 완료

- 소스코드(GoTimeGraph.cs): GoProperty 속성 13개, 이벤트 없음
- 생성자에서 Selectable = true
- SetDataSource의 XAxisName은 DateTime 타입 (GoLineGraph의 string과 다름)
- start/end 파라미터로 표시 범위 제한 가능
