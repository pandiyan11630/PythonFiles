def display():
    print("Hello")
    
def add(num1,num2):
    return num1+num2

def displayNames(*names):
    for name in names:
        print(name)

def show(**employeeData):
    for key,value in employeeData.items():
        print(key,value)

result=lambda x,y : x+y

def calculateFactorial(n):
    if(n>0):
        return n*calculateFactorial(n-1)
    else:
        return 1

def calculateSalaryAfterHike(hikePercent):
    return lambda baseSalary:baseSalary+(baseSalary*(hikePercent/100))

totalSalary=calculateSalaryAfterHike(10)
print("Revised Salary :",totalSalary(10000))

#show(Name="Pandiyan",Emp_id=1002,Experience_in=[".Net","Java","Python","Node"])

#displayNames("Ajay","Akil","Ashok","Vijay")

#display()

#print(add(10,20))

#print("Sum : ",result(30,40))

#print("Factorial Result :",calculateFactorial(5))

