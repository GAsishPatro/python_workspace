'''
To be a Footballer

-> I need to be human -> True
-> I know what football rules -> True
-> I am suppose to be atleast 5 years -> True

and -> you need to follow all
'''

isItHuman = input("Are you a human (Yes/No): ") == "Yes"
doYouKNowTheRules = input("Do you know the rules of Footbal (Yes/No): ") == "Yes"
yourAge = int(input("Enter your age: "))

if(isItHuman and doYouKNowTheRules and yourAge >= 5):
    print("Awesome! You can be footballer")
elif(isItHuman and doYouKNowTheRules and not(yourAge >= 5)):
    print("Wait to be 5 years old")
else:
    print("You can't be a footballer")
