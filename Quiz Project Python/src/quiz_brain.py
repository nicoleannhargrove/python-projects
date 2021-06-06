#Creating a class called QuizBrain.
#self.question_number is assigned 0.
#self.score is assigned 0.
#self.question_list is assigned q_list.
#next_question function, current_question is assigned the list of questions.
#To locate the current_question, question_number stored question_list.
#We increatement question_number count by +1.
#Use input function to get user answer and store its value.
#We check the user's answer against our answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print ("You got it right!")
        else:
            print ("That's wrong")
        print (f"The correct answer was:  {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number} ")
        print ("\n")