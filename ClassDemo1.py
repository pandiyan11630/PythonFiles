class Employee: #BaseClass or Parent Class
    #def __init__(self,employeeId,employeeName,departmentName):
        #self.empId=employeeId
        #self.__empName=employeeName
        #self.depName=departmentName
    def getEmpInfo(self):
        self.empId=int(input('Enter Employee ID :'))
        self._empName=input('Enter Employee Name :')
        self.depName=input('Enter Department Name :')
    #def showEmployeeInfo(self):
        

class PermenentEmployee(Employee):  #Derived Class or Child Class
    def getSalary(self):
        self.salary=float(input('Enter your Salary:'))
    def displayPermenentEmpInfo(self):
        print("Employee ID:",self.empId)
        print("Employee Name:",self._empName)
        print("Department Name:",self.depName)
        print('Salary:',self.salary)

class ContractEmployee(Employee):
    def getWages(self):
        self.salary=float(input('Enter your Salary:'))
    def displayContractEmpInfo(self):
        print("Employee ID:",self.empId)
        print("Employee Name:",self._empName)
        print("Department Name:",self.depName)
        print('Salary:',self.salary)


myEmpObj1=PermenentEmployee()
myEmpObj1.getEmpInfo()
myEmpObj1.getSalary()
myEmpObj1.displayPermenentEmpInfo()


myEmpObj2=ContractEmployee()
myEmpObj2.getEmpInfo()
myEmpObj2.getWages()
myEmpObj2.displayContractEmpInfo()
