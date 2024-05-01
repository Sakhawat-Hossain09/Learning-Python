def calculateHypotenuse():
    side_a = float(input("Enter the length of side A (in meters): "))
    side_b = float(input("Enter the length of side B (in meters): "))
    side_c = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
    print(f"The length of the hypotenuse is {side_c:,.3f} meters.")
