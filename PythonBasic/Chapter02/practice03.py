fat=input("지방의 그램을 입력하세요 : ")
carbo=input("탄수화물의 그램을 입력하세요 : ")
protein=input("단백질의 그램을 입력하세요 : ")

totalC=int(fat)*9+int(protein)*4+int(carbo)*4

print("총 칼로리 : ",totalC,"cal")

print("============================")

#3
hong_number="881120-1068234"

print(hong_number[:6])
print(hong_number[7:])


#4
#hong_number.index('1')

print(hong_number.index("-"))
print(hong_number[:6])
print(hong_number[7:])