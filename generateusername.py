'''
Ask the user for the Name
Ask the user to enter Date of birth (DD-MM-YYYY) e.g: 12-07-2025

Validate the DOB
1. is containing 2 "-"
2. Validate the month -> 1 to 12 
3. Check the dates 
    -> if it is month 1,3,5,7,8,10,12 date not beyond 31
    -> else date suppose to be upto 30
    -> Try leap year month 2 
HINT: 
Extract the date , month and year from the user inputed the Date of birth
And convert each them to Int , so that they can be used compraisions


1. Reverse the name of the user
2. make it uppercase if it is not
3. Replace 
    A -> @
    H -> #
    I -> !
    S -> $

Final username will be = YEAR-GENERATENAME-DATE

EG: 
NAME: dhruv
DOB: 12-12-2010

VURHD -> VUR#D

username = 2010-VUR#D-12
'''