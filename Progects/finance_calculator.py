"""
My Homework for video 1:
1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships) so they
can see how much they have left over each month.
2. Recreate the user input section to safely handle users inserting the wrong type without 
crashing the program.

"""
def finance_calculator(monthly_earning: float, tax_rate: float, currency: str) -> None:
    monthly_tax_deduction = monthly_earning * (tax_rate / 100)
    monthly_net_earning = monthly_earning - monthly_tax_deduction
    yearly_earning: float = monthly_earning * 12
    yearly_tax_deduction = monthly_tax_deduction * 12
    yearly_net_earning = monthly_net_earning * 12


    print("----------------------------------------------------------------")
    print(f"Your monthly earning is: {monthly_earning}.")
    print(f"Your tax rate is {tax_rate}.")
    print(f"Your monthly tax deduction is {monthly_tax_deduction}.")
    print(f"Your net income is {monthly_net_earning}.")
    print(f"Your yearly earning is: {yearly_earning}.")
    print(f"Your yearly tax deduction is: {yearly_tax_deduction}.")
    print(f"Your yearly net income is: {yearly_net_earning}.")
    print("----------------------------------------------------------------")




finance_calculator(monthly_earning=10000, tax_rate=35.7, currency="USD")