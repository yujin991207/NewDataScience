# 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1()

# 인수가 있는 함수
def userFunc2(x,y):
    print('userFunc2')
    z = x + y

    print(f'z = {z}')

userFunc2(20,30)

# return 있는 함수
def userFun3(x,y):
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div # 한개의 튜플리턴

x = int(input('x를 입력하세요 : '))
y = int(input('y를 입력하세요 : '))

t,s,m,d = userFun3(x,y)
print(f'tot = {t}')
print(f'sub = {s}')
print(f'mul = {m}')
print(f'div = {d}')
