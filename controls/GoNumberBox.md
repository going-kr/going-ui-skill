# GoNumberBox

숫자 증감 컨트롤. +/- 버튼으로 값을 Tick 단위로 조절.
상속: GoControl → GoNumberBox

⚠ **Tick** 속성은 double(nullable 아님). GoKnob/GoSlider의 Tick(double?)과 다름.
⚠ **ButtonSize** — +/- 버튼 너비(px). 기본 40.
⚠ **ValueColor** — 값 표시 영역 배경색. GoButton의 ButtonColor와 다른 용도.
⚠ Direction: Horizon=좌[-]중[값]우[+], Vertical=상[값]하좌[-]하우[+]

## .gud JSON

```json
{
  "Type": "GoNumberBox",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore",
    "BorderColor": "Base3",
    "ButtonColor": "Base3",
    "ValueColor": "Base1",
    "Round": 1,
    "Value": 0,
    "Minimum": 0,
    "Maximum": 100,
    "Tick": 1,
    "Format": null,
    "ButtonSize": 40,
    "AutoFontSize": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,150,40",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| GoDirectionHV | Direction | 배치 방향 | 0 (Horizon) |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BorderColor | 테두리 색상 | "Base3" |
| string | ButtonColor | +/- 버튼 색상 | "Base3" |
| string | ValueColor | 값 영역 배경 | "Base1" |
| GoRoundType | Round | 모서리 | 1 (All) |
| double | Value | 현재 값 | 0 |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| double | Tick | 증감 단위 | 1 |
| string? | Format | 값 포맷 | null |
| float | ButtonSize | 버튼 너비(px) | 40 |
| GoAutoFontSize | AutoFontSize | 자동 폰트 | 0 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 발생 |

⚠ 길게 누르면 자동 반복 증감 (500ms 후 가속)

## C# 사용

```csharp
var nbCount = (GoNumberBox)dic["nbCount"];

nbCount.ValueChanged += (s, e) =>
{
    DeviceManager.Current.SetCount((int)nbCount.Value);
};
```

## 검증 완료

- 소스코드(GoNumberBox.cs): 속성 16개 + 이벤트 1개(ValueChanged)
- 소스코드 PCategory.Control 인덱스 9가 누락 (10부터 Value) — 내부 순서 문제, JSON 직렬화에 영향 없음
