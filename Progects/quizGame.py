import time

def quizGame():
    questions = [
        "How many elements does the periodic table have?",
        "What is the farthest planet in our solar system?",
        "Which animal lays the largest eggs?",
        "What is the biggest planet in our solar system?",
        "How many bones are there in a human body?",
        "What is the most abundant gas in Earth's atmosphere?",
        "Which year was Bangladesh declared independent?",
        "What is the smallest planet in our solar system?",
        "How many planets are there in our solar system?",
        "What is the hottest planet in our solar system?"
    ]

    options = [
        ["A. 120", "B. 180", "C. 118", "D. 121"],
        ["A. Uranus", "B. Neptune", "C. Jupiter", "D. Mars"],
        ["A. Horse", "B. Whale", "C. Ostrich", "D. Elephant"],
        ["A. Jupiter", "B. Saturn", "C. Neptune", "D. Mercury"],
        ["A. 206", "B. 200", "C. 131", "D. 231"],
        ["A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"],
        ["A. 1870", "B. 1871", "C. 1970", "D. 1971"],
        ["A. Mercury", "B. Venus", "C. Mars", "D. Earth"],
        ["A. 8", "B. 9", "C. 6", "D. 7"],
        ["A. Mercury", "B. Earth", "C. Venus", "D. Uranus"]
    ]

    answers = [
        "C",
        "B",
        "C",
        "A",
        "A",
        "A",
        "D",
        "A",
        "A",
        "C"
    ]

    guesses = []
    score = 0
    time_limit = 30  # Time limit in seconds

    for question_number in range(len(questions)):
        print(f"Question {question_number + 1}: {questions[question_number]}")
        print("---------------")
        for option in options[question_number]:
            print(option)

        start_time = time.time()
        guess = input("Enter the answer [A,B,C,D]: ").upper()
        end_time = time.time()

        elapsed_time = end_time - start_time
        if elapsed_time > time_limit:
            print(f"Time's up! The correct answer is {answers[question_number]}.\n")
            continue

        guesses.append(guess)
        if guess == answers[question_number]:
            score += 1
            print("\nCORRECT\n")
        else:
            print("INCORRECT")
            print(f"The right answer is {answers[question_number]}.\n")

    print("\n\n\n------------------------------")
    print(f"\n\nYour total score is {score}.")

quizGame()