#7 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
def make_url(url):
    print(f'www.{url}.com')

url_input = input('url를 입력하세요 : ')
make_url(url_input)

#8
def input_ingredient():
    ingredient_list = []

    while True:
        ingredient = input('안녕하세요 원하시는 재료를 입력하세요 (종료 =>"엔터") : ')

        if ingredient == '': # 엔터시 종료
            print()
            return ingredient_list

        else:
            ingredient_list.append(ingredient) # 종료시 내가 입력했던 재료를 list에 추가

def make_sandwiches(ingredient_list):
        print('샌드위치를 만들겠습니다')

        for list in ingredient_list: # 내가 입력한 리스트를 다 입력할 때까지 for문 돌기
            print(f'{list}를 추가합니다')

        print('\n여기 주문하신 샌드위치 만들었습니다 맛있게 드세요\n')

while True:
    print('안녕하세요 저희 가게에 방문해주셔서 감사합니다. (1. 주문 2. 종료)')

    market_input = int(input('입력 : '))

    if market_input == 2:
        break

    ingredient_list = input_ingredient()

    make_sandwiches(ingredient_list)