import random


def python_trivia_game():
    questions_list: list = list(questions.keys())
    total_questions: int = 5
    score: int = 0

    selected_questions: list = random.sample(questions_list, total_questions)

    for index, question in enumerate(selected_questions):
        print(f"{index + 1}. {question}")
        user_answer: str = input("Your answer: ").lower().strip()
        correct_answer: str = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer is: {correct_answer}.\n")

    print(f"Game Over!\n Your final score is: {score}/{total_questions}")


if __name__ == "__main__":
    questions: dict = {
        "What is the keyword to define a function in Python?": "def",
        "Which data type is used to store True or False values?": "boolean",
        "What is the correct file extension for Python files?": ".py",
        "Which symbol is used to comment in Python?": "#",
        "What function is used to get input from the user?": "input",
        "How do you start a for loop in Python?": "for",
        "What is the output of 2 ** 3 in Python?": "8",
        "What keyword is used to import a module in Python?": "import",
        "What does the len() function return?": "length",
        "What is the result of 10 // 3 in Python?": "3",
        "Which built-in function is used to find the maximum value in a list?": "max",
        "Which method is used to add an element to the end of a list?": "append",
        "Which keyword is used to handle exceptions in Python?": "try",
        "What is the purpose of the '__init__' method in a Python class?": "constructor",
        "What type of error occurs when you try to access an index that is out of bounds in a list?": "indexerror",
        "Which data structure in Python is unordered and contains unique elements?": "set",
    }

    python_trivia_game()
