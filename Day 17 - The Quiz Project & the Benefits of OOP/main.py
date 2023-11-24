from data import question_data
from quiz_brain import QuizBrain
import random, os

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_question():
    quiz_brain.next_question()
print(f"You have completed the Challenge. Final Score: {quiz_brain.score}")