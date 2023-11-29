from turtle import Turtle, Screen
import random 

color_pallet= [(250, 246, 243), (248, 245, 246), (211, 154, 97), (52, 107, 132), (176, 78, 34), (238, 246, 243), (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157), (229, 197, 128), (231, 238, 242), (190, 88, 109), (55, 38, 19), (11, 51, 65), (44, 168, 125), (197, 122, 141), (50, 125, 120), (167, 21, 29), (225, 94, 80)]

def move():
    for _ in range(0,10):
        turtle.dot(20,random.choice(color_pallet))
        turtle.forward(50)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.speed('fastest')

screen = Screen()
screen.colormode(255)
screen.setup(500,500)

y_coordinate = -215

for _ in range(0,10):
    turtle.setposition(-230,y_coordinate)
    move()
    y_coordinate += 50

screen.exitonclick()