# GoRadioButton

라디오 버튼 컨트롤. 같은 컨테이너 내 다른 GoRadioButton과 상호 배타적 선택.
상속: GoControl → GoRadioButton

⚠ GoRadioButton ≠ GoRadioBox. GoRadioButton은 버튼형, GoRadioBox는 체크박스형.
⚠ Checked = true 설정 시, **같은 Parent의 다른 GoRadioButton은 자동으로 Checked=false** 됨.
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoRadioButton",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "Text": "button",
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
| string | Text | 표시 텍스트 | "button" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | ButtonColor | 기본 배경 | "Base3" |
| string | CheckedButtonColor | 선택 시 배경 | "Select" |
| string | BorderColor | 기본 테두리 | "Base3" |
| string | CheckedBorderColor | 선택 시 테두리 | "Select" |
| GoRoundType | Round | 모서리 | 1 (All) |
| float | BorderWidth | 테두리 두께 | 1 |
| GoButtonFillStyle | FillStyle | 채우기 스타일 | 0 (Flat) |
| bool | Checked | 선택 상태 | false |
| GoAutoFontSize | AutoFontSize | 자동 폰트 | 0 |
| GoAutoFontSize | AutoIconSize | 자동 아이콘 | 0 |

+ GoControl 공통 속성 → _common.md 참조

⚠ GoToggleButton과 달리 **CheckedText, AllowToggle 없음**. 클릭 시 항상 Checked=true로만 전환.

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ButtonClicked | 버튼 클릭 시 |
| EventHandler | CheckedChanged | Checked 값 변경 시 |

## C# 사용

```csharp
var rbAuto = (GoRadioButton)dic["rbAuto"];
var rbManual = (GoRadioButton)dic["rbManual"];

rbAuto.CheckedChanged += (s, e) =>
{
    if (rbAuto.Checked) SetAutoMode();
};

rbManual.CheckedChanged += (s, e) =>
{
    if (rbManual.Checked) SetManualMode();
};
```

## 검증 완료

- 소스코드(GoRadioButton.cs): 속성 19개 + 이벤트 2개
- 클릭 시 Checked = true만 (false 전환 없음), 같은 Parent 내 배타적 선택
