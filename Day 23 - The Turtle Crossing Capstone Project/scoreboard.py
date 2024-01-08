from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-215,260)
        self.level = 1
        self.write(f'Level: {self.level}',align='center',font=FONT)
    
    def scoreboard_refresh(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}',align='center',font=FONT)
    
    def game_over(self):
        self.setpos(0,0)
        self.write(f'GAME OVER',align='center',font=FONT)