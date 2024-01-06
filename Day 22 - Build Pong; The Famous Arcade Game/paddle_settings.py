from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.setpos(position)
    
    def move_up(self):
        self.sety(self.ycor()+20)
    
    def move_down(self):
        self.sety(self.ycor()-20)
    
    def reset_pong(self):
        self.setpos(self.position)