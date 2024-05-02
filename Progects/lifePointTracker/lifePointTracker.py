def convert_to_int(filename):
    """
This function attempts to convert the contents of a text file to an integer.
      
    Args:
              filename: The name of the text file.
              
                Returns:
                      The integer value from the file, or None if the conversion fails.
                        """
                        
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
                                                              
                                                              # Example usage
                                                              filename = "numbers.txt"
                                                              number = convert_to_int(filename)
                                                              
                                                              if number is not None:
                                                                print(f"The integer from '{filename}' is: {number}")
                                                                Use code with caution.
                                                                content_copy
                                                                This code defines a function convert_to_int that takes the filename as input. It uses a try-except block to handle potential errors:
                                                                
                                                                FileNotFoundError: If the file is not found, it prints an error message and returns None.
                                                                ValueError: If the file content is not a valid number (e.g., contains text), it prints an error message and returns None.
                                                                If the conversion is successful, the function returns the integer value.
                                                                
                                                                The example usage demonstrates how to call the function and handle the returned value.
                                                                
                                                                
                                                                
                                                                
                                                                tune
                                                                
                                                                share
                                                                
                                                                
                                                                more_vert
                                                                
                                                                
                                                                expand_content
                                                                add_photo_alternatephoto_camera
                                                                
                                                                mic
                                                                send
                                                                shortFormVideo  = ("You can now watch 10 short form video.", 10)
longVideo = ("You can now watch 1 long form video. ", 10)
print("Avalable functions are listed below:")
print("1. check balence ['get balence -a']")
print("2. See what can be bought ['check avltm -a']")
print("2. Add to your balence ['add balence ('Amount')']")
userRequest = input("What do you want to do: ")
pointsFile = "Progects/lifePointTracker/lifePointTracker.txt"
pointsInfo = open(pointsFile, 'r')
points = int(pointsInfo)
if userRequest == "get balence -a":
    print(f"Your point is {points.read()}")
elif userRequest == "check avltm -a":
  if points >= shortFormVideo[1]:
     print(shortFormVideo[0])

