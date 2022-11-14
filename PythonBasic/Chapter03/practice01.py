#1
for num in range(1,101):
    print(num)

#=======================================

#2
cnt = tot = 0

while cnt < 1000:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt # 누적

print("1~1000까지의 자연수 중 3의 배수의 합 = %d" %tot)

#==========================================

#3
aClass = [70,60,55,75,95,90,80,80,85,100]
sum = 0
for aClass2 in aClass:
    sum += aClass2
    avg = sum/len(aClass)

print(f'a학급의 평균 점수는? {avg} 입니다')



