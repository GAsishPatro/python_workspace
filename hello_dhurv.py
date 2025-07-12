
# Taking input from the user and converting it to a int
number1 = input("Enter your first number: ")


number2 = int(input("Enter your second number: "))

userChoice = input("What you want to do with the numbers, Add/Substract/Multiply/Divide/Remainder: ")

result = 0

if(userChoice == "+"):
    print("User actually wants to add")
    result = number1 + number2

elif(userChoice == "-"):
    print("User want to substract")
    result = number1 - number2

elif(userChoice == "*"):
    print("User want to Multiply")
    result = number1 * number2

elif(userChoice == "/"):
    print("User want to Divide")
    result = number1 / number2


print("Result of the numbers is ", result)





'''
Ask the user for a input from 0 to 100

>, < , == , >= , <= 

101 -> You are not follwing the rules

0 - 100

grater than 90 -> A grade
greate than 80 and less than 90 -> B grade

'''