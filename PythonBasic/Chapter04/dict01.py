shop_customer = {'kim99':12000,
                 'lee66':11000,
                 'han55':3000,
                 'hong77':5000,
                 'hwang33':18000}

num = 1

# dict출력
for key in shop_customer:
    print(f'{num}. 아이디 : {key} 마일리지 : {shop_customer[key]}점')

    num += 1

print()

# 값수정
findId = 'han55'
shop_customer[findId] = 5000

print(f'{findId}님의 마일리지가 {shop_customer[findId]}점으로 수정되었습니다.')

print()

# 값추가
addId = 'jang88'
shop_customer[addId] = 7000

print(f'{addId}님의 마일리지({shop_customer[addId]}점)가 추가되었습니다.')
print()

print(f'{shop_customer}')


score = []
for id in shop_customer:
    score.append(shop_customer[id])

    max_result = max(score) # 마일리지가 가장 큰값
    min_result = min(score) # 마일리지가 가장 작은값

for id in shop_customer:
    if shop_customer[id] == max_result:
        max_id = id
    elif shop_customer[id] == min_result:
        min_id = id

print()
print(f'{max_id}님의 {max_result}점이 가장 높은 점수입니다.')
print(f'{min_id}님의 {min_result}점이 가장 낲은 점수입니다.')


