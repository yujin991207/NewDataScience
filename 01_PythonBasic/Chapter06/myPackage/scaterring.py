#평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt

#산술평균 함수
def Avg(data):
    avg = mean(data)
    return avg

#분산/표준편차 함수
def var_sd(data):
    avg = Avg(data)
    diff = [(d-avg) ** 2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var,sd