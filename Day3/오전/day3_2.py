'''
캡슐화(Encapsulation)와 프로퍼티(@property) — 내 지갑과 AI 가중치는 아무나 못 건드려!
1. 재미있는 문법 스토리텔링: 금고 잠금장치(__)와 스마트 문지기(@property)
만약 은행 앱에서 누군가 wallet.balance = -999999처럼 내 통장 잔고를 직접 수정할 수 있다면 어떨까요? 
또는 딥러닝 모델의 학습률(Learning Rate)에 실수로 -50.0을 대입해 학습이 폭발한다면 큰일입니다. 
그래서 중요한 내부 데이터는 금고(Private 변수 __변수명)에 숨기고, 
검증 로직을 갖춘 스마트 문지기(@property와 @setter)를 통해서만 출입을 허락합니다.
self.__balance (맹글링 금고): 
변수 앞에 언더바 두 개(__)를 붙이면 클래스 외부에서 직접 접근이 차단됩니다. 
@property (안전한 조회 창구): 메서드이지만 외부에서는 
일반 변수처럼(wallet.balance) 깔끔하게 읽을 수 있게해줍니다.
@balance.setter (검문소 문지기): 값을 대입할 때(wallet.balance = 값) 자동으로 호출되어 
음수나 비정상 범위를 걸러냅니다.
@property (안전한 조회 창구): 메서드(클래스안에 함수)이지만 외부에서는 일반 변수처럼(wallet.balance) 
깔끔하게 읽을 수 있게 해줍니다.
@balance.setter (검문소 문지기): 값을 대입할 때(wallet.balance = 값) 자동으로 호출되어 
음수나 비정상 범위를 걸러냅니다.
캡슐화해서 쓰면은 외부에서는 사용자는 변수처럼 
'''
class DigitalWallet:
    def __init__(self, owner: str, initial_balance: int = 0):
        self.owner = owner
        self.__balance = 0
        self.balance = initial_balance #setter검문소를 거쳐 안전하게 초기화

    @property # 값을 읽어올때는 property
    def balance(self) -> int:
       print("balance 출력호출")
       return self.__balance

    @balance.setter # 값을 넣을때는 setter
    def balance(self, amount: int) -> None:
         print("balance 셋팅호출")
         if amount < 0:
            print(f"[보안 경고] 잔액은 음수가 될 수 없습니다! (입력값: {amount}원 -> 거부됨)")
            return 
         self.__balance = amount

    def deposit(self, amount: int) -> str:
        if amount <= 0:
         return "[오류] 입금액은 0원보다 커야 합니다."
        self.balance += amount
        return f"[{self.owner}] {amount:,}원 입금 완료 (현재 잔액: {self.balance:,}원)"

    def __str__(self) -> str:
       return('객체자체를 호출하면 이 함수가 실행됩니다')
    


wallet = DigitalWallet("이코딩", 10000)
# print(wallet.deposit(5000))
# wallet.balance = -99999 # 외부에서 불법 음수 대입 시도 -> setter가 즉시 차단!
# print(f"최종 안전 잔액: {wallet.balance:,}원")

print(wallet)

# 안에서만 쓸수있고 외부에서는 접근할수 없다 --> Private
# 함수를 통해서만 가져온거 Property, Setter 
# 값을 읽는거면 property 변수명.setter
# property 내부에서만 할수 있고 외부에서는 쓸수 없으므로 
# 변수명.setter 
# 값을 읽고 쓸때는 함수 호출
#__init__ 객체만들때 자동으로 호출
# __str__ 특정 객체를 출력하려고 할때 자동으로 호출
#__()__ 특정사건을 발생할때 자동으로 호출


#class => 각각의 개체가 동일한 함수와 변수를 쓸수있게 만든
# 다른언어랑 다르게 파이썬에서만 class에서 정의된 변수나 함수의 속성 외의 다른 변수나 함수도 
# 쓸수 있다고 한다
