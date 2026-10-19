"""실행: python verify.py (실패 시 AssertionError와 함께 종료 코드 1).

정수 입력을 대상으로 Mission 1을 검증한다.
명세에 없는 실수, 문자열 등의 처리 방식은 검증 대상에 포함하지 않는다.
"""

from random import Random

from Day2.smart_fizzbuzz_analyzer.main import analyze_fizzbuzz


KEYS = ("FizzBuzz", "Fizz", "Buzz", "Number")


def test_known_results():
    # 튜플의 순서: FizzBuzz, Fizz, Buzz, Number.
    # 14/15/16, 29/30/31로 공배수 경계와 limit 포함 여부를 확인한다.
    cases = {
        1: (0, 0, 0, 1),
        2: (0, 0, 0, 2),
        3: (0, 1, 0, 2),
        4: (0, 1, 0, 3),
        5: (0, 1, 1, 3),
        6: (0, 2, 1, 3),
        14: (0, 4, 2, 8),
        15: (1, 4, 2, 8),
        16: (1, 4, 2, 9),
        29: (1, 8, 4, 16),
        30: (2, 8, 4, 16),
        31: (2, 8, 4, 17),
        100: (6, 27, 14, 53),
    }
    for limit, values in cases.items():
        expected = dict(zip(KEYS, values))
        actual = analyze_fizzbuzz(limit)
        assert actual == expected, f"limit={limit}: {actual=}, {expected=}"


def test_below_one():
    expected = dict.fromkeys(KEYS, 0)
    for limit in (-10**12, -100, -15, -1, 0):
        actual = analyze_fizzbuzz(limit)
        assert actual == expected, f"limit={limit}: 모든 카운트는 0이어야 함, {actual=}"


def test_result_contract():
    for limit in range(-5, 301):
        actual = analyze_fizzbuzz(limit)
        assert type(actual) is dict, f"limit={limit}: dict 반환 필요"
        assert set(actual) == set(KEYS), f"limit={limit}: 키 불일치, {actual=}"
        for key, value in actual.items():
            assert type(value) is int, f"limit={limit}, {key}: int 필요, {value=}"
            assert value >= 0, f"limit={limit}, {key}: 음수 카운트, {value=}"
        assert sum(actual.values()) == max(limit, 0), (
            f"limit={limit}: 중복 또는 누락된 숫자가 있음, {actual=}"
        )


def test_against_math_reference():
    # 구현의 반복/조건 분기를 복사하지 않고 배수 개수 공식으로 교차 검증한다.
    # 고정 시드를 사용하여 실행할 때마다 같은 입력을 검증한다.
    rng = Random(42)
    limits = list(range(501)) + [999, 1000, 10000]
    limits += [rng.randint(501, 10000) for _ in range(50)]
    for limit in limits:
        both = limit // 15
        fizz = limit // 3 - both
        buzz = limit // 5 - both
        expected = {
            "FizzBuzz": both,
            "Fizz": fizz,
            "Buzz": buzz,
            "Number": limit - both - fizz - buzz,
        }
        actual = analyze_fizzbuzz(limit)
        assert actual == expected, f"limit={limit}: {actual=}, {expected=}"


def test_fifteen_number_period():
    # 연속된 15개 숫자마다 각 분류는 각각 1, 4, 2, 8개씩 증가한다.
    increments = dict(zip(KEYS, (1, 4, 2, 8)))
    for limit in range(101):
        before = analyze_fizzbuzz(limit)
        after = analyze_fizzbuzz(limit + 15)
        for key in KEYS:
            assert after[key] - before[key] == increments[key], (
                f"limit={limit}, {key}: 15개 단위 증가량 불일치"
            )


def test_independent_calls():
    first = analyze_fizzbuzz(15)
    second = analyze_fizzbuzz(15)
    assert first is not second, "호출마다 새 딕셔너리를 반환해야 함"
    first["Fizz"] = -999
    assert second == {"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 8}
    assert analyze_fizzbuzz(15) == second, "이전 결과 수정이 다음 호출에 영향을 줌"
    zero = analyze_fizzbuzz(0)
    zero["Number"] = 999
    assert analyze_fizzbuzz(-1) == dict.fromkeys(KEYS, 0)


def run_validation_pipeline():
    # -O/-OO 옵션은 assert를 제거하므로 검증 없이 성공하는 상황을 차단한다.
    if not __debug__:
        raise RuntimeError("assert 검증을 위해 -O/-OO 옵션 없이 실행하세요.")

    stages = (
        test_known_results,
        test_below_one,
        test_result_contract,
        test_against_math_reference,
        test_fifteen_number_period,
        test_independent_calls,
    )
    for index, stage in enumerate(stages, start=1):
        stage()
        print(f"[PASS {index}/{len(stages)}] {stage.__name__}")
    print("All 6 validation stages passed.")


if __name__ == "__main__":
    run_validation_pipeline()
