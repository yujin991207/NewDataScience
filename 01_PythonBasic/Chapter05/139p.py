def wrap(func):
    def decorated():
        print('반가워요!')
        func()
        print('잘가요!')
    return decorated

@wrap
def hello():
    print('hi~~~~',"홍길동")

hello()