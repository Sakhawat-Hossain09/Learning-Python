import math
import time
def createMadLibsStory():
    adjective1 = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    adjective2 = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    adjective3 = input("Enter an adjective: ")
    print(f"Today I went to a {adjective1} zoo.")
    print(f"In an exhibit, I saw a {noun}.")
    print(f"The {noun} was {adjective2} and {verb}ing.")
    print(f"I was {adjective3}.")
def calculateRectangleArea():
    length = float(input("Enter the length of the rectangle (in meters): "))
    width = float(input("Enter the width of the rectangle (in meters): "))
    area = length * width
    print(f"The area of the rectangle is {area:,.3f} square meters.")
def calculateCubeVolume():
    length = float(input("Enter the length of the cube (in meters): "))
    width = float(input("Enter the width of the cube (in meters): "))
    height = float(input("Enter the height of the cube (in meters): "))
    volume = length * width * height
    print(f"The volume of the cube is {volume:,.3f} cubic meters.")
def calculateCircleCircumference():
    radius = float(input("Enter the radius of the circle (in meters): "))
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is {circumference:,.5f} meters.")
def calculateCircleArea():
    radius = float(input("Enter the radius of the circle (in meters): "))
    area = math.pi * math.pow(radius, 2)
    print(f"The area of the circle is {area:,.5f} square meters.")
def calculateHypotenuse():
    side_a = float(input("Enter the length of side A (in meters): "))
    side_b = float(input("Enter the length of side B (in meters): "))
    side_c = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
    print(f"The length of the hypotenuse is {side_c:,.3f} meters.")
def calculateArithmeticExpression():
  firstNumber = int(input("Enter the first number: "))
  operator = input("Enter the arithmetic operator (+, -, *, /): ")
  secondNumber = int(input("Enter the second number: "))
  if operator in "+-*/":
    if operator == "+":
      print(firstNumber + secondNumber)
    elif operator == "-":
      print(firstNumber - secondNumber)
    elif operator == "*":
      print(firstNumber * secondNumber)
    else:
      print(firstNumber / secondNumber)
  else:
    print("Invalid operator. Please use +, -, *, or /.")
def convertWeight():
  weight = float(input("What is the weight: "))
  unit = input("Is it in Kilograms or Pounds (K,L): ").upper()
  if unit == "K":
    weight *= 2.205
    print(f"The weight in pounds is {weight:,.5f}.")
  elif unit == "L":
    weight /= 2.205 
    print(f"The weight in kilograms is {weight:,.5f}.")
  else:
    print("Encountered unknown unit. Please try again.")
def convertTemperature():
    enteredTemperature = int(input("What is the temperature you want to convert: "))
    enteredTemperatureUnit = input("Which unit is the temperature in [Celsius(C), Fahrenheit(F), Kelvin(K)]: ").upper()
    conversionTemperatureUnit = input("In which unit do you want the temperature to be in [Celsius(C), Fahrenheit(F), Kelvin(K)]: ").upper()
    if enteredTemperatureUnit == "C":
        if enteredTemperature < -273.15:
            print("Temperature below -273.15 doesn't exist in Celsius scale.")
        else:
            if conversionTemperatureUnit == "K":
                convertedTemperature = enteredTemperature + 273.15
                print(f"The temperature in Kelvin is: {convertedTemperature:,.3f}")
            elif conversionTemperatureUnit == "F":
                convertedTemperature = (9 * enteredTemperature) / 5 + 32
                print(f"The temperature in Fahrenheit is: {convertedTemperature:,.3f}")
    elif enteredTemperatureUnit == "F":
        if enteredTemperature < -459.67:
            print("Temperature below -459.67 doesn't exist in Fahrenheit scale.")
        else:
            if conversionTemperatureUnit == "C":
                convertedTemperature = (enteredTemperature - 32) * 5 / 9
                print(f"The temperature in Celsius is: {convertedTemperature:,.3f}")
            elif conversionTemperatureUnit == "K":
                convertedTemperature = ((enteredTemperature - 32) * 5 / 9) + 273.15
                print(f"The temperature in Kelvin is: {convertedTemperature:,.3f}")
    elif enteredTemperatureUnit == "K":
        if enteredTemperature < 0:
            print("Temperature below 0 doesn't exist in Kelvin scale.")
        else:
            if conversionTemperatureUnit == "C":
                convertedTemperature = enteredTemperature - 273.15
                print(f"The temperature in Celsius is: {convertedTemperature:,.3f}")
            elif conversionTemperatureUnit == "F":
                convertedTemperature = (9 * (enteredTemperature - 273.15)) / 5 + 32
                print(f"The temperature in Fahrenheit is: {convertedTemperature:,.3f}")
    else:
        print("Encountered unknown unit. Please try again.")
def sliceEmailAddress():
    email = input("Enter your e-mail: ")
    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]
    print(f"Your username is {username}, and your domain name is {domain}.")
def arcDistanceCalculator():
    radius = float(input("What is the radius of the circle [In meter/s]: "))
    theta = float(input("What is the theta angle of the arc: "))
    arcDistance = (theta / 360) * 2 * math.pi * radius
    print(f"The arc distance is {arcDistance} meter/s.")
def sectorAreaCalculator():
    radius = float(input("What is the radius of the circle [In meter/s]: "))
    theta = float(input("What is the theta angle of the arc: "))
    arcDistance = (theta / 360) * 2 * math.pi * pow(radius, 2)
    print(f"The sector is {arcDistance} meter^2/s.")
def countdownProgram():
    try:
        enteredTime = input("How long do you want the timer to last [Hour:Minute:Second] : ")
        enteredHour = int(enteredTime[0:2])
        enteredMinute = int(enteredTime[3:5])
        enteredSecond = int(enteredTime[6:8])       
        totalSeconds = enteredHour*3600+enteredMinute*60+enteredSecond
        for i in range(totalSeconds, 0, -1):
            displayingSecond = i%60
            displayingMinute = int(i/60)%60
            displayingHour = int(i/3600)%60
            print(f"{displayingHour:02}:{displayingMinute:02}:{displayingSecond:02}")
            time.sleep(1)
        print("Countdown finished successfully.")
    except: ValueError
    print("Check if entered values are correct.")
def surfaceAreaOfSphere():
    radius = float(input("What is the radius of the sphere [In meter/s]: "))
    surfaceArea = 4 * math.pi * pow(radius, 2)
    print(f"The surface area of the sphere is {surfaceArea:,.3f} meter^2/s")
def volumeOfSphere():
    radius = float(input("What is the radius of the sphere [In meter/s]: "))
    volume = 4/3 * math.pi * pow(radius, 3)
    print(f"The volume of the sphere is {volume:,.3f} meter^3/s")
def surfaceAreaOfThePrism():
    areaOfTheBase = float(input("What is the area of the base: "))  
    perimeterOfTheBase = float(input("What is the perimeter of the base: ")) 
    height = float(input("What is the height of the prism"))
    surfaceArea = 2 * areaOfTheBase + perimeterOfTheBase * height
    print(f"The surface area of the prism is {surfaceArea:,.3f}")
def creditCardValidatorProgram():
    sumOfOddNumbers = 0
    sumOfEvenNumbers = 0
    sumOfSumOfEvenNumbersSumOfOddNumbers = 0
    enteredCreditCardNumber = input("Enter a credit card number: ")
    enteredCreditCardNumber = enteredCreditCardNumber.replace("-", "")
    enteredCreditCardNumber = enteredCreditCardNumber.replace(" ", "")
    enteredCreditCardNumber = enteredCreditCardNumber[::-1]
    for x in enteredCreditCardNumber[::2]:
        sumOfOddNumbers += int(x)
    for x in enteredCreditCardNumber[1::2]:
        x = int(x) * 2
        if x >= 10:
            sumOfEvenNumbers += (1+ (x % 10)) 
        else:
            sumOfEvenNumbers += x
    sumOfSumOfEvenNumbersSumOfOddNumbers = sumOfEvenNumbers + sumOfOddNumbers
    if sumOfSumOfEvenNumbersSumOfOddNumbers % 10 == 0:
        enteredCreditCardNumber = enteredCreditCardNumber[::-1]
        print(f"The credit card number ({enteredCreditCardNumber}) is valid.")
    else:
        print(f"The credit card number ({enteredCreditCardNumber}) is not valid.")
def shoppingCart():
    items = []
    prices = []
    total = 0
    while True:
        item = input("What item would you like to buy [press 'Q' to quit]: ")
        if item.upper() != "Q":
            price = int(input("What is the price of the item: "))
            items.append(item)
            prices.append(price)
            total += price
        else:
            break
    print(f"You have bought {items} and the prices are {prices} and total is ${total}.")
def quizGame():
    questions = ("1. How many elements does the periodic table elements have? ",
                 "2. What is the farthest planet in our solar system? ",
                 "3. Which animal lays the largest eggs? ",
                 "4. What is the biggest planet in our solar system? ",
                 "5. How many boons are thee is a human body? ",
                 "6. What is the most abundant gas in Earth's atmosphere? ",
                 "7. Which year was Bangladesh declared independent? ",
                 "8. What is the smallest planet in our solar system? ",
                 "9. How many planets are there in your solar system? ",
                 "10. What is the hottest planet in our solar system? ",)
    options = (("A. 120", "B. 180", "C. 118", "D. 121"),
               ("A. Uranus", "B. Neptune", "C. Jupiter", "D. Mars"),
               ("A. Horse", "B. Whale", "C. Ostrich", "D. Elephant"),
               ("A. Jupiter", "B. Saturn", "C. Neptune", "D. Mercery"),
               ("A. 206", "B. 200", "C. 131", "D. 231"),
               ("A. Nitrogens", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
               ("A. 1870", "B. 1871", "C. 1970", "D. 1971"), 
               ("A. Mercery", "B. Venus", "C. Mars", "D. Earth"),
               ("A. 8", "B. 9", "C. 6", "D. 7"),
               ("A. Mercery", "B. Earth", "C. Venus", "D. Uranus"))
    answers = ("C", "B", "C", "A", "A", "A", "D", "A", "A", "C")
    guesses = []
    score = 0
    questionNumber = 0
    for question in questions:
        print(question)
        print("---------------")
        for option in options[questionNumber]:
            print(option)
        guess = input("Enter the answer [A,B,C,D]: ").upper()
        guesses.append(guess)
        if guess == answers[questionNumber]:
            score += 1
            print("\nCORRECT\n")
        else:
            print("INCORRECT")
            print(f"The right answer is {answers[questionNumber]}.\n")
        questionNumber += 1
    print("\n\n\n------------------------------")
    print(f"\n\nYour total score is {score}.")
def concessionStandProgram():
    menu = {"pizza": 3.00,
                "nachos": 4.50,
                "popcorn": 6.00,
                "fries": 2.50,
                "chips": 1.00,
                "pretzel": 3.50,
                "soda": 3.00,
                "lemonade": 4.25}
    cart = []
    total = 0

    print("--------- MENU ---------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("------------------------")

    while True:
        food = input("Select an item (q to quit): ").lower()
        if food == "q":
            break
        elif menu.get(food) is not None:
            cart.append(food)

    print("------ YOUR ORDER ------")
    for food in cart:
        total += menu.get(food)
        print(food, end=" ")

    print()
    print(f"Total is: ${total:.2f}")













concessionStandProgram()