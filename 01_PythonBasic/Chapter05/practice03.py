#5 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
def print_5xn(string):
        for s in range(0,len(string),5): # 0부터 string의 길이만큼 5개씩
            print(string[s:s+5])

string = input('문자를 입력하세요 : ')
print_5xn(string)


#6 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라.
# 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다
def calc_monthly_salary(annual_salary):

    salary = annual_salary / 12
    print(f'당신의 월급은 {int(salary)}만원입니다')

    #return salary

annual_salary = int(input('연봉을 입력하세요 : '))

calc_monthly_salary(annual_salary)
#print(f'당신의 월급은 {int(salary)}만원입니다')