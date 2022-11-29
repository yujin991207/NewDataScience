#3 하나의 문자열를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_smile(x):
        print(f'{x}:D')
        return x

x = input('메시지 입력 : ')
print_with_smile(x)

#4 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라.
# 단 if 문을 사용해서 수를 비교하라.
def print_max(x,y,z):
    if x > y:
        max_num = x
    else:
        max_num = y

    if max_num < z:
        max_num = z

    print(f'세수 중 가장 큰 수는 {max_num}입니다')


max_number = list(map(int,input('세수를 입력해주세요 (예) 10 50 60 : ').split()))
print_max(max_number[0],max_number[1],max_number[1])



