"""
문제. 키오스크 프로그램의 메뉴에 아메리카노, 카페라떼, 모카를 넣자. 아메리카노와 카페라떼는 각각 주문을 받을 수 있도록 코드를 수정하자.
"""

print("안녕하세요 커피 메뉴를 선택하세요\n1. 아메리카노[1500원] 2. 카페라떼[2500원] 3. 카페모카[2800원]")

americano = 10
latte = 10
mocha = 10

while True:
    select = int(input("주문하시겠습니까? 메뉴를 골라주세요. "))

    price = 0
    cups = 0

    if select == 1:
        price = 1500
        print("아메리카노를 선택하셨습니다")

        cups = int(input("몇 잔 주문하시겠습니까? "))

        if cups > americano:
            print("죄송합니다 주문량에 비해 아메리카노가 부족합니다.")
            print(f"현재 주문 가능한 수량은 {americano}잔 입니다.")

            cups = int(input("몇 잔 주문하시겠습니까? "))

    if select == 2:
        price = 2500
        print("카페라떼를 선택하셨습니다")

        cups = int(input("몇 잔 주문하시겠습니까? "))

        if cups > latte:
            print("죄송합니다 주문량에 비해 카페라떼가 부족합니다.")
            print(f"현재 주문 가능한 수량은 {latte}잔 입니다.")

            cups = int(input("몇 잔 주문하시겠습니까? "))

    if select == 3:
        price = 2800
        print("카페모카를 선택하셨습니다")

        cups = int(input("몇 잔 주문하시겠습니까? "))

        if cups > latte:
            print("죄송합니다 주문량에 비해 카페모카가 부족합니다.")
            print(f"현재 주문 가능한 수량은 {mocha}잔 입니다.")

            cups = int(input("몇 잔 주문하시겠습니까? "))

    print(f"결제하실 금액은 {cups * price}원 입니다.")