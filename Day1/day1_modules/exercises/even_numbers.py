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

