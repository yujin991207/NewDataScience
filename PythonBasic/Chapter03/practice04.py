#4
for i in range(1,6):
    for j in range(i+1):
        print("*",end = '')
    print()

print()

#5
for i in range(1,6):
    print(" " * (6-1-i),end = '')
    print("*" * (i+1))
