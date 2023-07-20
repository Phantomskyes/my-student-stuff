import random

chars = "abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPQRUSTUVWXYZ0123456789"

amount = int(input("Enter how many passwords should be generated: "))
passLen = int(input("Enter how long the passwords should be: "))

password = ""

for i in range(amount):
    password = ""
    for i in range(passLen):
        password = password + random.choice(chars)
    print(password)