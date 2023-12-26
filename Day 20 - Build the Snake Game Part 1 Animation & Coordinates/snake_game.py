from turtle import Screen
import time
from snake_settings import Snake

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

game_on = True

snake = Snake()

screen.listen()
screen.onkey(snake.turn_up,'Up')
screen.onkey(snake.turn_down,'Down')
screen.onkey(snake.turn_left,'Left')
screen.onkey(snake.turn_right,'Right')

while game_on:
    snake.initialize()
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
