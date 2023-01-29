import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())
print("결과예측하기")

wine = pd.read_csv('white_winequality.csv', sep = ',', header = 0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic = {}
columns_list = ['alcohol','chlorides','citric_acid','density','fixed_acidity','free_sulfur_dioxide','pH',
               'residual_sugar','sulphates','total_sulfur_dioxide','volatile_acidity']

for num in range(1,12):
    combi_list = list(combinations(columns_list,num))

    for tup in combi_list:
        my_formula = 'quality ~ '

        for data in tup:
            my_formula += '%s + ' %data
        my_formula = my_formula.strip().rstrip('+')

        lm = ols(my_formula, data = wine).fit()
        dependent_variable = wine['quality']

        independent_variables = wine[list(tup)]
        y_predict = lm.predict(independent_variables)
        y_predict_round = [round(score) for score in y_predict]

        match_count = 0

        for index in range(len(y_predict_round)):
            if y_predict_round[index] == dependent_variable.values[index]:
                match_count += 1

        print('\n>> '+my_formula.replace('quality ~ ',''))
        print('>> match count = ',match_count)
        print(f'>> 정답률 : %.2f %%' %(match_count / len(y_predict_round) * 100))

        match_dic['%s' % my_formula.replace('quality ~ ','')] = match_count / len(y_predict_round) * 100

match_dic = sorted(match_dic.items(), key = operator.itemgetter(1), reverse = True)


print("\n\n>>>독립변수 최적화 분석 결과<<<")
print('총 조합 갯수: %d' %len(match_dic))
print("MAX 조합: %s >> %.2f %%" %(match_dic[0][0],match_dic[0][1]))

end = datetime.fromtimestamp(time.time())

print(f'분석 시작: {start}')
print(f'분석 종료: {end}')
print(f'총 분석 시간: {end-start}')
