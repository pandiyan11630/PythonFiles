from django.shortcuts import render,redirect
from .forms import EmployeeForm
import oracledb

def initializeConnection():
    userName='Raavanan'
    passWord='Pandiyan#123'
    connectionString='localhost:1521/orcl' 

    connectionObj=oracledb.connect(dsn=connectionString,user=userName,password=passWord)
    return connectionObj


# Create your views here.
def readAllEmployees(request):
    employees=[]
    myConn=initializeConnection()
    myCursor=myConn.cursor()
    myCursor.execute('select * from employees')
    for myRow in myCursor.fetchall():
        employees.append({'employee_id':myRow[0],'employee_name':myRow[1],'employee_salary':myRow[2],'department_name':myRow[3]})
    myConn.close()
    return render (request,'employeesList.html',{'employees':employees})

def addNewEmployee(request):
    if request.method=='GET':
        return render(request,'addEmployee.html')
    if request.method=='POST':
        myForm=EmployeeForm(request.POST)
        if myForm.is_valid():
            employeeId=myForm.cleaned_data.get('employee_id')
            employeeName=myForm.cleaned_data.get('employee_Name')
            employeeSalary=myForm.cleaned_data.get('employee_salary')
            departmentName=myForm.cleaned_data.get('department_name')

            myConn=initializeConnection()
            myCursor=myConn.cursor()
            myCursor.execute('insert into employees values(:employeeId,:employeeName,:employeeSalary,:departmentName)',[employeeId,employeeName,employeeSalary,departmentName])
            myConn.commit()
            myConn.close()

            return redirect('employeesList')