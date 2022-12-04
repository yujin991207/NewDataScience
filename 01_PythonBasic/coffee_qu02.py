"""
커피 키오스크 코드를 수정하는데 이번에는 돈과 커피의 개수를 받아 다음과 같이 결과를 출력하자.

돈을 입력하세요: 600
커피는 몇 잔 드릴까요? 2
커피 두 잔 나왔습니다."""

coffee = 10
print("커피 한 잔의 가격은 300원 입니다.")

while True:
    if coffee <= 0:
        print("커피가 품절되었습니다.")
        break

    cups = int(input("커피는 몇 잔 드릴까요? "))

    if cups > coffee: # 주문한 커피 갯수가 남아있는 커피보다 많으면
        print(f"커피가 {coffee}잔 남았습니다. 개수를 다시 지정해주세요.")
        continue
    print(f"내실 돈의 총 가격은 {cups * 300}원 입니다.")

    money = int(input("내실 돈을 입력하세요 : "))

    if money >= 300: # 넣은돈이 커피값과 같거나 크면
        if money - (cups * 300) != 0: # 넣은돈이 딱 맞을 경우
            print(f"거스름돈은 {money - (cups * 300)}원 입니다.")

        coffee -= cups
    else:
        print(f"돈이 {(cups * 300) - money}원이 부족합니다 돈을 반환합니다.")

