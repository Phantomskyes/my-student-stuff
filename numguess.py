import random

numbers = ["1","2","3","4","5","6","7","8","9","10"]
num = random.choice(numbers)
guess = False

pick = input("Pick a number (1-10) : ")


if pick == num:
    print("You guessed the number!")
    guess = True

if pick != num:
    while guess == False:
        if pick == num:
            print("You guessed the number!")
            guess = True
        elif int(pick) <= 5 and int(num) <= 5:
            print("Warm!")
            pick = input("Pick a number (1-10) : ")
        elif int(pick) <= 5 and int(num) > 5:
            print("Cold!")
            pick = input("Pick a number (1-10) : ")
        elif int(pick) >= 5 and int(num) >= 5:
            print("Warm!")
            pick = input("Pick a number (1-10) : ")
        elif int(pick) >= 5 and int(num) < 5:
            print("Cold!")
            pick = input("Pick a number (1-10) : ")



