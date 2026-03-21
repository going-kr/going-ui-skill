# GoInput

추상 입력 컨트롤 기본 클래스. 7개의 구체 서브클래스로 다양한 입력 타입 지원.
상속: GoControl → GoInput (abstract) → GoInputString / GoInputNumber\<T\> / GoInputBoolean / GoInputCombo / GoInputSelector / GoInputColor / GoInputDateTime

⚠ GoInput은 추상 클래스 — 직접 인스턴스화 불가! 반드시 하위 타입 사용.
⚠ **GoInputNumber\<Int32\>** 사용! `GoInputNumber<int>` (X) — CLR 타입명 필수!
⚠ **ValueColor** = "Base1" (GoValue의 "Base2"와 다름!)
⚠ **FillColor** = "Base3" (다른 컨트롤의 기본값과 다를 수 있음)
⚠ Selectable 기본값: **true** (생성자에서 변경)

---

## GoInput 공통 속성

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
| string | ValueColor | 값 영역 배경색 | "Base1" |
| GoRoundType | Round | 모서리 | 1 (All) |
| float? | TitleSize | 타이틀 영역 크기(px) | null |
| string? | Title | 타이틀 텍스트 | null |
| float? | ButtonSize | 버튼 영역 크기(px) | null |
| List\<GoButtonItem\> | Buttons | 부가 버튼 목록 | [] |
| GoAutoFontSize | AutoFontSize | 자동 폰트 크기 | 0 (NotUsed) |
| GoAutoFontSize | AutoIconSize | 자동 아이콘 크기 | 0 (NotUsed) |

+ GoControl 공통 속성 → _common.md 참조

## GoInput 공통 이벤트

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler\<ButtonClickEventArgs\> | ButtonClicked | Buttons 배열의 부가 버튼 클릭 시 |

---

## 서브클래스별 JSON 및 속성

### GoInputString

문자열 입력.

```json
{
  "Type": "GoInputString",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base1",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Value": "",
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
| string | Value | 문자열 값 | "" |

추가 이벤트:

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 |
| Func\<string, bool\> | Editing | 편집 값 필터 (false 반환 시 무시) |

---

### GoInputNumber\<T\>

숫자 입력. T = SByte, Int16, Int32, Int64, Byte, UInt16, UInt32, UInt64, Single, Double, Decimal.

⚠ **CLR 타입명 사용!** `GoInputNumber<Int32>` (O), `GoInputNumber<int>` (X)
⚠ **C# 코드에서는 별칭 사용 가능:** `new GoInputNumber<int>()` — 코드에서는 OK.
⚠ **JSON Type 문자열에서만 CLR 명 필수:** `"GoInputNumber<Int32>"`

```json
{
  "Type": "GoInputNumber<Int32>",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base1",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Value": 0,
    "Minimum": null, "Maximum": null,
    "FormatString": null,
    "Unit": null, "UnitSize": null,
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
| T? | Minimum | 최솟값 | null |
| T? | Maximum | 최댓값 | null |
| string? | FormatString | 포맷 문자열 ("0.0", "N2" 등) | null |
| string? | Unit | 단위 텍스트 ("°C", "kg" 등) | null |
| float? | UnitSize | 단위 영역 너비(px) | null |

추가 이벤트:

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 |
| Func\<T, bool\> | Editing | 편집 값 필터 |

일반적 T 타입 매핑:

| C# 별칭 | CLR 타입명 (JSON용) |
|---------|-------------------|
| int | Int32 |
| long | Int64 |
| float | Single |
| double | Double |
| decimal | Decimal |
| byte | Byte |
| short | Int16 |

---

### GoInputBoolean

ON/OFF 토글 입력.

```json
{
  "Type": "GoInputBoolean",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base1",
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

추가 이벤트:

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 |
| Func\<bool, bool\> | Editing | 편집 값 필터 |

---

### GoInputCombo

드롭다운 선택.

```json
{
  "Type": "GoInputCombo",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base1",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Items": [
      { "IconString": null, "Text": "항목1" },
      { "IconString": null, "Text": "항목2" }
    ],
    "ItemHeight": 30, "MaximumViewCount": 8,
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
| List\<GoListItem\> | Items | 선택 항목 목록 | [] |
| int | ItemHeight | 드롭다운 항목 높이(px) | 30 |
| int | MaximumViewCount | 최대 표시 항목 수 | 8 |

⚠ **Items는 문자열 배열이 아닌 GoListItem 객체 배열!** `"항목"` (X) → `{ "Text": "항목" }` (O) → _common.md 참조

런타임 전용 (C#):

| 타입 | 이름 | 설명 |
|------|------|------|
| int | SelectedIndex | 선택된 항목 인덱스 (-1=미선택). **선택 변경은 이 속성을 설정** |
| GoListItem? | SelectedItem | 선택된 항목. **get 전용(읽기전용)! 설정 불가** |

⚠ **SelectedItem은 읽기전용!** `combo.SelectedItem = item;` → 컴파일 오류. `combo.SelectedIndex = idx;`를 사용하라.

추가 이벤트:

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | SelectedIndexChanged | 선택 변경 시 |
| EventHandler\<GoCancelableEventArgs\> | DropDownOpening | 드롭다운 열리기 전 (Cancel=true로 차단 가능) |

---

### GoInputSelector

좌우 화살표 선택기. 항목이 적을 때(2~4개) 적합.

```json
{
  "Type": "GoInputSelector",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base1",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Items": [],
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
| List\<GoListItem\> | Items | 선택 항목 목록 | [] |

런타임 전용:

| 타입 | 이름 | 설명 |
|------|------|------|
| int | SelectedIndex | 선택된 항목 인덱스 (-1=미선택) |
| GoListItem? | SelectedItem | 선택된 항목 |

추가 이벤트:

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | SelectedIndexChanged | 선택 변경 시 |

> **GoInputCombo vs GoInputSelector:**
> | | GoInputCombo | GoInputSelector |
> |---|---|---|
> | UX | 드롭다운 팝업 | 좌우 화살표 순환 |
> | 속성 | Items + ItemHeight + MaximumViewCount | Items만 |
> | 적합 | 항목 5개 이상 | 항목 2~4개 |

---

### GoInputColor

색상 선택 (HSV 컬러 피커 팝업).

```json
{
  "Type": "GoInputColor",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base1",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Value": 4294967295,
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
| SKColor | Value | 색상 값 (uint ARGB) | SKColors.White (4294967295) |

추가 이벤트:

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 |

⚠ JSON에서 SKColor는 **uint** 값으로 직렬화됨 (ARGB). 예: 흰색=4294967295, 빨강=4294901760

---

### GoInputDateTime

날짜/시간 입력.

```json
{
  "Type": "GoInputDateTime",
  "Value": {
    "IconString": null, "IconSize": 12, "IconGap": 5,
    "FontName": "나눔고딕", "FontStyle": 0, "FontSize": 12,
    "Direction": 0,
    "TextColor": "Fore", "BorderColor": "Base3",
    "FillColor": "Base3", "ValueColor": "Base1",
    "Round": 1,
    "TitleSize": null, "Title": null,
    "ButtonSize": null, "Buttons": [],
    "AutoFontSize": 0, "AutoIconSize": 0,
    "Value": "2024-01-01T00:00:00",
    "DateTimeStyle": 0,
    "DateFormat": "yyyy-MM-dd",
    "TimeFormat": "HH:mm:ss",
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
| DateTime | Value | 날짜/시간 값 | DateTime.MinValue |
| GoDateTimeKind | DateTimeStyle | 표시 모드 (DateTime=0, Date=1, Time=2) | 0 |
| string | DateFormat | 날짜 포맷 | "yyyy-MM-dd" |
| string | TimeFormat | 시간 포맷 | "HH:mm:ss" |

추가 이벤트:

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ValueChanged | Value 변경 시 |

---

## C# 사용

```csharp
var inpName = (GoInputString)dic["inpName"];
var inpTemp = (GoInputNumber<double>)dic["inpTemp"];
var inpOnOff = (GoInputBoolean)dic["inpOnOff"];
var inpMode = (GoInputCombo)dic["inpMode"];
var inpColor = (GoInputColor)dic["inpColor"];
var inpDate = (GoInputDateTime)dic["inpDate"];

// GoInputString
inpName.ValueChanged += (s, e) =>
{
    Console.WriteLine($"이름: {inpName.Value}");
};

// GoInputNumber<T>
inpTemp.ValueChanged += (s, e) =>
{
    Console.WriteLine($"온도: {inpTemp.Value:F1}°C");
};

// GoInputBoolean
inpOnOff.ValueChanged += (s, e) =>
{
    Console.WriteLine($"상태: {inpOnOff.Value}");
};

// GoInputCombo
inpMode.Items.Add(new GoListItem { Text = "자동", Tag = "Auto" });
inpMode.Items.Add(new GoListItem { Text = "수동", Tag = "Manual" });
inpMode.SelectedIndexChanged += (s, e) =>
{
    var item = inpMode.SelectedItem;
    Console.WriteLine($"모드: {item?.Text}");
};

// OnUpdate에서 외부 값 반영
protected override void OnUpdate()
{
    inpTemp.Value = DeviceManager.Current.Temperature;
    inpOnOff.Value = DeviceManager.Current.IsRunning;
}
```

## 검증 완료

- 소스코드(GoInput.cs): 공통 속성 18개 + 공통 이벤트 1개
- 서브클래스 7종 모두 확인: GoInputString, GoInputNumber\<T\>, GoInputBoolean, GoInputCombo, GoInputSelector, GoInputColor, GoInputDateTime
- GoInputNumber\<T\>: 생성자에서 숫자 타입 검증 (sbyte~decimal)
- GoInputCombo vs GoInputSelector: Items 구조 동일(GoListItem), UX 차이
- ValueColor "Base1" (GoInput) vs "Base2" (GoValue) 차이 확인
