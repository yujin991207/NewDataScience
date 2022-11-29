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
            print(f"귀하는 {grade}등급이며 요금은 무료입니다")

        elif 0 <= age <= 3:
            grade = "유아"
            print(f"귀하는 {grade}등급이며 요금은 무료입니다")



