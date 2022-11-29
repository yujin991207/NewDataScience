class multiply3:
    #멤버변수, 생성자 없음

    #동적 멤버변수 생성/초기화
    def data(self,x,y):
        self.x = x
        self.y = y

    #곱셈연산
    def mul(self):
        result = self.x * self.y
        self.display(result) #메서드 호출

    def display(self,result):
        print(f'곱셈 = {result}')

obj = multiply3() #기본 생성자
obj.data(10,20)
obj.mul()