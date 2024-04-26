#Question to be asked
quiz_questions= [
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyperlink Text Markup Language", "B. Hyper Transfer Markup Language", "C. Hypertext Markup Language", "D. High-Level Text Markup Language"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for web development?",
        "options": ["A. Python", "B. Java", "C. Ruby", "D. JavaScript"],
        "answer": "D"
    },
    {
        "question": "What is the primary function of CSS in web development?",
        "options": ["A. Data storage", "B. Styling and layout", "C. Server-side scripting", "D. Database management"],
        "answer": "B"
    },
    {
        "question": "What does the acronym SQL stand for?",
        "options": ["A. Structured Query Language", "B. Simple Query Language", "C. Standard Query Language", "D. Sequential Query Language"],
        "answer": "A"
    },
    {
        "question": "What does API stand for in the context of web development?",
        "options": ["A. Application Programming Interface", "B. Advanced Programming Interface", "C. Automated Program Interaction", "D. All of the above"],
        "answer": "A"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "In Python, which library is commonly used for data visualization?",
        "options": ["A. NumPy", "B. Pandas", "C. Matplotlib", "D. TensorFlow"],
        "answer": "C"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. int", "B. double", "C. list", "D. tuple"],
        "answer": "B"
    },
    {
        "question": "What is the result of the following Python code: print(3 + '3')a ?",
        "options": ["A. 6", "B. '33'", "C. TypeError", "D. '6'"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for developing mobile applications?",
        "options": ["A. Java", "B. Python", "C. C#", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "What is the purpose of the `if` statement in programming?",
        "options": ["A. To perform a loop", "B. To declare a function", "C. To make decisions based on conditions", "D. To define a class"],
        "answer": "C"
    }
]
#display quiz_data and checks given input is correct or wrong
def check_question(question_data):
    print(question_data["question"]) #question will display
    for option in question_data["options"]:  #interating each option
        print(option)  #display options
    user_input = input("Enter your answer (A,B,C,D): ").upper()   #takes options as input and convert it into capital alphabets
    while user_input.upper() not in ['A', 'B', 'C', 'D']:
        user_input = input("Invalid input! Enter your answer (A, B, C, D): ").upper()  #checks invalid inputs
    if user_input == question_data["answer"]:  
        return True
    else:
        return False
score=0   #empty variable to count score
s=len(quiz_questions)
print("       ********************Welcome to Basic Quiz test********************         ")
for i in range(s):
    print(f'Question {i} of {s}')  #diaplay question number out of total questions
    if check_question(quiz_questions[i]):   #calling def funtion and checks each answer
        print("Correct!")  #feedback on correct answer
        score += 1
    else:
        print(f"Wrong! The correct answer is {quiz_questions[i]['answer']}.")  #feeback on wrong answer
    print("Your score is",score)  #display score on every question
    print("\n======================================================================================")
print(f"Your final score is {score}/{s}.")  #display overall score
print("Correct answers are",score)  #no.of correct answers
print("Wrong answers are ",s-score)   #no.of wrong answers
