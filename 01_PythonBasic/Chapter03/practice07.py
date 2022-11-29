# *******
freeticket = 3
memberticket = 5
count = 0
price = 0

while True:
    age = int(input("나이를 입력하세요 : "))

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

        if price != 0: # 요금이 무료가 아니면 count가 하나씩 올라가야한다
            count += 1
            #print(f'귀하는 {grade}등급이며 요금은 {price}원 입니다')
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

            # 티켓무료이벤트
            if (freeticket > 0 and count % 7 == 0):
                freeticket -= 1 # 하나씩차감
                print(f'축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. [잔여 무료 티켓 : {freeticket}장]')
            elif (memberticket > 0 and count % 4 == 0):
                memberticket -= 1
                print(f'축하합니다. 연간 회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. [잔여 할인 티켓 : {memberticket}장]')
        else:
            print(f'귀하는 {grade} 등급이며 요금은 무료입니다')



