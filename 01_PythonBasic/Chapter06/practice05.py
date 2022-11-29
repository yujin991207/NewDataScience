class Restaurant:
    # 멤버변수
    restaurant_name = ""
    cuisine_type = ""

    # 생성자
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # 메서드
    def describe_restaurant(self):
        print(f'저희 레스토랑 명칭은 [{self.restaurant_name}] 이고 [{self.cuisine_type}] 전문점입니다.')

    def open_restaurant(self):
        print(f'저희 [{self.restaurant_name}] 레스토랑 오픈했습니다. 어서오세요!')

    def __del__(self):
        print(f'[{self.restaurant_name}] 레스토랑 문닫습니다.')


restaurant = []

for i in range(3):
    restaurant_select = input('레스토랑 이름과 요리 종류를 선택하세요 (공백으로 구분) : ')
    restaurant_select = restaurant_select.split()  # 공백으로 구분

    restaurant.append(Restaurant(restaurant_select[0],restaurant_select[1]))
    restaurant[i].describe_restaurant()
    restaurant[i].open_restaurant()
    print('\n')

print('저녁 10시가 되었습니다.')