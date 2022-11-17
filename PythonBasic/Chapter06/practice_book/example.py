from PythonBasic.Chapter06.myCalcPackage.calcModule \
    import Add,Sub,Mul,Div

x = 10
y = 5

print(f'Add = {Add(x,y)}')
print(f'Sub = {Sub(x,y)}')
print(f'Mul = {Mul(x,y)}')
print(f'Div = {Div(x,y)}')

#================================================================
print()
import PythonBasic.Chapter06.myCalcPackage.calcModule

x = 10
y = 5

print(f'Add = {PythonBasic.Chapter06.myCalcPackage.calcModule.Add(x,y)}')
print(f'Sub = {PythonBasic.Chapter06.myCalcPackage.calcModule.Sub(x,y)}')
print(f'Mul = {PythonBasic.Chapter06.myCalcPackage.calcModule.Mul(x,y)}')
print(f'Div = {PythonBasic.Chapter06.myCalcPackage.calcModule.Div(x,y)}')