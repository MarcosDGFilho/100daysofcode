import questionary
from questionary import question

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            questionary.print("Correct answer", style="bold italic fg:darkblue")
            return True
        else:
            questionary.print("Wrong answer", style="bold italic fg:darkred")
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = questionary.select(f"Q.{self.question_number+1} {question.text}", choices=["True","False"]).ask()
        if self.check_answer(user_answer, question.answer):
            self.score += 1
        self.question_number += 1

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

