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
