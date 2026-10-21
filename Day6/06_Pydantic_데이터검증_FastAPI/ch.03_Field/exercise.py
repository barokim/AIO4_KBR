from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    title: str = Field(min_length=2, max_length=60)
    price: int = Field(ge=0)
    stock: int = Field(default=0,ge=0)
    SKUcode: str = Field(pattern=r"SKU-[0-9]{4}$")


def main() -> None:
    # price와 stock은 기본값이 없는 필수 필드이므로 반드시 값을 전달해야 합니다.
    product1 = Product(
        title="전자제품",
        price=120000,
        stock=10,
        SKUcode="SKU-0002",
    )
    print("첫 번째 검증 성공:", product1.model_dump())

    invalid_cases = [
        {'title': 'A'},
        {'title': 'A' * 61},
        {'price': 0},
        {'stock': -1},
        {'sku': 'SKU-001'},
    ]
    
    for changes in invalid_cases:
        data = product.model_dump()
        data.update(changes)

    try:
        # price와 stock을 생략했으므로 ValidationError가 발생합니다.
        product2 = Product(title="노트북", SKUcode="SKU-0005")
        print("두 번째 검증 성공:", product2.model_dump())
    except ValidationError as e:
        # 검증에 실패하면 product2 객체가 만들어지지 않습니다.
        # 따라서 product2.model_dump()가 아니라 오류 객체를 출력해야 합니다.
        print("두 번째 검증 실패:", e)


if __name__ == "__main__":
    main()
