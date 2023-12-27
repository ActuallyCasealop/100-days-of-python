from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.sety(280)
        self.color('white')
        self.hideturtle()
        self.init_scoreboard()
    
    def init_scoreboard(self):
        self.write(f'Current Score: {self.score}',align='center',font=('arial',12,'normal'))
    
    def score_increase(self):
        self.score += 1
        self.clear()
        self.init_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over.',align='center',font=('arial',12,'normal'))