# What          : 무엇을 만들지
# Consistants   : 어떤제약으로 동작해야 하는지
# How           : 구현은 어떻게
# Vibe Check    : 결과물 검증
# 3대 핵심 룰 P(prompt), G(generator), V(validator)
# P(prompt)     : input (입력), Output(출력), 알고리즘 제약 조건,  함수명시
# Validator     : 결과 검증, 테스트 케이스 검증

#1부터 10까지의 짝수의 합과 개수구하기
# [Problem] 1부터 n까지의 정수 중 짝수들의 합과 짝수의 총 개수를 계산한다
# [Function] calculate_even_sum_and_count(n)
# [Rules]
#     - n이 1 미만인 경우 합 0, 개수 0을 반환할것
#     - for 문과 if 문을 활용하여 짝수(i % 2 ==0)를 판단할 것
# [Output]    {"Sum": int, "Count":int  }

# 실습규칙
'''
문제정의 / 입력값 / 출력값/ 제약조건을 작성
assert 함수를 활용하여 테스트 케이스
'''


