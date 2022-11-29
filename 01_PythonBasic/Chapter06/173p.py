#리스트 열거형객체 이용
lst = [1,3,5]

for i,c in enumerate(lst): #import가 필요없는 builtins모듈의 enumerate 내장클래스
    print(f'색인 : {i}',end = ', ')
    print(f'내용 : {c}')

#튜플 열거형객체 이용
dit = {'name':'홍길동','job':'회사원','addr':'서울시'}

for i,k in enumerate(dit):
    print(f'순서 : {i}',end = ', ')
    print(f'키 : {k}',end = ', ')
    print(f'값 : {dit[k]}')

