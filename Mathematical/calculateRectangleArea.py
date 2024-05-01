def calculateRectangleArea():
    length = float(input("Enter the length of the rectangle (in meters): "))
    width = float(input("Enter the width of the rectangle (in meters): "))
    area = length * width
    print(f"The area of the rectangle is {area:,.3f} square meters.")