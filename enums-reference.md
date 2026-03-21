# Going UI -- Enum 전체 레퍼런스

> **⚠ Enum 값은 .gud JSON에서 반드시 숫자로 직렬화하라. 문자열 불가!**
> `"Normal"` (X) -> `0` (O), `"Fill"` (X) -> `5` (O)

네임스페이스: `Going.UI.Enums`
소스 검증: `Going.UI/Enums/*.cs`, `Going.UI/Datas/GoButtonItem.cs`

---

## GoContentAlignment

컨텐츠 정렬 위치 (9방향). 대부분의 컨트롤에서 기본값은 `4` (MiddleCenter).

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | TopLeft | 좌상 |
| 1 | TopCenter | 상단 중앙 |
| 2 | TopRight | 우상 |
| 3 | MiddleLeft | 좌측 중앙 |
| 4 | MiddleCenter | 중앙 (기본값) |
| 5 | MiddleRight | 우측 중앙 |
| 6 | BottomLeft | 좌하 |
| 7 | BottomCenter | 하단 중앙 |
| 8 | BottomRight | 우하 |

---

## GoVerticalAlignment

수직 정렬.

| 값 | 이름 |
|----|------|
| 0 | Top |
| 1 | Middle |
| 2 | Bottom |

---

## GoHorizonAlignment

수평 정렬.

| 값 | 이름 |
|----|------|
| 0 | Left |
| 1 | Center |
| 2 | Right |

---

## GoDirection

4방향. GoTabControl의 TabPosition, GoProgress의 Direction 등에 사용.

| 값 | 이름 |
|----|------|
| 0 | Left |
| 1 | Right |
| 2 | Up |
| 3 | Down |

---

## GoDirectionHV

가로/세로 방향. GoSlider, GoNumberBox, GoButtons 등의 Direction에 사용.

| 값 | 이름 |
|----|------|
| 0 | Horizon |
| 1 | Vertical |

---

## GoDockStyle

컨트롤 Dock 스타일. 모든 GoControl의 `Dock` 속성에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | None | 절대 좌표 배치 (기본값) |
| 1 | Left | 왼쪽 도킹 |
| 2 | Top | 상단 도킹 |
| 3 | Right | 오른쪽 도킹 |
| 4 | Bottom | 하단 도킹 |
| 5 | Fill | 부모 영역 전체 채우기 |

> `"Fill": true` 속성은 존재하지 않는다. `"Dock": 5`를 사용.

---

## GoFontStyle

폰트 스타일. `FontStyle` 속성에 사용.

| 값 | 이름 |
|----|------|
| 0 | Normal |
| 1 | Italic |
| 2 | Bold |
| 3 | BoldItalic |

---

## GoAutoFontSize

자동 폰트 크기 조절 레벨. `AutoFontSize` 속성에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | NotUsed | 자동 크기 조절 안함 (기본값) |
| 1 | XXS | 가장 작은 크기 |
| 2 | XS | 매우 작은 크기 |
| 3 | S | 작은 크기 |
| 4 | M | 중간 크기 |
| 5 | L | 큰 크기 |
| 6 | XL | 매우 큰 크기 |
| 7 | XXL | 가장 큰 크기 |

---

## GoRoundType

모서리 둥글기 적용 위치. `Round` 속성에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | Rect | 직각 (라운드 없음) |
| 1 | All | 네 모서리 모두 라운드 |
| 2 | L | 왼쪽 두 모서리만 라운드 |
| 3 | R | 오른쪽 두 모서리만 라운드 |
| 4 | T | 위쪽 두 모서리만 라운드 |
| 5 | B | 아래쪽 두 모서리만 라운드 |
| 6 | LT | 좌상단만 라운드 |
| 7 | RT | 우상단만 라운드 |
| 8 | LB | 좌하단만 라운드 |
| 9 | RB | 우하단만 라운드 |
| 10 | Ellipse | 타원형 |

---

## GoDialogResult

다이얼로그 버튼 클릭 결과.

| 값 | 이름 |
|----|------|
| 0 | Ok |
| 1 | Cancel |
| 2 | Yes |
| 3 | No |

---

## GoMouseButton

마우스 버튼 종류. MouseDown/MouseUp 이벤트에 사용.

| 값 | 이름 |
|----|------|
| 0 | Left |
| 1 | Right |
| 2 | Middle |

---

## GoItemSelectionMode

리스트/그리드 항목 선택 모드. GoListBox, GoTreeView, GoToolBox의 `SelectionMode`에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | None | 선택 불가 |
| 1 | Single | 단일 선택 |
| 2 | Multi | 다중 선택 |
| 3 | MultiPC | 다중 선택 (PC 방식: Ctrl/Shift 클릭) |

---

## GoButtonsMode

GoButtons 컨트롤 선택 모드. `Mode` 속성에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | Button | 일반 버튼 (선택 상태 없음) |
| 1 | Toggle | 토글 (다중 선택 가능) |
| 2 | Radio | 라디오 (단일 선택) |

---

## GoButtonFillStyle

버튼 배경 채우기 스타일. GoButton, GoButtons, GoToggleButton 등의 `FillStyle`에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | Flat | 단색 채우기 |
| 1 | Emboss | 엠보스 효과 |
| 2 | Gradient | 그라데이션 |

---

## GoDateTimeKind

날짜/시간 선택기 표시 종류. GoInputDateTime의 `DateTimeStyle`에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | DateTime | 날짜 + 시간 |
| 1 | Date | 날짜만 |
| 2 | Time | 시간만 |

---

## GoImageScaleMode

이미지 스케일 모드. GoPicture, GoAnimate, GoPicturePanel의 `ScaleMode`에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | Real | 원본 크기 그대로 좌상단에 표시 |
| 1 | CenterImage | 원본 크기 그대로 영역 중앙에 배치 |
| 2 | Stretch | 영역 크기에 맞게 늘리기 (비율 무시) |
| 3 | Zoom | 비율 유지하면서 영역에 맞게 확대/축소 |

---

## GoKeys

키보드 키 코드 열거형. KeyDown/KeyUp 이벤트에서 사용.

### 특수 키

| 값 | 이름 | 설명 |
|----|------|------|
| -1 | Unknown | 알 수 없는 키 |
| 32 | Space | 스페이스바 |
| 256 | Escape | ESC |
| 257 | Enter | 엔터 |
| 258 | Tab | 탭 |
| 259 | Backspace | 백스페이스 |
| 260 | Insert | Insert |
| 261 | Delete | Delete |

### 방향 키

| 값 | 이름 |
|----|------|
| 262 | Right |
| 263 | Left |
| 264 | Down |
| 265 | Up |

### 탐색 키

| 값 | 이름 |
|----|------|
| 266 | PageUp |
| 267 | PageDown |
| 268 | Home |
| 269 | End |

### 잠금 키

| 값 | 이름 |
|----|------|
| 280 | CapsLock |
| 281 | ScrollLock |
| 282 | NumLock |
| 283 | PrintScreen |
| 284 | Pause |

### 기호 키

| 값 | 이름 | 문자 |
|----|------|------|
| 39 | Apostrophe | ' |
| 44 | Comma | , |
| 45 | Minus | - |
| 46 | Period | . |
| 47 | Slash | / |
| 59 | Semicolon | ; |
| 61 | Equal | = |
| 91 | LeftBracket | [ |
| 92 | Backslash | \ |
| 93 | RightBracket | ] |
| 96 | GraveAccent | ` |

### 숫자 키 (D0~D9)

| 값 | 이름 |
|----|------|
| 48 | D0 |
| 49 | D1 |
| 50 | D2 |
| 51 | D3 |
| 52 | D4 |
| 53 | D5 |
| 54 | D6 |
| 55 | D7 |
| 56 | D8 |
| 57 | D9 |

### 알파벳 키 (A~Z)

| 값 | 이름 |
|----|------|
| 65 | A |
| 66 | B |
| 67 | C |
| 68 | D |
| 69 | E |
| 70 | F |
| 71 | G |
| 72 | H |
| 73 | I |
| 74 | J |
| 75 | K |
| 76 | L |
| 77 | M |
| 78 | N |
| 79 | O |
| 80 | P |
| 81 | Q |
| 82 | R |
| 83 | S |
| 84 | T |
| 85 | U |
| 86 | V |
| 87 | W |
| 88 | X |
| 89 | Y |
| 90 | Z |

### 펑션 키 (F1~F25)

| 값 | 이름 |
|----|------|
| 290 | F1 |
| 291 | F2 |
| 292 | F3 |
| 293 | F4 |
| 294 | F5 |
| 295 | F6 |
| 296 | F7 |
| 297 | F8 |
| 298 | F9 |
| 299 | F10 |
| 300 | F11 |
| 301 | F12 |
| 302 | F13 |
| 303 | F14 |
| 304 | F15 |
| 305 | F16 |
| 306 | F17 |
| 307 | F18 |
| 308 | F19 |
| 309 | F20 |
| 310 | F21 |
| 311 | F22 |
| 312 | F23 |
| 313 | F24 |
| 314 | F25 |

### 키패드 (KeyPad0~KeyPad9, 연산)

| 값 | 이름 |
|----|------|
| 320 | KeyPad0 |
| 321 | KeyPad1 |
| 322 | KeyPad2 |
| 323 | KeyPad3 |
| 324 | KeyPad4 |
| 325 | KeyPad5 |
| 326 | KeyPad6 |
| 327 | KeyPad7 |
| 328 | KeyPad8 |
| 329 | KeyPad9 |
| 330 | KeyPadDecimal |
| 331 | KeyPadDivide |
| 332 | KeyPadMultiply |
| 333 | KeyPadSubtract |
| 334 | KeyPadAdd |
| 335 | KeyPadEnter |
| 336 | KeyPadEqual |

### 수정자 키

| 값 | 이름 |
|----|------|
| 340 | LeftShift |
| 341 | LeftControl |
| 342 | LeftAlt |
| 343 | LeftSuper |
| 344 | RightShift |
| 345 | RightControl |
| 346 | RightAlt |
| 347 | RightSuper |
| 348 | Menu |

---

## GoKeyModifiers (Flags)

키 수정자 플래그. `[Flags]` 속성이 적용되어 비트 OR 조합 가능.

| 값 | 이름 |
|----|------|
| 0x0001 | Shift |
| 0x0002 | Control |
| 0x0004 | Alt |
| 0x0008 | Super |
| 0x0010 | CapsLock |
| 0x0020 | NumLock |

---

## 기타 (특정 컨트롤 전용)

### GoDataGridSelectionMode

GoDataGrid의 `SelectionMode`에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | None | 선택 불가 |
| 1 | Selector | 체크박스 선택 |
| 2 | Single | 단일 행 선택 |
| 3 | Multi | 다중 행 선택 |
| 4 | MultiPC | 다중 행 선택 (PC 방식) |

### GoBarGraphMode

GoBarGraph의 `Mode`에 사용.

| 값 | 이름 |
|----|------|
| 0 | Stack |
| 1 | List |

### ProgressDirection

GoProgress의 `Direction`에 사용.

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | LeftToRight | 왼쪽에서 오른쪽 |
| 1 | RightToLeft | 오른쪽에서 왼쪽 |
| 2 | BottomToTop | 아래에서 위 |
| 3 | TopToBottom | 위에서 아래 |

### GoDataGridColumnSortState

GoDataGrid 열 정렬 상태.

| 값 | 이름 |
|----|------|
| 0 | None |
| 1 | Asc |
| 2 | Desc |

---

> **⚠ 다시 한번 강조: Enum 값은 .gud JSON에서 반드시 숫자로 직렬화하라. 문자열 불가!**
