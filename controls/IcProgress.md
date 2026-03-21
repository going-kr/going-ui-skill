# IcProgress

ImageCanvas 진행 막대. OffBarImage/OnBarImage 이미지를 사용하여 진행률을 렌더링한다.
상속: GoControl → IcProgress

⚠ OnBarImage/OffBarImage가 **null이면 부모 이미지에서 슬라이싱** (부모 OffImage/OnImage 공유 모드).
⚠ OnBarImage/OffBarImage를 지정하면 **독립 이미지 모드**로 동작.
⚠ Value는 Minimum~Maximum 범위로 자동 클램프된다.

## .gud JSON

```json
{
  "Type": "IcProgress",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Black",
    "OnBarImage": null,
    "OffBarImage": null,
    "FormatString": "0",
    "Minimum": 0,
    "Maximum": 100,
    "Value": 0,
    "DrawText": true,
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
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Black" |
| string? | OnBarImage | 채워진 영역 이미지 키 | null |
| string? | OffBarImage | 빈 영역(배경 바) 이미지 키 | null |
| string | FormatString | 값 표시 형식 문자열 | "0" |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| double | Value | 현재 값. 변경 시 ValueChanged 발생 | 0 |
| bool | DrawText | 값 텍스트 표시 여부 | true |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 발생 |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var prog = (IcProgress)dic["icProgTemp"];

prog.Minimum = 0;
prog.Maximum = 100;
prog.Value = 75.5;
prog.FormatString = "0.0";

prog.ValueChanged += (s, e) =>
{
    var val = prog.Value;
};
```

## 검증 완료

- 소스코드(IcProgress.cs): 속성 11개 + 이벤트 1개(ValueChanged) 확인
- Value setter: MathTool.Constrain으로 Min/Max 클램프 + ValueChanged 발생 확인
- 부모 이미지 공유 모드 / 독립 이미지 모드 분기 확인
