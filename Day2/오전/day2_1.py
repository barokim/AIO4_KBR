# if ~ elif ~ else: 조건에 조건에 조건인 구문  ##절대경로: 풀경로 ## 상대 경로: 간단한 경로
score = int(input("점수를 입력하세요: ")) 
## 0~100사이의 숫자만 입력하도록 하고 잘못 입력시 다시 입력하도록 하는 경고창이 뜨도록 하는 로직도 설정 가능

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")