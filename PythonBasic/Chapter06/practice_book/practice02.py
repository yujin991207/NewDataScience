#2
from statistics import mean
from math import sqrt

x = [5 , 9 , 1 , 7 , 4 , 6]

# 산포도 클래스
class Scattering:
    # 생성자
    def __init__(self,x):
        self.x = x

    # 메서드 : 분산
    def var_func(self):
        avg = mean(x)
        diff = [(d - avg) ** 2 for d in x]
        var = sum(diff) / (len(x) - 1)

        return var

    # 메서드 : 표준편차
    def std_func(self):
        avg = mean(x)
        diff = [(d - avg) ** 2 for d in x]
        var = sum(diff) / (len(x) - 1)
        sd = sqrt(var)

        return sd

s = Scattering(x)
var = s.var_func()
print(f'분산 : {var}')

std = s.std_func()
print(f'표준편차 : {std}')