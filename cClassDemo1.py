class Employee:
    def getEmployeeInfo(self):
        self.empId=int(input('Enter Employee ID :'))
        self.empName=input('Employee Name :')

    def showEmployeeInfo(self):
        print("Employee ID:",self.empId)
        print("Employee Name:",self.empName)
