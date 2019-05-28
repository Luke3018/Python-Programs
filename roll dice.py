import random

def genNum():
    n = random.randint(1,6)
    return n

genNum()

def bet():
    x = "y"
    while x == "y":
        dice = genNum()
        b = int(input("enter bet"))
        num = int(input("guess number"))
        if num == dice:
            money = b * 2
            print("well done you won: ", money)
        else:
            print("better luck next time")
        print(dice)
        x = str(input("play again [y/n]"))
bet()

    
        
