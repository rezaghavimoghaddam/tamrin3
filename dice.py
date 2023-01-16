import random

while True:
    dice = random.randint(1, 6)
    op = input("welcome to dice play.! type R for roll: ")

    if op == "R":
        print(dice)

    if dice == 6:
        print("your prize")

    if dice < 6:
        break    
