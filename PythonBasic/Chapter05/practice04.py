#7 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
def make_url(url):
    print(f'www.{url}.com')

url = input('url를 입력하세요 : ')
make_url(url)

#8
market = int(input('안녕하세요 저희 가게에 방문해 주셔서 감사합니다 (1.주문 2.종료) '))
ingredient_list = []


def input_ingredient():
    while True:
        ingredient = input('안녕하세요 원하시는 재료를 입력하세요 : ')

        if ingredient == ' ':
            print()
            return ingredient_list

        else:
            ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list):
        print('샌드위치를 만들겠습니다')

        for list in ingredient_list:
            print(f'{list}를 추가합니다')

        print('여기 주문하신 샌드위치 만들었습니다 맛있게 드세요')

        return ingredient_list

if market == 1:
        input_ingredient()
        make_sandwiches(ingredient_list)

elif market == 2:
        print('종료합니다.')