#1
def my_div(num1,num2):
    try:
        div = num1 / num2
        quotient = num1 // num2
        rest = num1 % num2

        print(div)
        print(rest)
        print(quotient)

        return div,rest,quotient

    except Exception as e:
        if num2 == 0:
            print(e)


num1 = int(input('첫번째 수를 입력하세요 : '))
num2 = int(input('두번째 수를 입력하세요 : '))
my_div(num1,num2)