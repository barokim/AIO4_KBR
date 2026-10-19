'''
파이썬 예외처리(try-except-else-finally) — 에러를 먹고 자라는 무적 프로그램!

try (위험 감지 주행 구간): 파일 읽기, 숫자 변환, 딕셔너리 조회 등 에러가 날 가능성이 있는 코드를 배치합니다.
except (맞춤형 에어백 전개): ValueError(타입 변환 실패), KeyError(필수 키 누락)처럼 
에러 종류별로 정밀하게 대응합니다.
else (무사고 보너스 구간): try 블록에서 단 하나의 예외도 발생하지 않았을 때만 실행되는 
안전한 후속 처리 구간입니다.
finally (블랙박스 저장 및 시동 끄기): 에러 발생 여부와 무관하게 100% 무조건 실행되어 파일 닫기나 
DB 연결 해제를 보장합니다.
'''

names = ['홍길동','이순신','강감찬']

# id = 1
# for name in names:
#     print(f'{id}. {name}')
#     id += 1

# for name in enumerate(names,start=1):
#     print(id, name)

# 리스트 컴프리헨션 - 한즐 코드 

raw_logs = [
             "epoch=1,loss=0.45,acc=88.5",
             "epoch=2,loss=invalid,acc=91.0",
             "epoch=3,loss=0.31",
             "epoch=4,loss=0.22,acc=94.2",
]
for line in raw_logs:
    parts = dict(item.split("=") for item in line.split(","))
    try:
        
    
        record = {
               "epoch": int(parts["epoch"]),
               "loss": float(parts["loss"]),
               "acc": float(parts["acc"]),
            }
        print(record)
    except ValueError as e: ##Exception => Key error, Value error등의 모든 error의 부모
        print("값이 잘못되었습니다.",e)
    except KeyError as e:
        print("키값을 확인하세요",e)

    ## 쓰는 이유: 중단 없이 끝까지 코드를 실행하고 싶을때 Try 구문을 사용 
    ## 다른 언어에서는 try ~ catch 파이썬에서는 try ~ except
    ## finally 좀비 프로세스 - 실제에서는 많이 안씀