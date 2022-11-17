#1
class Rectangle:
    # 멤버변수
    width = height = 0

    # 생성자
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        #print(f'사각형의 넓이 : {area}')

        return area
    def circum_calc(self):
        circumference = (self.width + self.height) * 2
        #print(f'사각형의 둘레 : {circumference}')

        return circumference

print('사각형 넓이와 둘레를 계산합니다.')
w = int(input('사각형 가로 입력 : '))
h = int(input('사각형 세로 입력 : '))

rec = Rectangle(w,h)
area = rec.area_calc()
print(f'사각형의 넓이 : {area}')

circum = rec.circum_calc()
print(f'사각형의 둘레 : {circum}')





