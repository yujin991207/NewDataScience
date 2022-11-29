"""[레스토랑 ver1]
Restaurant 클래스를 만드시오.
Restaurant의 __init__(name,type) 메서드는 restaurant_name과 cuisine_type 두 가지 속성을 저장해야 한다.
restaurant_name, cuisine_type은 클래스의 멤버 변수로 저장한다.
이들 정보를 출력하는 describe_restaurant() 메서드와 레스토랑이 열렸다는 메시지를 출력하는 open_restaurant()를 만드세요.
describe_restaurant()출력
"저희 레스토랑 명칭은 [restaurant_name] 이고 [cuisine_type] 전문점입니다."
open_restaurant() 출력
"저희 [restaurant_name] 레스토랑 오픈했습니다. 어서오세요."

- 클래스에서 restaurant 인스턴스를 만드시오. 두 속성을 각각 출력(print함수)하기위해 메서드를 모두 호출하시오.

프로그램 실행예)

레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : 띵호화 중식 <= input함수 사용

저희 레스토랑 명칭은 '띵호화'이고 중식 전문점입니다.  <= describe_restaurant() 함수에서 처리
저희 띵호화 레스토랑이 오픈했습니다.                   <= open_restaurant() 함수에서 처리
"""
class Restaurant:
    # 멤버변수
    restaurant_name = ""
    cuisine_type = ""

    # 생성자
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f'저희 레스토랑 명칭은 [{self.restaurant_name}] 이고, [{self.cuisine_type}] 전문점입니다.')

    def open_restaurant(self):
        print(f'저희 [{self.restaurant_name}] 레스토랑 오픈했습니다. 어서오세요.')


restaurant_select = input('레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ')
restaurant_select = restaurant_select.split()

r = Restaurant(restaurant_select[0],restaurant_select[1])
r.describe_restaurant()
r.open_restaurant()




