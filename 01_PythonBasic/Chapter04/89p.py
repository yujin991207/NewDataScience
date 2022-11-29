x = [1,2,3,4]
y = [1.5, 2.5]

z = x + y
print(z)

x.extend(y) # x확장
print(x)

x.append(y)
print(x)

lst = [1,2,3,4]
result = lst * 2
print(result)

print(result)
result.sort()

result.sort(reverse=True)
print(result)

import random
r = []
for i in range(5):
    r.append(random.randint(1,5))

print(r) # 5,5,1,2,1

if 4 in r:
    print("있음")

else:
    print("없음")