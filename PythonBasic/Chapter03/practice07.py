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
    if price != 0:
        print(f"귀하는 {grade}등급이며 요금은 {price}원입니다.")

    else:
        if age >= 66:
            grade = "노인"
            #print(f"귀하는 {grade}등급이며 요금은 무료입니다")

        elif 0 <= age <= 3:
            grade = "유아"
            #print(f"귀하는 {grade}등급이며 요금은 무료입니다")

    if price == 0:
        print(f"귀하는 {grade}등급이며 요금은 무료입니다")

    else:
        print("감사합니다 티켓을 발행합니다.")

        myprice = int(input("요금을 입력하세요 : "))

        if myprice > price:
            change = myprice - price
            print("감사합니다 티켓을 발행하고 거스름돈 " + format(change,'3,d')+"원을 반환 합니다")

        elif myprice < price:
            change2 = price - myprice
            print(format(change2,'3,d')+"원이 모자랍니다 입력하신 " +format(myprice,'3,d')+"원을 반환합니다")
