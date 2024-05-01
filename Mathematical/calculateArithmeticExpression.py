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
