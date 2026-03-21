# GoOnOff

ON/OFF 토글 스위치 컨트롤. 슬라이딩 커서로 ON/OFF 전환.
상속: GoControl → GoOnOff

⚠ GoOnOff ≠ GoSwitch! GoOnOff는 원형 커서가 좌우로 슬라이드, GoSwitch는 좌/우 영역 클릭.
⚠ **CursorColor** 속성이 있다. SliderColor가 아님!
⚠ Selectable 기본값: **true** (생성자에서 변경)

## .gud JSON

```json
{
  "Type": "GoOnOff",
  "Value": {
    "DrawText": true,
    "OnText": "On",
    "OffText": "Off",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "BoxColor": "Base1",
    "BorderColor": "Base3",
    "CursorColor": "Base3",
    "OnColor": "lime",
    "OffColor": "gray",
    "CursorIconDraw": true,
    "CursorIconString": "fa-power-off",
    "CursorIconSize": null,
    "Corner": null,
    "OnOff": false,
    "AutoFontSize": 0,
    "AutoCursorIconSize": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,100,40",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| bool | DrawText | ON/OFF 텍스트 표시 | true |
| string | OnText | ON 표시 텍스트 | "On" |
| string | OffText | OFF 표시 텍스트 | "Off" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BoxColor | 배경 색상 | "Base1" |
| string | BorderColor | 테두리 색상 | "Base3" |
| string | CursorColor | 커서 색상 | "Base3" |
| string | OnColor | ON 아이콘 색상 | "lime" |
| string | OffColor | OFF 아이콘 색상 | "gray" |
| bool | CursorIconDraw | 커서 아이콘 표시 | true |
| string | CursorIconString | 커서 아이콘 | "fa-power-off" |
| float? | CursorIconSize | 커서 아이콘 크기(null=자동) | null |
| float? | Corner | 모서리 둥글기(null=높이) | null |
| bool | OnOff | ON/OFF 상태 | false |
| GoAutoFontSize | AutoFontSize | 자동 폰트 크기 | 0 |
| GoAutoFontSize | AutoCursorIconSize | 자동 커서 아이콘 크기 | 0 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | OnOffChanged | OnOff 값 변경 시 발생 (애니메이션 완료 후) |

## C# 사용

```csharp
var swPower = (GoOnOff)dic["swPower"];

swPower.OnOffChanged += (s, e) =>
{
    if (swPower.OnOff)
        DeviceManager.Current.Start();
    else
        DeviceManager.Current.Stop();
};

// OnUpdate에서 외부 상태 반영
protected override void OnUpdate()
{
    swPower.OnOff = DeviceManager.Current.IsRunning;
}
```

## 검증 완료

- 소스코드(GoOnOff.cs): 속성 19개 + 이벤트 1개(OnOffChanged)
- 애니메이션 포함 (Animation.Time200)
