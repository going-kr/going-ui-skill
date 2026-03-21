# GoProgress

프로그레스 바 컨트롤. 값 범위(Min~Max) 대비 현재 값을 막대로 표시.
상속: GoControl → GoProgress

⚠ GoProgress에는 **Round 속성이 없다!** CornerRadius를 사용하라.
⚠ Direction은 GoProgress 전용 enum **ProgressDirection** (LeftToRight=0, RightToLeft=1, BottomToTop=2, TopToBottom=3)
⚠ FontSize(바 외부) vs **ValueFontSize**(바 내부 값 표시) — 두 폰트 크기가 별도!
⚠ ShowValueLabel=true로 해야 바 위에 값 텍스트가 표시됨

## .gud JSON

```json
{
  "Type": "GoProgress",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 18,
    "ValueFontSize": 14,
    "TextColor": "Fore",
    "FillColor": "Good",
    "EmptyColor": "Base1",
    "BorderColor": "Transparent",
    "Direction": 0,
    "Value": 0,
    "Minimum": 0,
    "Maximum": 100,
    "Format": "0",
    "Gap": 5,
    "CornerRadius": 5,
    "BarSize": null,
    "ShowValueLabel": false,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,200,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 외부 텍스트 폰트 크기 | 18 |
| float | ValueFontSize | 바 내부 값 폰트 크기 | 14 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | FillColor | 채움 색상 | "Good" |
| string | EmptyColor | 빈 영역 색상 | "Base1" |
| string | BorderColor | 테두리 색상 | "Transparent" |
| ProgressDirection | Direction | 진행 방향 (LeftToRight=0, RightToLeft=1, BottomToTop=2, TopToBottom=3) | 0 |
| double | Value | 현재 값 | 0 |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| string | Format | 값 표시 포맷 | "0" |
| int | Gap | 바 내부 여백 | 5 |
| int | CornerRadius | 모서리 둥글기(px) | 5 |
| int? | BarSize | 바 두께(null=컨트롤 크기) | null |
| bool | ShowValueLabel | 값 텍스트 표시 | false |

+ GoControl 공통 속성 → _common.md 참조

⚠ GoProgress에 **없는** 속성: Round, BorderWidth, BackgroundDraw, BorderOnly, FillStyle, IconString, ContentAlignment

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 발생 |

## C# 사용

```csharp
var pgTemp = (GoProgress)dic["pgTemp"];

// OnUpdate에서 값 반영
protected override void OnUpdate()
{
    pgTemp.Value = DeviceManager.Current.Temperature;
}

// 이벤트
pgTemp.ValueChanged += (s, e) =>
{
    Console.WriteLine($"Progress: {pgTemp.Value}");
};
```

## 검증 완료

- 소스코드(GoProgress.cs): 속성 17개 + 이벤트 1개(ValueChanged)
- ProgressDirection enum은 GoProgress.cs 내부에 정의됨 (Going.UI.Controls 네임스페이스)
