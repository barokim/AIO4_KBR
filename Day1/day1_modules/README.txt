Python Day 1 모듈별 복습 실습
===========================

실행 방법 (Python 3 필요, 외부 패키지 설치 불필요)

브라우저에서 실습하기 (Python 및 서버 설치 불필요)

web/index.html 파일을 더블클릭하여 브라우저에서 여세요.
5개 실습을 선택하고 값을 입력하면 화면에서 결과를 확인할 수 있습니다.
HTML로 입력 화면을 구성하고 JavaScript로 계산과 게임을 실행합니다.
Python 모듈을 직접 실행하는 방식이 아니라 동일한 로직을 브라우저에서 재현합니다.
인터넷 연결이나 외부 라이브러리는 필요하지 않습니다.
web 폴더의 index.html, styles.css, app.js를 함께 보관하세요.
새로고침하면 입력과 게임 상태가 초기화됩니다.
게임은 1~100 범위 입력만 허용하고, 점수 차감 규칙은 원본과 같습니다.

터미널에서 Python 모듈 실행하기

1. C:\AIO4에서 실행:
   python -m day1_modules

2. 실행 파일을 직접 지정:
   python C:\AIO4\day1_modules\main.py

3. 이 폴더로 이동해서 실행:
   cd C:\AIO4\day1_modules
   python main.py

Windows에서 python 대신 py 명령을 사용하는 환경은 py로 바꾸세요.
명령을 찾을 수 없다면 설치된 Python 실행 파일의 전체 경로를 사용하세요.

파일 구성

main.py                          실습 선택 메뉴와 실행
__main__.py                      python -m day1_modules의 진입점
__init__.py                      패키지 표시
exercises/__init__.py            실습 패키지 표시
exercises/variables.py           실습 1: 변수와 산술 연산
exercises/pass_fail.py           실습 2: 합격 판정
exercises/even_numbers.py        실습 3: 리스트와 짝수 찾기
exercises/multiplication_table.py 실습 4: 구구단
exercises/number_game.py         실습 5: 숫자 맞추기 게임

실습 순서

1. 각 모듈의 함수 안에 있는 설명을 읽으세요.
2. '직접 해 보기'를 먼저 풀고 참고 코드와 비교하세요.
3. 메뉴에서 실습 번호를 선택하고 Enter를 눌러 실행하세요.
4. '확인할 결과'를 확인한 뒤 '추가 과제'에 도전하세요.
5. 메뉴에서 0을 입력하면 종료합니다.

학습 내용과 점수 규칙은 기존 day1_practice.py와 같습니다.
숫자 입력에는 정수를 사용하세요. 문자 입력은 ValueError를 발생시킵니다.
각 모듈은 가져오기(import)만으로 실습을 실행하지 않습니다.

모듈을 따로 사용하기 (C:\AIO4에서 Python을 실행한 경우)

from day1_modules.exercises.variables import practice_1
practice_1()

기존 day1_practice.py는 단일 파일 버전으로 보존되어 있습니다.
