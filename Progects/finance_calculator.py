"""
My Homework for video 1:
1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships) so they
can see how much they have left over each month.
2. Recreate the user input section to safely handle users inserting the wrong type without 
crashing the program.

"""
def finance_calculator(monthly_earning: float, tax_rate: float, currency: str) -> None:
    yearly_earning: float = monthly_earning * 12
    monthly_tax_deduction = monthly_earning * (tax_rate / 100)
    yearly_tax_deduction = monthly_tax_deduction * 12
    monthly_net_earning = monthly_earning - monthly_tax_deduction
    yearly_net_earning = monthly_net_earning * 12


    print("----------------------------------------------------------------")
    print(f"Your monthly earning is: {monthly_earning}")

