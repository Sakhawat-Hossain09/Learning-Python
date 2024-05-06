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
  print("Available functions are listed below:")
  print("1. check balance ['get balance -a']")
  print("2. See what can be bought ['check avltm -a']")
  print("2. Add to your balance ['add balance ('Amount')']")
  userRequest = input("What do you want to do: ")
  if userRequest != " ":
    return None

  else:
    print("Redo the procces.")
    commendInput()
    return str(userRequest)

commendInput()
shortFormVideo  = ("You can now watch 10 short form videos.", 10)
longVideo = ("You can now watch 1 long form video. ", 10)


pointsFile = "Progects/lifePointTracker/lifePointTracker.txt"
pointsInfo = open(pointsFile, 'r')
points = int(pointsInfo)

convertToint("Progects//lifePointTracker//lifePointTracker.txt")
'''if userRequest == "get balence -a": print(f"Your point is {points.read()}") elif userRequest == "check avltm -a": print("Hello world") elif points >= shortFormVideo[1]: print(shortFormVideo[0]'''