# 교과서 1번
baggage=int(input("짐의 무게는 얼마입니까? "))

if baggage >= 10:
    print("수수료는 "+format(10000,'3,d')+"입니다")

else:
    print("수수료는 없습니다.")

#========================================

# 교과서 2번
baggage=int(input("짐의 무게는 얼마입니까? "))

if baggage >= 10:
     price = (baggage//10) * 10000
     print("수수료는 "+format(price,'3,d')+"입니다")

else:
    print("수수료는 없습니다.")

#=======================================

# 교과서 3번
import random

print('== 숫자 맞추기 게임 ==')
com = random.randint(1,10) # 난수

while True:
    my = int(input('예상 숫자를 입력하세요 : '))

    if my == com:
        print('숫자를 맞췄습니다')
        break

    elif my < com:
        print('더 큰 수 입력하세요')

    else:
        print('더 작은 수 입력하세요')
