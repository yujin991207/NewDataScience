#1
#for number in range(1,101):
#    print(number)
#===================================================
#2
# cnt = total = 0
# while cnt < 1000:
#     cnt += 1 # 하나씩 카운트가 올라간다
#     if cnt % 3 == 0:
#         total += cnt # 누적합
#
# print(f'1부터 1000까지의 자연수 중 3의 배수의 총 합 : {total}')
#==================================================================
#3
# aClasses = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# sum = 0
#
# for aClass in aClasses:
#     sum += aClass
#     avg = sum / len(aClasses)
#
# print(f'A학급의 평균 점수는 {int(avg)}점 입니다.')
#================================================================
#4
# for i in range(0,6):
#     for j in range(i+1):
#         print("*",end = '')
#     print()
# 공원 요금 계산
free_ticket = 3
member_ticket = 5
count = 0

while True:
    age = int(input('나이를 입력하세요 : '))
    price = 0

    if 4 <= age <= 13:
        grade = "어린이"
        price = 2000

    elif 14 <= age <= 18:
        grade = "청소년"
        price = 3000

    elif 19 <= age <= 65:
        grade = "성인"
        price = 5000

    elif 0 <= age <= 3:
        grade = "유아"

    elif age >= 66:
        grade = "노인"

    else:
        print('다시 입력하세요.')
        continue

    if price != 0:
        print(f'귀하는 {grade}등급이며 요금은 {price}원 입니다.')
        count += 1

        pay_select = int(input('요금 유형을 선택하세요 (1.현금 2.공원전용신용카드) '))

        if pay_select == 1:
            pay = int(input('요금을 입력하세요 : '))

            if price > pay:
                print(f'{price-pay}원이 모자랍니다. 입력하신 {pay}원을 반환합니다')

            elif price == pay:
                print('감사합니다 티켓을 발행합니다.')

            elif price < pay:
                print(f'감사합니다 티켓을 발행하고 거스름돈 {pay-price}원을 반환합니다')

        elif pay_select == 2:
            price *= 0.9 # 카드 결제 고객은 모두다 할인
            if 60 <= age <= 65:
                price *= 0.95

            print(f'{int(price)}원 결제되었습니다 티켓을 발행합니다.')

        # 티켓 당첨 이벤트
        if free_ticket > 0 and count % 7 == 0:
            free_ticket -= 1
            print(f'축하합니다 1주년 이벤트에 당첨되었습니다 여기 무료 티켓을 발행합니다. 잔여무료티켓 [{free_ticket}장]')

        elif member_ticket > 0 and count % 4 == 0:
            member_ticket -= 1
            print(f'축하합니다 연간회원권 구매이벤트에 당첨되었습니다 연간 회원 할인 티켓을 발행합니다 잔여할인티켓 [{member_ticket}장]')

    else:
        print(f'귀하는 {grade}등급이며 요금은 무료입니다.')




