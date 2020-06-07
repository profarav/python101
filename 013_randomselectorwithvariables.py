import random
print("This program will ask you for eight names and give you a random one of them")
people = []
for x in range(0, 8):
    name = input("Enter a name:")
    people.append(name)
index = random.randint(0,7)
print(people[index])
