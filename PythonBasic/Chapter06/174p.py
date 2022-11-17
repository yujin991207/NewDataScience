#import가 필요한 import 모듈 내장클래스
import datetime
from datetime import date, time

today = date(2022,11,17) #date 객체생성
print(today)

#date 객체 멤버변수 호출
print(today.year)
print(today.month)
print(today.day)

w = today.weekday()
print(f'요일 정보 : {w}')

currTime = time(10,21,30) #time 객체생성
print(currTime)

print(currTime.hour)
print(currTime.minute)
print(currTime.second)

isoTime = currTime.isoformat() # HH:MM:SS
print(isoTime)