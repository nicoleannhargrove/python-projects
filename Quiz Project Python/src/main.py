#Creating the list of question objects from data.py.
#question_bank is an empty list.
#Using question_data, question_text is used to store value of text.
#question_answer is used to store value of answer.
#new_question stores both question_text and question_answer.
#We use .append to add a new_question to question_bank.
#quiz populates QuizBrain with the question_bank
#Using while loop to ensure tha the loop continues as long as there are questions

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    #question_text = question["text"]
    #question_answer = question["answer"]
    #new_question = Question(question_text, question_answer)
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was:  {quiz.score}/{quiz.question_number}")