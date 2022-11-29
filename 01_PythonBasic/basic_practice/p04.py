#4
import random

lotto = []
#lotto_num = random.randint(1,45) # 1~45
index = 0

while index < 6: # 0~5
#for number in range(6):
    lotto_num = random.randint(1,46)
    if lotto_num in lotto: # 숫자가있으면
        continue
    else:
        lotto.append(lotto_num)
        index += 1

print(f'이번주 로또번호 {lotto}')
