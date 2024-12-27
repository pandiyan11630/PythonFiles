mark=int(input('Enter Your mark : '))
if(mark>=81 and mark<=100):
    print("Outstanding")
elif(mark>=61 and mark<=80):
    print("Good")
elif(mark>=41 and mark<=60):
    print("Pass")
elif(mark>=1 and mark<=40):
    print("Fail")
else:
    print("Please Enter Valid Mark")
