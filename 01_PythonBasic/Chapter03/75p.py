String="""나는 홍길동 입니다
주소는 서울시 입니다
나이는 35세 입니다"""

sents = []
words = []

for sen in String.split(sep = "\n"): # 문장 분리
    sents.append(sen)
    for word in sen.split(): # 단어 분리
        words.append(word)

print(f"문장 : {sents}")
print(f"문장 수 : {len(sents)}")

print(f"단어 : {words}")
print(f"단어 수 : {len(words)}")