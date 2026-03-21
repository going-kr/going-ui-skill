# GoSwitch

양방향 스위치 컨트롤. 좌(Off)/우(On) 영역 클릭으로 ON/OFF 전환.
상속: GoControl → GoSwitch

⚠ GoSwitch ≠ GoOnOff! GoSwitch는 좌/우 영역 클릭, GoOnOff는 커서 슬라이드.
⚠ GoSwitch에는 **Value 속성이 없다!** OnOff(bool)만 사용.
⚠ GoSwitch에는 **TextColor 속성이 없다!** OnTextColor/OffTextColor로 분리.
⚠ **SwitchColor** 속성 사용. CursorColor/SliderColor 아님!
⚠ Selectable 기본값: **true** (생성자에서 변경)

## .gud JSON

```json
{
  "Type": "GoSwitch",
  "Value": {
    "OnText": "On",
    "OffText": "Off",
    "OnIconString": null,
    "OffIconString": null,
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "OnTextColor": "Fore",
    "OffTextColor": "Base5",
    "BoxColor": "Base1",
    "BorderColor": "Base3",
    "SwitchColor": "Base3",
    "OnIconColor": "lime",
    "OffIconColor": "red",
    "OnOff": false,
    "AutoFontSize": 0,
    "AutoIconSize": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,120,40",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | OnText | ON 텍스트 | "On" |
| string | OffText | OFF 텍스트 | "Off" |
| string? | OnIconString | ON 아이콘 | null |
| string? | OffIconString | OFF 아이콘 | null |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 방향 | 0 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | OnTextColor | ON 텍스트 색상 | "Fore" |
| string | OffTextColor | OFF 텍스트 색상 | "Base5" |
| string | BoxColor | 배경 색상 | "Base1" |
| string | BorderColor | 테두리 색상 | "Base3" |
| string | SwitchColor | 스위치 색상 | "Base3" |
| string | OnIconColor | ON 아이콘 색상 | "lime" |
| string | OffIconColor | OFF 아이콘 색상 | "red" |
| bool | OnOff | ON/OFF 상태 | false |
| GoAutoFontSize | AutoFontSize | 자동 폰트 크기 | 0 |
| GoAutoFontSize | AutoIconSize | 자동 아이콘 크기 | 0 |

+ GoControl 공통 속성 → _common.md 참조

⚠ GoSwitch에 **없는** 속성: Value, TextColor, Round, BorderWidth, CursorColor, BackgroundDraw, FillStyle

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | OnOffChanged | OnOff 값 변경 시 발생 (애니메이션 완료 후) |

## C# 사용

```csharp
var swMode = (GoSwitch)dic["swMode"];

swMode.OnOffChanged += (s, e) =>
{
    if (swMode.OnOff)
        SetAutoMode();
    else
        SetManualMode();
};
```

## 검증 완료

- 소스코드(GoSwitch.cs): 속성 20개 + 이벤트 1개(OnOffChanged)
- GoSwitch는 GoOnOff와 달리 드래그 없이 좌/우 영역 클릭만 지원
