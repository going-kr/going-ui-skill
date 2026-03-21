# GoIconButton

아이콘 버튼 컨트롤. FontAwesome 아이콘만 표시 (텍스트 없음).
상속: GoControl → GoIconButton

⚠ 속성이 매우 적다 (4개만). Text, FontSize, Round 등 없음!
⚠ **Rotate** — 아이콘 회전 각도(도). 기본 0.
⚠ **ClickBoundsExtends** — true면 사각 영역 전체 클릭, false면 아이콘 경로만 클릭
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoIconButton",
  "Value": {
    "IconString": null,
    "Rotate": 0,
    "ButtonColor": "Base3",
    "ClickBoundsExtends": false,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,30,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

권장 크기: 정사각형 30×30

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | IconString | FontAwesome 아이콘 | null |
| float | Rotate | 회전 각도(도) | 0 |
| string | ButtonColor | 아이콘 색상 | "Base3" |
| bool | ClickBoundsExtends | 확장 클릭 영역 | false |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | ButtonClicked | 아이콘 클릭 시 |

## C# 사용

```csharp
var btnClose = (GoIconButton)dic["btnClose"];
btnClose.ButtonClicked += (s, e) =>
{
    Design?.HideWindow();
};
```

## 검증 완료

- 소스코드(GoIconButton.cs): 속성 4개 + 이벤트 1개(ButtonClicked)
