charset = ['abc','code','band','band','abc']
wc = {}

for key in charset:
    # get()함수 : key이용 value 가져오기
    wc[key] = wc.get(key,0) + 1

print(wc)