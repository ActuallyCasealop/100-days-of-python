class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.score = 0
        self.list = q_list
    
    def still_have_question(self): 
        return self.number < len(self.list)
    
    def next_question(self):
        user_input = input(f"Q.{self.number + 1} : {self.list[self.number].text} True/False\n>>>: ").lower()
        self.check_answer(user_input, self.list[self.number].answer.lower())

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"Correct. Current Score: {self.score}/{len(self.list)}")
        else:
            print(f"Incorrect; the right answer is: {self.list[self.number].answer}")
        self.number += 1


    