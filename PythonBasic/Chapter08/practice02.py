#2
while True:
    content = input('저장할 내용을 입력하세요(종료 => 엔터) : ')

    if content == '':
        break

    else:
        file = open("data/test2.txt", mode='a')

        file.write(content)
        file.write('\n')
        file.close()





