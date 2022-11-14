count = 0
freeticket = 3
memberticket = 5

while True:
    price = 0
    age = int(input('나이를 입력하세요 : '))
    if(age >= 19 and age <= 65):
        grade = '성인'
        price = 5000
    elif (age>=14 and age<=18):
        grade = '청소년'
        price = 3000
    elif (age >= 4 and age <= 13):
        grade = '어린이'
        price = 2000
    elif (age >= 66):
        grade = '노인'
    elif (age <= 3 and age >= 0):
        grade = '유아'
    else:
        print('다시 입력하세요')
        continue

    if price != 0:
        count += 1
        print(f'귀하는 {grade} 등급이며 요금은 {price}입니다')

        payWay = int(input("요금 유형을 선택하세요 (1: 현금, 2: 공원 전용 신용 카드) "))

        if payWay == 1:
            pay = int(input('요금을 입력하세요 : '))
            if pay > price:
                print(f'"감사합니다. 티컷을 발행하고 거스름돈 {pay-price}원을 반환 합니다."\n')
            elif pay < price:
                print(f'"{price-pay}가 모자랍니다. 입력 하신 {pay}원을 반환합니다."\n')
            else:
                print(f'"감사합니다. 티컷을 발행합니다."\n')
        elif payWay == 2:
            price * 0.9
            if (age >= 60 and age <= 65):
                price * 0.95
            print(f'{int(price)}원 결제되었습니다. 티켓을 발행합니다\n')

        if (freeticket > 0 and count % 7 == 0):
            freeticket -= 1
            print(f'축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓: {freeticket}장\n')
        elif (memberticket > 0 and count % 4 == 0):
            memberticket -= 1
            print(f'축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓: {memberticket}장\n')
    else:
        print(f'귀하는 {grade} 등급이며 요금은 무료입니다')