# 교과서 1번
def StarCount(height):

    return height

height = int(input('height : '))
print('stars 개수 : %d'%StarCount(height))

#1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(number):
    if number % 2 == 0:
        #print('입력하신 수는 짝수입니다')
        return '짝수'
    else:
        #print('입력하신 수는 홀수입니다')
        return '홀수'
    #return x

number = 10
#is_odd(number)
print(f'{number}은 {is_odd(number)}입니다')


#2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.) split()함수 이용...

