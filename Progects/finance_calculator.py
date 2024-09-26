#My Homework for video 1:
#1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships) so they
#can see how much they have left over each month.
   
def finance_calculator(monthly_earning: float, tax_rate: float, currency: str) -> None:
    """
    Calculates and prints the monthly and yearly financial information based on the given
    monthly earning, tax rate, and currency.

    Args:
        monthly_earning: The monthly income of the user.
        tax_rate: The tax rate applied to the monthly income.
        currency: The currency used for the calculations.
    """

    # Calculate monthly deductions and net earnings
    monthly_tax_deduction = monthly_earning * (tax_rate / 100)
    monthly_net_earning = monthly_earning - monthly_tax_deduction

    # Calculate yearly values
    yearly_earning = monthly_earning * 12
    yearly_tax_deduction = monthly_tax_deduction * 12
    yearly_net_earning = monthly_net_earning * 12

    # Print the results
    print("----------------------------------------------------------------")
    print(f"Your monthly earning is: {monthly_earning}.")
    print(f"Your tax rate is {tax_rate}.")
    print(f"Your monthly tax deduction is {monthly_tax_deduction}.")
    print(f"Your net income is {monthly_net_earning}.")
    print(f"Your yearly earning is: {yearly_earning}.")
    print(f"Your yearly tax deduction is: {yearly_tax_deduction}.")
    print(f"Your yearly net income is: {yearly_net_earning}.")
    print("----------------------------------------------------------------")


def main():
    """
    The main function that handles user input and calls the finance calculator.
    """

    while True:
        try:
            # Get user input for currency, monthly earning, and tax rate
            currency = str(input("Enter your currency: ").upper())
            monthly_earning = float(input(f"Enter your monthly earning (in {currency}) (Use \"_\" as thousand separator ex: 10_000): "))
            tax_rate = float(input("Enter your tax rate (in %): "))

            # Break the loop if input is valid
            break
        except ValueError:
            # Handle invalid input and continue the loop
            print("Invalid input. Please enter a number for monthly earning and tax rate.")

    # Call the finance calculator with the user input
    finance_calculator(monthly_earning=monthly_earning, tax_rate=tax_rate, currency=currency)


if "__main__" == __name__:
    main()
