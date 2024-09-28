def convertTemperature():
    entered_temperature = int(input("What is the temperature you want to convert: "))
    entered_temperature_unit = input("Which unit is the temperature in [Celsius(C), Fahrenheit(F), Kelvin(K)]: ").upper()
    conversion_temperature_unit = input("In which unit do you want the temperature to be in [Celsius(C), Fahrenheit(F), Kelvin(K)]: ").upper()
    if entered_temperature_unit == "C":
        if entered_temperature < -273.15:
            print("Temperature below -273.15 doesn't exist in Celsius scale.")
        else:
            if conversion_temperature_unit == "K":
                entered_temperature_unit = entered_temperature + 273.15
                print(f"The temperature in Kelvin is: {entered_temperature_unit:,.3f}")
            elif conversion_temperature_unit == "F":
                entered_temperature_unit = (9 * entered_temperature) / 5 + 32
                print(f"The temperature in Fahrenheit is: {entered_temperature_unit:,.3f}")
    elif entered_temperature_unit == "F":
        if entered_temperature < -459.67:
            print("Temperature below -459.67 doesn't exist in Fahrenheit scale.")
        else:
            if conversion_temperature_unit == "C":
                entered_temperature_unit = (entered_temperature - 32) * 5 / 9
                print(f"The temperature in Celsius is: {entered_temperature_unit:,.3f}")
            elif conversion_temperature_unit == "K":
                entered_temperature_unit = ((entered_temperature - 32) * 5 / 9) + 273.15
                print(f"The temperature in Kelvin is: {entered_temperature_unit:,.3f}")
    elif entered_temperature_unit == "K":
        if entered_temperature < 0:
            print("Temperature below 0 doesn't exist in Kelvin scale.")
        else:
            if conversion_temperature_unit == "C":
                entered_temperature_unit = entered_temperature - 273.15
                print(f"The temperature in Celsius is: {entered_temperature_unit:,.3f}")
            elif conversion_temperature_unit == "F":
                entered_temperature_unit = (9 * (entered_temperature - 273.15)) / 5 + 32
                print(f"The temperature in Fahrenheit is: {entered_temperature_unit:,.3f}")
    else:
        print("Encountered unknown unit. Please try again.")


def main():
    convertTemperature()

if __name__ == "__main__":
    main()