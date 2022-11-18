#6
dan = input('원하는 단을 입력하세요 : ')

# 모든 구구단 출력
def all_gugu():
    for i in range(2,10):
        for j in range(1,10):
            result = i * j
            print(f'{int(result)} \t',end ='')
        print()

# 내가 원하는 단만 출력
def gugu(dan):
    for i in range(1,10):
        result = int(dan) * i
        print(f'{result} \t',end = '')


if dan == 'all':
    all_gugu()
else:
    gugu(dan)