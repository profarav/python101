import matplotlib.pyplot as plt
import time as t
import random
words = ["happy", "superflous", "construction"]
time = []
mistake = 0
for i in range(5):
    whichone = random.randint(0, len(words) - 1)
    winner = words[whichone]
    print("The word you will type now is", winner, "Type it as fast as you can.")
    b = 0
    while b < 1:
        start = t.time()
        answer = input("Type the word now:").lower()
        if answer == winner:
            print("Nice job")
            end = t.time()
            time_elapsed = end - start
            time.append(time_elapsed)
            b += 1
        else:
            print("You typed it incorrectly")
            mistake += 1 
            print(mistake)
x = [1, 2, 3, 4, 5]
y = time
print("You made", mistake, "mistakes while typing")
plt.plot(x,y)
plt.show()
