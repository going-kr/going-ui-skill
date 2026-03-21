# GoGauge

원형 게이지 컨트롤. 호(arc) 방식으로 Min~Max 범위의 값을 시각적으로 표시.
상속: GoControl → GoGauge

⚠ **FillColor** — 채워진 호 색상. EmptyColor와 혼동 주의.
⚠ **StartAngle/SweepAngle** — 기본 135/270 = 하단 중앙 열린 원호(7시~5시).
⚠ Selectable 기본값: **false** (읽기 전용 표시 컨트롤)
⚠ **Value 애니메이션** — OnUpdate에서 Value를 갱신하면 자동 애니메이션 적용.

## .gud JSON

```json
{
  "Type": "GoGauge",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 18,
    "Title": "Title",
    "TitleFontSize": 12,
    "TextColor": "Fore",
    "FillColor": "Good",
    "EmptyColor": "Base1",
    "BorderColor": "Base1",
    "Value": 0,
    "Minimum": 0,
    "Maximum": 100,
    "Format": "0",
    "StartAngle": 135,
    "SweepAngle": 270,
    "BarSize": 24,
    "Gap": 0,
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
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 값 폰트 크기 | 18 |
| string | Title | 타이틀 텍스트 | "Title" |
| float | TitleFontSize | 타이틀 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | FillColor | 채움 호 색상 | "Good" |
| string | EmptyColor | 빈 영역 호 색상 | "Base1" |
| string | BorderColor | 테두리 색상 | "Base1" |
| double | Value | 현재 값 | 0 |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| string | Format | 값 표시 포맷 | "0" |
| int | StartAngle | 호 시작 각도(도) | 135 |
| int | SweepAngle | 호 범위 각도(도) | 270 |
| int | BarSize | 호 두께(px) | 24 |
| int | Gap | 값 텍스트와 타이틀 간격 | 0 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 발생 |

## C# 사용

```csharp
var gauge = (GoGauge)dic["gauge"];

// OnUpdate 패턴 — 매 프레임 통신 데이터 반영
protected override void OnUpdate()
{
    var data = Main.DevMgr.Data;
    gauge.Value = data.Temperature;
    base.OnUpdate();
}
```

## 검증 완료

- 소스코드(GoGauge.cs): GoProperty 속성 17개 + 이벤트 1개(ValueChanged)
- 생성자에서 Selectable 변경 없음 → 기본 false
