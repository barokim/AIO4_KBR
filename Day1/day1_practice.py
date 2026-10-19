"""
Python Day 1 복습 실습 모음
=========================

실행 방법: 터미널에서 python day1_practice.py

실습 방법
1. 각 실습의 '직접 해 보기'를 읽고 별도로 코드를 작성해 보세요.
2. 아래 함수의 참고 코드와 비교해 보세요.
3. 메뉴에서 실행하여 '확인할 결과'를 확인하세요.
4. 기본 실습이 끝나면 '추가 과제'에 도전하세요.

사용 기술: Python 3, 콘솔 입출력, 조건문, 반복문, 리스트, random.
외부 패키지 설치는 필요하지 않습니다.
숫자 입력에는 정수를 사용하세요. 문자를 입력하면 ValueError가 발생합니다.
"""

import random


def practice_1():
    """
    실습 1. 변수와 산술 연산 (원본: Day1.py)
    핵심: 변수에 값 저장하기, + 연산자, print().

    직접 해 보기
    - number1에 100, number2에 200을 저장하세요.
    - 두 변수의 합을 출력하세요.

    확인할 결과: number1 + number2 =  300
    추가 과제: 뺄셈, 곱셈, 나눗셈 결과도 출력하세요.
    """
    number1 = 100
    number2 = 200
    print("number1 + number2 = ", number1 + number2)


def practice_2():
    """
    실습 2. 점수에 따른 합격 판정 (원본: day1_2.py)
    핵심: input(), int(), 비교 연산자 >=, if / else.

    직접 해 보기
    - 사용자에게 점수를 입력받으세요.
    - input()의 반환값은 문자열이므로 int()로 정수로 바꾸세요.
    - 60점 이상이면 '합격', 그 외에는 '불합격'을 출력하세요.

    확인할 결과: 60 입력 → 합격 / 59 입력 → 불합격.
    추가 과제: 0~100 밖의 점수에는 '잘못된 점수입니다'를 출력하세요.
    """
    score = int(input("점수를 입력하세요: "))
    if score >= 60:
        print("합격")
    else:
        print("불합격")


def practice_3():
    """
    실습 3. 리스트에 저장하고 짝수 찾기 (원본: day1_3.py)
    핵심: 빈 리스트 [], append(), for, range(), %, f-string.

    직접 해 보기
    - 빈 리스트 numbers를 만드세요.
    - 정수 5개를 입력받아 append()로 저장하세요.
    - 전체 리스트를 출력한 다음 짝수만 출력하세요.

    힌트
    - range(5)는 0, 1, 2, 3, 4를 순서대로 제공합니다.
    - f"{i + 1}.숫자"처럼 문자열에 변수나 계산 결과를 넣을 수 있습니다.
    - number % 2 == 0이면 2로 나눈 나머지가 0이므로 짝수입니다.

    확인할 결과: 1, 2, 3, 4, 5 입력 → 리스트 [1, 2, 3, 4, 5], 짝수 2와 4.
    추가 과제: 홀수도 출력하고, 짝수가 몇 개인지 세어 보세요.
    """
    numbers = []
    for i in range(5):
        number = int(input(f"{i + 1}.숫자를 입력하세요: "))
        numbers.append(number)

    print("저장된 숫자:", numbers)
    print("짝수:")
    for number in numbers:
        if number % 2 == 0:
            print(number)


def practice_4():
    """
    실습 4. 구구단을 가로로 출력하기 (원본: day1_4.py)
    핵심: 중첩 for문, range(시작, 끝), print()의 end 옵션.

    직접 해 보기
    - 한 줄에 2단부터 9단까지 출력하세요.
    - 곱하는 수를 1부터 9까지 바꾸며 총 9줄을 출력하세요.

    힌트
    - range(2, 10)은 2~9이며 마지막 값 10은 포함하지 않습니다.
    - 바깥 반복문은 곱하는 수, 안쪽 반복문은 단을 바꿉니다.
    - end="\t"는 줄바꿈 대신 탭으로 간격을 만듭니다.
    - 안쪽 반복문이 끝난 뒤 print()로 다음 줄로 이동하세요.

    확인할 결과
    - 첫 줄: 2 X 1 = 2부터 9 X 1 = 9까지.
    - 마지막 줄: 2 X 9 = 18부터 9 X 9 = 81까지.
    추가 과제: 사용자가 선택한 단 하나만 출력하도록 바꾸세요.
    """
    for multiplier in range(1, 10):
        for dan in range(2, 10):
            print(f"{dan} X {multiplier} = {dan * multiplier}", end="\t")
        print()


def practice_5():
    """
    실습 5. 숫자 맞추기 게임 (원본: day1_5.py)
    핵심: import, random.randint(), while True, elif, break, +=, -=.

    직접 해 보기
    - 컴퓨터가 1~100 사이의 정수를 무작위로 선택하게 하세요.
    - 사용자가 정답을 맞힐 때까지 반복해서 정수를 입력받으세요.
    - 입력한 수가 정답보다 크거나 작은지 알려 주세요.
    - 시도 횟수를 세고, 매 시도마다 100점에서 10점씩 차감하세요.
    - 정답이면 횟수와 점수를 출력하고 break로 반복을 끝내세요.

    힌트
    - random.randint(1, 100)은 1과 100을 모두 포함합니다.
    - count += 1은 count = count + 1과 같습니다.
    - 정답을 맞힌 시도에도 10점이 차감됩니다.

    확인할 결과
    - 검증할 때 com_number = 50으로 잠시 바꾸세요.
    - 70, 30, 50 순서로 입력하면 '큽니다', '작습니다', '정답입니다'.
    - 총 시도 횟수 3번, 최종 점수 70점이어야 합니다.
    - 확인 후 random.randint(1, 100)으로 되돌리세요.

    원본에서 정리한 부분
    - 반복문 앞의 입력은 비교에 사용되지 않아 제거했습니다.
    - 입력한 모든 숫자가 시도 횟수에 반영됩니다.
    - 원본 점수 규칙을 유지하므로 11번 이상 시도하면 음수가 됩니다.

    추가 과제
    - 점수가 0점 아래로 내려가지 않도록 바꾸세요.
    - 1~100 밖의 입력은 시도 횟수와 점수에 반영하지 마세요.
    """
    com_number = random.randint(1, 100)
    count = 0
    score = 100

    while True:
        user_number = int(input("1~100 사이의 숫자를 입력하세요: "))
        count += 1
        score -= 10

        if user_number > com_number:
            print("컴퓨터보다 큽니다.")
        elif user_number < com_number:
            print("컴퓨터보다 작습니다.")
        else:
            print("정답입니다.")
            print(f"총 시도 횟수는: {count}번입니다.")
            print(f"최종 점수는: {score}점입니다.")
            break


def main():
    # 함수와 딕셔너리는 여러 실습을 한 파일에서 선택하기 위한 보조 구조입니다.
    exercises = {
        "1": ("변수와 산술 연산", practice_1),
        "2": ("합격 판정", practice_2),
        "3": ("리스트와 짝수 찾기", practice_3),
        "4": ("구구단", practice_4),
        "5": ("숫자 맞추기 게임", practice_5),
    }

    while True:
        print("\n=== Python Day 1 복습 ===")
        for key, (title, _) in exercises.items():
            print(f"{key}. {title}")
        print("0. 종료")
        choice = input("실습 번호를 선택하세요: ").strip()

        if choice == "0":
            print("실습을 종료합니다.")
            break
        if choice not in exercises:
            print("0~5 중에서 선택하세요.")
            continue

        _, exercise = exercises[choice]
        print(exercise.__doc__)
        input("Enter를 누르면 참고 코드를 실행합니다.")
        exercise()


if __name__ == "__main__":
    main()
