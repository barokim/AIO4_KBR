import random


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

