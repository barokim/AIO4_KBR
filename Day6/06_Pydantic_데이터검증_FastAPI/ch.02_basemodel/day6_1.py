'''
Pydantic - 데이터 유효성 및 타입을 체크
기능이 구현된 클래스를 상속받아서 pydantic 클래스 또는 모델을 만들수 있음
'''

from pydantic  import BaseModel, ValidationError
#일반 파이썬 클래스

class NormalClass:
    def __init__(self, name:str, age:int):  #NormalClass() -> 매개변수 없는 생성자 호출
        #__init__은 객체변수 (인스턴스변수) --> 독립적으로 존재
        self.name = name
        self.age = age

# params = {'age':20, 'name': '홍길동'}
# user1 = NormalClass('홍길동',20) # 매개변수 순서대로 들어간다, 
# #매개변수를 직접 거론하여 호출하는 경우 순서가 달라져도 된다, 
# user2 = NormalClass(**params)

# Pydantic클래스
class pydanticUser(BaseModel):
    name:str
    age:int
    