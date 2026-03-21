# GoPicturePanel

이미지 배경 패널. 배경 이미지 위에 자식 컨트롤을 배치한다.
상속: GoContainer → GoPicturePanel

⚠ Image는 GoDesign에 등록된 이미지 키 문자열이다. 파일 경로가 아님.
⚠ ScaleMode: Real=0, CenterImage=1, Stretch=2, Zoom=3

## .gud JSON

```json
{
  "Type": "GoPicturePanel",
  "Value": {
    "Childrens": [],
    "Image": null,
    "ScaleMode": 0,
    "Round": 1,
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
| string? | Image | GoDesign에 등록된 이미지 키 | null |
| GoImageScaleMode | ScaleMode | 이미지 크기 조절 모드 (Real=0, CenterImage=1, Stretch=2, Zoom=3) | 0 (Real) |
| GoRoundType | Round | 모서리 스타일 (Rect=0, All=1, ...) | 1 (All) |

+ GoControl 공통 속성: Id, Name, Visible, Enabled, Selectable, Bounds, Dock, Margin → _common.md 참조

## Events

없음 — 공통 이벤트(`MouseClicked`, `MouseDoubleClicked` 등)만 사용. `controls/_common.md` 참조.

## C# 사용

```csharp
var pic = (GoPicturePanel)dic["picBackground"];

pic.Image = "bg_image";
pic.ScaleMode = GoImageScaleMode.Zoom;
```

## 검증 완료

- 소스코드(GoPicturePanel.cs): Image, ScaleMode, Round, Childrens 확인
