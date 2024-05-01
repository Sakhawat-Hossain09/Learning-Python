def convertWeight():
  weight = float(input("What is the weight: "))
  unit = input("Is it in Kilograms or Pounds (K,L): ").upper()
  if unit == "K":
    weight *= 2.205
    print(f"The weight in pounds is {weight:,.5f}.")
  elif unit == "L":
    weight /= 2.205 
    print(f"The weight in kilograms is {weight:,.5f}.")
  else:
    print("Encountered unknown unit. Please try again.")
