"""05장: 중첩 모델, Enum, 복합 입력 검증."""
from enum import Enum
from pydantic import BaseModel, Field, ValidationError


class DeliveryMethod(str, Enum):
    STANDARD = 'standard'
    EXPRESS = 'express'

method = DeliveryMethod.STANDARD
print(method)
print(method.value)
print(method.name)
print(method == 'standard')
print(isinstance(method, str))

class Address(BaseModel):
    city: str
    street: str


class OrderItem(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(ge=1) 
    unit_price: int = Field(ge=0)


class Order(BaseModel):
    customer_name: str
    address: Address
    items: list[OrderItem] = Field(min_length=1)
    method: DeliveryMethod = DeliveryMethod.STANDARD

    @property    #get 
    def total(self) -> int:
        return sum(item.quantity * item.unit_price for item in self.items)


def main() -> None:
    raw = {
        'customer_name': '홍길동',
        'address': {'city': '서울', 'street': '세종대로 1'},
        'items': [{'product_id': 10, 'quantity': 2, 'unit_price': 12000}],
        'method': 'express',
    }
    order = Order.model_validate(raw)   
    #검증방법 => 딕셔너리 데이터를 검증 자기 타입 뿐만 아니라 딕셔너리 데이터 자체를 검증 하면서 객체를 만들어준다
    print('STEP 1 - 중첩 모델:', order.address.city, order.items[0].quantity)
    print('STEP 2 - 합계:', order.total)
    print('STEP 3 - 중첩 구조의 오류 위치')
    raw['items'][0]['quantity'] = 0
    try:
        Order.model_validate(raw)
    except ValidationError as error:
        print('오류 위치:', error.errors()[0]['loc'])   # quantity가 1이상이여야 하는데 0이므로 오류발생
    print('05장 성공')


if __name__ == '__main__':
    main()