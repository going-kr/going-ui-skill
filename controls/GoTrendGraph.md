# GoTrendGraph

실시간 트렌드 그래프 컨트롤. Start/Stop으로 데이터 수집, SetData로 값 갱신.
상속: GoControl → GoTrendGraph

⚠ **Start(obj) → SetData(obj) 패턴** — GoTimeGraph의 SetDataSource와 완전히 다름!
⚠ **Interval** — 데이터 수집 주기(ms). 기본 1000ms. 고속 수집 시 10~100ms.
⚠ **MaximumXScale** — X축 최대 확대 범위. 이 범위를 넘는 오래된 데이터는 자동 삭제.
⚠ **IsStart** — get only. Start() 호출 후 true, Stop() 후 false.
⚠ **Pause** — [JsonIgnore] 런타임 전용. 일시정지 중 데이터 버퍼링, 해제 시 반영.
⚠ **Series** — GoLineGraphSeries 사용. 시리즈별 Minimum/Maximum으로 개별 Y축 스케일.
⚠ Selectable 기본값: **true** (생성자에서 설정)
⚠ 범례 영역 더블클릭 시 시리즈 표시/숨김 선택 다이얼로그 표시.

## .gud JSON

```json
{
  "Type": "GoTrendGraph",
  "Value": {
    "GridColor": "Base3",
    "TextColor": "Fore",
    "RemarkColor": "Base2",
    "GraphColor": "Back",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "MaximumXScale": "1.00:00:00",
    "XScale": "01:00:00",
    "XAxisGraduationTime": "00:10:00",
    "YAxisGraduationCount": 10,
    "TimeFormatString": null,
    "ValueFormatString": null,
    "Interval": 1000,
    "IsStart": false,
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
| TimeSpan | MaximumXScale | X축 최대 범위 (데이터 보존 한도) | "1.00:00:00" (1일) |
| TimeSpan | XScale | X축 표시 범위 | "01:00:00" (1시간) |
| TimeSpan | XAxisGraduationTime | X축 눈금 간격 | "00:10:00" (10분) |
| int | YAxisGraduationCount | Y축 눈금 수 | 10 |
| string? | TimeFormatString | X축 시간 포맷 | null |
| string? | ValueFormatString | Y축 값 포맷 | null |
| int | Interval | 데이터 수집 주기(ms) | 1000 |
| bool | IsStart | 수집 실행 상태 (get only) | false |
| List\<GoLineGraphSeries\> | Series | 시리즈 목록 | [] |

런타임 전용 (JSON 미포함):

| 타입 | 이름 | 설명 |
|------|------|------|
| bool | Pause | 일시정지 (버퍼링 후 해제 시 반영) |

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

## 메서드 (Methods)

| 리턴 | 이름 | 파라미터 | 설명 |
|------|------|---------|------|
| void | Start\<T\> | (T value) | 수집 시작. T의 프로퍼티명이 Series.Name과 매칭 |
| void | Stop | () | 수집 중지 |
| void | SetData\<T\> | (T Data) | 현재 시점 데이터 갱신 |

## C# 사용

```csharp
public partial class PageTrend : GoPage
{
    Data2 value = new Data2();

    public PageTrend()
    {
        InitializeComponent();

        var grpTrend = (GoTrendGraph)dic["grpTrend"];

        // 1. Start<T>(template) — 트렌드 수집 시작
        grpTrend.Start(value);
    }

    // 2. OnUpdate — 매 프레임 데이터 갱신
    protected override void OnUpdate()
    {
        var data = Main.DevMgr.Data;
        value.Temp = data.Temperature;
        value.Hum = data.Humidity;

        // SetData로 소스 객체 갱신 → 다음 Interval에 반영
        grpTrend.SetData(value);
        base.OnUpdate();
    }
}
```

### 흐름

`Start(obj)` → 매 프레임 `SetData(obj)` → 내부에서 `Interval`(ms) 주기로 자동 샘플링 → `Stop()`으로 중단.

### 데이터 클래스 예시

```csharp
public class Data2
{
    public DateTime Date { get; set; }  // (트렌드에서는 사용 안 함)
    public double Temp { get; set; }    // Series.Name="Temp"
    public double Hum { get; set; }     // Series.Name="Hum"
}
```

## 검증 완료

- 소스코드(GoTrendGraph.cs): GoProperty 속성 16개 + Pause([JsonIgnore])
- 메서드 3개: Start, Stop, SetData
- 생성자에서 Selectable = true
- GoTimeGraph와 달리 SetDataSource가 아닌 Start/SetData 패턴 사용
