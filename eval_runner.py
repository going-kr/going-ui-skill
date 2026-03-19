#!/usr/bin/env python3
"""
Going UI Skill — Eval Runner

evals.json 테스트 케이스를 Anthropic API로 실행하고,
must_contain/must_not_contain 검증 + .gud JSON 구조 validation을 수행한다.

사용법:
  # 전체 실행
  python eval_runner.py

  # 특정 케이스만 실행
  python eval_runner.py --name "GoButton 클릭 이벤트 바인딩"

  # .gud 파일 단독 검증
  python eval_runner.py --validate path/to/file.gud

  # 모델 지정
  python eval_runner.py --model claude-sonnet-4-6-20250514

환경 변수:
  ANTHROPIC_API_KEY — Anthropic API 키 (필수)
"""

import argparse
import io
import json
import os
import re
import sys
import time
from pathlib import Path

# Windows cp949 인코딩 문제 방지
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

HAS_ANTHROPIC = False
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    pass


# ─── 경로 설정 ───────────────────────────────────────────────

SKILL_DIR = Path(__file__).parent
EVALS_PATH = SKILL_DIR / "evals.json"
SKILL_MD_PATH = SKILL_DIR / "SKILL.md"


# ─── .gud JSON Validator ─────────────────────────────────────

class GudValidationError:
    def __init__(self, path: str, message: str):
        self.path = path
        self.message = message

    def __str__(self):
        return f"  [{self.path}] {self.message}"


def validate_gud(data):
    """GoDesign JSON 구조를 검증한다. 에러 목록을 반환."""
    errors = []

    # 최상위 필드 검증
    if not isinstance(data, dict):
        errors.append(GudValidationError("$", "최상위가 dict가 아님"))
        return errors

    # Name 검증 — 유효한 C# 식별자
    name = data.get("Name")
    if not name:
        errors.append(GudValidationError("$.Name", "Name 필드 누락"))
    elif not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name):
        errors.append(GudValidationError("$.Name", f"유효한 C# 식별자가 아님: '{name}'"))

    # Pages 검증 — Dictionary 형태
    pages = data.get("Pages")
    if pages is not None:
        if isinstance(pages, list):
            errors.append(GudValidationError("$.Pages", "Array [] 불가 — Dictionary {} 형태여야 함"))
        elif isinstance(pages, dict):
            for page_name, page_obj in pages.items():
                errors.extend(_validate_page_or_window(f"$.Pages.{page_name}", page_obj, "Page"))
        else:
            errors.append(GudValidationError("$.Pages", f"dict 또는 null이어야 함, got {type(pages).__name__}"))

    # Windows 검증 — Dictionary 형태
    windows = data.get("Windows")
    if windows is not None:
        if isinstance(windows, list):
            errors.append(GudValidationError("$.Windows", "Array [] 불가 — Dictionary {} 형태여야 함"))
        elif isinstance(windows, dict):
            for wnd_name, wnd_obj in windows.items():
                errors.extend(_validate_page_or_window(f"$.Windows.{wnd_name}", wnd_obj, "Window"))
        else:
            errors.append(GudValidationError("$.Windows", f"dict 또는 null이어야 함, got {type(windows).__name__}"))

    return errors


def _validate_page_or_window(path, obj, kind):
    """Page/Window의 Type/Value 래퍼 구조를 검증한다."""
    errors = []

    if not isinstance(obj, dict):
        errors.append(GudValidationError(path, f"dict여야 함, got {type(obj).__name__}"))
        return errors

    if "Type" not in obj:
        errors.append(GudValidationError(path, "Type 필드 누락"))
    if "Value" not in obj:
        errors.append(GudValidationError(path, "Value 래퍼 누락 — { \"Type\": ..., \"Value\": { ... } } 구조 필수"))
        return errors

    value = obj.get("Value", {})
    if not isinstance(value, dict):
        errors.append(GudValidationError(f"{path}.Value", f"dict여야 함, got {type(value).__name__}"))
        return errors

    # Childrens 확인 (Controls가 아닌 Childrens)
    if "Controls" in value:
        errors.append(GudValidationError(f"{path}.Value", "'Controls' 불가 — 'Childrens' 사용"))

    # Id 검증
    if "Id" not in value:
        errors.append(GudValidationError(f"{path}.Value", "Id(UUID) 필드 누락"))

    # Childrens 내부 컨트롤 검증
    childrens = value.get("Childrens")
    if childrens is not None:
        if isinstance(childrens, list):
            for i, ctrl in enumerate(childrens):
                errors.extend(_validate_control(f"{path}.Value.Childrens[{i}]", ctrl))
        elif isinstance(childrens, dict):
            # GoTableLayoutPanel 등의 {"indexes":{...},"ls":[...]} 구조
            ls = childrens.get("ls", [])
            for i, ctrl in enumerate(ls):
                errors.extend(_validate_control(f"{path}.Value.Childrens.ls[{i}]", ctrl))

    return errors


def _validate_control(path, ctrl):
    """개별 컨트롤의 Type/Value 래퍼, Id, Bounds, Enum을 검증한다."""
    errors = []

    if not isinstance(ctrl, dict):
        errors.append(GudValidationError(path, f"dict여야 함, got {type(ctrl).__name__}"))
        return errors

    # Type/Value 래퍼 검증
    if "Type" not in ctrl:
        errors.append(GudValidationError(path, "Type 필드 누락"))
    if "Value" not in ctrl:
        errors.append(GudValidationError(path, "Value 래퍼 누락"))
        return errors

    value = ctrl.get("Value", {})
    if not isinstance(value, dict):
        errors.append(GudValidationError(f"{path}.Value", f"dict여야 함, got {type(value).__name__}"))
        return errors

    # Id 검증
    if "Id" not in value:
        errors.append(GudValidationError(f"{path}.Value", "Id(UUID) 필드 누락"))

    # Bounds 검증 — "L,T,R,B" 문자열
    bounds = value.get("Bounds")
    if bounds is not None:
        if not isinstance(bounds, str):
            errors.append(GudValidationError(f"{path}.Value.Bounds", f"문자열이어야 함, got {type(bounds).__name__}"))
        else:
            parts = bounds.split(",")
            if len(parts) != 4:
                errors.append(GudValidationError(f"{path}.Value.Bounds", f"'L,T,R,B' 4값이어야 함: '{bounds}'"))
            else:
                try:
                    l, t, r, b = [float(p) for p in parts]
                    if r < l:
                        errors.append(GudValidationError(f"{path}.Value.Bounds", f"R({r}) < L({l}) — R은 L보다 커야 함"))
                    if b < t:
                        errors.append(GudValidationError(f"{path}.Value.Bounds", f"B({b}) < T({t}) — B는 T보다 커야 함"))
                except ValueError:
                    errors.append(GudValidationError(f"{path}.Value.Bounds", f"숫자 파싱 실패: '{bounds}'"))

    # Margin/TextPadding 검증 — 객체여야 함, 문자열 불가
    for prop_name in ("Margin", "TextPadding"):
        prop = value.get(prop_name)
        if prop is not None and isinstance(prop, str):
            errors.append(GudValidationError(f"{path}.Value.{prop_name}", f"문자열 불가 — {{\"Left\":0,...}} 객체여야 함"))

    # Enum 검증 — 숫자여야 함
    enum_props = ("Dock", "ContentAlignment", "Round", "FontStyle", "Direction",
                  "FillStyle", "AutoFontSize", "AutoIconSize", "ScrollMode", "SelectionMode")
    for prop_name in enum_props:
        prop = value.get(prop_name)
        if prop is not None and isinstance(prop, str):
            errors.append(GudValidationError(f"{path}.Value.{prop_name}", f"Enum은 숫자여야 함, 문자열 '{prop}' 불가"))

    # Controls → Childrens 오류
    if "Controls" in value:
        errors.append(GudValidationError(f"{path}.Value", "'Controls' 불가 — 'Childrens' 사용"))

    # Width/Height 오류 (Bounds 대신 사용한 경우)
    if "Width" in value or "Height" in value:
        errors.append(GudValidationError(f"{path}.Value", "Width/Height 불가 — Bounds 'L,T,R,B' 사용"))

    # 재귀 — 하위 Childrens
    childrens = value.get("Childrens")
    if childrens is not None:
        if isinstance(childrens, list):
            for i, child in enumerate(childrens):
                errors.extend(_validate_control(f"{path}.Value.Childrens[{i}]", child))
        elif isinstance(childrens, dict):
            ls = childrens.get("ls", [])
            for i, child in enumerate(ls):
                errors.extend(_validate_control(f"{path}.Value.Childrens.ls[{i}]", child))

    # GoSwitchPanel Pages
    switch_pages = value.get("Pages")
    if switch_pages is not None and isinstance(switch_pages, list):
        for i, sp in enumerate(switch_pages):
            if isinstance(sp, dict):
                for j, child in enumerate(sp.get("Childrens", [])):
                    errors.extend(_validate_control(f"{path}.Value.Pages[{i}].Childrens[{j}]", child))

    # GoTabControl TabPages
    tab_pages = value.get("TabPages")
    if tab_pages is not None and isinstance(tab_pages, list):
        for i, tp in enumerate(tab_pages):
            if isinstance(tp, dict):
                for j, child in enumerate(tp.get("Childrens", [])):
                    errors.extend(_validate_control(f"{path}.Value.TabPages[{i}].Childrens[{j}]", child))

    return errors


def validate_gud_file(filepath):
    """파일 경로로 .gud 파일을 검증한다."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [GudValidationError("$", f"JSON 파싱 실패: {e}")]
    except FileNotFoundError:
        return [GudValidationError("$", f"파일을 찾을 수 없음: {filepath}")]

    return validate_gud(data)


# ─── Eval Runner ─────────────────────────────────────────────

def load_skill_context():
    """SKILL.md를 시스템 프롬프트용 컨텍스트로 로드한다."""
    skill_text = SKILL_MD_PATH.read_text(encoding="utf-8")
    return skill_text


def load_reference_docs(references):
    """references 목록의 md 파일들을 읽어 컨텍스트에 추가한다."""
    docs = []
    for ref in references:
        ref_path = SKILL_DIR / ref
        if ref_path.exists():
            content = ref_path.read_text(encoding="utf-8")
            docs.append(f"--- {ref} ---\n{content}")
    return "\n\n".join(docs)


def extract_json_from_response(text):
    """응답에서 JSON 블록을 추출한다. .gud 관련 케이스에서 사용."""
    # ```json ... ``` 블록 찾기
    json_match = re.search(r'```(?:json)?\s*\n(.*?)\n```', text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(1))
        except json.JSONDecodeError:
            pass

    # 전체 텍스트에서 { ... } 찾기
    brace_match = re.search(r'\{.*\}', text, re.DOTALL)
    if brace_match:
        try:
            return json.loads(brace_match.group(0))
        except json.JSONDecodeError:
            pass

    return None


def run_eval(client, eval_case, model, skill_context):
    """단일 eval 케이스를 실행하고 결과를 반환한다."""
    name = eval_case["name"]
    prompt = eval_case["prompt"]
    must_contain = eval_case.get("must_contain", [])
    must_not_contain = eval_case.get("must_not_contain", [])
    references = eval_case.get("references", [])

    # 참조 문서 로드
    ref_docs = load_reference_docs(references)
    system_prompt = f"{skill_context}\n\n{ref_docs}" if ref_docs else skill_context

    # API 호출
    start_time = time.time()
    try:
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            system=system_prompt,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = response.content[0].text
        elapsed = time.time() - start_time
    except Exception as e:
        return {
            "name": name,
            "passed": False,
            "errors": [f"API 호출 실패: {e}"],
            "elapsed": time.time() - start_time,
        }

    # must_contain 검증
    errors = []
    for keyword in must_contain:
        if keyword not in response_text:
            errors.append(f"MUST_CONTAIN 실패: '{keyword}' 미포함")

    # must_not_contain 검증
    for keyword in must_not_contain:
        if keyword in response_text:
            errors.append(f"MUST_NOT_CONTAIN 실패: '{keyword}' 포함됨")

    # .gud 관련 케이스 — JSON 구조 validation
    # evals.json에 "validate_gud": true 태그가 있거나,
    # 응답에 JSON 블록이 있고 그 안에 GoDesign 관련 키가 있으면 검증
    is_gud_case = eval_case.get("validate_gud", False)
    gud_errors = []
    extracted = extract_json_from_response(response_text)
    if extracted:
        # GoDesign 관련 키가 있으면 자동 감지
        gud_keys = {"Pages", "Windows", "DesignWidth", "DesignHeight", "TitleBar"}
        if is_gud_case or (isinstance(extracted, dict) and gud_keys & set(extracted.keys())):
            is_gud_case = True
    if is_gud_case and extracted:
            gud_validation = validate_gud(extracted)
            gud_errors = [str(e) for e in gud_validation]
            if gud_errors:
                errors.extend([f"GUD_VALIDATION: {e}" for e in gud_errors])

    return {
        "name": name,
        "passed": len(errors) == 0,
        "errors": errors,
        "elapsed": elapsed,
        "response_preview": response_text[:200] + "..." if len(response_text) > 200 else response_text,
    }


def main():
    parser = argparse.ArgumentParser(description="Going UI Skill Eval Runner")
    parser.add_argument("--name", type=str, help="특정 케이스 이름만 실행")
    parser.add_argument("--validate", type=str, help=".gud 파일 단독 검증")
    parser.add_argument("--model", type=str, default="claude-sonnet-4-6-20250514",
                        help="사용할 모델 (기본: claude-sonnet-4-6-20250514)")
    parser.add_argument("--verbose", action="store_true", help="응답 미리보기 출력")
    args = parser.parse_args()

    # .gud 단독 검증 모드
    if args.validate:
        print(f"\n=== .gud Validation: {args.validate} ===\n")
        errors = validate_gud_file(args.validate)
        if errors:
            print(f"FAIL — {len(errors)}개 오류:\n")
            for e in errors:
                print(f"  {e}")
        else:
            print("PASS — 구조 검증 통과")
        sys.exit(1 if errors else 0)

    # anthropic 패키지 확인
    if not HAS_ANTHROPIC:
        print("ERROR: anthropic 패키지가 필요합니다. pip install anthropic")
        sys.exit(1)

    # API 키 확인
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY 환경 변수를 설정하세요.")
        sys.exit(1)

    # evals.json 로드
    with open(EVALS_PATH, "r", encoding="utf-8") as f:
        evals = json.load(f)

    # 특정 케이스 필터
    if args.name:
        evals = [e for e in evals if args.name.lower() in e["name"].lower()]
        if not evals:
            print(f"ERROR: '{args.name}'에 해당하는 케이스 없음")
            sys.exit(1)

    # 스킬 컨텍스트 로드
    skill_context = load_skill_context()
    client = anthropic.Anthropic(api_key=api_key)

    print(f"\n{'='*60}")
    print(f"  Going UI Skill Eval Runner")
    print(f"  Model: {args.model}")
    print(f"  Cases: {len(evals)}")
    print(f"{'='*60}\n")

    results = []
    passed = 0
    failed = 0

    for i, eval_case in enumerate(evals, 1):
        name = eval_case["name"]
        print(f"[{i}/{len(evals)}] {name} ... ", end="", flush=True)

        result = run_eval(client, eval_case, args.model, skill_context)
        results.append(result)

        if result["passed"]:
            passed += 1
            print(f"PASS ({result['elapsed']:.1f}s)")
        else:
            failed += 1
            print(f"FAIL ({result['elapsed']:.1f}s)")
            for err in result["errors"]:
                print(f"    {err}")

        if args.verbose and "response_preview" in result:
            print(f"    Response: {result['response_preview']}")

        print()

    # 결과 요약
    total = passed + failed
    print(f"{'='*60}")
    print(f"  Results: {passed}/{total} passed ({passed/total*100:.0f}%)")
    if failed:
        print(f"  Failed: {failed}")
        print(f"\n  실패 케이스:")
        for r in results:
            if not r["passed"]:
                print(f"    - {r['name']}")
    print(f"{'='*60}\n")

    # 결과 JSON 저장
    output_path = SKILL_DIR / "eval_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({
            "model": args.model,
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": f"{passed/total*100:.1f}%",
            "results": results,
        }, f, ensure_ascii=False, indent=2)
    print(f"결과 저장: {output_path}")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
