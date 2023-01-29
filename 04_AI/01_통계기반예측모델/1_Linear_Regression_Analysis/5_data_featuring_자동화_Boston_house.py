# 통계 모델: 선형회귀 분석 (Linear Regression Analysis)

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())
print("결과 예측하기")
house = pd.read_csv('Boston_house.csv',sep=',',header=0)

match_dic={}
# CRIM: 범죄율
# INDUS: 비소매상업지역 면적 비율
# NOX: 일산화질소 농도
# RM: 주택당 방 수
# LSTAT: 인구 중 하위 계층 비율
# B: 인구 중 흑인 비율
# PTRATIO: 학생/교사 비율
# ZN: 25,000 평방피트를 초과 거주지역 비율
# CHAS: 찰스강의 경계에 위치한 경우는 1, 아니면 0
# AGE: 1940년 이전에 건축된 주택의 비율
# RAD: 방사형 고속도로까지의 거리
# DIS: 직업센터의 거리
# TAX: 재산세율
# Target: 주택가격
colums_list = ['CRIM','INDUS','NOX','RM','LSTAT','B','PTRATIO',
               'ZN','CHAS','AGE','RAD','DIS','TAX']

for num in range(1,15):
    # 몇개를 꺼낼것이냐
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        my_formula = 'Target ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=house).fit()
        dependent_variable = house['Target']
        # independent_variables = wine[wine.columns.difference(['quality','type','in_sample'])]
        independent_variables = house[list(tup)] # formula 에 들어간 columns만 골라서 고정 변수로 줌
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count=0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count+=1
        print('\n>> '+my_formula.replace('Target ~ ',''))
        print('>> match count=',match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(y_predicted_rounded)*100))
        match_dic['%s'%my_formula.replace('Target ~ ','')] = match_count/len(y_predicted_rounded)*100


# 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
# print(match_dic)

print("\n\n>>>독립변수 최적화 분석 결과<<<")
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
end = datetime.fromtimestamp(time.time())
print(f'분석 시작: {start}')
print(f'분석 종료: {end}')
print(f'총 분석 시간: {end-start}')