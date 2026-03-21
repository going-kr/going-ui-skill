# GoPanel

패널 컨테이너. 타이틀 헤더 + 콘텐츠 영역 구조의 카드형 컨테이너.
상속: GoContainer → GoPanel

⚠ Selectable 기본값: **false** (생성자에서 설정)
⚠ ButtonWidth가 null이면 버튼 영역이 렌더링되지 않는다. Buttons를 사용하려면 ButtonWidth를 설정해야 한다.

## .gud JSON

```json
{
  "Type": "GoPanel",
  "Value": {
    "Childrens": [],
    "IconString": null,
    "IconSize": 12,
    "IconGap": 5,
    "Text": "Panel",
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "PanelColor": "Base2",
    "Round": 1,
    "BackgroundDraw": true,
    "BorderOnly": false,
    "TitleHeight": 40,
    "Buttons": [],
    "ButtonWidth": null,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,500,400",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | IconString | 타이틀 아이콘 문자열 (FontAwesome) | null |
| float | IconSize | 아이콘 크기 | 12 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | Text | 타이틀 텍스트 | "Panel" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 타이틀 텍스트 색상 (테마 키) | "Fore" |
| string | PanelColor | 패널 배경 색상 (테마 키) | "Base2" |
| GoRoundType | Round | 모서리 스타일 (Rect=0, All=1, ...) | 1 (All) |
| bool | BackgroundDraw | 배경 그리기 여부 | true |
| bool | BorderOnly | 테두리만 그리기 (배경 투명) | false |
| float | TitleHeight | 타이틀 영역 높이 (px) | 40 |
| List\<GoButtonItem\> | Buttons | 타이틀 우측 버튼 목록 | [] |
| float? | ButtonWidth | 버튼 영역 전체 너비. null이면 버튼 표시 안 함 | null |
| List\<IGoControl\> | Childrens | 콘텐츠 영역 자식 컨트롤 목록 | [] |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler\<ButtonClickEventArgs\> | ButtonClicked | 타이틀 버튼 클릭 시 발생 |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var panel = (GoPanel)dic["pnlMain"];

panel.Text = "설정";
panel.PanelColor = "Base3";

// 버튼 이벤트
panel.ButtonClicked += (s, e) =>
{
    var btnName = e.Button.Name;
    // 버튼 처리
};
```

## 검증 완료

- 소스코드(GoPanel.cs): 속성 15개 + 이벤트 1개 확인
