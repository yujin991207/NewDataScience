t = (10,)
print(t)

t2 = (1,2,3,4,5,3)
print(t2)

print(t2[0], t2[1:4], t2[-1])

#t2[0] = 10 # 수정불가에러

for i in t2:
    print(i,end='')

print()

if 6 in t2:
    print("6 있음")
else:
    print("6 없음")