#리스트
# 사용자로부터 데이터를 입력받아서(5개) 리스트에 저장하고 
# 저장된 리스트의 값 중에서 짝수만 출력해보기

# number1 = input("숫자를 입력하세요: ")
# number2 = input("숫자를 입력하세요: ")
# number3 = input("숫자를 입력하세요: ")
# number4 = input("숫자를 입력하세요: ")
# number5 = input("숫자를 입력하세요: ")

# numbers = [int(number1), int(number2), int(number3), int(number4), int(number5)]

numbers =[]  #빈 리스트 생성
for i in range(5):
    scores = int(input(f"{i+1}.숫자를 입력하세요: "))
    numbers.append(scores)    ## f를 쓰면(i+1)이 변수로 존재, i는 0~4까지 
print("저장된숫자: ", numbers)   
for i in numbers:
    if i % 2 == 0:   # % 는 나머지 연산자, 2로 나누었을때 나머지가 0이면 짝수
        print(i)

