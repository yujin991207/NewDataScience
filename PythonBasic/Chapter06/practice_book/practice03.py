#3
class Person:
    # 생성자
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    # 메서드
    def display(self):
        print('='*30)
        print(f'이름 : {self.name}, 성별 : {self.gender}\n나이 : {self.age}')
        print('='*30)


name = input('이름 : ')
gender = input('성별(male/female) : ')
age = input('나이 : ')

P = Person(name,gender,age)
P.display()
