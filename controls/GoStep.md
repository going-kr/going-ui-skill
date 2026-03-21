# GoStep

스텝 인디케이터 컨트롤. 현재 단계를 시각적으로 표시 (이전/다음 버튼 포함).
상속: GoControl → GoStep

⚠ 이벤트명이 **StepChagend** (오타 아닌 실제 이름 — 소스코드 기준)
⚠ Step은 0-based 인덱스 (0 ~ StepCount-1)
⚠ Selectable 기본값: **true**

## .gud JSON

```json
{
  "Type": "GoStep",
  "Value": {
    "PrevIconString": "fa-chevron-left",
    "NextIconString": "fa-chevron-right",
    "ButtonColor": "Base3",
    "StepColor": "Base2",
    "SelectColor": "Select",
    "IsCircle": false,
    "UseButton": true,
    "Step": 0,
    "StepCount": 7,
    "Id": "{UUID}",
    "Name": null,
    "Visible": true,
    "Enabled": true,
    "Selectable": true,
    "Bounds": "0,0,200,30",
    "Dock": 0,
    "Margin": { "Left": 3, "Top": 3, "Right": 3, "Bottom": 3 }
  }
}
```

## 속성 (Properties)

| 타입 | 이름 | 설명 | 기본값 |
|------|------|------|--------|
| string? | PrevIconString | 이전 버튼 아이콘 | "fa-chevron-left" |
| string? | NextIconString | 다음 버튼 아이콘 | "fa-chevron-right" |
| string | ButtonColor | 버튼 색상 | "Base3" |
| string | StepColor | 비선택 스텝 색상 | "Base2" |
| string | SelectColor | 선택 스텝 색상 | "Select" |
| bool | IsCircle | 원형 스텝 표시 | false |
| bool | UseButton | 이전/다음 버튼 표시 | true |
| int | Step | 현재 스텝 (0-based) | 0 |
| int | StepCount | 스텝 총 개수 | 7 |

+ GoControl 공통 속성 → _common.md 참조

## 이벤트 (Events)

| 시그니처 | 이름 | 설명 |
|---------|------|------|
| EventHandler | StepChagend | Step 값 변경 시 발생 |

⚠ 이벤트명 "StepChagend"는 소스코드 기준 정확한 철자임 (Changed의 오타이나 그대로 사용)

## C# 사용

```csharp
var step = (GoStep)dic["stepProgress"];

step.StepChagend += (s, e) =>
{
    lblStep.Text = $"단계: {step.Step + 1} / {step.StepCount}";
};
```

## 검증 완료

- 소스코드(GoStep.cs): 속성 9개 + 이벤트 1개(StepChagend)
- StepChagend 철자는 소스코드 원본 기준 (line 53)
