# IcOnOff

ImageCanvas ON/OFF 상태 표시. OnOff 값에 따라 OffImage/OnImage 배경 영역을 전환 렌더링한다.
상속: GoControl → IcOnOff

⚠ OnOff=true면 부모의 OnImage에서, false면 OffImage에서 해당 영역을 잘라 표시.
⚠ **ToggleMode=false가 기본값** — 클릭으로 자동 토글하려면 true로 설정.
⚠ ToggleMode=true일 때 MouseDown에서 토글된다 (MouseUp 아님).

## .gud JSON

```json
{
  "Type": "IcOnOff",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "Text": "onoff",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Black",
    "OnOff": false,
    "ToggleMode": false,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,70,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | IconString | 오버레이 아이콘 문자열 (FontAwesome) | null |
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 방향 (Horizon=0, Vertical=1) | 0 (Horizon) |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | Text | 오버레이 텍스트 | "onoff" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Black" |
| bool | OnOff | ON/OFF 상태. 변경 시 ValueChanged 발생 | false |
| bool | ToggleMode | 클릭 시 자동 토글 여부 | false |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | OnOff 값 변경 시 발생 |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var onoff = (IcOnOff)dic["icOnOffPump"];

// 프로그램에서 상태 설정
onoff.OnOff = true;

// 값 변경 이벤트
onoff.ValueChanged += (s, e) =>
{
    var state = onoff.OnOff;
};
```

## 검증 완료

- 소스코드(IcOnOff.cs): 속성 11개 + 이벤트 1개(ValueChanged) 확인
- OnOff 프로퍼티: setter에서 ValueChanged 발생 확인
- ToggleMode: MouseDown에서 클릭 시 토글 확인
