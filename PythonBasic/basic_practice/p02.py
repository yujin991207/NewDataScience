#2
content = input('메시지를 입력하세요 : ')

for i in range(1,11):
    file = open("../basic_practice/file/메세지.txt", mode='a', encoding='utf-8')

    file.write(content+f'{i}')
    file.write('\n')
    file.close()


