#zip => 리스트 2개를 묶어주는것 => 딕셔너리의 item
list_1 = ['a', 'b', 'c']
list_2 = [100,200,300]
result = zip(list_1,list_2)
for i in result:
    print(i)
for i in result:
    print(i)

#zip으로 생성한 객체를 dictionary 변환
# zip()은 **한 번 꺼낸 요소를 다시 꺼낼 수 없는 이터레이터(iterator)**를 반환하기 때문입니다.
# 참고로 zip()은 같은 위치의 요소들을 튜플로 묶어 주는 함수입니다. 
# 딕셔너리를 직접 반환하지는 않지만, 다음처럼 딕셔너리를 만들 때 사용할 수 있습니다.

# result = dict(result)
# print(result)

# assert는 조건이 참인지 확인하는 키워드입니다.
# - 조건이 참(True)이면 다음 코드로 진행합니다.
# - 조건이 거짓(False)이면 AssertionError가 발생하고 실행이 중단됩니다.
# 예를 들어 덧셈 결과를 확인할 수 있습니다.

# AI agent를 컨트롤 하는 테크 리더

# R I O C 규칙
# Role : 역할
# Input :  입력
# Output : 출력
# Constraints & logic : 