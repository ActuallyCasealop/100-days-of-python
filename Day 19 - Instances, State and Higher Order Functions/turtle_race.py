from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500,height=400)

colors = ['blue','red','green','yellow','pink','black']

user_choice = screen.textinput(title='Make your bet!',prompt='Which turtle would win?').lower()
if user_choice not in colors:
    user_choice = screen.textinput(title='Make your bet!',prompt='Which turtle would win?').lower()


turtles = []

race_is_on = True

y_loc = -100
for i in range(0,6):
    turts = Turtle(shape='turtle')
    turts.color(colors[i])
    turtles.append(turts)
    turts.penup()
    y_loc += 30
    turts.goto(x=-230,y=y_loc)

while race_is_on:
    for turts in turtles:
        if turts.xcor() >= 200:
            race_is_on = False
            if turts.pencolor() == user_choice:
                print(f'You Win! {turts.pencolor()} won the race.')
            else:
                print(f'You Lose! {turts.pencolor()} won the race.')
        turts.forward(random.randint(0,15))
        turts_position = turts.pos()

screen.exitonclick()