# [Mission 1: Smart FizzBuzz Analyzer]
# - 함수명: analyze_fizzbuzz(limit: int) -> dict
# - 로직 제약:
#   1. 1부터 limit까지 순회한다.
#   2. 3의 배수이면서 5의 배수이면: "FizzBuzz" 카운트 증가
#   3. 3의 배수이면: "Fizz" 카운트 증가
#   4. 5의 배수이면: "Buzz" 카운트 증가
#   5. 그 외의 숫자이면: "Number" 카운트 증가
# - 반환값 형식:
#   {"FizzBuzz": int, "Fizz": int, "Buzz": int, "Number": int}
# - 엣지 케이스: limit가 1 미만인 경우 모든 카운트가 0인 딕셔너리 반환

import json


def analyze_fizzbuzz(limit: int) -> dict:
    """1부터 limit까지의 숫자를 FizzBuzz 규칙으로 분류하여 센다."""
    counts = {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 0}

    if limit < 1:
        return counts

    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            counts["FizzBuzz"] += 1
        elif number % 3 == 0:
            counts["Fizz"] += 1
        elif number % 5 == 0:
            counts["Buzz"] += 1
        else:
            counts["Number"] += 1

    return counts


if __name__ == "__main__":
    print(json.dumps(analyze_fizzbuzz(15)))
