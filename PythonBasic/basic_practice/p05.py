#5
dan = int(input('원하는 단을 입력하세요 : '))

def gugu(dan):
    for i in range(1,10):
        result = dan * i
        print(f'{result} \t',end = '')


gugu(dan)