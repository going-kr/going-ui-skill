# GoRadioBox

라디오 박스 컨트롤. 원형 라디오 버튼 + 텍스트. 같은 컨테이너 내 상호 배타적.
상속: GoControl → GoRadioBox

⚠ GoRadioBox ≠ GoRadioButton! GoRadioBox는 원형 라디오+텍스트, GoRadioButton은 버튼형.
⚠ Checked=true 설정 시 **같은 Parent의 다른 GoRadioBox는 자동으로 Checked=false**
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoRadioBox",
  "Value": {
    "Text": "radiobox",
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

GoCheckBox와 동일 구조 (12개 속성).

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | Text | 표시 텍스트 | "radiobox" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BoxColor | 원형 배경 | "Base1" |
| string | CheckColor | 선택 표시 색상 | "Fore" |
| bool | Checked | 선택 상태 | false |
| int | BoxSize | 원형 크기(px) | 24 |
| int | Gap | 원-텍스트 간격 | 10 |
| GoContentAlignment | ContentAlignment | 정렬 | 4 |
| GoAutoFontSize | AutoFontSize | 자동 폰트 | 0 |

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | CheckedChanged | Checked 값 변경 시 |

## C# 사용

```csharp
var rbSerial = (GoRadioBox)dic["rbSerial"];
var rbTCP = (GoRadioBox)dic["rbTCP"];

rbSerial.CheckedChanged += (s, e) =>
{
    if (rbSerial.Checked) SetCommMode("Serial");
};
rbTCP.CheckedChanged += (s, e) =>
{
    if (rbTCP.Checked) SetCommMode("TCP");
};
```

## 검증 완료

- 소스코드(GoRadioBox.cs): 속성 12개 + 이벤트 1개
- GoCheckBox와 구조 동일, 동작만 다름 (상호 배타)
