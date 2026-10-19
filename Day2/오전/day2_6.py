# 딕셔너리
# key-value 한쌍이 하나의 값

# 리스트 vs 딕셔너리
list_1 = [10, 20, 30, [1,2,3]]
dict_1 = {'kor':80 , 'eng':80 , 'math':90}

# dict.keys()
# dict.values()
# dict.items()

# for i in dict_1.items(): # dict_1은 dict_1.keys로 해석 => key값을 가져온다
#     print(i,i[0],i[1])


# number1,number2 = (10,20)

for key,value in dict_1.items():
    print(f"key = {key} {value}")

#딕셔너리는 순서의 개념이 없으므로 인덱스로 찾지 않고 []로 해서 key값으로 조회
#없는 키를 대괄호로 조회하면 KeyError가 발생합니다. 
# **키가 없을 수도 있다면 get()**을 사용하세요.
# get(키, 기본값)은 키가 없으면 기본값을 반환합니다.
