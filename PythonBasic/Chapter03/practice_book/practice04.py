#4
tot=0
print("수열 = ",end = ' ')

for i in range(1,101):
    if i % 3 == 0 and i % 2 != 0:
        print(f"{i}",end = ' ')
        tot += i

print(f'\n누적합 = {tot}')


