from random import randint

minNumber = int(input("please enter min number: "))
maxNumber = int(input("please enter Max number: "))

if(maxNumber < minNumber):
    print("Invalid input shutting down")
else:
    rnd_number = randint(minNumber,maxNumber)
    print("Random number",rnd_number)