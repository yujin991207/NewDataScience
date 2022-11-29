#3
file = open("data/life.txt", mode='r')

#for s in file:
    #replace = s.replace("java","python")
string = file.read().replace("java","python")

file = open("data/life.txt", mode ='w')
file.write(string)

#print(string)
file.close()