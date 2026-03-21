# GoKnob

노브(다이얼) 컨트롤. 원형 드래그로 Min~Max 범위 값 조절.
상속: GoControl → GoKnob

⚠ **KnobColor** 속성 사용! ButtonColor, SliderColor 아님.
⚠ **CursorColor** — 노브 포인터(바늘) 색상.
⚠ **SweepAngle** — 노브 회전 범위(도). 기본 270도.
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoKnob",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "KnobColor": "Base3",
    "CursorColor": "Fore",
    "Value": 0,
    "Minimum": 0,
    "Maximum": 100,
    "Tick": null,
    "Format": "0",
    "SweepAngle": 270,
    "DrawText": true,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,80,80",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

권장 크기: 정사각형 80×80 이상

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | KnobColor | 노브 배경 색상 | "Base3" |
| string | CursorColor | 포인터 색상 | "Fore" |
| double | Value | 현재 값 | 0 |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| double? | Tick | 단계 값(null=연속) | null |
| string | Format | 값 표시 포맷 | "0" |
| int | SweepAngle | 회전 범위(도) | 270 |
| bool | DrawText | 중앙 값 표시 | true |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 발생 |

## C# 사용

```csharp
var knbVolume = (GoKnob)dic["knbVolume"];

knbVolume.ValueChanged += (s, e) =>
{
    DeviceManager.Current.SetVolume(knbVolume.Value);
};

protected override void OnUpdate()
{
    knbVolume.Value = DeviceManager.Current.Volume;
}
```

## 검증 완료

- 소스코드(GoKnob.cs): 속성 13개 + 이벤트 1개(ValueChanged)
