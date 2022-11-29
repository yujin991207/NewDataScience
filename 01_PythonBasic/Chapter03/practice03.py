while True:
    age=int(input('나이를 입력하세요 : '))

    if 19 <= age <= 65:
            price = 5000
    elif 14 <= age <= 18:
        price = 3000
    elif 4 <= age <= 13:
        price = 2000
    else:
        price = 0
    if price != 0:
        print(f'요금은 {price}원 입니다')
    else:
        print(f'요금은 무료입니다')