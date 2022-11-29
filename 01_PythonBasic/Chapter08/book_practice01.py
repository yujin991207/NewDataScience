# 교과서 1번 문제
file = open("data/ftest.txt", mode ='r')

lines = file.readline() # 줄단위 전체 읽기
#print(file.read())
docs = [] # 문장 저장
words = [] # 단어 저장
