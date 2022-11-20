#2
file = open("file/메세지.txt", mode='w', encoding='utf-8')

content = input('메시지를 입력하세요 : ')

for i in range(1,11):
    file.write(f'{content}{i}\n')
    #file.write('\n')
    #file.close()

file.close() # for문 밖에서 close해준다.


