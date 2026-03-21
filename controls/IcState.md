# IcState

ImageCanvas 다중 상태 이미지. State 값에 따라 StateImages 목록에서 해당 이미지를 렌더링한다.
상속: GoControl → IcState

⚠ StateImages의 각 항목은 State(int)와 Image(string? 키)를 갖는다.
⚠ 현재 State 값에 매칭되는 StateImage의 Image를 전체 영역에 표시한다.
⚠ 부모의 OffImage/OnImage를 사용하지 않고, **독립적인 이미지 목록**을 사용한다.

## .gud JSON

```json
{
  "Type": "IcState",
  "Value": {
    "StateImages": [
      { "Image": "state_off", "State": 0 },
      { "Image": "state_on", "State": 1 },
      { "Image": "state_alarm", "State": 2 }
    ],
    "State": 0,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,70,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| List\<StateImage\> | StateImages | 상태별 이미지 목록 | [] |
| int | State | 현재 상태 번호 | 0 |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

### StateImage

| 타입 | 이름 | 설명 |
|------|------|------|
| string? | Image | GoDesign에 등록된 이미지 키 |
| int | State | 상태 번호 |

## C# 사용

```csharp
var state = (IcState)dic["icStateValve"];

// 상태 변경
state.State = 1; // state_on 이미지 표시
state.State = 2; // state_alarm 이미지 표시
```

## 검증 완료

- 소스코드(IcState.cs): StateImages(List\<StateImage\>), State(int) 확인
- StateImage 클래스: Image(string?), State(int) 확인
