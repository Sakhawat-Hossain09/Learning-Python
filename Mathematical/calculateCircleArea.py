def calculateCircleArea():
    radius = float(input("Enter the radius of the circle (in meters): "))
    area = math.pi * math.pow(radius, 2)
    print(f"The area of the circle is {area:,.5f} square meters.")
