6
def serach_visitor(name):
   with open("data/방명록.txt", mode ='r', encoding ='utf-8') as file:
       visitor = file.read()

       if visitor.find(name) == -1: # 찾는 이름과 입력한 값의 이름이 같은지 여부 체크
            return False
       return True

name = input('이름을 입력하세요 (예: 홍길동) : ')

visitor_name = serach_visitor(name)

if visitor_name:
    print(f'{name}님 다시 방문해 주셔서 감사합니다. 즐거운시간되세요.')

else:
    birth = int(input('생년월일을 입력하세요 (예 : 801212) : '))
    with open("data/방명록.txt", mode='a', encoding ='utf-8') as file:
        file.write(f'\n{name} {birth}')
    print(f'{name}님 환영합니다. 아래 내용을 입력하셨습니다')
    print(f'{name} {birth}')

