# 교과서 4번
tot=0
print("수열 = ",end = ' ')

for i in range(1,101):
    if i%3 == 0 and i%2 != 0:
        print(f"i = {i} ",end = ' ')
        tot += i

print(f'누적합 = {tot}')

#======================================

# 교과서 5번
multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀처럼 매력적인 언어입니다."""

cnt = 0
word = []
sents = []

for sen in multiline.split(sep = "\n"):
    sents.append(sen)

print(sents)
