class Car:
    #멤버변수
    cc = 0 #엔진
    door = 0 #문
    carType = None

    def __init__(self,cc,door,carType):
        #멤버변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType

    def display(self):
        print(f'자동차 %d cc이고 문짝은 %d개 타입은 %s 입니다.' %(self.cc,self.door,self.carType))

#객체생성
car1 = Car(2000,4,"승용차")
car2 = Car(3000,5,"SUV")

#멤버호출 : object.member()
car1.display() # car1 멤버 호출
car2.display() # car2 멤버 호출

