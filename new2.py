import random

# 1. Build the same game within 100

# Needs optimization, lots of if statements.
# says warm if you're in the right ten but everywhere else it just says cold
# ( at least it's supposed too )

def guess_the_num():
    # Num selection

    num = random.choice(range(1, 100))
    print(num)
    guess = False

    pick = input("Pick a number (1-100) : ")

    # Guess statements

    if pick == num:
        print("You guessed the number!")
        guess = True

    if pick != num:
        while guess == False:
            if int(pick) == int(num):
                print("You guessed the number!")
                guess = True

            # Warm guesses

            elif int(pick) <= 10 and int(num) <= 10:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 20 and int(num) <= 20:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 30 and int(num) <= 30:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 40 and int(num) <= 40:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 50 and int(num) <= 50:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 60 and int(num) <= 60:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 70 and int(num) <= 70:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 80 and int(num) <= 80:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) <= 90 and int(num) <= 90:
                print("Warm!")
                pick = input("Pick a number (1-100) : ")

           # Cold guesses

            elif int(pick) >= 10 and int(num) < 10 or int(pick) <= 10 and int(num) > 10:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 20 and int(num) < 20 or int(pick) <= 20 and int(num) > 20:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 30 and int(num) < 30 or int(pick) <= 30 and int(num) > 30:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 40 and int(num) < 40 or int(pick) <= 40 and int(num) > 40:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 50 and int(num) < 50 or int(pick) <= 50 and int(num) > 50:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 60 and int(num) < 60 or int(pick) <= 60 and int(num) > 60:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 70 and int(num) < 70 or int(pick) <= 70 and int(num) > 70:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 80 and int(num) < 80 or int(pick) <= 80 and int(num) > 80:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")

            elif int(pick) >= 90 and int(num) < 90 or int(pick) <= 90 and int(num) > 90:
                print("Cold!")
                pick = input("Pick a number (1-100) : ")


# 2. Build your own version of the guessing game

Shapes = ["circle", "square", "triangle", "rectangle", "oval"]
answer = random.choice(Shapes)
guess = False

player = input("Guess the shape : ")

if player.lower() == answer:
    print("You guessed correctly! The shape is", answer + "!")
    guess = True

if player.lower() != answer:
    while guess == False:
        if player.lower() != answer:
            print("That isn't quite right.. try again.")
            guess = input("Guess the shape : ")

