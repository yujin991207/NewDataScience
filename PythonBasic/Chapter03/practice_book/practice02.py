#2
baggage = int(input('짐의 무게는 얼마입니까? '))

if baggage >= 10:
    price = (baggage // 10 * 10000) # 10의배수단위로 만원씩 증가
    print('수수료는 '+format(price,'3,d')+'원 입니다.')

else:
    print('수수료는 없습니다.')