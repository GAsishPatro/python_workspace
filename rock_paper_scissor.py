import random

print("ROCK,PAPER,SCISSOR")
print("1 -> Rock")
print("2 -> Paper")
print("3 -> Scissor")

user_choice = input("Enter your choice: ")

user_action = ""

if(user_choice == "1"):
    user_action = "Rock"
elif(user_choice == "2"):
    user_action = "Paper"
else:
    user_action = "Scissor"

print("User choosed: ", user_action)

computer_choice = random.randint(1,3)

print("Computer Choice: ", computer_choice)

computer_action = ""

if(computer_choice == 1):
    computer_action = "Rock"
elif(computer_choice == 2):
    computer_action = "Paper"
else:
    computer_action = "Scissor"

print("Computer choosed: ", computer_action)

'''
IF i want to pin 

I -> Rock and Computer -> Scissor
OR
I -> Paper and Computer -> Rock
OR
I -> Scissor and Computer -> Paper

'''

if(
    (user_action == "Rock" and computer_action == "Scissor") or
    (user_action == "Paper" and computer_action == "Rock") or
    (user_action == "Scissor" and computer_action == "Paper")
    ):
    print("User won")
elif(user_action == computer_action):
    print("It's a draw")
else:
    print("User lost")
