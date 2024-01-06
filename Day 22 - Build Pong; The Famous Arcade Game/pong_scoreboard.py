from turtle import Turtle

class Score_board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.sety(280)
        self.color('white')
        self.hideturtle()
        self.init_scoreboard()
    
    def init_scoreboard(self):
        self.write(f'{self.l_score} : {self.r_score}',align='center',font=('arial',12,'normal'))
    
    def score_increase(self,side):
        if side == 'left':
            self.l_score += 1
        elif side == 'right':
            self.r_score += 1
        self.clear()
        self.init_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over.',align='center',font=('arial',12,'normal'))