# for i in range(0,3) :
#     print(i)


numlist = [1,2,4,5,6,7,8,8]
sum = 0

# for index in range(0,len(numlist)):
#     numlist[index] = int(input("Enter some value:"))

for index in range(0,len(numlist)):
    print(f"Index is {index} ,value on index is {numlist[index]}")

sum = 0

for index in range(len(numlist)):
    sum = sum + numlist[index]

print("The sum is:",sum)


sum2 = 0 

for number in numlist:
    print(number)
    sum2 = sum2 + number

print("The sum 2 is:",sum2)

