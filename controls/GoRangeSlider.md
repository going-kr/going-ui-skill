# GoRangeSlider

범위 슬라이더 컨트롤. 두 핸들(Lower/Upper)로 Min~Max 내 범위 선택.
상속: GoControl → GoRangeSlider (IDisposable)

⚠ GoSlider와 거의 동일한 속성 구조이나, **Value 대신 LowerValue/UpperValue** 사용!
⚠ **SliderColor** 속성 사용 (GoSlider와 동일). CursorColor 아님!
⚠ **MinHandleSeparation** — 두 핸들 간 최소 간격 (정규화 값 0~1). 기본 0.05.
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoRangeSlider",
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
    "LowerValue": 0,
    "UpperValue": 0,
    "LowerValueString": null,
    "UpperValueString": null,
    "Minimum": 0,
    "Maximum": 100,
    "MinHandleSeparation": 0.05,
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

## 속성 (Properties)

GoSlider와 동일한 외형 속성 (IconString~TickSize) + 아래 범위 전용:

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| double | LowerValue | 하한 값 | 0 |
| double | UpperValue | 상한 값 | 0 |
| string? | LowerValueString | 하한 표시 문자열(자동) | null |
| string? | UpperValueString | 상한 표시 문자열(자동) | null |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| float | MinHandleSeparation | 핸들 최소 간격(0~1) | 0.05 |

+ GoSlider와 동일 외형 속성 26개 + GoControl 공통 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | LowerValueChanged | LowerValue 변경 시 |
| EventHandler | UpperValueChanged | UpperValue 변경 시 |
| EventHandler | RangeChanged | 어느 쪽이든 변경 시 |
| EventHandler | SliderDragStarted | 드래그 시작 |
| EventHandler | SliderDragCompleted | 드래그 완료 |

## C# 사용

```csharp
var rng = (GoRangeSlider)dic["rngTemp"];

rng.RangeChanged += (s, e) =>
{
    lblRange.Text = $"{rng.LowerValue:F0} ~ {rng.UpperValue:F0}°C";
};
```

## 검증 완료

- 소스코드(GoRangeSlider.cs): 속성 33개 + 이벤트 5개
- GoSlider 대비 추가: LowerValue, UpperValue, LowerValueString, UpperValueString, MinHandleSeparation
