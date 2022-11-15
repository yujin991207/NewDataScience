#샌드위치문제
def input_ingredient():
    #재료추가
    ingredient_list = [] # 재료 입력값 저장

    while True:
        ingredient = input("재료를 입력하세요 (종료는'엔터'치세요) : ")

        # 재료를 입력하지않고 종료를 하고싶다면..
        if ingredient == '':
            print()
            return ingredient_list

        # 종료를 하지않고 계속 재료를 입력한다면..
        else:
            ingredient_list.append(ingredient)

def make_sandwich(ingredient_list):
    print("샌드위치를 만들겠습니다!")

    for list in ingredient_list:
        print(f'{list}를 추가합니다')

    print("\n여기 주문하신 샌드위치입니다 맛있게 드세요 d(^0^)b\n")


while True:
    print("안녕하세요 저희 가게에 방문해주셔서 감사합니다 (1.주문 2.종료)")

    select = int(input("입력 : "))

    if select == 2:
        break

    ingredient_list = input_ingredient()
    make_sandwich(ingredient_list)