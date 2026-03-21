# IcButton

ImageCanvas 버튼. 클릭 시 부모의 OnImage 영역을 렌더링하고 텍스트/아이콘을 오버레이한다.
상속: GoControl → IcButton

⚠ 누르면 부모의 OnImage에서, 뗀 상태에서는 OffImage에서 해당 영역을 잘라 표시한다.
⚠ **TextColor 기본값은 "Black"** (GoButton의 "Fore"와 다름).
⚠ 이벤트는 **ButtonClicked** (EventHandler, 제네릭 아님).

## .gud JSON

```json
{
  "Type": "IcButton",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "Text": "button",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Black",
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
| string? | IconString | 아이콘 문자열 (FontAwesome) | null |
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 방향 (Horizon=0, Vertical=1) | 0 (Horizon) |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | Text | 표시 텍스트 | "button" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Black" |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ButtonClicked | 버튼 클릭 시 발생 (EventArgs.Empty) |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var btn = (IcButton)dic["icBtnStart"];

btn.ButtonClicked += (s, e) =>
{
    // 버튼 클릭 처리
};
```

## 검증 완료

- 소스코드(IcButton.cs): 속성 9개 + 이벤트 1개(ButtonClicked) 확인
