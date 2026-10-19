# 논리 연산자
isSuccess = True
isPass = False
# True and True => True, True and False => False, 
# False and True => False, False and False => False
# => and 연산자는 곱하기 => 두 조건이 모두 True일 때만 True를 반환

# or 연산자는 덧셈 => 두 조건중 하나라도 True이면 True를 반환
# True or True => true, True or False => True,
# False or True => True, False or False => False


if isSuccess and isPass: 
    print("A")
else:
    print("B")


if isSuccess or isPass: 
    print("A")
else:
    print("B")

# 단락 평가 Short-circuit evaluation 
def expensive_check():
    print("시간이 오래 걸리는 함수 실행")
    return True

is_active = False

if is_active or expensive_check(): ## false or true => true
    print("통과")
else:
    print("차단 (expensive_check 실행안됨)")

# 객체 지향 -> 객체 단위로 프로그래밍
# 변수 여러개를 하나의 객체에 담아서 관리 ==> 클래스 ==> 오브젝트
# 랜덤 => 객체가 생성 안됨 => 에러가 발생 => 객체를 생성해야 함
# None값을 방어
user_profile = None
if user_profile is not None and user_profile.get('is_verified'):
    print('인증된 사용자')
else:
    print('인증되지 않은 사용자')
