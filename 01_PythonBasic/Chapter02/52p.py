oneLine = "this is one line String"
print('t 글자수 : ',oneLine.count('t')) # t의 글자수를 센다

words = oneLine.split(' ') # 단어로 끊는다
print(f'단어 : {words}')


sent2 = ','.join(words) # '구분자'.join(String)
print(sent2)