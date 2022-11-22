while True:
    age = int(input("나이를 입력하세요 : "))
    grade = ""
    price = ""

    if age < 0:
        print("다시 입력하세요")
        quit()

    # elif 0 <= age <= 3:
    #    grade = "유아"
    #    price = "무료"

    elif 4 <= age <= 13:
        grade = "어린이"
        price = 2000

    elif 14 <= age <= 18:
        grade = "청소년"
        price = 3000

    elif 19 <= age <= 65:
        grade = "성인"
        price = 5000

    else:
       price = 0

    if price == 0:
        if age >= 66:
            grade = "노인"
            print(f"귀하는 {grade}등급이며 요금은 무료입니다")

        elif 0 <= age <= 3:
            grade = "유아"
            print(f"귀하는 {grade}등급이며 요금은 무료입니다")

    else:
        print(f"귀하는 {grade}등급이며 요금은 {price}원입니다.")

        priceWay = int(input("요금 유형을 선택하세요(1.현금 2.공원전용신용카드) : "))

        if priceWay == 1:
            myprice = int(input("요금을 입력하세요 : "))

            if myprice == price:
                    print("감사합니다. 티켓을 발행합니다")

            elif myprice < price:
                change = price - myprice
                print(f"{change}원이 모자랍니다 입력하신 {myprice}원 반환합니다.")

            elif myprice > price:
                change = myprice - price
                print(f"감사합니다 티켓을 발행하고 거스름돈 {change}원을 반환합니다")

        elif priceWay == 2:
            price *= 0.9 # 카드결제이기때문에 요금을 입력하지않고 바로 출력되기때문에 price를 사용

            if 60 <= age <= 65:
                price *= 0.95
            print(f"{int(price)}원 결제되었습니다. 티켓을 발행합니다")