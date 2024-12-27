num1=int(input('Enter Number 1:'))
num2=int(input('Enter Number 2:'))
result=0
try:
    result=num1/num2
except ZeroDivisionError:
    print("While dividing a number with 0 produces infinite")
    
print("Result : ",result)
