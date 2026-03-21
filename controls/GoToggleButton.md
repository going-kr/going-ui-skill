# GoToggleButton

토글 버튼 컨트롤. 클릭 시 Checked 상태가 전환되며 색상이 변경.
상속: GoControl → GoToggleButton

⚠ **ButtonClicked** + **CheckedChanged** 이벤트 2개. GoButton(ButtonClicked만)과 다름.
⚠ **CheckedText** 속성 — Checked=true일 때 표시되는 텍스트. GoButton에는 없음.
⚠ **AllowToggle** — false로 설정하면 토글 없이 ButtonClicked만 발생 (일반 버튼처럼 동작)
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoToggleButton",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "Text": "button",
    "CheckedText": "button",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "ButtonColor": "Base3",
    "CheckedButtonColor": "Select",
    "BorderColor": "Base3",
    "CheckedBorderColor": "Select",
    "Round": 1,
    "BorderWidth": 1,
    "FillStyle": 0,
    "Checked": false,
    "AllowToggle": true,
    "AutoFontSize": 0,
    "AutoIconSize": 0,
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
| string? | IconString | 아이콘 | null |
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 방향 | 0 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | Text | 기본 텍스트 | "button" |
| string | CheckedText | Checked 시 텍스트 | "button" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | ButtonColor | 기본 배경 색상 | "Base3" |
| string | CheckedButtonColor | Checked 배경 색상 | "Select" |
| string | BorderColor | 기본 테두리 | "Base3" |
| string | CheckedBorderColor | Checked 테두리 | "Select" |
| GoRoundType | Round | 모서리 | 1 (All) |
| float | BorderWidth | 테두리 두께 | 1 |
| GoButtonFillStyle | FillStyle | 채우기 스타일 | 0 (Flat) |
| bool | Checked | 토글 상태 | false |
| bool | AllowToggle | 토글 허용 여부 | true |
| GoAutoFontSize | AutoFontSize | 자동 폰트 | 0 |
| GoAutoFontSize | AutoIconSize | 자동 아이콘 | 0 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ButtonClicked | 버튼 클릭 시 (토글 후) |
| EventHandler | CheckedChanged | Checked 값 변경 시 |

## C# 사용

```csharp
var tglAuto = (GoToggleButton)dic["tglAuto"];

tglAuto.CheckedChanged += (s, e) =>
{
    if (tglAuto.Checked)
        DeviceManager.Current.SetAutoMode();
    else
        DeviceManager.Current.SetManualMode();
};
```

## 검증 완료

- 소스코드(GoToggleButton.cs): 속성 21개 + 이벤트 2개(ButtonClicked, CheckedChanged)
