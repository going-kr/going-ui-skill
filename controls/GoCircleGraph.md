# GoCircleGraph

원형(파이/도넛) 그래프 컨트롤. 카테고리별 비율을 원형 차트로 표시.
상속: GoControl → GoCircleGraph

⚠ **Series** — GoGraphSeries 사용 (GoLineGraphSeries 아님). 시리즈별 Minimum/Maximum 없음.
⚠ Selectable 기본값: **true** (생성자에서 설정)
⚠ **SetDataSource** — XAxisName(CategoryAxisName)은 반드시 **string 타입** 프로퍼티.
⚠ 마우스 호버 시 해당 영역 강조 + 중앙에 값/비율 표시.
⚠ 좌/우 화살표로 카테고리 간 이동 가능.

## .gud JSON

```json
{
  "Type": "GoCircleGraph",
  "Value": {
    "GridColor": "Base3",
    "TextColor": "Fore",
    "RemarkColor": "Base2",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
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
| string | GridColor | 격자/테두리 색상 | "Base3" |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | RemarkColor | 범례 배경 색상 | "Base2" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| List\<GoGraphSeries\> | Series | 시리즈 목록 | [] |

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
var grpCircle = (GoCircleGraph)dic["grpCircle"];

// SetDataSource<T>(CategoryAxisName, data)
// - CategoryAxisName: string 타입 프로퍼티 → 카테고리 라벨
// - 숫자형 프로퍼티가 Series.Name과 매칭되어 자동 바인딩
grpCircle.SetDataSource("Date", SampleData.Datas);
```

### 데이터 클래스 예시

```csharp
public class Data1
{
    public string Date { get; set; }    // 카테고리 라벨 (string)
    public double Temp { get; set; }    // Series.Name="Temp"
    public double Hum { get; set; }     // Series.Name="Hum"
}
```

## 검증 완료

- 소스코드(GoCircleGraph.cs): GoProperty 속성 7개, 이벤트 없음
- 생성자에서 Selectable = true
- Series는 GoGraphSeries (GoLineGraphSeries 아님)
- 소스코드 생성자에서 Selectable = true로 설정됨 → true가 정본
