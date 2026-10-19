'''
사용자 정의 예외(Custom Exception)와 raise 

— 비즈니스 규칙을 지키는 맞춤형 경보 시스템!
1. 재미있는 문법 스토리텔링: 일반 화재경보기 vs 스마트 상황실 정밀 경보
파이썬 기본 예외(ValueError, RuntimeError)만 쓰면 
"무언가 잘못됨!"이라는 사이렌만 울릴 뿐, '일일 AI 토큰 한도가 몇 개 부족해서 실패했는지' 
즉시 파악하기 어렵습니다. 
Exception 클래스를 상속받아 우리 서비스만의 도메인 맞춤 예외 클래스를 만들고 raise로 직접 경보를 발령하면, 
에러 처리 코드가 문서처럼 명확해집니다.
2. 나만의 예외상황을 상속받아 사용 
'''

class AIServiceError(Exception):
    """AI 서비스 최상위 기본 예외 클래스"""
    pass

class PromptEmptyError(AIServiceError):
    """프롬프트가 비어있을 때 발생하는 예외"""
    pass

class TokenQuotaExceededError(AIServiceError):
    """토큰 한도 초과 시 요청량과 잔여 한도 컨텍스트를 함께 전달하는 예외"""
    def __init__(self, requested: int, remaining: int):
        self.requested = requested
        self.remaining = remaining
        super().__init__(f"토큰 한도 초과! (요청: {requested}개, 잔여 한도: {remaining}개)")

class CodexClient:
    def __init__(self, daily_quota: int = 100):
       self.remaining_tokens = daily_quota
    def generate_code(self, prompt: str, estimated_tokens: int) -> str:
        if not prompt.strip():
              raise PromptEmptyError("프롬프트에 최소 1글자 이상의 명령어를 입력해주세요.")
        if estimated_tokens > self.remaining_tokens:
              raise TokenQuotaExceededError(estimated_tokens, self.remaining_tokens)
        self.remaining_tokens -= estimated_tokens
        return f"[생성 성공] '{prompt}' 코드 생성 완료 (남은 토큰: {self.remaining_tokens})"

client = CodexClient(daily_quota=50) ##CodexClient라는 객체를 만들어 client라는 변수에 할당

test_requests = [
                    ("클래스 리팩토링 코드 작성", 30),
                    (" ", 10),
                    ("대규모 프로젝트 전체 변환", 40),
                 ]
for prompt_text, tokens in test_requests:
    try:
        result = client.generate_code(prompt_text, tokens)
        print(result)
    except PromptEmptyError as e:
       print(f"[입력 검증 실패] {e}")
    except TokenQuotaExceededError as e:
       print(f"[쿼터 경보] {e} -> 기본 요금제를 업그레이드하거나 요청 길이를 줄이세요.")

# class PromptEmptyError(Exception):
#     pass

# prompt = ""
# try:
#     if not prompt.strip():
#        raise PromptEmptyError()

# except PromptEmptyError as e:
#     print("프롬프트는 반드시 제공되어야합니다")

# print("정상종료")

## 논리적으로 예외를 허용할수 없다 하면 에러를 발생 --> 처리하면됨
# -->강제로 해결 --> 위험해보이지만 가장안전 --> raise 키워드를 이용해 
#                                           세상에 존재하지 않는 예외를 상속받아서 발생시킴