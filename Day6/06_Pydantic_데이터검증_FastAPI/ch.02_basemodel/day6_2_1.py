# 필수 / 기본값, 모델 생성/검증
from pydantic import BaseModel,ValidationError   #import => py파일이 코딩이 되서 가지고 있으므로

class Member(BaseModel):
    username : str
    age : int
    active : bool = True
    nickname : str | None = None

#라이브러리로 들어가서 같이 실행 ==> if __name__ == '__main__' =>name이 main일때만 사용되게한

class MemberOut(Member):
    id : int

def main()  -> None:
    member = Member(username= 'kim', age= 30)
    print(member)
    raw = {'username':'kim', 'age':'34', 'active':False}
    parsed = Member.model_validate(raw)
    print(parsed, 'age 타입', type(parsed.age).__name__)
    print('nickname 기본값', parsed.nickname)

    #필수 필드 누락
    try:
        Member(username='kim')
    except ValidationError as e:
        print(e, e.errors()[0]['loc'], e.errors()[0]['type'])

#Memberout객체 형성
    memberout = MemberOut(id=1, username='kim', age=30)
    print(memberout)


if __name__=='__main__':
    main()
