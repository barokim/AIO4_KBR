class SaFeProfile:  # 클래스 => 함수들을 하나로 묶어놓는것
    def __init__(self): # 함수=> 코드들을 묶어놓고
        pass
    def get(self,key):
        return True


# user_profile = SaFeProfile() # 클래스 객체를 할당 ==> 여기에 None이면 오류발생
user_profile = None 
# 이것이 none이면 오류발생하므로 코드를 방어하기 위해 
# if user_profile  user_profile.get('is_verified'): 로 작성해야 함 
# ==> 부모자식 관계 클래스 상속

if user_profile and user_profile.get('is_verified'): 
#.get이 살려면은 앞에 user_profile이 살아야 한데 그 값이 none이므로 none값을 방어 하기 위해 사용
    print('성공')
else:
    print('실패')