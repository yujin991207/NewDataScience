# 캡슐화 예제
class Account:
    # 은닉멤버변수
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNo = None # 계좌번호

    # 생성자
    def __init__(self,bal,name,no):
        # 초기화
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    # 계좌정보확인 : Getter
    def getBalance(self):
        return self.__balance,self.__accName,self.__accNo

    # 입금하기 : setter
    def desposit(self,money):
        if money < 0:
            print('금액 확인')
            return # 종료
        self.__balance += money # 입금

    def withdraw(self,money):
        if self.__balance < money:
            print('잔액 부족')
            return
        self.__balance -= money # 출금

# object생성
acc = Account(1000,'홍길동','125-152-4125-41') # 생성자

# getter 호출
bal = acc.getBalance()
print(f'계좌 정보 : {bal}')

# setter 호출
acc.desposit(10000) # 만원입금
bal = acc.getBalance()
print(f'계좌 정보 : {bal}') # 입금 확인

#==========================================
acc.withdraw(12000) # 출금 .. 잔액부족 출력
bal = acc.getBalance()
print(f'계좌 정보 : {bal}')

acc.withdraw(3000) # 출금 ... 8000원 남음
bal = acc.getBalance()
print(f'계좌 정보 : {bal}') # 입금확인




