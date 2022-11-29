# 얕은 복사 : 내용과 주소 모두 동일하다
name = ['홍길동','이순신','강감찬']
print('name adress =',id(name))

name2 = name # 복사
print('name adress =',id(name2))

print(name)
print(name2)

print()

name2[0] = '김길동'
print(name)
print(name2)

print()

# 깊은복사 : 내용복사 (내용은 동일, 주소는 다르다)
import copy
name3 = copy.deepcopy(name)
print(name3)

print('name adress =',id(name))
print('name3 adress =',id(name3))

print()

name[1] = "이순신장군"
print(name)
print(name3)