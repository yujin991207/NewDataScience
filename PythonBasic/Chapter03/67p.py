import random
help(random)

help(random.random)

r = random.random()
print('r = ',r)

cnt = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.01:
        break
    else:
        cnt += 1

print(f'난수 개수 = {cnt}')