# GoMeter

아날로그 계기판(미터) 컨트롤. 바늘과 눈금으로 값을 표시.
상속: GoControl → GoMeter

⚠ **NeedleColor** — GoMeter 전용. GoKnob의 CursorColor와 혼동 주의.
⚠ **NeedlePointColor** — 바늘 중심점(끝) 색상. 기본값 "Red".
⚠ **GraduationLarge/Small** — Large는 큰 눈금 간격(값 단위), Small은 큰 눈금 사이 작은 눈금 수.
⚠ **StartAngle/SweepAngle** — 내부 const 135/270 (고정, JSON 속성 아님).
⚠ Selectable 기본값: **false** (읽기 전용 표시 컨트롤)

## .gud JSON

```json
{
  "Type": "GoMeter",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 18,
    "Title": "Title",
    "TitleFontSize": 12,
    "RemarkFontSize": 10,
    "TextColor": "Fore",
    "NeedleColor": "Fore",
    "NeedlePointColor": "Red",
    "RemarkColor": "Base5",
    "Value": 0,
    "Minimum": 0,
    "Maximum": 100,
    "GraduationLarge": 10,
    "GraduationSmall": 2,
    "Format": "0",
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
| float | RemarkFontSize | 눈금 레이블 폰트 크기 | 10 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | NeedleColor | 바늘 색상 | "Fore" |
| string | NeedlePointColor | 바늘 중심점 색상 | "Red" |
| string | RemarkColor | 눈금 텍스트 색상 | "Base5" |
| double | Value | 현재 값 | 0 |
| double | Minimum | 최솟값 | 0 |
| double | Maximum | 최댓값 | 100 |
| int | GraduationLarge | 큰 눈금 간격(값 단위) | 10 |
| int | GraduationSmall | 작은 눈금 수(큰 눈금 사이) | 2 |
| string | Format | 값 표시 포맷 | "0" |
| int | Gap | 값 텍스트와 타이틀 간격 | 0 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 발생 |

## C# 사용

```csharp
var meter = (GoMeter)dic["meter"];

// OnUpdate 패턴 — 매 프레임 통신 데이터 반영
protected override void OnUpdate()
{
    var data = Main.DevMgr.Data;
    meter.Value = data.Pressure;
    base.OnUpdate();
}
```

## 검증 완료

- 소스코드(GoMeter.cs): GoProperty 속성 17개 + 이벤트 1개(ValueChanged)
- StartAngle/SweepAngle은 internal const (135/270) — JSON 직렬화 대상 아님
- 생성자에서 Selectable 변경 없음 → 기본 false
