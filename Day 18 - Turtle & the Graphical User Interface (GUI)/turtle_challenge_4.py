from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

turtle.pensize(width=10)
direction = [0,90,180,270]

turtle.speed('fast')

colors = ['cornflower blue','midnight blue','cyan','steel blue','light sea green','dark slate gray']

for i in range(200):
    turtle.forward(20)
    turtle.left(random.choice(direction))
    turtle.color(random.choice(colors))


    

screen.exitonclick()