'''
*
**
***
****
*****
'''

'''
***** -> line 1 - 5 times 
**** -> line 2 - 4 times
*** -> line 3 - 3 times
** -> line 4 - 2 times
* -> line 5 - 1 times
'''

length = 5

# for i in range(length):
#     for j in range(i+1):
#         print("*",end="")
#     print()

for i in range(1,length+1):
    print(i*"*")

for i in range(1,length+1):
    print((length  + 1 - i)*"*")

# i = 1 -> 5 + 1 -1 -> 5
# i = 2 -> 5 + 1 -2 -> 4

'''
1
12
123
1234
12345
12345
1234
123
12
1
'''


