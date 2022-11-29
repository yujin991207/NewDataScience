# 부모클래스 : 사원 (급여계산():)
# 자식클래스 : 정규직 (급여계산(): pay = 기본급 + 상여금), 임시직 (급여계산(): pay = 시급 + 근무시간)

# 부모클래스
class Employee:
    name = None
    pay = 0

    def __init__(self,name):
        self.name = name

    def pay_calc(self):
        pass

# 자식클래스 : 정규직
class Permanent(Employee):
    #def __init__(self,name):
    #    super().__init__(name) # 부모 생성자 호출

    def pay_calc(self,name,base,bonus):
        super().__init__(name)
        #self.name = name
        self.pay = base + bonus # 급여 = 기본급 + 상여금
        print(f'정규직 {name}님의 총 수령액 : ',format(self.pay,'3,d'),'원')

# 자식클래스 : 임시직
class Temporary(Employee):
    def __init__(self,name):
        super().__init__(name) # 부모 생성자 호출

    def pay_calc(self,name,tpay,time):
        self.name = name
        self.pay = tpay * time # 급여 = 시급 * 근무시간
        print(f'임시직 {name}님의 하루 수령액 : ',format(self.pay,'3,d'),'원')

p = Permanent('홍길동')
p.pay_calc('홍길동',3000000,200000)

t = Temporary('홍길순')
t.pay_calc('홍길순',8,10000)
