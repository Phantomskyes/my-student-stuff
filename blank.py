import random

def rps_game():
    play = input("Enter r for Rock, p for Paper, and s for Scissors: ")
    comp = random.choice(["r","p","s"])
    print(comp)
    if play == comp:
        return print("Draw")
    elif (play == "r" and comp == "p") or (play == "s" and comp == "r") or (play == "p" and comp == "s"):
        return "Computer wins!"
    elif (play == "p" and comp == "r") or (play == "r" and comp == "s") or (play == "s" and comp == "p"):
        return "Player wins."

print(rps_game())