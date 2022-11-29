#5
multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀처럼 매력적인 언어입니다."""

cnt = 0
word = []
sents = []

for sen in multiline.split(sep = "\n"):
    sents.append(sen)

print(sents)