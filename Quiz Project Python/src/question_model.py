#Generating the initial function for the class named Question.
#q_text variable will store the questions.
#q_answer will store answers to questions.


class Question:
    def __init__(self, q_text, q_answer) :
        self.text = q_text
        self.answer = q_answer