# GoBoxPanel

단순 배경 박스 컨테이너. 테두리와 배경색만 그리며 자식 컨트롤을 포함한다.
상속: GoContainer → GoBoxPanel

## .gud JSON

```json
{
  "Type": "GoBoxPanel",
  "Value": {
    "Childrens": [],
    "BorderColor": "Base3",
    "BoxColor": "Base2",
    "Round": 1,
    "BackgroundDraw": true,
    "BorderSize": 1,
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
| List\<IGoControl\> | Childrens | 자식 컨트롤 목록 | [] |
| string | BorderColor | 테두리 색상 (테마 키) | "Base3" |
| string | BoxColor | 배경 색상 (테마 키) | "Base2" |
| GoRoundType | Round | 모서리 스타일 (Rect=0, All=1, L=2, R=3, ...) | 1 (All) |
| bool | BackgroundDraw | 배경 그리기 여부 | true |
| float | BorderSize | 테두리 두께 | 1 |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var box = (GoBoxPanel)dic["boxMain"];

box.BoxColor = "Base3";
box.BorderColor = "Base2";
box.BackgroundDraw = false; // 배경 숨기기
```

## 검증 완료

- 소스코드(GoBoxPanel.cs): BorderColor, BoxColor, Round, BackgroundDraw, BorderSize 확인
