import random

player = input("Rock(r) paper(p) or scissors(s)? : ")
attack = ["r","p","s"]
bot = random.choice(attack)

print("Bot choice :", bot)

if bot == player:
    print("Tie!")

# Bot wins !
elif bot == "s" and player =="p":
    print("Bot wins!")
elif bot == "p" and player =="r":
    print("Bot wins!")
elif bot == "r" and player =="s":
    print("Bot wins!")

# Bot losses !
elif bot == "p" and player =="s":
    print("Player wins!")
elif bot == "s" and player =="r":
    print("Player wins!")
elif bot == "r" and player =="p":
    print("Player wins!")




