#import MyArithmeticModule
#import MyArithmeticModule as ar

from MyApp.MyModules.MyArithmeticModule import add,product

x=int(input('Enter Number 1:'))
y=int(input('Enter Number 2:'))

print("SUM :",add(x,y))
print("Product:",product(x,y))
#print("Difference:",difference(x,y))

