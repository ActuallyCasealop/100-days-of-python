from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()

for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)

screen.exitonclick()