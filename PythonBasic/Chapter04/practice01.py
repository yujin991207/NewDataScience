#1
lst = [10,1,5,2]

result1 = lst * 2
print(f"단계1 : {result1}")

first = result1[0] * 2
#print(first)
result1.append(first)
print(f"단계2 : {result1}")

result3 = result1[1::2]
print(f"단계3 : {result3}")

#2
vector = int(input("vector의 수 : "))
lst = []

for i in range(vector):
    lst.append(i)
    print(i)

print(f'vector 크기 : {len(lst)}')

#3
if i in lst:
    print('yes')
else:
    print('no')
