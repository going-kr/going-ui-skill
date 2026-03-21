# GoSlider

슬라이더 컨트롤. 드래그 핸들로 Min~Max 범위 내 값 조절.
상속: GoControl → GoSlider (IDisposable)

⚠ **SliderColor** 속성 사용! CursorColor 아님! (다른 프레임워크에서 유추하지 마라)
⚠ **ProgressColor** 속성이 있다 — 슬라이더 트랙의 진행 영역 색상.
⚠ **BoxColor** 속성 (배경색). BackColor, BackgroundColor 아님!
⚠ Direction은 **GoDirectionHV** (Horizon=0, Vertical=1). ProgressDirection이 아님!
⚠ Selectable 기본값: **true** (생성자에서 변경)

## .gud JSON

```json
{
  "Type": "GoSlider",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconGap": 5,
    "IconDirection": 0,
    "Text": "slider",
    "FontName": "나눔고딕",
    "FontSize": 12,
    "BackgroundDraw": false,
    "BorderOnly": false,
    "TextColor": "Fore",
    "BoxColor": "Back",
    "SliderColor": "Base5",
    "ProgressColor": "Base1",
    "BorderColor": "danger",
    "Round": 1,
    "Direction": 0,
    "ShowValueLabel": true,
    "ValueFormat": "0",
    "BarSize": 4,
    "HandleRadius": 15,
    "EnableShadow": true,
    "HandleHoverScale": 1.05,
    "Tick": null,
    "ShowTicks": false,
    "TickCount": 5,
    "TickSize": 10,
    "Value": 0,
    "ValueString": null,
    "Minimum": 0,
    "Maximum": 100,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,200,50",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

권장 크기: 가로 최소 150, 세로 50

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | IconString | 아이콘 | null |
| float | IconSize | 아이콘 크기 | 12 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| GoDirectionHV | IconDirection | 아이콘 방향 | 0 |
| string | Text | 라벨 텍스트 | "slider" |
| string | FontName | 폰트명 | "나눔고딕" |
| float | FontSize | 폰트 크기 | 12 |
| bool | BackgroundDraw | 배경 그리기 | false |
| bool | BorderOnly | 테두리만 그리기 | false |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BoxColor | 배경 색상 | "Back" |
| string | SliderColor | 핸들+진행바 색상 | "Base5" |
| string | ProgressColor | 트랙 빈영역 색상 | "Base1" |
| string | BorderColor | 테두리 색상 | "danger" |
| GoRoundType | Round | 모서리 (All=1) | 1 |
| GoDirectionHV | Direction | 방향 (Horizon=0, Vertical=1) | 0 |
| bool | ShowValueLabel | 핸들 위 값 표시 | true |
| string | ValueFormat | 값 포맷 | "0" |
| int | BarSize | 트랙 두께(px) | 4 |
| float | HandleRadius | 핸들 반경(px) | 15 |
| bool | EnableShadow | 그림자 효과 | true |
| float | HandleHoverScale | 호버 시 핸들 확대 비율 | 1.05 |
| double? | Tick | 단계 값(null=연속) | null |
| bool | ShowTicks | 틱 마크 표시 | false |
| int | TickCount | 틱 개수 | 5 |
| float | TickSize | 틱 크기(px) | 10 |
| double | Value | 현재 값 | 0 |
| string? | ValueString | 값 문자열(자동 생성) | null |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | SliderDragStarted | 드래그 시작 |
| EventHandler | SliderDragCompleted | 드래그 완료 |
| EventHandler | ValueChanged | Value 변경 시 발생 |

## 메서드 (Methods)

| 반환 | 이름 | 설명 |
|------|------|------|
| void | IncrementalValue() | 값 1단계 증가 (Tick 있으면 Tick 단위) |
| void | DecrementalValue() | 값 1단계 감소 |
| void | SetValueToMinimum() | 최솟값으로 설정 |
| void | SetValueToMaximum() | 최댓값으로 설정 |

## C# 사용

```csharp
var sldTemp = (GoSlider)dic["sldTemp"];

// Value 변경 감지
sldTemp.ValueChanged += (s, e) =>
{
    lblValue.Text = $"설정: {sldTemp.Value:F1}°C";
};

// 드래그 완료 시 서버 전송
sldTemp.SliderDragCompleted += (s, e) =>
{
    DeviceManager.Current.SetTemperature(sldTemp.Value);
};

// OnUpdate에서 외부 값 반영
protected override void OnUpdate()
{
    sldTemp.Value = DeviceManager.Current.CurrentTemp;
}
```

## 검증 완료

- 소스코드(GoSlider.cs): 속성 30개 + 이벤트 3개 + 메서드 4개
- GoFontStyle 속성이 소스코드에 없음 (FontName, FontSize만 있고 FontStyle은 없음) — 누락 아닌 의도적 미구현
