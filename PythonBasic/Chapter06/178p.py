#방법1. 모듈추가
import PythonBasic.Chapter06.myPackage.scaterring
data = [1 , 3 , 1.5 , 2 , 1 , 3.2]

#scaterring.py => 산술평균 함수 호출
print(f'평균 : {PythonBasic.Chapter06.myPackage.scaterring.Avg(data)}')

#scaterring.py => 분산과 표준편차 함수 호출
var,sd = PythonBasic.Chapter06.myPackage.scaterring.var_sd(data)
print(f'분산 : {var}')
print(f'표준편차 : {sd}')

#======================================================
#방법2. 모듈추가 (방법1보다 간단하다)
# from 상위패키지명.하위패키지명.모듈명 import 함수명
from PythonBasic.Chapter06.myPackage.scaterring import Avg,var_sd

print(f'평균 : {Avg(data)}')

var,sd = var_sd(data)
print(f'분산 : {var}')
print(f'표준편차 : {sd}')


