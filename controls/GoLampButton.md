# GoLampButton

램프+버튼 결합 컨트롤. 클릭 가능한 버튼에 ON/OFF 램프 표시.
상속: GoControl → GoLampButton

⚠ GoLampButton은 GoButton + GoLamp 결합. **ButtonClicked** + **OnOffChanged** 이벤트 2개.
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoLampButton",
  "Value": {
    "Text": "button",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "ButtonColor": "Base3",
    "BorderColor": "Base3",
    "OnColor": "Good",
    "OffColor": "Base2",
    "Round": 1,
    "BorderWidth": 1,
    "FillStyle": 0,
    "OnOff": false,
    "LampSize": 24,
    "Gap": 10,
    "AutoFontSize": 0,
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
| string | Text | 표시 텍스트 | "button" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | ButtonColor | 버튼 배경 | "Base3" |
| string | BorderColor | 테두리 색상 | "Base3" |
| string | OnColor | ON 램프 색상 | "Good" |
| string | OffColor | OFF 램프 색상 | "Base2" |
| GoRoundType | Round | 모서리 | 1 (All) |
| float | BorderWidth | 테두리 두께 | 1 |
| GoButtonFillStyle | FillStyle | 채우기 스타일 | 0 (Flat) |
| bool | OnOff | 램프 ON/OFF | false |
| int | LampSize | 램프 크기(px) | 24 |
| int | Gap | 램프-텍스트 간격 | 10 |
| GoAutoFontSize | AutoFontSize | 자동 폰트 | 0 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ButtonClicked | 버튼 클릭 시 |
| EventHandler | OnOffChanged | OnOff 값 변경 시 |

## C# 사용

```csharp
var lbtnPump = (GoLampButton)dic["lbtnPump"];

lbtnPump.ButtonClicked += (s, e) =>
{
    lbtnPump.OnOff = !lbtnPump.OnOff;
    DeviceManager.Current.SetPump(lbtnPump.OnOff);
};

// OnUpdate에서 외부 상태 반영
protected override void OnUpdate()
{
    lbtnPump.OnOff = DeviceManager.Current.IsPumpRunning;
}
```

## 검증 완료

- 소스코드(GoLampButton.cs): 속성 16개 + 이벤트 2개(ButtonClicked, OnOffChanged)
- GoLamp처럼 LampSize/Gap 있고, GoButton처럼 ButtonColor/FillStyle 있음
