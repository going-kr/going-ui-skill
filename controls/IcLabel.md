# IcLabel

ImageCanvas 레이블. 배경 이미지 위에 텍스트/아이콘을 렌더링한다.
상속: GoControl → IcLabel

⚠ 배경을 그리지 않는다 — 이미지 위에 텍스트만 오버레이.
⚠ **TextColor 기본값은 "Black"** (GoLabel의 "Fore"와 다름).
⚠ 반드시 IcPage 또는 IcContainer 안에 배치해야 렌더링된다.

## .gud JSON

```json
{
  "Type": "IcLabel",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "Text": "label",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Black",
    "ContentAlignment": 4,
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
| string? | IconString | 아이콘 문자열 (FontAwesome) | null |
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 방향 (Horizon=0, Vertical=1) | 0 (Horizon) |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | Text | 표시 텍스트 | "label" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Black" |
| GoContentAlignment | ContentAlignment | 텍스트 정렬 (MiddleCenter=4) | 4 (MiddleCenter) |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var lbl = (IcLabel)dic["icLblValue"];

lbl.Text = "온도: 25.3";
lbl.TextColor = "Red";
```

## 검증 완료

- 소스코드(IcLabel.cs): 속성 10개 확인, TextColor="Black" 기본값 확인
