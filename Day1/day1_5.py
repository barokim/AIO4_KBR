# 숫자 맞추기 게임
# 규칙
# 컴퓨터가 1~100사이의 값을 임의로 생성한후
#사용자가 맞추는 게임
# 사용자가 입력한 값이 크면 크다, 작으면 작다라고 알려줌
# 필요한 기능
# 입력: int(input())
# 컴퓨터가 1~100사이의 임의의 숫자를 선택 => random.randint(1,100)
# 비교연산자를 통해 크다 작다 판별
# 맞출때까지 반복 => while문
# 순환문 탈출 => break
# 조건문 

import random #random 모듈을 사용하기 위해 import

com_number = random.randint(1, 100)  # 1~100사이의 임의의 숫자 생성
user_number = int(input("1~100사이의 숫자를 입력하세요: "))  # 사용자로부터 숫자 입력받기
count = 0
score = 100

# while com_number != user_number:  # 컴퓨터 숫자와 사용자 숫자가 같지 않으면 반복
while True:  # 무한루프
    user_number = int(input("1~100사이의 숫자를 입력하세요: "))  # 사용자로부터 숫자 입력받기
    count += 1   #count = count + 1
    score -= 10   #score = score - 10
    if user_number > com_number:
        print("컴퓨터보다 큽니다.")

    elif user_number < com_number:
        print("컴퓨터보다 작습니다")

    elif score == 0:
        print("점수가 0점이 되었습니다. \n 게임을 종료합니다.")
        break  # while문 탈출
    

print("정답입니다")
print(f"총 시도횟수는 : {count}번입니다")
print(f"최종점수는: {score}점입니다")


