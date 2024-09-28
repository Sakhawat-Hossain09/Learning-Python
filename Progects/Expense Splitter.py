#from Utilities import is_currency_supported


def expense_splitter(total_bill_amount: float, number_of_persons: int, currency: str, tip_percentage: float = 0, tax_rate: float = 0) -> None:
    """
    Calculates and prints the amount each person has to pay for a bill, considering tip and tax.

    Args:
        total_bill_amount: The total amount of the bill.
        number_of_persons: The number of people splitting the bill.
        currency: The currency used for the calculations.
        tip_percentage: The percentage of the bill to be added as a tip (default is 0).
        tax_rate: The tax rate applied to the bill (default is 0).
    """

    if number_of_persons <= 0:
        print("Error: Number of persons must be greater than 0.")

    if total_bill_amount <= 0:
        print("Error: Total bill amount must be greater than 0.")

    if not is_currency_supported(currency):
        print("Error: Invalid currency.")

    # Calculate tip and tax amounts
    tip_amount = total_bill_amount * (tip_percentage / 100)
    tax_amount = total_bill_amount * (tax_rate / 100)

    # Calculate total amount including tip and tax
    total_amount = total_bill_amount + tip_amount + tax_amount

    # Calculate amount per person
    amount_per_person = total_amount / number_of_persons

    # Round the result to two decimal places
    amount_per_person = round(amount_per_person, 2)

    print("----------------------------------------------------------------")
    print(f"The total bill amount is {total_bill_amount}.")
    print(f"Number of people to split is {number_of_persons}.")
    print(f"Tip amount is {tip_amount}.")
    print(f"Tax amount is {tax_amount}.")
    print(f"Each person has to pay {amount_per_person} {currency}.")
    print("----------------------------------------------------------------")


def main():
    while True:
        try:
            total_bill_amount = float(input("Enter the total bill amount: "))
            number_of_persons = int(input("Enter the number of persons: "))
            currency = input("Enter the currency (USD, EUR, GBP, JPY, CNY): ").upper()
            tip_percentage = float(input("Enter the tip percentage (in %): "))
            tax_rate = float(input("Enter the tax rate (in %): "))

            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    expense_splitter(total_bill_amount, number_of_persons, currency, tip_percentage, tax_rate)


if __name__ == "__main__":
    main()

