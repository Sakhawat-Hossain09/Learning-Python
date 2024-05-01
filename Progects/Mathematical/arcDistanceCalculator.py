import math
def arcDistanceCalculator():
    radius = float(input("What is the radius of the circle [In meter/s]: "))
    theta = float(input("What is the theta angle of the arc: "))
    arcDistance = (theta / 360) * 2 * math.pi * radius
    print(f"The arc distance is {arcDistance} meter/s.")
