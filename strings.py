helloworld = 'Hello World'

hello = "Hello" 
''' 
0-> H
1 -> e
2 -> l
3 -> l
4 -> o
'''

thankyou = '''
Thank you
Regards Asish
'''

# print(name)
# print(type(name))
# print(name1)
# print(type(name1))
# print(thankyou)
# print(type(thankyou))

# Index start from 0

# String are immutable , means you can't change them.

longString = "A quick brown fox jumps over a lazy dog."
'''
"A quick brown fox jumps over a lazy dog."
"012345678910....."
'''
firstCharacter = longString[0]

print("The first index of the string is", firstCharacter)

print(longString)
print(longString[2])

# firstThreeCharacter = longString[0] + longString[1] + longString[2]

firstThreeWithRange = longString[0:5]

'''
[start,end] -> start index will be included, but end is not going to include
'''

print("First 3 character ", firstThreeWithRange)

stringFrom3to10 = longString[3:11]

up0to15 = longString[:16]

from15ToLast = longString[15:]

print("String 0 to 15 index:", up0to15)

print("15 to the end:", from15ToLast)


lengthOfString = len(longString)

print("Lenght of the String: ", lengthOfString)

singleword = "amazon is a good website"

# azon is a -> I want to skip each 2nd index
print("Some substring:",singleword[2:12:3])

isStartwithA =  singleword.startswith("A")
# print(isStartwithA)

print(singleword.endswith("website"))

captializesentence = singleword.capitalize()

print(singleword)
print(captializesentence)

uppercase = singleword.upper()
print(singleword)
print(uppercase)

print(singleword.count("a"))

print(singleword.find("w"))
print(singleword[17])

print(singleword.find("y"))

replacedString = singleword.replace("a", "C")
print(singleword)
print(replacedString)

print(singleword[::-1])

num1 =  "12"
print(type(num1))

numberwas = int(num1)

print(type(numberwas))