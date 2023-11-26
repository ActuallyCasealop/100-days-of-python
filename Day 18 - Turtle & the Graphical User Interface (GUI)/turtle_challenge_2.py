from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

for i in range(0,20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen.exitonclick()