# 부모클래스
class Parent:
    # 생성자 : 객체 + 초기화
    def __init__(self,name,job):
        self.name = name
        self.job = job

    # 멤버함수
    def display(self):
        print(f'name : {self.name} job : {self.job}')

# 부모클래스 객체생성
p = Parent('홍길동','회사원')
p.display()

class Children(Parent):
    gender = None

    # 자식 클래스 생성자
    def __init__(self,name,job,gender):
        super().__init__(name,job) # super클래스에 있는 name,job
        #self.name = name
        #self.job = job
        self.gender = gender # 자식멤버변수 초기화

    # 멤버함수 : 함수 재정의
    def display(self):
        print(f'name : {self.name} job : {self.job} gender : {self.gender}')

# 자식클래스 객체 생성
chil = Children('이순신','장군','남자')
chil.display()


