"""실습 메뉴. 실행: python day1_modules/main.py 또는 python -m day1_modules."""

if __package__:
    from .exercises.variables import practice_1
    from .exercises.pass_fail import practice_2
    from .exercises.even_numbers import practice_3
    from .exercises.multiplication_table import practice_4
    from .exercises.number_game import practice_5
else:
    from Day1.day1_modules.exercises.variables import practice_1
    from Day1.day1_modules.exercises.pass_fail import practice_2
    from Day1.day1_modules.exercises.even_numbers import practice_3
    from Day1.day1_modules.exercises.multiplication_table import practice_4
    from Day1.day1_modules.exercises.number_game import practice_5


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

