import math
def calculateCircleCircumference():
    radius = float(input("Enter the radius of the circle (in meters): "))
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is {circumference:,.5f} meters.")