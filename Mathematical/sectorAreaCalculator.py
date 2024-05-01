import math
def sectorAreaCalculator():
    radius = float(input("What is the radius of the circle [In meter/s]: "))
    theta = float(input("What is the theta angle of the arc: "))
    arcDistance = (theta / 360) * 2 * math.pi * pow(radius, 2)
    print(f"The sector is {arcDistance} meter^2/s.")
