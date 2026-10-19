# # 리스트 컴프리헨션 (List comprehension) 1줄로 표현
# # result = []
# list_1 = [1,2,3,4,5]

# # for i in list_1:
# #     result.append(i*2)


# result = [i*2 for i in list_1]

# print(result)

# 조건문이 하나만 올때는 다음과 같이 표시

# menu = ['아메리카노', '라떼', '초코']
# ice_menu = ['아이스' +i for i in menu]
# len_menu = [len(i) for i in menu if len(i)%2==0]

# print(len_menu)

#조건문이 여러개
# ['참' if 조건 else '거짓' for i in list]

ages = [20,15,60,25,30,45,5]
print([i for i in ages if i>=20])
print(['성인'if i >= 20 else '미성년' for i in ages])

bad_words = ['바보','멍충이','멍텅구리','바보']
words = sorted(set(word for word in bad_words if word), key=len, reverse=True)
print(words)

import re
pattern = "|".join(re.escape(word) for word in words)
print(pattern)
chat_message = '철수는 바보가 맞습니다'
re.sub(pattern, lambda match: "*" * len(match.group(0)),
                  chat_message, flags=re.IGNORECASE)

#정규표현식 => 복잡한 패턴 실생활 => 전화번호 포맷 형식, 이메일 패턴 (re)
# 정규표현식(Regular Expression, Regex)**은 문자열에서 일정한 패턴을 찾거나, 
# 검사하거나, 바꾸는 방법입니다.
# 예를 들어 "길이: 30cm"에서 숫자만 추출하거나, 
# 입력한 문자열이 정해진 형식인지 확인할 때 사용합니다.
# Python에서는 기본 제공하는 re 모듈을 사용합니다.

