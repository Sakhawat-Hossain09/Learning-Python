import math
def surfaceAreaOfSphere():
    radius = float(input("What is the radius of the sphere [In meter/s]: "))
    surfaceArea = 4 * math.pi * pow(radius, 2)
    print(f"The surface area of the sphere is {surfaceArea:,.3f} meter^2/s")
