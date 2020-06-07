print("This is a calculator for 2 numbers and simple operators")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = str(input("Enter the operator you want to multiply them by ex. //, *, + , -, **: "))
if operator == "*":
    print(num1*num2)
elif operator == "+":
    print(num1+num2)
elif operator == "**":
    print(num1**num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)





