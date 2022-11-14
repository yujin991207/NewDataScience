#4
a = [1,1,1,2,2,3,3,3,4,4,5]
aResult = []

for result in a:
    if result not in aResult:
        aResult.append(result)

print(aResult)


#5
shop = {'kim99':12000,
        'le66':11000,
        'han55':3000,
        'hong77':5000,
        'hwang33':18000}
num = 1

for k in shop:
    print(f"{num}. 아이디 : {k} 마일리지 : {shop[k]}점")
    num += 1


#6
TARKET_ID = 'han55'
shop[TARKET_ID] = 5000

for id in shop:
    if TARKET_ID == id:
        print(f"{TARKET_ID}님의 마일리지가 {shop[TARKET_ID]}점으로 수정되었습니다.")

#7
TARKET_ID = 'jang88'
shop[TARKET_ID] = 7000

print()
print(f"전체 딕셔너리 : {shop}")
print(f"{TARKET_ID}님의 마일리지({shop[TARKET_ID]}점)가 추가되었습니다.")

print()
#8
score = []

for id in shop:
    score.append(shop[id]) # score에 값저장

    result = max(score)

for id in shop:
    if shop[id] == result:
        max_id = id

print(f"{max_id}님의 {result}점이 가장 높은 점수 입니다.")

