def convertToint(filename):
  try:
    with open(filename, "r") as f:
      data = f.read().strip()
      return int(data)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None
  except ValueError:
    print(f"Error: The content of '{filename}' is not a valid number.")
    return None

def commendInput():
  print("To check your current balance type ['get balance -a']")
  print("To check what you can do type['check avltm -a']")
  print("To bye something type ['get (item name)]")
  print("")
  userRequest = input("What do you want to do: ")
  return userRequest
commendInput = commendInput()
point = convertToint("Progects//lifePointTracker//lifePointTracker.txt")
if commendInput == "get balance -a":
  print(f"Your current score is {point}")
elif commendInput == "check avltm -a":
  match point:
    case 10:
      print("\nYou can watch 10 short form video type ['shortVideo'] to purchase this item.")
    case 10:
      print("\nYou can watch 1 long form video type ['longVideo'] to purchase this item.")
    case _:
      print("You can't bye anything.")