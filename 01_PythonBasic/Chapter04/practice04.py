#4
a = [1,1,1,2,2,3,3,3,4,4,5]

a1 = set(a) # list => set
a2 = list(a1) # set => list
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
#아이디(키)를 찾아서 마일리지(값) 수정
findId = 'han55'
shop[findId] = 5000

for id in shop:
    if findId == id:
        print(f"{findId}님의 마일리지가 {shop[findId]}점으로 수정되었습니다.")

#7
# 추가
addId = 'jang88'
shop[addId] = 7000

print()
print(f"전체 딕셔너리 : {shop}")
print(f"{addId}님의 마일리지({shop[addId]}점)가 추가되었습니다.")

print()
#8
score = []

for id in shop:
    score.append(shop[id]) # score에 값저장

    result = max(score) # score에 있는 값 중에 가장 큰값

for id in shop:
    if shop[id] == result:
        max_id = id

print(f"{max_id}님의 {result}점이 가장 높은 점수 입니다.")

