# GoLabel

레이블 컨트롤. 텍스트/아이콘 표시 전용 (읽기 전용 표시).
상속: GoControl → GoLabel

⚠ GoLabel에는 **클릭 이벤트가 없다**. GoButton과 유사하지만 ButtonClicked 없음.
⚠ GoLabel 고유 속성: **LabelColor** (GoButton의 ButtonColor와 대응). 이름 주의!
⚠ GoLabel 고유 속성: **TextPadding** — 텍스트 영역 내부 여백. GoButton에는 없음.

## .gud JSON

```json
{
  "Type": "GoLabel",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "Text": "label",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextPadding": { "Left": 0, "Top": 0, "Right": 0, "Bottom": 0 },
    "TextColor": "Fore",
    "LabelColor": "Base2",
    "BorderColor": "Base2",
    "Round": 1,
    "BorderWidth": 1,
    "BackgroundDraw": true,
    "BorderOnly": false,
    "ContentAlignment": 4,
    "AutoFontSize": 0,
    "AutoIconSize": 0,
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
| string? | IconString | FontAwesome 아이콘 | null |
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 방향 (Horizon=0, Vertical=1) | 0 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | Text | 표시 텍스트 | "label" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| GoPadding | TextPadding | 텍스트 내부 여백 | {0,0,0,0} |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | LabelColor | 배경 색상 | "Base2" |
| string | BorderColor | 테두리 색상 | "Base2" |
| GoRoundType | Round | 모서리 (All=1) | 1 |
| float | BorderWidth | 테두리 두께 | 1 |
| bool | BackgroundDraw | 배경 그리기 | true |
| bool | BorderOnly | 테두리만 그리기 | false |
| GoContentAlignment | ContentAlignment | 정렬 (MiddleCenter=4) | 4 |
| GoAutoFontSize | AutoFontSize | 자동 폰트 크기 | 0 (NotUsed) |
| GoAutoFontSize | AutoIconSize | 자동 아이콘 크기 | 0 (NotUsed) |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

GoLabel 전용 이벤트 없음. GoControl 공통 이벤트만 사용 → _common.md 참조

## C# 사용

```csharp
var lblTitle = (GoLabel)dic["lblTitle"];

// OnUpdate에서 값 표시
protected override void OnUpdate()
{
    lblTitle.Text = $"온도: {DataManager.Current.Temperature:F1}°C";
}
```

## 검증 완료

- 소스코드(GoLabel.cs): 속성 19개, 전용 이벤트 0개 확인
- GoButton과 차이: LabelColor(Base2) vs ButtonColor(Base3), TextPadding 추가, FillStyle 없음
