from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.seth(90)
        self.setpos(STARTING_POSITION)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_player()
    
    def reset_player(self):
        self.setpos(STARTING_POSITION)
