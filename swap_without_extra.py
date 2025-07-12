a = 10 
b = 20

print("The value of A is", a) # -> Want 20 here
print("The value of B is", b) # -> Want 10 here

b = a + b # b = 30

a = b - a # a = 20 - 10 = 20
b = b - a # b = 30 - 20 = 10

print("The value of A is", a) # -> Want 20 here
print("The value of B is", b) # -> Want 10 here