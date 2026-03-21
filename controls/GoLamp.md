# GoLamp

램프 컨트롤. ON/OFF 상태를 색상(원형 램프)으로 표시.
상속: GoControl → GoLamp

⚠ **OnOff** 속성으로 상태를 제어한다. Value가 아님!
⚠ 이벤트: **OnOffChanged** — OnOff 값 변경 시 자동 발생.
⚠ GoLamp에는 Round 속성이 **없다**. (GoButton/GoLabel과 다름)

## .gud JSON

```json
{
  "Type": "GoLamp",
  "Value": {
    "Text": "lamp",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "OnColor": "Good",
    "OffColor": "Base2",
    "OnOff": false,
    "LampSize": 24,
    "Gap": 10,
    "ContentAlignment": 4,
    "AutoFontSize": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,70,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | Text | 표시 텍스트 | "lamp" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | OnColor | ON 상태 색상 | "Good" |
| string | OffColor | OFF 상태 색상 | "Base2" |
| bool | OnOff | ON/OFF 상태 | false |
| int | LampSize | 램프 원형 크기(px) | 24 |
| int | Gap | 램프-텍스트 간격 | 10 |
| GoContentAlignment | ContentAlignment | 정렬 (MiddleCenter=4) | 4 |
| GoAutoFontSize | AutoFontSize | 자동 폰트 크기 | 0 (NotUsed) |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | OnOffChanged | OnOff 값 변경 시 발생 |

## C# 사용

```csharp
var lampRun = (GoLamp)dic["lampRun"];
var lampAlarm = (GoLamp)dic["lampAlarm"];

// OnUpdate에서 상태 반영
protected override void OnUpdate()
{
    lampRun.OnOff = DeviceManager.Current.IsRunning;
    lampAlarm.OnOff = DeviceManager.Current.HasAlarm;
}

// 이벤트 바인딩
lampRun.OnOffChanged += (s, e) =>
{
    Console.WriteLine($"Run: {lampRun.OnOff}");
};
```

## 검증 완료

- 소스코드(GoLamp.cs): 속성 12개 + 이벤트 1개(OnOffChanged)
- GoLamp에는 Round, BorderWidth, BackgroundDraw, BorderOnly, FillStyle, IconString 없음
