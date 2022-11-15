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
vector = int(input("리스트를 입력하세요 : "))
#3
