print("=="*5 + "베스킨라빈스31 게임을 시작합니다."+"=="*5)
print("COM : 1!\nCOM : 2!")

num = 2
a = 1

while num < 30:
    a = 1
    ans = 0
    while ans != "n":
        num += 1
        ans = input("YOU : {0}! (총 3번중 {1}번 말씀하셨습니다. {2}번 더 말할수 있어요.) 숫자 {3}을(를) 말씀하시겠습니까? (y/n) : ".format(num, a, 3-a, num+1))
        while ans !="y" and ans !="n" :
            ans = input(" 답변오류, y 또는 n 을 입력하세요")
        a += 1
        if a >= 3 and ans == "y":
            num += 1
            print("YOU : {0}! (COM 턴으로 넘어갑니다)".format(num))
            ans = "n"


    while num % 4 != 2:
        num += 1
        print("COM : {0}!".format(num))

print("YOU : 31! 내가졌네요.")
