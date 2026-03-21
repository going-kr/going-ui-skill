# GoCheckBox

체크박스 컨트롤. 사각형 체크 표시 + 텍스트.
상속: GoControl → GoCheckBox

⚠ GoCheckBox ≠ GoRadioBox. GoCheckBox는 독립 토글, GoRadioBox는 상호 배타적.
⚠ **CheckColor** 속성 — 체크마크 색상. CheckedColor 아님!
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoCheckBox",
  "Value": {
    "Text": "checkbox",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "BoxColor": "Base1",
    "CheckColor": "Fore",
    "Checked": false,
    "BoxSize": 24,
    "Gap": 10,
    "ContentAlignment": 4,
    "AutoFontSize": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,120,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | Text | 표시 텍스트 | "checkbox" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BoxColor | 체크박스 배경 | "Base1" |
| string | CheckColor | 체크마크 색상 | "Fore" |
| bool | Checked | 체크 상태 | false |
| int | BoxSize | 체크박스 크기(px) | 24 |
| int | Gap | 박스-텍스트 간격 | 10 |
| GoContentAlignment | ContentAlignment | 정렬 | 4 (MiddleCenter) |
| GoAutoFontSize | AutoFontSize | 자동 폰트 | 0 |

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | CheckedChanged | Checked 값 변경 시 |

## C# 사용

```csharp
var chkAlarm = (GoCheckBox)dic["chkAlarm"];
chkAlarm.CheckedChanged += (s, e) =>
{
    DeviceManager.Current.AlarmEnabled = chkAlarm.Checked;
};
```

## 검증 완료

- 소스코드(GoCheckBox.cs): 속성 12개 + 이벤트 1개
