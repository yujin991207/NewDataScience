#4
a = [1,1,1,2,2,3,3,3,4,4,5]

a1 = set(a)
a2 = list(a1)
print(a2)

#aResult = []

#for result in a:
#    if result not in aResult:
#        aResult.append(result)

#print(aResult)

#5
shop = {'kim99':12000,
        'le66':11000,
        'han55':3000,
        'hong77':5000,
        'hwang33':18000}
num = 1

for key in shop:
    print(f"{num}. 아이디 : {key}, 마일리지 : {shop[key]}점")
    num += 1


#6
findId = 'han55'
shop[findId] = 5000

for id in shop:
    if findId == id:
        print(f"{findId}님의 마일리지가 {shop[findId]}점으로 수정되었습니다.")

#7
findId = 'jang88'
shop[findId] = 7000

print()
print(f"전체 딕셔너리 : {shop}")
print(f"{findId}님의 마일리지({shop[findId]}점)가 추가되었습니다.")

print()
#8
score = []

for id in shop:
    score.append(shop[id]) # score에 값저장

    result = max(score)

for id in shop:
    if shop[id] == result:
        maxId = id

print(f"{maxId}님의 {result}점이 가장 높은 점수 입니다.")

