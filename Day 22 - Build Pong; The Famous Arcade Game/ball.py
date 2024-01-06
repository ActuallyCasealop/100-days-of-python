from turtle import Turtle
import random
heading = [60,120,240,300]

pad_coll = False

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.seth(random.choice(heading))
        self.move()
    
    def move(self):
        self.forward(20)
        if self.ycor() > 290 or self.ycor() < -290:
            self.border_coll()

    def border_coll(self):
        global pad_coll
        if pad_coll == False:
            if self.heading() == 60:
                self.seth(300)
            elif self.heading() == 120:
                self.seth(240)
            elif self.heading() == 240:
                self.seth(120)
            elif self.heading() == 300:
                self.seth(60)
        else:
            pad_coll = False
            self.border_coll()
    
    def paddle_coll(self):
        global pad_coll
        if pad_coll == False:
            if self.heading() == 60:
                self.seth(120)
            elif self.heading() == 120:
                self.seth(60)
            elif self.heading() == 240:
                self.seth(300)
            elif self.heading() == 300:
                self.seth(240)
        pad_coll = True
    
    def reset_pos(self, side):
        self.setpos(0,0)
        if side == 'left':
            self.seth(random.choice((120,240)))
        elif side == 'right':
            self.seth(random.choice((60,300)))