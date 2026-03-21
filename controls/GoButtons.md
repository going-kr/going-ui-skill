# GoButtons

멀티 버튼 컨트롤. 여러 버튼을 하나의 컨트롤에 배열 (Button/Toggle/Radio 모드).
상속: GoControl → GoButtons

⚠ GoButtons ≠ GoButton! GoButton은 단일 버튼, GoButtons는 멀티 버튼.
⚠ **Mode**에 따라 동작이 다름: Button=0(단발), Toggle=1(토글), Radio=2(라디오)
⚠ **ButtonClicked**(EventHandler\<ButtonsClickEventArgs\>) vs GoButton의 ButtonClicked(EventHandler) — 시그니처 다름!
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoButtons",
  "Value": {
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "ButtonColor": "Base3",
    "BorderColor": "Base3",
    "SelectedButtonColor": "Select",
    "SelectedBorderColor": "Select",
    "Round": 1,
    "BorderWidth": 1,
    "FillStyle": 0,
    "Buttons": [],
    "Direction": 0,
    "Mode": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,200,40",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

### Buttons 배열 아이템 (GoButtonsItem)

```json
{
  "Name": "btn1",
  "Text": "버튼1",
  "IconString": null,
  "Size": "100%",
  "Selected": false
}
```

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string | Name | 버튼 식별자 | — |
| string? | Text | 표시 텍스트 | null |
| string? | IconString | 아이콘 | null |
| string | Size | 크기 ("100%", "80px") | "100%" |
| bool | Selected | 선택 상태 (Toggle/Radio) | false |

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 방향 | 0 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 | "Fore" |
| string | ButtonColor | 기본 배경 | "Base3" |
| string | BorderColor | 기본 테두리 | "Base3" |
| string | SelectedButtonColor | 선택 배경 | "Select" |
| string | SelectedBorderColor | 선택 테두리 | "Select" |
| GoRoundType | Round | 모서리 | 1 (All) |
| float | BorderWidth | 테두리 두께 | 1 |
| GoButtonFillStyle | FillStyle | 채우기 | 0 (Flat) |
| List\<GoButtonsItem\> | Buttons | 버튼 목록 | [] |
| GoDirectionHV | Direction | 배열 방향 | 0 (Horizon) |
| GoButtonsMode | Mode | 동작 모드 (Button=0, Toggle=1, Radio=2) | 0 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler\<ButtonsClickEventArgs\> | ButtonClicked | 버튼 클릭 시 (.Button 속성으로 클릭된 항목 확인) |
| EventHandler\<ButtonsSelectedEventArgs\> | SelectedChanged | Toggle/Radio 모드에서 선택 변경 시 |

### ButtonsClickEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| GoButtonsItem | Button | 클릭된 버튼 항목 |

### ButtonsSelectedEventArgs

| 타입 | 이름 | 설명 |
|------|------|------|
| GoButtonsItem | SelectedButton | 새로 선택된 버튼 |
| GoButtonsItem? | DeselectedButton | 선택 해제된 버튼 (Radio 모드) |

## C# 사용

```csharp
var btns = (GoButtons)dic["btnsMode"];

// Button 모드
btns.ButtonClicked += (s, e) =>
{
    Console.WriteLine($"클릭: {e.Button.Name}");
};

// Radio 모드
btns.SelectedChanged += (s, e) =>
{
    Console.WriteLine($"선택: {e.SelectedButton.Name}");
    if (e.DeselectedButton != null)
        Console.WriteLine($"해제: {e.DeselectedButton.Name}");
};
```

## 검증 완료

- 소스코드(GoButtons.cs): 속성 16개 + 이벤트 2개
- GoButtonsItem: GoButtonItem 상속 + Selected 추가
- GoButtonFillStyle enum: Flat=0, Emboss=1, Gradient=2 (GoButtonItem.cs에 정의)
