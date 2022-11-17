# 상속
# 부모클래스
class Super:
    # 생성자
    def __init__(self,name,age):
        # 초기화
        self.name = name
        self.age = age

    # 메서드
    def display(self):
        print(f'이름 : {self.name} 나이 : {self.age}')
        sup = Super('부모',55)
        sup.display() # 부모 멤버 호출

# 자식클래스
class Sub(Super): # 클래스 상속
    gender = None # 자식멤버

    # 생성자
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 메서드 확장
    def display(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}')

sub = Sub('자식',25,'여자')
sub.display() # 자식 멤버 호출
