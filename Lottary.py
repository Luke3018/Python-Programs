import random
def GenNum():
    num = random.randint(1,59)
    return num

def GenList():
    NumList = []
    while len(NumList) < 6:
        num = GenNum()
        if not num in NumList:
            NumList.append(num)
    return NumList

def valid():
    i = 0
    NList = []
    while i != 6:
        num = int(input("enter a number "))
        if num > 59 or num < 1:
            print("invalid number ")
            num = int(input("enter a number "))
        else:
            NList.append(num)
            i += 1
    return NList

def check(l1, l2):
    count = 0
    for num in l1:
        if num in l2:
            count += 1
    return count

user = valid()
lotto = GenList()
guess = check(user, lotto)

if guess == 6:
    print("won Jackpot")
elif guess == 5:
    print("won £1000")
elif guess == 4:
    print("won £250")
elif guess == 3:
    print("won £50")
elif guess < 3:
    print("sorry better luck next time")
print(lotto)


    
