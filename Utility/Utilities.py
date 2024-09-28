import math

class Mathematical:
    """
    A class to perform various mathematical operations.
    """

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


def main():
    mathematical = Mathematical()
    print(mathematical.calculate(first_number=100, second_number=10, operator="+"))

if __name__ == "__main__":
    main()