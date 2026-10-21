"""HTML 폼으로 두 숫자를 받아 사칙연산 결과를 보여주는 FastAPI 앱."""

import re
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="두 숫자 계산기")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")
NUMBER_PATTERN = re.compile(r"[+-]?(?:[0-9]{1,15}(?:\.[0-9]{1,10})?|\.[0-9]{1,10})\Z")


def parse_number(raw: str, label: str) -> Decimal:
    """지수 표기/특수값을 제외하고 정수 15자리, 소수 10자리까지 허용한다."""
    value = raw.strip()
    if not value:
        raise ValueError(f"{label} 숫자를 입력해 주세요.")
    if not NUMBER_PATTERN.fullmatch(value):
        raise ValueError(f"{label} 숫자는 정수 부분 15자리, 소수 부분 10자리 이내로 입력해 주세요. (예: -12.5)")
    return Decimal(value)


def format_number(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if value == 0 else text


def calculate(first: Decimal, second: Decimal) -> list[dict[str, str]]:
    # 허용 입력의 곱셈도 손실 없이 처리할 수 있는 정밀도.
    with localcontext() as context:
        context.prec = 60
        results = [
            {"label": "덧셈", "symbol": "+", "value": format_number(first + second)},
            {"label": "뺄셈", "symbol": "−", "value": format_number(first - second)},
            {"label": "곱셈", "symbol": "×", "value": format_number(first * second)},
        ]
        division = "0으로 나눌 수 없습니다."
        if second != 0:
            division = format_number((first / second).quantize(Decimal("0.0000000001")))
        results.append({"label": "나눗셈", "symbol": "÷", "value": division})
    return results


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html",
        context={"first": "", "second": "", "results": [], "error": None},
    )


@app.post("/calculate", response_class=HTMLResponse)
def calculate_form(
    request: Request,
    first: Annotated[str, Form()] = "",
    second: Annotated[str, Form()] = "",
):
    error = None
    results = []
    try:
        first_number = parse_number(first, "첫 번째")
        second_number = parse_number(second, "두 번째")
        results = calculate(first_number, second_number)
    except ValueError as exc:
        error = str(exc)
    return templates.TemplateResponse(
        request=request, name="index.html",
        context={"first": first, "second": second, "results": results, "error": error},
        status_code=400 if error else 200,
    )
