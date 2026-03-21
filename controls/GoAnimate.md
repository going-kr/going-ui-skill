# GoAnimate

애니메이션 이미지 컨트롤. OnOff 상태에 따라 다중 프레임 이미지를 순서대로 자동 재생한다.
상속: GoControl → GoAnimate

⚠ **OnImage / OffImage** — 둘 다 GoDesign 등록 이미지 키. 두 이미지 모두 설정해야 동작한다.
⚠ **Time** — 프레임 전환 간격. 단위는 밀리초(ms)가 아니라 OnUpdate 틱 기준 시간이다.
⚠ Selectable 기본값: **false**

## .gud JSON

```json
{
  "Type": "GoAnimate",
  "Value": {
    "OnImage": null,
    "OffImage": null,
    "ScaleMode": 0,
    "Round": 0,
    "Time": 30,
    "OnOff": false,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": false,
    "Bounds": "0,0,200,150",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | OnImage | ON 상태 이미지 키 (다중 프레임) | null |
| string? | OffImage | OFF 상태 이미지 키 (정지 프레임) | null |
| GoImageScaleMode | ScaleMode | 이미지 크기 조절 모드 | 0 (Real) |
| GoRoundType | Round | 모서리 클리핑 스타일 | 0 (Rect) |
| int | Time | 프레임 전환 간격(ms) | 30 |
| bool | OnOff | 애니메이션 재생 여부 | false |

**GoImageScaleMode**: Real=0, CenterImage=1, Stretch=2, Zoom=3

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | OnOffChanged | OnOff 값 변경 시 발생 |

## C# 사용

```csharp
var ani = (GoAnimate)dic["aniMotor"];

// 애니메이션 시작
ani.OnOff = true;

// 상태 변경 감지
ani.OnOffChanged += (s, e) =>
{
    Console.WriteLine($"Animation: {ani.OnOff}");
};

// 프레임 속도 조절
ani.Time = 50;  // 더 느리게
```

## 검증 완료

- 소스코드(GoAnimate.cs): GoProperty 속성 6개 (OnImage[GoImageProperty], OffImage[GoImageProperty], ScaleMode, Round, Time, OnOff)
- 이벤트 1개 (OnOffChanged)
- OnOff setter에서 idx=0 리셋 + OnOffChanged 발생
- Selectable 기본값 false (생성자에서 설정하지 않음)
