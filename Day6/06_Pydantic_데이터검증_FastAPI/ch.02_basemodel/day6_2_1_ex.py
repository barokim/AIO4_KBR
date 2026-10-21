from pydantic import BaseModel, ValidationError

# TODO Book 모델의 필드를 정의하세요.
# title:str (필수), price:int (필수), in_stock:bool=True, note:str|None=None
class Book(BaseModel):
    # 수정: 필드는 함수가 아니라 Pydantic 모델 클래스 안에 선언해야 합니다.
    title : str
    price : int
    in_stock :bool = True
    note : str | None = None


def main() -> None:
    # 수정: TODO라는 이름 대신 모델 객체를 의미하는 book을 사용합니다.
    book = Book(title='파이썬 기초', price='19000')

    # 수정: model_dump()의 반환값을 변수에 저장하고 출력합니다.
    book_data = book.model_dump()
    print(book_data)

    # 수정: Pydantic이 문자열 가격을 int로 변환했는지 확인합니다.
    print(type(book.price).__name__)

    try:
        # 수정: title을 누락하여 필수 필드 검증 오류를 확인합니다.
        Book(price='19000')
    except ValidationError as e:
        # 수정: ValidationError의 위치와 오류 종류를 출력합니다.
        print('error',e)

if __name__ == '__main__':
    main()
