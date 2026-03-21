# GoScalePanel

스케일 패널. BaseWidth/BaseHeight 기준으로 자식 컨트롤을 자동 확대/축소한다.
상속: GoContainer → GoScalePanel

⚠ BaseWidth/BaseHeight가 모두 null이면 스케일링 없이 실제 크기로 표시.
⚠ 하나만 지정하면 원본 종횡비를 유지하며 스케일링.
⚠ 둘 다 지정하면 BaseWidth x BaseHeight 비율로 스케일링.

## .gud JSON

```json
{
  "Type": "GoScalePanel",
  "Value": {
    "Childrens": [],
    "BaseWidth": null,
    "BaseHeight": null,
    "PanelAlignment": 4,
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
| int? | BaseWidth | 기준 너비(px). null이면 실제 크기 | null |
| int? | BaseHeight | 기준 높이(px). null이면 실제 크기 | null |
| GoContentAlignment | PanelAlignment | 패널 정렬 (MiddleCenter=4) | 4 (MiddleCenter) |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var scale = (GoScalePanel)dic["scalePanel"];

// 1920x1080 기준으로 디자인하면 실제 크기에 맞게 자동 축소/확대
scale.BaseWidth = 1920;
scale.BaseHeight = 1080;
scale.PanelAlignment = GoContentAlignment.MiddleCenter;
```

## 검증 완료

- 소스코드(GoScalePanel.cs): BaseWidth(int?), BaseHeight(int?), PanelAlignment 확인
