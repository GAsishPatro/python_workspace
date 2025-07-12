tictactocmtrix = [ ["X"," "," "]
                  ,[" "," "," "]
                  ,[" "," "," "] ]

# i want a cross on 0th row and 0th coulmn

print(tictactocmtrix[0][0])

row = int(input("what row")) #-> 1
column = int(input("what column")) #-> 1
# 1 ,1 -> X

tictactocmtrix[row][column] = "X"

print(tictactocmtrix)