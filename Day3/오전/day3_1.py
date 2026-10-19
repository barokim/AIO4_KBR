# 클래스와 객체==> 객체지향 프로그래밍(OOP)
'''
class (마스터 설계도): 로봇의 속성과 버튼을 정의한 청사진입니다. 설계도 자체는 일하지 않으며, 설계도로부터 실
체(인스턴스)를 찍어내야 움직입니다.
__init__ (출생 신고서 마법 메서드): 로봇이 공장에서 갓 조립되어 나올 때 단 한 번 자동으로 호출되며, 이름·초기
체력·트랙 같은 초기 속성을 세팅합니다. ==> 초기화가 필요한 작업에 넣어놓는다
self (나 자신을 가리키는 명찰): 똑같은 설계도로 만든 100명의 수강생 객체 중 "지금 커피를 마시고 레벨업하는 바
로 나 자신"의 메모리 주소를 가리키는 필수 첫 번째 매개변수입니다. => class 안에 있는지를 구분하는것
똑같은 설계도=> 객체를 여러개 => 독립적으로 기술을 구현
Class 안에 쓰는것-> 변수와 함수

<예제>
class KDTStudent: => class는 첫번째 글자를 대문자
def __init__(self, name: str, track: str): => self는 무조건 들어감
self.name = name => 변수없이 함수만 있어도 가능 => 그러니 이 부분 구현안해도 됨
self.track = track
self.level = 1
self.energy = 100
self.completed_missions = []
def study_coding(self, topic: str, cost_energy: int = 25 (defalt 매개변수)) -> str:
if self.energy < cost_energy:==> defalt 매개변수: 실행하는데 문제 되지 않게
return f"[휴식 필요] {self.name}님의 에너지가 부족합니다! (현재: {self.energy})"
self.energy -= cost_energy
self.level += 1
self.completed_missions.append(topic)
return f"[레벨업!] {self.name}님이 '{topic}' 실습을 완료했습니다! (Lv.{self.level}, 남은
에너지: {self.energy})"
def drink_coffee(self, boost: int = 40) -> str:
self.energy = min(100, self.energy + boost) ==> min함수는 ()안에 값중 최소값을 반환
return f"[충전 완료] 아이스 아메리카노 수혈! 현재 에너지: {self.energy}"
student1 = KDTStudent("김루키", "AI 엔지니어링")
print(student1.study_coding("Python 클래스 기초"))

'''
## 생성자 --> 객체를 생성하는데 필요한것 , 생성자 메카니즘은 같다
## 생성자 호출 => class 호출하는 순간 호출된다 => 값
## self위치는 첫번째로 고정
## 매개변수 (argument, parameter, 인자)--> 전달하는 값

class BaristaBot:
    def __init__(self, bot_name: str, bean_grams: int):
       self.bot_name = bot_name
       self.bean_grams = bean_grams
       self.total_cups = 0

    def brew_espresso(self, cups: int = 1) -> str:
        required_beans = cups * 18 # 원두가 부족하지 않게 
        if self.bean_grams < required_beans:
           return f"[{self.bot_name}] 원두 부족! (필요: {required_beans}g, 현재: {self.bean_grams}g)"
        self.bean_grams -= required_beans
        self.total_cups += cups
        return f"[{self.bot_name}] 에스프레소 {cups}잔 추출 완료! (남은 원두: {self.bean_grams}g, 누적: {self.total_cups}잔)"

bot = BaristaBot("코덱스바리스타-1호", 50)
print(bot.brew_espresso(2))
print(bot.brew_espresso(2))

bot2 = BaristaBot('알바생', 100)
print(bot2.brew_espresso(3))
print(bot2.brew_espresso(2))
print(bot2.brew_espresso(10))
print(bot2.brew_espresso(5))
