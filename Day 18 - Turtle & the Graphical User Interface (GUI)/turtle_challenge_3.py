from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

colors = ['cornflower blue','midnight blue','cyan','steel blue','light sea green','dark slate gray']

sides = 3
while sides < 11:
    for i in range(0,sides):
        turtle.forward(100)
        turtle.left(360/sides)
    sides += 1
    turtle.color(random.choice(colors))

screen.exitonclick()