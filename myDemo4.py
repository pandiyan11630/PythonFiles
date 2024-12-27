mySetInput=set()

myInput2={11,22,33}

mySetInput.add(10)
mySetInput.add(20)
mySetInput.add(30)
mySetInput.add(40)
mySetInput.add(50)
mySetInput.add(60)

print(mySetInput)

myInput2.remove(22)
print(myInput2)


myConstantValues=frozenset(mySetInput)
print(myConstantValues)
myConstantValues.add(70)
print(myConstantValues)
