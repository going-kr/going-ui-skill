# GoScrollablePanel

스크롤 가능한 컨테이너. 수직/수평 스크롤바를 자동으로 표시하고 콘텐츠 영역을 스크롤한다.
상속: GoContainer → GoScrollablePanel

⚠ BaseWidth를 설정하면 컨테이너보다 넓은 콘텐츠 영역을 확보하고 자동 축소 렌더링한다.
⚠ EditorHeight는 디자인 모드 전용 속성이다.

## .gud JSON

```json
{
  "Type": "GoScrollablePanel",
  "Value": {
    "Childrens": [],
    "BaseWidth": null,
    "EditorHeight": null,
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
| float? | BaseWidth | 콘텐츠 기준 너비. null이면 컨테이너 너비와 동일 | null |
| float? | EditorHeight | 에디터 모드 시 강제 세로 크기 (디자인 뷰용) | null |
| List\<IGoControl\> | Childrens | 자식 컨트롤 목록 | [] |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var scroll = (GoScrollablePanel)dic["scrollPanel"];

// 기준 너비를 설정하면 내용이 축소되어 표시
scroll.BaseWidth = 1920;
```

## 검증 완료

- 소스코드(GoScrollablePanel.cs): BaseWidth, EditorHeight, Childrens 확인
- ViewPosition은 내부 스크롤 오프셋 (읽기 전용)
