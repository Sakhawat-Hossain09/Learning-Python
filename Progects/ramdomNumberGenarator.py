import random
def ramdomNumberGenarator():
    minNumber = int(input("What is the minimun number: "))
    maxNumber = int(input("What is the maximum number: "))
    randomNumber = random(minNumber, maxNumber)
    print(randomNumber)