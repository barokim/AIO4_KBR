'''
추상 클래스(ABC)와 데이터클래스(@dataclass) — 현대적 파이썬 OOP 끝판왕!
팀 프로젝트에서 동료 개발자가 새로운 결제 수단 클래스를 만들면서 핵심 메서드 이름을 
process_payment() 대신 pay_money()라고 마음대로 지으면 전체 서버가 뻗어버립니다. 
이를 막아주는 두 가지 모던 파이썬 무기를 배웁니다.

ABC & @abstractmethod (프랜차이즈 필수 규격서): "이 추상 메서드를 구현하지 않으면 
아예 객체 생성조차 불허한다!"라고 강제하는 인터페이스 계약서입니다.

@dataclass (자동 문서 생성기): 데이터를 담는 영수증이나 DTO 클래스를 만들 때
 __init__, __repr__, 비교 연산자를 자동으로 생성해 코드 길이를 절반 이하로 줄여줍니다.
'''

from abc import ABC, abstractclassmethod

class PaymentGateway:
    @abstractclassmethod
    def process_payment(self,item:str, amount:int) -> str:
        pass

class CreditCardGateway(PaymentGateway):
    def process_payment(self, item:str, amount:str) -> str:
        return f'구매품목2: {item} 수량2:{amount}'
    pass

class BankGateway(PaymentGateway):
    pass

obj = CreditCardGateway()
print(obj.process_payment('식료품',100))
