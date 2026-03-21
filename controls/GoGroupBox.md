# GoGroupBox

그룹 박스 컨테이너. 타이틀이 테두리 선에 겹쳐지는 WinForms 스타일의 그룹 박스.
상속: GoContainer → GoGroupBox

⚠ Selectable 기본값: **false** (생성자에서 설정)
⚠ GoPanel과 달리 배경색 없이 **테두리만** 그린다. PanelColor 속성이 없다.
⚠ ButtonWidth가 null이면 버튼 영역이 렌더링되지 않는다.

## .gud JSON

```json
{
  "Type": "GoGroupBox",
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
    "BorderColor": "Base3",
    "Round": 1,
    "Buttons": [],
    "ButtonWidth": null,
    "BorderWidth": 1,
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
| string | Text | 그룹 타이틀 텍스트 | "Panel" |
| string | FontName | 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 타이틀 색상 (테마 키) | "Fore" |
| string | BorderColor | 테두리 색상 (테마 키) | "Base3" |
| GoRoundType | Round | 모서리 스타일 (Rect=0, All=1, ...) | 1 (All) |
| List\<GoButtonItem\> | Buttons | 타이틀 우측 버튼 목록 | [] |
| float? | ButtonWidth | 버튼 영역 전체 너비. null이면 버튼 표시 안 함 | null |
| float | BorderWidth | 테두리 두께 | 1 |
| List\<IGoControl\> | Childrens | 자식 컨트롤 목록 | [] |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler\<ButtonClickEventArgs\> | ButtonClicked | 타이틀 버튼 클릭 시 발생 |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var grp = (GoGroupBox)dic["grpSettings"];

grp.Text = "통신 설정";
grp.BorderColor = "Accent";

// 버튼 이벤트
grp.ButtonClicked += (s, e) =>
{
    var btnName = e.Button.Name;
};
```

## 검증 완료

- 소스코드(GoGroupBox.cs): 속성 13개 + 이벤트 1개 확인
