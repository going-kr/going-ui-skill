# GoSwitchPanel

전환 패널. 여러 서브페이지(GoSubPage) 중 선택된 하나만 표시한다.
상속: GoContainer → GoSwitchPanel

⚠ **SetPage("name") 패턴**으로 페이지를 전환한다.
⚠ 첫 렌더링 시 자동으로 첫 번째 페이지를 선택한다.
⚠ Childrens는 현재 선택된 페이지의 자식 컨트롤을 반환한다 (읽기 전용).

## .gud JSON

```json
{
  "Type": "GoSwitchPanel",
  "Value": {
    "Pages": [
      { "Name": "Sub1", "Childrens": [] },
      { "Name": "Sub2", "Childrens": [] }
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
| List\<GoSubPage\> | Pages | 서브 페이지 목록 | [] |
| GoSubPage? | SelectedPage | 현재 선택된 서브 페이지 (JsonIgnore) | null |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

### GoSubPage

| 타입 | 이름 | 설명 |
|------|------|------|
| string | Name | 서브 페이지 이름 |
| List\<IGoControl\> | Childrens | 이 서브 페이지의 자식 컨트롤 목록 |

### 메서드

| 반환 | 메서드 | 설명 |
|------|--------|------|
| void | SetPage(string name) | 이름으로 서브 페이지 전환 |

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | PageChanged | 페이지 전환 완료 시 발생 |
| EventHandler\<CancelEventArgs\> | PageChanging | 페이지 전환 전 발생. Cancel = true로 취소 가능 |

+ GoControl 공통 이벤트 → _common.md 참조

## C# 사용

```csharp
var sw = (GoSwitchPanel)dic["swPanel"];

// 페이지 전환
sw.SetPage("Sub1");

// 이벤트
sw.PageChanged += (s, e) =>
{
    var current = sw.SelectedPage?.Name;
};

sw.PageChanging += (s, e) =>
{
    // 조건에 따라 전환 취소
    e.Cancel = true;
};
```

## 검증 완료

- 소스코드(GoSwitchPanel.cs): Pages, SelectedPage, SetPage 메서드, PageChanged/PageChanging 이벤트 확인
- GoSubPage: Name, Childrens 확인
