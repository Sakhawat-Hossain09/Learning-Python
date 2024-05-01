def calculateCubeVolume():
    length = float(input("Enter the length of the cube (in meters): "))
    width = float(input("Enter the width of the cube (in meters): "))
    height = float(input("Enter the height of the cube (in meters): "))
    volume = length * width * height
    print(f"The volume of the cube is {volume:,.3f} cubic meters.")
