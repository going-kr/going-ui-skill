# GoPicture

이미지 표시 컨트롤. GoDesign에 등록된 이미지 키로 정적 이미지를 표시한다.
상속: GoControl → GoPicture

⚠ **Image** 속성은 GoDesign에 등록된 이미지 키 문자열이다. 파일 경로가 아님.
⚠ **Round** 기본값은 **Rect**(0) — 다른 컨트롤의 All(1)과 다름.
⚠ Selectable 기본값: **false**

## .gud JSON

```json
{
  "Type": "GoPicture",
  "Value": {
    "Image": null,
    "ScaleMode": 0,
    "Round": 0,
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
| string? | Image | GoDesign 등록 이미지 키 | null |
| GoImageScaleMode | ScaleMode | 이미지 크기 조절 모드 | 0 (Real) |
| GoRoundType | Round | 모서리 클리핑 스타일 | 0 (Rect) |

**GoImageScaleMode**: Real=0, CenterImage=1, Stretch=2, Zoom=3

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

(이벤트 없음)

## C# 사용

```csharp
var pic = (GoPicture)dic["picLogo"];

// 이미지 전환
pic.Image = "logo_dark";

// 스케일 모드 변경
pic.ScaleMode = GoImageScaleMode.Zoom;
```

## 검증 완료

- 소스코드(GoPicture.cs): GoProperty 속성 3개 (Image[GoImageProperty], ScaleMode, Round)
- 이벤트 없음
- Selectable 기본값 false (생성자에서 설정하지 않음)
