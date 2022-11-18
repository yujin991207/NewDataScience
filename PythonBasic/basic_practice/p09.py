#9
result = list(filter((lambda x : x > 0 ),[1,-2,3,-5,8,-3]))
print(result)

#10
#def mul(x):
#    return x * 3
#result2 = list(map(mul,[1,2,3,4]))
#print(result2)

result3 = list(map((lambda x : x * 3),[1,2,3,4]))
print(result3)


