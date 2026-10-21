"""05장 학생 실습: 강좌와 수강생의 중첩 관계 모델링.

demo.py의 주문 예제와 비교하면 다음과 같습니다.
- OrderItem → Learner: 리스트 안에 들어가는 개별 데이터를 검증합니다.
- Order → Course: 다른 모델을 포함하는 중첩 모델입니다.
- items → learners: 딕셔너리 목록을 모델 객체 목록으로 변환합니다.

주문 예제의 DeliveryMethod(str, Enum)는 배송 방법을 제한합니다.
STANDARD의 value는 'standard', name은 'STANDARD'입니다.
str을 함께 상속하므로 문자열과 비교하거나 isinstance(method, str)로
확인할 수 있고, 모델 검증 시 'express'는 해당 Enum 멤버로 변환됩니다.
이 실습에서는 정해진 선택지가 필요한 필드가 없어 Enum은 사용하지 않습니다.
"""

from pydantic import BaseModel, Field, ValidationError


class Learner(BaseModel):
    """수강생 한 명의 이름과 점수를 검증합니다."""

    name: str
    # ge: 이상, le: 이하. 숫자의 상한은 max_length가 아니라 le로 지정합니다.
    score: int = Field(ge=0, le=100)


class Course(BaseModel):
    """강좌 하나에 여러 수강생이 속하는 중첩 모델입니다."""

    title: str
    # 리스트 원소마다 Learner의 필드 조건도 함께 검증합니다.
    # min_length는 리스트 길이를 제한하므로 수강생이 최소 한 명 필요합니다.
    learners: list[Learner] = Field(min_length=1)

    @property
    def average_score(self) -> float:
        """주문의 total처럼 저장된 데이터로부터 값을 계산합니다."""
        # @property 덕분에 average_score() 대신 average_score로 접근합니다.
        # 검증을 통과한 learners는 비어 있지 않으므로 평균을 계산할 수 있습니다.
        return sum(learner.score for learner in self.learners) / len(self.learners)


def main() -> None:
    # Course의 필드 이름에 맞춰 딕셔너리를 구성합니다.
    # learners는 딕셔너리 두 개를 담은 리스트입니다.
    raw = {
        'title': 'AI_프로그래밍',
        'learners': [
            {'name': '홍길동', 'score': 50},
            {'name': '김제동', 'score': 70},
        ],
    }

    # model_validate는 입력의 타입과 Field 조건을 검사하고 객체를 만듭니다.
    # 내부 딕셔너리도 Learner 객체로 변환되어 점(.)으로 필드에 접근합니다.
    # 기본 설정에서는 가능한 타입 변환도 수행합니다(예: 점수 '50' → 50).
    course = Course.model_validate(raw)
    print('STEP 1 - 강좌:', course.title)
    print('STEP 2 - 중첩 모델:', course.learners[0].name, course.learners[0].score)
    print('STEP 3 - 평균 점수:', course.average_score)  # 60.0

    # 원본 딕셔너리를 바꾼 뒤 다시 검증하여 잘못된 점수를 확인합니다.
    # 이미 생성된 course의 점수는 이 딕셔너리 수정으로 바뀌지 않습니다.
    raw['learners'][0]['score'] = 101
    try:
        Course.model_validate(raw)
    except ValidationError as error:
        # loc는 오류가 발생한 경로입니다.
        # ('learners', 0, 'score'): 첫 번째 수강생의 score 필드가 잘못되었습니다.
        print('STEP 4 - 오류 위치:', error.errors()[0]['loc'])
        print('오류 원인:', error.errors()[0]['msg'])

    # 점수 검증과 별개로, 빈 수강생 목록도 허용되지 않습니다.
    try:
        Course.model_validate({'title': 'AI_프로그래밍', 'learners': []})
    except ValidationError as error:
        print('STEP 5 - 빈 목록 오류 위치:', error.errors()[0]['loc'])
        print('오류 원인:', error.errors()[0]['msg'])

    print('05장 성공')


if __name__ == '__main__':
    # 이 파일을 직접 실행할 때만 main()을 호출합니다.
    main()
