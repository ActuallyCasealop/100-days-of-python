from turtle import Turtle

coor = [(-20,0),(-40,0),(-60,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]
    
    def create_snake(self):
        for i in coor:
            self.add_segment(i)
    
    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        self.segments.append(new_segment)
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
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
