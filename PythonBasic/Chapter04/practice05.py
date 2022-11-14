#9
temperature = {'월':25.5,
               '화':28.3,
               '수':33.2,
               '목':32.1,
               '금':17.3,
               '토':35.3,
               '일':33.3}

LINE_NUM = 54
print('-' * LINE_NUM)

for day in temperature:
    print(f'  {day}\t', end='')

print()
print('-' * LINE_NUM)

for day in temperature:
    print(f' {temperature[day]}\t', end='')

print()
print('-' * LINE_NUM)

#10
temperature_list = []

for day in temperature:
    temperature_list.append(temperature[day]) # 하나씩 값을 꺼내어 저장
    result = min(temperature_list)

print("가장 낮은 최고 기온 : %.1f ℃" %result)

#11
result = []

for day in temperature:
    if temperature[day] >= 30:
        result.append(day)
print("기온이 30℃ 이상인 요일 : ",end='')

print(",".join(result))

#12
sum = 0

for day in temperature:
    sum += temperature[day]
    result = sum / len(temperature)

print("일주일간 최고 기온의 평균 : %.1f ℃" %result)