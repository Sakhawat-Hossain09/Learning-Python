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
