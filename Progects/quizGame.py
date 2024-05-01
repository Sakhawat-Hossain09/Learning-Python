def quizGame():
    questions = ("1. How many elements does the periodic table elements have? ",
                 "2. What is the farthest planet in our solar system? ",
                 "3. Which animal lays the largest eggs? ",
                 "4. What is the biggest planet in our solar system? ",
                 "5. How many boons are thee is a human body? ",
                 "6. What is the most abundant gas in Earth's atmosphere? ",
                 "7. Which year was Bangladesh declared independent? ",
                 "8. What is the smallest planet in our solar system? ",
                 "9. How many planets are there in your solar system? ",
                 "10. What is the hottest planet in our solar system? ",)
    options = (("A. 120", "B. 180", "C. 118", "D. 121"),
               ("A. Uranus", "B. Neptune", "C. Jupiter", "D. Mars"),
               ("A. Horse", "B. Whale", "C. Ostrich", "D. Elephant"),
               ("A. Jupiter", "B. Saturn", "C. Neptune", "D. Mercery"),
               ("A. 206", "B. 200", "C. 131", "D. 231"),
               ("A. Nitrogens", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
               ("A. 1870", "B. 1871", "C. 1970", "D. 1971"), 
               ("A. Mercery", "B. Venus", "C. Mars", "D. Earth"),
               ("A. 8", "B. 9", "C. 6", "D. 7"),
               ("A. Mercery", "B. Earth", "C. Venus", "D. Uranus"))
    answers = ("C", "B", "C", "A", "A", "A", "D", "A", "A", "C")
    guesses = []
    score = 0
    questionNumber = 0
    for question in questions:
        print(question)
        print("---------------")
        for option in options[questionNumber]:
            print(option)
        guess = input("Enter the answer [A,B,C,D]: ").upper()
        guesses.append(guess)
        if guess == answers[questionNumber]:
            score += 1
            print("\nCORRECT\n")
        else:
            print("INCORRECT")
            print(f"The right answer is {answers[questionNumber]}.\n")
        questionNumber += 1
    print("\n\n\n------------------------------")
    print(f"\n\nYour total score is {score}.")
quizGame()