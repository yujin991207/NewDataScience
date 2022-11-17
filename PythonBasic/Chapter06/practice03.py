"""Q3] 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
즉 다음과 같이 동작해야 한다. (함수 override 사용할 것!)"""
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100: # 100이상이면 100출력
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
#cal.add(60) # 60 더하기
#cal.add(70)
cal.add(30)

print(cal.value) # 100 출력






