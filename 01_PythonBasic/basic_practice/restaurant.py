class Restaurant:
    # 멤버변수
    # restaurant_name = ""
    # cuisine_type = ""
    #
    # today_customer = 0 # 금일 서빙한 손님 수
    # number_served = 0 # 전체 누적 서빙 손님 수

    # 생성자
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.today_customer = 0
        self.number_served = 0

    def describe_restaurant(self):
        print(f'저희 레스토랑 명칭은 [{self.restaurant_name}] 이고 [{self.cuisine_type}] 전문점입니다.')

    def open_restaurant(self):
        print(f'저희 [{self.restaurant_name}] 레스토랑 오픈했습니다 어서오세요!')

    # 서빙한 고객 숫자 지정
    def reset_number_served(self):
        self.today_customer = 0 # 0으로 초기화

        print('0으로 초기화 됩니다.\n')

    # 서빙한 고객 숫자 늘림.
    def increment_number_served(self,number):
        self.today_customer += number # 숫자누적
        self.number_served += number

        print(f'손님 {number}명 들어오셨습니다. 자리를 안내해 드리겠습니다\n')

    # 서빙한 고객 숫자 확인
    def check_customer_number(self):
        print(f'오늘 총 {self.today_customer}명 손님께서 오셨습니다 (전체 누적 손님 : {self.number_served}명)\n')

    # 소멸자
    def __del__(self):
        print(f'{self.restaurant_name} 레스토랑 문닫습니다.')
        with open("file/고객서빙현황로그.txt", mode ='a', encoding ='utf-8') as customer_f:
            customer_f.write("%d\t %d\n" %(self.today_customer,self.number_served))



rest_name, rest_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split(" ")
opening_rest = Restaurant(rest_name, rest_type)
opening_rest.describe_restaurant()
is_open = (input("레스토랑을 오픈하시겠습니까? (yes ('y') / no ('n')): ")).lower()

if is_open[0] == 'y':
    input_num = 0
    opening_rest.open_restaurant()
    while True:
        input_num = input("어서오세요. 몇명이십니까? (초기화:0, 입력종료:-1, 누적고객확인:p) : ")
        if input_num == 'p':
            opening_rest.check_customer_number()
        elif int(input_num) == 0:
            opening_rest.reset_number_served()
        elif int(input_num) == -1:
            break
        elif int(input_num) > 0:
            opening_rest.increment_number_served(int(input_num))

del opening_rest











