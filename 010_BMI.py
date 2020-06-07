print("This program calculates your BMI and gives you your classification")
height = float(input("Enter your height in meters:") )
weight = float(input("Enter your weight in kilograms:") )
bmi = weight / (height * height)
if (bmi >= 30):
    classification = "obese"
elif (bmi > 24.9 and bmi <= 29.9):
    classification = "overweight"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "Normal weight"
else:   
    classification = "underweight"
print('Your BMI is', round(bmi, 2), 'and this means you are', classification)



