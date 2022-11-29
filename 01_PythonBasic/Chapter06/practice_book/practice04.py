#3
class Employee:
    name = None
    pay = 0

    def __init__(self,name):
        self.name = name

    #def pay_calc(self):
     #   pass

# 자식클래스 : 정규직
class Permanent(Employee):
    def __init__(self,name,base,bonus):
        super().__init__(name) # 부모 생성자 호출
        self.pay = base + bonus
#    def perpay_calc(self,name,base,bonus):
#        super().__init__(name) # 부모 생성자 호출
#        per_pay = base + bonus

#        print("="*30)
#        print('고용형태 : 정규직')
#        print(f'이름 : {name}\n 급여 : '+format(per_pay,'3,d'))

#        return per_pay

# 자식클래스 : 임시직
class Temporary(Employee):
    def __init__(self,name,tpay,time):
        super().__init__(name)
        self.pay = tpay * time
#    def tempay_clac(self,name,tpay,time):
#        super().__init__(name)
#        temp_pay = tpay * time

#        return temp_pay

while True:
    empType = input("고용형태 선택 (정규직<p> 임시직<t>) : ")
    emp = Employee(empType)

    if empType == 'p':
            name = input('이름 : ')
            base = int(input('기본급 : '))
            bonus = int(input('상여금 : '))

            p = Permanent(name,base,bonus) # 정규직(자식)클래스 호출

            print()
            print('=' * 30)
            print('고용형태 : 정규직')
            print(f'이름 : {p.name}')
            print(f'급여 : ' + format(p.pay,'3,d') + '만원')
            print('=' * 30)
            print()

    elif empType == 't':
            name = input('이름 : ')
            time = int(input('작업시간 : '))
            tpay = int(input('시급 : '))

            t = Temporary(name,time,tpay) # 임시직(자식)클래스 호출

            print()
            print('=' * 30)
            print('고용형태 : 임시직')
            print(f'이름 : {t.name}')
            print(f'급여 : ' + format(t.pay, '3,d') + '원')
            print('=' * 30)
            print()

    else:
            print('=' * 30)
            print('입력오류입니다. 다시 입력해주세요')




