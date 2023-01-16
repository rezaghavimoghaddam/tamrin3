import random

pc_number = random.randint(0, 20)
g = 0

while True:
    user_number = int(input("enter number: "))
    g += 1

    if pc_number == user_number:
        print("you win")
        print("number of guess: ", g)
        break

    if pc_number < user_number:
        print("go down")

    else:
        print("go up")    
