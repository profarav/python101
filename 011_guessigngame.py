import random
number = random.randint(1,10)
x = 1
guess = int(input("Try and guess my number between 1 and 10, you only have 3 chances:") )
while x < 3:
    if guess == number:
        print("Congrats you guessed the number in under 3 tries")
        break
    else:
        guess = int(input("Try again!:"))
        x = x + 1

if x >= 3:
    print("Sorry you don't have any chances left")
    
