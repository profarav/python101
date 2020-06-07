months = ("January", "February", "March", "April", "May", "June", "July","August", "September", "october", "November", "December")
bday = input("Enter your birthday in dd-mm-yyyy format:")
answer = int(bday[3:5]) - 1
print("You were born in", months[answer])
