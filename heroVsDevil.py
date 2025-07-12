import random

hero = input("Enter your name: ")

print("You can have 3 choices from the below.")
print("Fire/Water/Earth/Thudner/DarkMagic/Freeze")

availablepowers = "Fire/Water/Earth/Thudner/DarkMagic/Freeze".split("/")

listSuperPowers = []

firstSuperPower = input("First power: ")
secondPower = input("Second power: ")
thirdPower = input("Third power: ")

# listSuperPowers.append(firstSuperPower)
# listSuperPowers.append(secondPower)
# listSuperPowers.append(thirdPower)

listSuperPowers = [firstSuperPower,secondPower,thirdPower]

print(listSuperPowers)

devilsWeakNess = random.sample(availablepowers,3)

print(devilsWeakNess)

if((listSuperPowers[0] in devilsWeakNess) or (listSuperPowers[1] in devilsWeakNess) or (listSuperPowers[2] in devilsWeakNess)):
    print(hero,"Won")
else:
    print("YOU LOSE")
