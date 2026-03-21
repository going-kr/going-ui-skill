# GoColorSelector

HSV 색상 선택기 컨트롤. 색상 팔레트 + Hue 바 + R/G/B 입력으로 색상을 선택한다.
상속: GoControl → GoColorSelector

⚠ **Value** 속성은 `SKColor` 타입이며 `[JsonIgnore]`이지만 JSON에서는 uint(ARGB) 정수로 직렬화된다.
⚠ **InputColor** — R/G/B 입력 영역 배경색. BoxColor가 아님.
⚠ Selectable 기본값: **true** (생성자에서 설정)

## .gud JSON

```json
{
  "Type": "GoColorSelector",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "InputColor": "Base1",
    "BorderColor": "Base3",
    "ContentAlignment": 4,
    "Value": 4294967295,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,300,250",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

권장 크기: 정사각형에 가까운 300×250 이상 (팔레트 + Hue바 + RGB 입력 공간 필요)

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | R/G/B 레이블 텍스트 색상 | "Fore" |
| string | InputColor | R/G/B 입력 영역 배경 색상 | "Base1" |
| string | BorderColor | R/G/B 입력 영역 테두리 색상 | "Base3" |
| GoContentAlignment | ContentAlignment | 팔레트 정렬 위치 | 4 (MiddleCenter) |
| SKColor | Value | 선택된 색상 (내부 HSV→RGB 변환) | White (4294967295) |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

(이벤트 없음 — Value 변경은 마우스 조작으로 직접 수행)

## C# 사용

```csharp
var cs = (GoColorSelector)dic["csColor"];

// 주기적으로 현재 색상 읽기
protected override void OnUpdate()
{
    var color = cs.Value;
    labelR.Text = $"R: {color.Red}";
    labelG.Text = $"G: {color.Green}";
    labelB.Text = $"B: {color.Blue}";
}

// 코드에서 색상 설정
cs.Value = new SKColor(255, 128, 0);
```

## 검증 완료

- 소스코드(GoColorSelector.cs): GoProperty 속성 8개 (FontName, FontStyle, FontSize, TextColor, InputColor, BorderColor, ContentAlignment, Value)
- Value는 [JsonIgnore] 마크이나 별도 직렬화 경로로 uint ARGB 저장
- 생성자에서 Selectable = true 설정 확인
