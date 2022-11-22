#3
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

