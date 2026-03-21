# GoTabControl

탭 컨트롤. 탭 헤더 위치(Up/Down/Left/Right)를 선택할 수 있으며 GoTabPage별로 컨트롤을 분리한다.
상속: GoContainer → GoTabControl

⚠ **SetTab("name") 패턴**으로 탭을 전환한다.
⚠ 첫 렌더링 시 자동으로 첫 번째 탭을 선택한다.
⚠ TabPosition은 GoDirection 열거형: Left=0, Right=1, Up=2, Down=3 (기본: Up=2)

## .gud JSON

```json
{
  "Type": "GoTabControl",
  "Value": {
    "IconDirection": 0,
    "IconSize": 12,
    "IconGap": 5,
    "FontName": "나눔고딕",
    "FontStyle": 0,
    "FontSize": 12,
    "TextColor": "Fore",
    "TabColor": "Base2",
    "TabBorderColor": "Base3",
    "TabPosition": 2,
    "NavSize": 40,
    "TabPages": [
      { "Name": "Tab1", "IconString": null, "Text": "Tab1", "Childrens": [] }
    ],
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
| GoDirectionHV | IconDirection | 탭 아이콘 방향 (Horizon=0, Vertical=1) | 0 |
| float | IconSize | 아이콘 크기 | 12 |
| float | IconGap | 아이콘-텍스트 간격 | 5 |
| string | FontName | 탭 텍스트 폰트명 | "나눔고딕" |
| GoFontStyle | FontStyle | 폰트 스타일 (Normal=0, Italic=1, Bold=2, BoldItalic=3) | 0 |
| float | FontSize | 폰트 크기 | 12 |
| string | TextColor | 탭 텍스트 색상 (테마 키) | "Fore" |
| string | TabColor | 탭/페이지 배경 색상 (테마 키) | "Base2" |
| string | TabBorderColor | 탭 테두리 색상 (테마 키) | "Base3" |
| GoDirection | TabPosition | 탭 헤더 위치 (Left=0, Right=1, Up=2, Down=3) | 2 (Up) |
| float | NavSize | 탭 헤더 영역 크기 (높이 또는 너비) | 40 |
| GoTabPage? | SelectedTab | 현재 선택된 탭 (JsonIgnore) | null |
| List\<GoTabPage\> | TabPages | 탭 페이지 목록 | [] |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

### GoTabPage

| 타입 | 이름 | 설명 |
|------|------|------|
| string | Name | 탭 페이지 이름 |
| string? | IconString | 탭 헤더 아이콘 |
| string? | Text | 탭 헤더 텍스트 |
| List\<IGoControl\> | Childrens | 이 탭의 자식 컨트롤 목록 |

### 메서드

| 반환 | 메서드 | 설명 |
|------|--------|------|
| void | SetTab(string name) | 이름으로 탭 전환 |

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | TabChanged | 탭 전환 완료 시 발생 |
| EventHandler\<CancelEventArgs\> | TabChanging | 탭 전환 전 발생. Cancel = true로 취소 가능 |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var tab = (GoTabControl)dic["tabMain"];

// 탭 전환
tab.SetTab("Tab1");

// 이벤트
tab.TabChanged += (s, e) =>
{
    var current = tab.SelectedTab?.Name;
};

tab.TabChanging += (s, e) =>
{
    // 조건에 따라 전환 취소
    e.Cancel = true;
};
```

## 검증 완료

- 소스코드(GoTabControl.cs): 속성 13개 + 이벤트 2개 + SetTab 메서드 확인
- GoTabPage: Name, IconString, Text, Childrens 확인
