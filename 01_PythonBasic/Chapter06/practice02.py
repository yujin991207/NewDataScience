#2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

# 자식클래스
class UpgradeCalculator(Calculator): # 상속
    def minus(self,val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력



