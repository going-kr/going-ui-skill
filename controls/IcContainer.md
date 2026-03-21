# IcContainer

ImageCanvas 컨테이너. IcPage와 동일하게 OffImage 배경을 렌더링하고 Ic* 컨트롤을 호스팅한다.
상속: GoContainer → IcContainer

⚠ ImageCanvas 전용 컨테이너. Ic* 컨트롤은 반드시 IcPage 또는 IcContainer 안에 배치해야 한다.
⚠ OffImage가 없으면 BackgroundColor로 배경을 채운다.
⚠ 자식 Ic* 컨트롤은 부모의 OffImage/OnImage에서 자신의 영역을 잘라 렌더링한다.

## .gud JSON

```json
{
  "Type": "IcContainer",
  "Value": {
    "BackgroundColor": "white",
    "OffImage": null,
    "OnImage": null,
    "Childrens": [],
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
| string | BackgroundColor | OffImage 없을 때 사용할 배경 색상 | "white" |
| string? | OffImage | OFF 상태 배경 이미지 키 | null |
| string? | OnImage | ON 상태 배경 이미지 키 | null |
| List\<IGoControl\> | Childrens | 자식 컨트롤 목록 | [] |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var ic = (IcContainer)dic["icPanel"];

ic.OffImage = "panel_off";
ic.OnImage = "panel_on";
ic.BackgroundColor = "white";
```

## 검증 완료

- 소스코드(IcContainer.cs): BackgroundColor="white", OffImage, OnImage, Childrens 확인
