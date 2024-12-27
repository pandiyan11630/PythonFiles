myInput=(10,"Pandiyan",92.3,25,36,45,"Ajay")
print(myInput)
for data in myInput:
    print(data)

print(myInput[1])

print(myInput[-5:])

print(myInput[-5:-3])

myConvertedList=list(myInput)
myConvertedList[2]=100

myInput=tuple(myConvertedList)
print(myInput)


