#age=int(input('Enter your Age:'))
#if(age>18):
#    print("Valid Age")


num1=int(input('Enter Value 1:'))
num2=int(input('Enter Value 2:'))
result=0
inp1=int(input('Enter a value:'))
sumValue=0
try:
    result=num1/num2
    sumValue=num1+inp1
except(ZeroDivisionError,TypeError):
    print('Invalid Input')
finally:
    print('Finally block is executed')
#except TypeError:
#    print('String Value cannot added with Number value')
    
print("Result : ",result)
print('Sumation : ',sumValue)
