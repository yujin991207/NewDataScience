su=5
dan=800

#print("su 주소 : ",id(su))
#print("dan 주소 : ",id(dan))

print(f'su 주소 : {id(su)}') # ****
print(f'dan 주소 : {id(dan)}')

totalprice=su*dan

#print("금액 = ",totalprice)
print(f'금액 = {totalprice}')

print("===============================")

#1
korean=80
english=75
math=90
science=95

#avg=(int(korean)+int(english)+int(math)+int(science))/4
avg2=(korean+english+math+science)/4

#print("홍길동 평균 점수 : ",avg)
print("홍길동 평균 점수 : ",avg2)