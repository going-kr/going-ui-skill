# IcSlider

ImageCanvas 슬라이더. OffBarImage/OnBarImage/OffCursorImage/OnCursorImage 4개 이미지로 구성된다.
상속: GoControl → IcSlider

⚠ 바 이미지(OffBarImage/OnBarImage)가 **null이면 부모 이미지에서 슬라이싱** (부모 공유 모드).
⚠ 바 이미지를 지정하면 **독립 이미지 모드**로 동작.
⚠ OffCursorImage/OnCursorImage로 드래그 커서 이미지를 지정한다.
⚠ Tick이 설정되면 값이 Tick 단위로 스냅된다.
⚠ Value는 Minimum~Maximum 범위로 자동 클램프된다.

## .gud JSON

```json
{
  "Type": "IcSlider",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Black",
    "OffBarImage": null,
    "OnBarImage": null,
    "OffCursorImage": null,
    "OnCursorImage": null,
    "FormatString": "0",
    "Minimum": 0,
    "Maximum": 100,
    "Value": 0,
    "Tick": null,
    "DrawText": true,
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
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Black" |
| string? | OffBarImage | 슬라이더 빈 바 이미지 키 | null |
| string? | OnBarImage | 슬라이더 채워진 바 이미지 키 | null |
| string? | OffCursorImage | 커서 기본 이미지 키 | null |
| string? | OnCursorImage | 커서 클릭(Down) 이미지 키 | null |
| string | FormatString | 값 표시 형식 문자열 | "0" |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| double | Value | 현재 값. Tick이 있으면 스냅. 변경 시 ValueChanged 발생 | 0 |
| double? | Tick | 스냅 단위. null이면 연속값 | null |
| bool | DrawText | 커서 위 값 텍스트 표시 여부 | true |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 발생 |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var slider = (IcSlider)dic["icSliderSpeed"];

slider.Minimum = 0;
slider.Maximum = 100;
slider.Tick = 10;      // 10단위 스냅
slider.Value = 50;
slider.FormatString = "0";

slider.ValueChanged += (s, e) =>
{
    var val = slider.Value;
};
```

## 검증 완료

- 소스코드(IcSlider.cs): 속성 14개 + 이벤트 1개(ValueChanged) 확인
- Value setter: MathTool.Constrain + Tick 스냅 + ValueChanged 발생 확인
- 부모 이미지 공유 모드 / 독립 이미지 모드 분기 확인
- 커서 드래그: MouseDown/MouseMove/MouseUp에서 Value 계산 확인
