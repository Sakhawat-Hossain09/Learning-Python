import math
def volumeOfSphere():
    radius = float(input("What is the radius of the sphere [In meter/s]: "))
    volume = 4/3 * math.pi * pow(radius, 3)
    print(f"The volume of the sphere is {volume:,.3f} meter^3/s")
