import random
colors = ['red', 'blue', 'green']
while True:     
    print("I'm thinking about a color, can you guess it!")
    guess = input('Enter your guess:')
    answer = colors[random.randint(0, len(colors)-1)]
    if answer ==  guess:
        print("Congrats you did it!")
        print('If you would like to play again, type yes if not type no')
        ragequit = input("Type yes or no here:")
        if ragequit == "yes":
            continue
        else:
            break
    else:
        print("Try again")
    
