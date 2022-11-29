"""Q1] 사칙 연산이 가능한 FourCal 클래스를 구현하시오
멤버 필드: first, second
멤버 함수: add(self), mul(self), sub(self), div(self), setdata(self, first, second),
생성자 __init__(self, first, second)
생성자, setdata()를 통하여 first, second 값을 지정할 수 있다.
"""

class FourCal:
    first = second = 0

    def __init__(self,first,second):
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        add = self.first + self.second
        return add

    def mul(self):
        mul = self.first * self.second
        return mul

    def sub(self):
        sub = self.first - self.second
        return sub

    def div(self):
        div = self.first / self.second
        return div


a = FourCal(0,0)
b = FourCal(3,8)
a.setdata(4,2)

print(a.add())
print(b.add())

print(a.div())

