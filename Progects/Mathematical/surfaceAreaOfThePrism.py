def surfaceAreaOfThePrism():
    areaOfTheBase = float(input("What is the area of the base: "))  
    perimeterOfTheBase = float(input("What is the perimeter of the base: ")) 
    height = float(input("What is the height of the prism"))
    surfaceArea = 2 * areaOfTheBase + perimeterOfTheBase * height
    print(f"The surface area of the prism is {surfaceArea:,.3f}")
