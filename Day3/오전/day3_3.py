'''
상속(Inheritance)과 다형성(Polymorphism) — 거인의 어깨 위에서 코드 재사용하기!
비전 AI 모델과 거대언어모델(LLM)을 만들 때마다 모델 이름, 버전 기록, 
로그 출력 코드를 매번 복사·붙여넣기 한다면 유지보수가 불가능해집니다. 
상속(Inheritance)은 공통 기능을 부모 클래스(BaseAIModel)에 모아두고 자식 클래스가
물려받는 기술이며, 
다형성(Polymorphism)은 똑같은 model.predict(data) 버튼을 눌렀을 때 (실행했을때) 
비전 모델은 이미지를 분류하고 LLM은 문장을 요약하도록 동작하는 마법입니다.
동작할때 다양하게 하는것
super().__init__(...): 부모 클래스의 출생 신고서를 먼저 호출해 공통 속성(이름, 버전)을 
깔끔하게 세팅합니다.==> super() 상속받을 부모객체를 호출
메서드 오버라이딩(Method Overriding): 부모가 물려준 기본 predict() 메서드를 
자식 클래스가 자신의 전공 분야에 맞게 재정의(덮어쓰기)합니다.

'''

class BaseAIModel:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    def predict(self, input_data: str) -> str:
        return f"[{self.name} v{self.version}] 기본 추론: {input_data}"

class VisionClassifier(BaseAIModel):
    def __init__(self, name: str, version: str, resolution: str):
        super().__init__(name, version) # 부모 초기화 코드 재사용
        self.resolution = resolution

    def predict(self, input_data: str) -> str: # 다형성 오버라이딩
        return f"[Vision {self.name} ({self.resolution})] 이미지 '{input_data}' 분석 결과 ->'고양이 (확률 98.4%)'"

class TextSummarizerLLM(BaseAIModel):
    def __init__(self, name: str, version: str, max_tokens: int):
        super().__init__(name, version)
        self.max_tokens = max_tokens

    def predict(self, input_data: str) -> str: # 다형성 오버라이딩
       summary = input_data[:18] + "..." if len(input_data) > 18 else input_data
       return f"[LLM {self.name} (max={self.max_tokens})] 텍스트 요약 결과 -> '{summary}'"

    # 다형성의 위력: 서로 다른 모델 클래스들을 단일 for 루프로 일괄 실행!

pipeline: list[BaseAIModel] = [VisionClassifier("YOLO-KDT", "8.2", "640x640"),TextSummarizerLLM("Codex-Mini", "2.0", 512),]
# Pipeline 설명 

for model in pipeline:
    print(model.predict("실습 데이터 샘플 입력입니다")) ## 이런식으로 쓰는 것이 다형성 --> 재정의한다 (오버라이딩)

    
