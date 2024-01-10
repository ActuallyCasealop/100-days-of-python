from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.sety(280)
        self.color('white')
        self.hideturtle()
        self.init_scoreboard()
    
    def init_scoreboard(self):
        with open('Day 20-21 - Build the Snake Game - (Animation & Coordinates - Inheritance & listing)\score.txt',mode='r') as highscore:
            if int(highscore.read()) == 0:
                pass
            else:
                self.highscore = int(highscore.read())
        highscore.close()


        self.write(f'Current Score: {self.score} Highscore: {self.highscore}',align='center',font=('arial',12,'normal'))
    
    def score_increase(self):
        self.score += 1
        self.clear()
        self.init_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over.',align='center',font=('arial',12,'normal'))
    
    def score_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        with open('Day 20-21 - Build the Snake Game - (Animation & Coordinates - Inheritance & listing)\score.txt',mode='w') as highscore:
            highscore.write(self.highscore)
            highscore.close()