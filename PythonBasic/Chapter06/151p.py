# 함수정의
def calc_func(a,b): #외부함수
    #변수선언
    x=a
    y=b

    def plus(): #내부함수
        p = x + y
        return p

    def minus(): #내부함수
        m = x - y
        return m
    return plus,minus

p,m = calc_func(10,20)
print('plus = ',p())
print('minus = ',m())

#=====================================================

# 클래스정의
class calc_class:
    x = y = 0 #클래스변수

    #생성자
    def __init__(self,a,b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10,20) #동일한 class이름

print('plus = ',obj.plus())
print('minus = ',obj.minus())



