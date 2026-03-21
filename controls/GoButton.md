# GoButton

버튼 컨트롤. 텍스트/아이콘 표시, 클릭 이벤트 처리.
상속: GoControl → GoButton

⚠ **ButtonClicked** 이벤트를 사용하라. MouseClicked 아님! GoButton은 자체 ButtonClicked 이벤트를 갖는다.
⚠ GoButton ≠ GoButtons. GoButton은 단일 버튼, GoButtons는 멀티 버튼(controls/GoButtons.md).
⚠ Selectable 기본값: **true** (GoControl 기본 false와 다름 — 생성자에서 변경)

## .gud JSON

```json
{
  "Type": "GoButton",
  "Value": {
    "IconString": null,
    "IconSize": 12,
    "IconDirection": 0,
    "IconGap": 5,
    "Text": "button",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "ButtonColor": "Base3",
    "BorderColor": "Base3",
    "Round": 1,
    "BorderWidth": 1,
    "BackgroundDraw": true,
    "BorderOnly": false,
    "FillStyle": 0,
    "ContentAlignment": 4,
    "AutoFontSize": 0,
    "AutoIconSize": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,100,40",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

권장 크기: 최소 60×30, 일반 100×40

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | IconString | FontAwesome 아이콘 문자열 | null |
| float | IconSize | 아이콘 크기 | 12 |
| GoDirectionHV | IconDirection | 아이콘 배치 방향 (Horizon=0, Vertical=1) | 0 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | Text | 표시 텍스트 | "button" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 텍스트 색상 (테마 키) | "Fore" |
| string | ButtonColor | 버튼 배경 색상 (테마 키) | "Base3" |
| string | BorderColor | 테두리 색상 (테마 키) | "Base3" |
| GoRoundType | Round | 모서리 스타일 (Rect=0, All=1, L=2, R=3, ...) | 1 (All) |
| float | BorderWidth | 테두리 두께 | 1 |
| bool | BackgroundDraw | 배경 그리기 여부 | true |
| bool | BorderOnly | 테두리만 그리기 (배경 투명) | false |
| GoButtonFillStyle | FillStyle | 채우기 스타일 (Flat=0, Emboss=1, Gradient=2) | 0 (Flat) |
| GoContentAlignment | ContentAlignment | 내용 정렬 (MiddleCenter=4) | 4 |
| GoAutoFontSize | AutoFontSize | 높이 기반 자동 폰트 크기 (NotUsed=0) | 0 |
| GoAutoFontSize | AutoIconSize | 높이 기반 자동 아이콘 크기 (NotUsed=0) | 0 |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, UseLongClick, LongClickTime, Selectable, Bounds, Dock, Margin → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ButtonClicked | 버튼 클릭 시 발생 (EventArgs.Empty) |

⚠ Click, MouseClick, MouseClicked는 GoButton 전용 이벤트가 아니다! GoControl의 MouseClicked와 혼동하지 마라.
⚠ ButtonClicked의 시그니처는 `EventHandler` (제네릭 아님). `EventArgs.Empty`가 전달된다.

+ GoControl 공통 이벤트: MouseClicked, MouseDown, MouseUp, MouseDoubleClicked, MouseLongClicked, MouseMove, MouseWheel, Drawn, DragDrop → _common.md 참조

## C# 사용

```csharp
// dic 캐스팅 (Designer.cs에서 자동 생성)
var btnStart = (GoButton)dic["btnStart"];
var btnStop = (GoButton)dic["btnStop"];

// 이벤트 바인딩
btnStart.ButtonClicked += (s, e) =>
{
    lampRun.OnOff = true;
};

btnStop.ButtonClicked += (s, e) =>
{
    lampRun.OnOff = false;
};
```

## 검증 완료

- 소스코드(GoButton.cs): 속성 19개 + 이벤트 1개 확인
- 기존 MD(gud-structure.md): JSON 속성 일치, 기본값 "Base3" 일치
