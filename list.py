number = 10

listofnumbers = [10,20,30,40,12,50,12, "Asish", "Dhruv"]

print("First object : ",listofnumbers[0])
print(listofnumbers[2:6])

print(listofnumbers[0:5:2])

print(listofnumbers)

# THIS WAS NOT POSSIBLE IN STRING, BUT IN LIST IT IS POSSIBLE
# LIST ARE MUTABLE BUT STRINGS ARE NOT
listofnumbers[1] = 34

print(listofnumbers)

print("25-12-2000".split("-"))

listOfNumbers = [40,12,343,60,2,70,12]

print("Before sorting: ", listOfNumbers)

listOfNumbers.sort()

print("After Sorting: ",listOfNumbers)

listOfNumbers.reverse()

print("After Sorting In Descending: ",listOfNumbers)

listOfNumbers.append(90)

print(listOfNumbers)

listOfNumbers.insert(3, 98)

print(listOfNumbers)

listOfNumbers.remove(90)

print(listOfNumbers)

popedValue = listOfNumbers.pop(3)

print("Poped value:",popedValue)

print(listOfNumbers)