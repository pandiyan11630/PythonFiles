class MyInvalidAgeError(Exception):
    def __init__(self,errMsg):
        super().__init__(errMsg)

myOpt=True

while myOpt:
    try:
        age=int(input('Enter Your Age : '))
        if(age>100 or age<=0):
            raise MyInvalidAgeError('Please Enter age in valid range(1-100)')
        else:
            print('Age :',age)
            myOpt=False
    except MyInvalidAgeError as obj:
        print(obj)
        myOpt=True
