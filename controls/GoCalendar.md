# GoCalendar

달력 컨트롤. 월별 날짜를 표시하고 날짜를 선택한다. 이전/다음 월 이동 지원.
상속: GoControl → GoCalendar

⚠ **CurrentYear / CurrentMonth / SelectedDays** 는 `[JsonIgnore]` — 런타임 전용 속성. JSON에 포함되지 않는다.
⚠ **BoxColor** 기본값은 **"Base3"** — 다른 컨트롤의 "Base1"과 다름.
⚠ **Round** 기본값은 **All**(1).
⚠ Selectable 기본값: **true** (생성자에서 설정)

## .gud JSON

```json
{
  "Type": "GoCalendar",
  "Value": {
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "BoxColor": "Base3",
    "SelectColor": "Select",
    "Round": 1,
    "BackgroundDraw": true,
    "MultiSelect": false,
    "NoneSelect": false,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,250,250",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

권장 크기: 정사각형 250×250 이상

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BoxColor | 배경 색상 | "Base3" |
| string | SelectColor | 선택일 강조 색상 | "Select" |
| GoRoundType | Round | 모서리 스타일 | 1 (All) |
| bool | BackgroundDraw | 배경 그리기 여부 | true |
| bool | MultiSelect | 다중 날짜 선택 허용 | false |
| bool | NoneSelect | 선택 없음 허용 | false |

**런타임 전용 속성 (JsonIgnore)**:

| 타입 | 이름 | 설명 |
|------|------|------|
| int | CurrentYear | 현재 표시 연도 |
| int | CurrentMonth | 현재 표시 월 |
| List\<DateTime\> | SelectedDays | 선택된 날짜 목록 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | SelectedDaysChanged | 날짜 선택 변경 시 발생 |

## C# 사용

```csharp
var cal = (GoCalendar)dic["calSchedule"];

cal.SelectedDaysChanged += (s, e) =>
{
    foreach (var day in cal.SelectedDays)
        Console.WriteLine($"Selected: {day:yyyy-MM-dd}");
};

// 다중 선택 모드
cal.MultiSelect = true;
```

## 검증 완료

- 소스코드(GoCalendar.cs): GoProperty 속성 10개 (FontName, FontStyle, FontSize, TextColor, BoxColor, SelectColor, Round, BackgroundDraw, MultiSelect, NoneSelect)
- 런타임 전용 3개 (CurrentYear, CurrentMonth, SelectedDays)
- 이벤트 1개 (SelectedDaysChanged)
- 생성자에서 Selectable = true 설정 확인
