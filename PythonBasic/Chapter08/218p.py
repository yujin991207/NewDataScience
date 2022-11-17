import os
print('\n현재 경로 : ',os.getcwd())

try:
    #파일읽기
    ftest1 = open('data/ftest.txt',mode = 'r')
    print(ftest1.read())

    #파일쓰기
    ftest2 = open('data/ftest2.txt',mode = 'w')
    ftest2.write('my first test~~~')

    #추가한파일에 내용추가
    ftest3 = open('data/ftest2.txt',mode = 'a')
    ftest3.write('\nmy second test~~~')

except Exception as e:
    print(f'Error발생 : {e}')

finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()