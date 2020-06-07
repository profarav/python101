print("This program will give you a circumference and area of a circle given a radius of your choice")
import math
radius = float(input("Please enter a radius of your choice:"))
area = radius ** 2 * 3.14
circum = radius * 2 * 3.14
print("The area of the circle is", round(area, 1))
print("The circumference of the circle is", round(circum, 1))
