# Python Trivia Game

This is a simple command-line Python trivia game designed to test your knowledge of basic Python concepts.

## How to Play

1.  **Save the code:** Copy the provided Python code and save it as a `.py` file (e.g., `trivia_game.py`).
2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command:
    ```bash
    python trivia_game.py
    ```
3.  **Answer the questions:** The game will present you with a series of multiple-choice questions about Python. Type your answer in the terminal and press Enter.
4.  **See your score:** After answering a set number of questions, the game will display your final score.

## Features

* **Randomized Questions:** Each time you play, a random selection of questions from the available pool will be presented.
* **Immediate Feedback:** The game tells you immediately whether your answer is correct or incorrect and shows the correct answer if you are wrong.
* **Score Tracking:** Your final score is displayed at the end of the game, showing how many questions you answered correctly out of the total asked.
* **Expandable Question Pool:** The questions and answers are stored in a Python dictionary, making it easy to add more questions to increase the game's variety.

## How to Add More Questions

To add more questions to the game, simply modify the `questions` dictionary within the Python script. The dictionary follows the format:

```python
questions: dict = {
    "Your Question Here?": "Correct Answer",
    "Another Python Question?": "The Right Response",
    # Add more questions and answers here
}
