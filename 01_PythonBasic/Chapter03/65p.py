cnt = tot = 0

while cnt < 5:
    cnt += 1 # cnt = cnt + 1
    tot += cnt # tot = tot + cnt
    print(cnt,tot)

cnt = tot = 0
dataset = []

while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt
        dataset.append(cnt)

print('1~100사이의 3의 배수 합 = %d' %tot)
print(f'dataset = {dataset}')
