#1
baggage = int(input('짐의 무게는 얼마입니까? '))
#
# if baggage < 10:
#     print('수수료는 없습니다.')
#
# elif baggage >= 10:
#     print('수수료는 '+format(10000,'3,d')+'원 입니다.')

if baggage >= 10:
    print('수수료는 '+format(10000,'3,d')+'원 입니다.')

else:
    print('수수료는 없습니다.')