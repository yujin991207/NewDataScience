# 다형성
# 부모클래스
class Flight:
    # 부모 원형 함수
    def fly(self):
        print('날다, fly 원형 메서드')


# 자식클래스 : 비행기
class Airplane(Flight):
    def fly(self):
        print('비행기가 날다.')

# 자식클래스 : 새
class Bird(Flight):
    def fly(self):
        print('새가 날다.')

# 자식클래스 : 종이비행기
class paperAirplane(Flight):
    def fly(self):
        print('종이비행기가 날다.')

# 객체생성
flight = Flight() # 부모클래스 객체
air = Airplane() # 자식1클래스 객체
bird = Bird() # 자식2클래스 객체
paper = paperAirplane() # 자식3클래스 객체

flight.fly()

# 상황에 따라서 flight.fly()함수호출이 달라진다
# air할당
flight = air
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()