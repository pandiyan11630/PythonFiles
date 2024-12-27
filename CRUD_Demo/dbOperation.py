import oracledb

userName='Raavanan'
passWord='Pandiyan#123'
connectionString='localhost:1521/orcl' 

connection=oracledb.connect(dsn=connectionString,user=userName,password=passWord)

myCursor=connection.cursor()

# myCursor.execute('''
# create table employees(emp_id number,emp_name varchar(10),salary number,dep_name varchar(10))''')
# print('Table Created Successfully')
# myCursor.close()

def insertRecord():
    emp_id=int(input('Enter Employee ID : '))
    emp_name=input('Enter Employee Name : ')
    salary=float(input('Enter Employee Salary : '))
    dep_name=input('Enter Department Name : ')

    myCursor.execute('insert into employees values(:1,:2,:3,:4)',(emp_id,emp_name,salary,dep_name))
    connection.commit()
    print('Record Inserted Successfully')

def showRecords():
    myCursor.execute('select * from employees')
    for myRow in myCursor:
        print(myRow)


insertRecord()
showRecords()

