#list of questions
#store the answers
import random
  
questions = {
    "What is the keyword to define a function in python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in python?": "#",
    "What function is used to get input from the user": "input",
    "How do you start a for loop in python?": "for",
    "What is the output of 2**3 in python?": "8",
    "What keyword is used to import module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10//3 in Python?": "3" 
}

def trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

#randomly pick questions
    selected_questions = random.sample(questions_list, total_questions)

#ask the questions
    for index, question in enumerate(selected_questions):
        print(f"{index + 1}.{question}")
        user_answer = input("Your answer : ").lower().strip()
        correct_answer = questions[question]

#see if they are correct
#keep track of the score

        if user_answer == correct_answer.lower():
            print("Correct! \n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {correct_answer}.\n")

#tell the user their score
    print(f"Game Over! Your final score is: {score}/{total_questions}")



trivia_game()
