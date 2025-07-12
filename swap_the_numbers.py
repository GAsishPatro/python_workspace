a = 10

b = 20

print("The value of A is", a) # -> Want 20 here
print("The value of B is", b) # -> Want 10 here

c = a

a = b
b = c

print("UPDATED VALUE")
print("The value of A is", a) # -> Want 20 here
print("The value of B is", b) # -> Want 10 here