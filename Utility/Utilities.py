import math
import time
import random

class Progects:
    def __init__(self):
        pass        




    def sliceEmailAddress(self, email: str) -> None:
        username = email[:email.index("@")]
        domain = email[email.index("@") + 1:]
        print(f"Your username is {username}, and your domain name is {domain}.")



    #TODO: add variables in the bracket thing
    def shoppingCart(self):
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



    def ramdomNumberGenarator(self, min: float, max: float):
        randomNumber = random.uniform(min, max)  #ai did this
        print(randomNumber)



    def quizGame(self):
        questions = [
            "How many elements does the periodic table have?",
            "What is the farthest planet in our solar system?",
            "Which animal lays the largest eggs?",
            "What is the biggest planet in our solar system?",
            "How many bones are there in a human body?",
            "What is the most abundant gas in Earth's atmosphere?",
            "Which year was Bangladesh declared independent?",
            "What is the smallest planet in our solar system?",
            "How many planets are there in our solar system?",
            "What is the hottest planet in our solar system?"
        ]

        options = [
            ["A. 120", "B. 180", "C. 118", "D. 121"],
            ["A. Uranus", "B. Neptune", "C. Jupiter", "D. Mars"],
            ["A. Horse", "B. Whale", "C. Ostrich", "D. Elephant"],
            ["A. Jupiter", "B. Saturn", "C. Neptune", "D. Mercury"],
            ["A. 206", "B. 200", "C. 131", "D. 231"],
            ["A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"],
            ["A. 1870", "B. 1871", "C. 1970", "D. 1971"],
            ["A. Mercury", "B. Venus", "C. Mars", "D. Earth"],
            ["A. 8", "B. 9", "C. 6", "D. 7"],
            ["A. Mercury", "B. Earth", "C. Venus", "D. Uranus"]
        ]

        answers = [
            "C",
            "B",
            "C",
            "A",
            "A",
            "A",
            "D",
            "A",
            "A",
            "C"
        ]

        guesses = []
        score = 0
        time_limit = 30  # Time limit in seconds

        for question_number in range(len(questions)):
            print(f"Question {question_number + 1}: {questions[question_number]}")
            print("---------------")
            for option in options[question_number]:
                print(option)

            start_time = time.time()
            guess = input("Enter the answer [A,B,C,D]: ").upper()
            end_time = time.time()

            elapsed_time = end_time - start_time
            if elapsed_time > time_limit:
                print(f"Time's up! The correct answer is {answers[question_number]}.\n")
                continue

            guesses.append(guess)
            if guess == answers[question_number]:
                score += 1
                print("\nCORRECT\n")
            else:
                print("INCORRECT")
                print(f"The right answer is {answers[question_number]}.\n")

        print("\n\n\n------------------------------")
        print(f"\n\nYour total score is {score}.")


        def creditCardValidatorProgram(self, credit_card_number: str) -> None:
            sum_of_odd_digits = 0
            sum_of_even_digits = 0
            total_sum = 0
            credit_card_number = credit_card_number.replace("-", "")
            credit_card_number = credit_card_number.replace(" ", "")
            reversed_credit_card_number = credit_card_number[::-1]
            
            for digit in reversed_credit_card_number[::2]:
                sum_of_odd_digits += int(digit)
            
            for digit in reversed_credit_card_number[1::2]:
                doubled_digit = int(digit) * 2
                if doubled_digit >= 10:
                    sum_of_even_digits += (1 + (doubled_digit % 10))
                else:
                    sum_of_even_digits += doubled_digit
            
            total_sum = sum_of_even_digits + sum_of_odd_digits
            
            if total_sum % 10 == 0:
                print(f"The credit card number ({credit_card_number}) is valid.")
            else:
                print(f"The credit card number ({credit_card_number}) is not valid.")



    def createMadLibsStory(self, adjective1: str, adjective2: str, adjective3:str, adjective4: str, verb:str, noun:str,) -> None:
        print(f"Today I went to a {adjective1} zoo.")
        print(f"In an exhibit, I saw a {noun}.")
        print(f"The {noun} was {adjective2} and {verb}ing.")
        print(f"I was {adjective4}.")



    #TODO: fix line 174 in the concession stand program

    def concession_stand_program(self) -> None:
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
#            total += menu.get(food)
            print(food, end=" ")
        print()
        print(f"Total is: ${total:.2f}")

    
    def convertTemperature(self, entered_temperature: float, entered_temperature_unit: str, conversion_temperature_unit: str) -> float:
        converted_temperature: float
        if entered_temperature_unit == "C":
            if entered_temperature < -273.15:
                print("Temperature below -273.15 doesn't exist in Celsius scale.")
            else:
                if conversion_temperature_unit == "K":
                        converted_temperature = entered_temperature + 273.15
                elif conversion_temperature_unit == "F":
                        converted_temperature = (9 * entered_temperature) / 5 + 32
        elif entered_temperature_unit == "F":
            if entered_temperature < -459.67:
                print("Temperature below -459.67 doesn't exist in Fahrenheit scale.")
            else:
                if conversion_temperature_unit == "C":
                    converted_temperature = (entered_temperature - 32) * 5 / 9
                elif conversion_temperature_unit == "K":
                    converted_temperature = ((entered_temperature - 32) * 5 / 9) + 273.15
        elif entered_temperature_unit == "K":
            if entered_temperature < 0:
                print("Temperature below 0 doesn't exist in Kelvin scale.")
            else:
                if conversion_temperature_unit == "C":
                    converted_temperature = entered_temperature - 273.15
                elif conversion_temperature_unit == "F":
                    converted_temperature = (9 * (entered_temperature - 273.15)) / 5 + 32
        else:
            print("Encountered unknown unit. Please try again.")

        return converted_temperature



    def countdownProgram(self, starttingTime: str) -> None:

        try:
            enteredHour = int(starttingTime[0:2])
            enteredMinute = int(starttingTime[3:5])
            enteredSecond = int(starttingTime[6:8])       
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





class Mathematical:
    """
    A class to perform various mathematical operations.
    """


    def arc_distance_calculator(self, radius: float, theta_degrees: float) -> float:
        """
        Calculates the arc distance given a radius and an angle in degrees.

        Parameters:
            radius: The radius of the circle.
            theta_degrees: The angle in degrees.

        Returns:
            The arc distance.
        """
        arc_distance: float = (theta_degrees / 360) * 2 * math.pi * radius
        return arc_distance


    def calculate_circle_area(self, radius: float) -> float:
        """
        Calculates the area of a circle given its radius.

        Parameters:
            radius: The radius of the circle.

        Returns:
            The area of the circle.
        """
        area: float = math.pi * math.pow(radius, 2)
        return area

    def calculate_cube_volume(self, length: float, width: float, height: float) -> float:
        """
        Calculates the volume of a cube given its length, width, and height.

        Parameters:
            length: The length of the cube.
            width: The width of the cube.
            height: The height of the cube.

        Returns:
            The volume of the cube.
        """
        volume: float = length * width * height
        return volume

    def calculate_circle_circumference(self, radius: float) -> float:
        """
        Calculates the circumference of a circle given its radius.

        Parameters:
            radius: The radius of the circle.

        Returns:
            The circumference of the circle.
        """
        circumference: float = 2 * math.pi * radius
        return circumference

    def calculate_hypotenuse(self, side_a: float, side_b: float) -> float:
        """
        Calculates the hypotenuse of a right-angled triangle given the lengths of the other two sides.

        Parameters:
            side_a: The length of one side of the triangle.
            side_b: The length of the other side of the triangle.

        Returns:
            The length of the hypotenuse.
        """
        hypotenuse = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
        return hypotenuse

    def calculate_rectangle_area(self, length: float, width: float) -> float:
        """
        Calculates the area of a rectangle given its length and width.

        Parameters:
            length: The length of the rectangle.
            width: The width of the rectangle.

        Returns:
            The area of the rectangle.
        """
        area: float = length * width
        return area

    def surface_area_of_sphere(self, radius: float) -> float:
        """
        Calculates the surface area of a sphere given its radius.

        Parameters:
            radius: The radius of the sphere.

        Returns:
            The surface area of the sphere.
        """
        surface_area: float = 4 * math.pi * pow(radius, 2)
        return surface_area

    def surface_area_of_prism(self, area_of_base: float, perimeter_of_base: float, height: float) -> float:
        """
        Calculates the surface area of a prism given the area of the base, the perimeter of the base, and the height.

        Parameters:
            area_of_base: The area of the base of the prism.
            perimeter_of_base: The perimeter of the base of the prism.
            height: The height of the prism.

        Returns:
            The surface area of the prism.
        """
        surface_area = 2 * area_of_base + perimeter_of_base * height
        return surface_area

    def volume_of_sphere(self, radius: float) -> float:
        """
        Calculates the volume of a sphere given its radius.

        Parameters:
            radius: The radius of the sphere.

        Returns:
            The volume of the sphere.
        """
        volume = 4/3 * math.pi * pow(radius, 3)
        return volume

    def calculate(self, first_number: float, operator: str, second_number: float) -> float:
        """
        Calculates the result of an arithmetic expression.

        Args:
            first_number: The first number.
            operator: The arithmetic operator (+, -, *, /).
            second_number: The second number.

        Returns:
            The result of the arithmetic expression.

        Raises:
            ValueError: If the input is invalid.
            ZeroDivisionError: If the second number is 0 and the operator is '/'.
        """
        if operator not in "+-*/":
            raise ValueError("Invalid operator. Please use +, -, *, or /.")

        if second_number == 0 and operator == '/':
            raise ZeroDivisionError("Division by zero is not allowed.")

        result: float = 0
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        else:
            result = first_number / second_number

        return result

    def __init__(self):
        pass


    def is_currency_supported(self, currency: str) -> bool:
        """
        Checks if a given currency is supported.

        Args:
            currency: The currency to check.

        Returns:
            True if the currency is supported, False otherwise.
        """
        supported_currencies: tuple = ("USD", "EUR", "JPY", "GBP", "CAD", "CHF", "AUD", "NZD", "SEK", "NOK", "DKK", "INR", "CNY", "BRL", "RUB", "ZAR", "KRW", "MXN", "TRY")

        if not isinstance(currency, str):
            raise ValueError("Currency must be a string")

        currency = currency.upper()
        return currency in supported_currencies



def main():

    progects = Progects()

    # progects.concession_stand_program()
    print(progects.convertTemperature(entered_temperature=10, entered_temperature_unit="c", conversion_temperature_unit="f"))
    progects.countdownProgram(starttingTime="60:41:31")



if __name__ == "__main__":
     main()