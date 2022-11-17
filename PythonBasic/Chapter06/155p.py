#생성자 이용 멤버변수 초기화
class multiply:
    #멤버변수
    x = y = 0

    #생성자 : 초기화
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

obj = multiply(10,20)
print(f'곱셈 = {obj.mul()}')

    #메서드 이용 멤버변수 초기화
class mutiply2:
    x = y = 0

    #생성자없음. => 기본 생성자 제공
    def __init__(self):
        pass

    def data(self,x,y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

obj = mutiply2()
obj.data(10,20)
print(f'곱셈 = {obj.mul()}')