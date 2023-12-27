from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]
    
    def create_snake(self):
        segment_cor = 0
        for i in range(0,3):
            new_segment = Turtle(shape='square')
            self.segments.append(new_segment)
            new_segment.penup()
            new_segment.color('white')
            new_segment.setx(segment_cor)
            segment_cor -= 20
    
    def initialize(self):
        for i in range(len(self.segments)-1,0,-1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor,y_cor)
        self.snake_head.forward(20)
    
    def turn_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.seth(90)
    
    def turn_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.seth(270)

    def turn_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.seth(180)

    def turn_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.seth(0)