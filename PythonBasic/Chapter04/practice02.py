#4
message = ['spam','ham','spam','ham','spam']

dummy = [1 if msg == 'spam' else 0 for msg in message] # 'spam'이면 1을 출력
print(dummy)

#5
spam_list = [ msg for msg in message if msg == 'spam']
print(spam_list)


#6
position = ['과장','부장','대리','사장','대리','과장']

sposition = set(position) # list => set
lposition = list(sposition) # set => list
print(f"중복되지 않은 직위 : {lposition}")

ps = {}

for key in position:
    ps[key] = ps.get(key,0) + 1

print(f"각 직위별 빈도수 : {ps}")