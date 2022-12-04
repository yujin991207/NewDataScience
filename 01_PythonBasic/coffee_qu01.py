# 문제 : 돈을 200원 넣으면 100원이 부족하다는 메시지가 출력되게 하자.
coffee = 10

while True:
    if coffee == 0:
        print("죄송합니다 커피가 소진되었습니다.")
        break

    money = int(input('내실 돈을 입력하세요 : '))
    if money == 300:
        print('주문하신 커피 나왔습니다.')
        coffee -= 1
    elif money > 300:
        print(f'주문하신 커피 나왔습니다. 거스름돈 {money-300}원 입니다.')
        coffee -= 1
    else:
        print(f'돈이 {300-money}원 부족합니다. 돈을 반환합니다.')

