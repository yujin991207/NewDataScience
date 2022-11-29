class DatePro:
    #멤버변수
    content = "날짜 처리 클래스"

    #생성자
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    #객체메서드
    def display(self):
        print(f'{self.year}-{self.month}-{self.day}')

    #클래스메서드
    @classmethod
    def date_string(cls,dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f'{year}년 {month}월 {day}일')

#객체멤버
date = DatePro(2022,11,17)
print(date.content)
print(date.year)
date.display()

print(DatePro.content)
#print(DatePro.year)
DatePro.date_string('20221117')