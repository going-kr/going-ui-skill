# GoValue

추상 값 표시 컨트롤 기본 클래스. 3개의 구체 서브클래스로 읽기 전용 값 표시.
상속: GoControl → GoValue (abstract) → GoValueString / GoValueNumber\<T\> / GoValueBoolean

⚠ GoValue는 추상 클래스 — 직접 인스턴스화 불가! 반드시 하위 타입 사용.
⚠ **GoValueNumber\<Int32\>** 사용! `GoValueNumber<int>` (X) — JSON Type에서 CLR 타입명 필수!
⚠ **ValueColor** = "Base2" (GoInput의 "Base1"과 다름!)
⚠ GoValue는 **읽기 전용 표시** 컨트롤. 사용자 입력이 필요하면 GoInput 계열 사용.
⚠ Selectable 기본값: **true** (생성자에서 변경)

---

## GoValue 공통 속성

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | IconString | 아이콘 | null |
| float | IconSize | 아이콘 크기 | 12 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 (Normal) |
| float | FontSize | 폰트 크기 | 12 |
| GoDirectionHV | Direction | 레이아웃 방향 (Horizon=0, Vertical=1) | 0 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | BorderColor | 테두리 색상 | "Base3" |
| string | FillColor | 타이틀/버튼 채우기 색상 | "Base3" |
| string | ValueColor | 값 영역 배경색 | "Base2" |
| GoRoundType | Round | 모서리 | 1 (All) |
| float? | TitleSize | 타이틀 영역 크기(px) | null |
| string? | Title | 타이틀 텍스트 | null |
| float? | ButtonSize | 버튼 영역 크기(px) | null |
| List\<GoButtonItem\> | Buttons | 부가 버튼 목록 | [] |
| GoAutoFontSize | AutoFontSize | 자동 폰트 크기 | 0 (NotUsed) |
| GoAutoFontSize | AutoIconSize | 자동 아이콘 크기 | 0 (NotUsed) |

+ GoControl 공통 속성 → _common.md 참조

## GoValue 공통 이벤트

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler\<ButtonClickEventArgs\> | ButtonClicked | Buttons 배열의 부가 버튼 클릭 시 |
| EventHandler | ValueClicked | 값 영역 클릭 시 |

---

## 서브클래스별 JSON 및 속성

### GoValueString

문자열 표시.

```json
{
  "Type": "GoValueString",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base2",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Value": null,
    "Id": "{UUID}", "Name": null,
    "Visible": true, "Enabled": true, "Selectable": true,
    "Bounds": "0,0,200,30", "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

추가 속성:

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | Value | 표시 문자열 | null |

---

### GoValueNumber\<T\>

숫자 표시. T = SByte, Int16, Int32, Int64, Byte, UInt16, UInt32, UInt64, Single, Double, Decimal.

⚠ **CLR 타입명 사용!** `GoValueNumber<Double>` (O), `GoValueNumber<double>` (X)

```json
{
  "Type": "GoValueNumber<Double>",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base2",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Value": 0,
    "FormatString": null,
    "Unit": null, "UnitFontSize": 12, "UnitSize": null,
    "AutoUnitFontSize": 0,
    "Id": "{UUID}", "Name": null,
    "Visible": true, "Enabled": true, "Selectable": true,
    "Bounds": "0,0,200,30", "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

추가 속성:

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| T | Value | 숫자 값 | default(T) |
| string? | FormatString | 포맷 문자열 ("0.0", "N2" 등) | null |
| string? | Unit | 단위 텍스트 ("°C", "kg" 등) | null |
| float | UnitFontSize | 단위 폰트 크기 | 12 |
| float? | UnitSize | 단위 영역 너비(px) | null |
| GoAutoFontSize | AutoUnitFontSize | 자동 단위 폰트 크기 | 0 (NotUsed) |

⚠ **UnitSize**를 설정해야 단위 영역이 표시됨. null이면 단위 미표시.
⚠ GoValueNumber\<T\>에는 UnitFontSize, AutoUnitFontSize가 있지만 GoInputNumber\<T\>에는 없음!

---

### GoValueBoolean

ON/OFF 상태 표시.

```json
{
  "Type": "GoValueBoolean",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base2",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Value": false,
    "OnText": "ON", "OffText": "OFF",
    "OnIconString": null, "OffIconString": null,
    "Id": "{UUID}", "Name": null,
    "Visible": true, "Enabled": true, "Selectable": true,
    "Bounds": "0,0,200,30", "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

추가 속성:

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| bool | Value | 불리언 값 | false |
| string? | OnText | ON 표시 텍스트 | "ON" |
| string? | OffText | OFF 표시 텍스트 | "OFF" |
| string? | OnIconString | ON 아이콘 | null |
| string? | OffIconString | OFF 아이콘 | null |

---

## OnUpdate 표시 패턴

GoValue는 읽기 전용이므로 OnUpdate에서 외부 데이터를 Value에 반영하는 것이 기본 패턴.

```csharp
var valTemp = (GoValueNumber<double>)dic["valTemp"];
var valName = (GoValueString)dic["valName"];
var valState = (GoValueBoolean)dic["valState"];

// OnUpdate에서 외부 데이터 반영
protected override void OnUpdate()
{
    var data = Main.DevMgr.Data;
    valTemp.Value = data.Temperature;
    valName.Value = data.DeviceName;
    valState.Value = data.IsRunning;
    base.OnUpdate();
}
```

### Title + Button 조합 사용

```csharp
// .gud에서 TitleSize: 80, Title: "온도", ButtonSize: 40, Buttons: [{ Text: "R", Size: "100%" }]
valTemp.ButtonClicked += (s, e) =>
{
    // 부가 버튼 클릭 시 동작 (예: 리셋)
    valTemp.Value = 0;
};
```

---

## GoValue vs GoInput 비교

| | GoValue | GoInput |
|---|---|---|
| 용도 | 읽기 전용 표시 | 사용자 입력 |
| ValueColor 기본값 | "Base2" | "Base1" |
| 서브클래스 수 | 3종 | 7종 |
| 고유 이벤트 | ValueClicked | (서브클래스별 ValueChanged/SelectedIndexChanged) |
| GoValueNumber 고유 | UnitFontSize, AutoUnitFontSize | — |
| GoInputNumber 고유 | — | Minimum, Maximum |

## 검증 완료

- 소스코드(GoValue.cs): 공통 속성 18개 + 공통 이벤트 2개
- 서브클래스 3종 모두 확인: GoValueString, GoValueNumber\<T\>, GoValueBoolean
- GoValueNumber\<T\>: 생성자에서 숫자 타입 검증 (sbyte~decimal)
- ValueColor "Base2" (GoValue) vs "Base1" (GoInput) 차이 확인
- GoValueNumber\<T\> 고유 속성: UnitFontSize(12), UnitSize(null), AutoUnitFontSize(0)
