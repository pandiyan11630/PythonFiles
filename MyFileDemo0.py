#userName=input('Enter your Name : ')
myFileObject=open('C:\\Pandiyan\\Python Files\\Files\\MyFileInput.txt',"r")
#print(myFileObject.read())
print(myFileObject.readline())
#myFileObject.write("\n"+userName)
for name in myFileObject:
    print(name)
myFileObject.close()