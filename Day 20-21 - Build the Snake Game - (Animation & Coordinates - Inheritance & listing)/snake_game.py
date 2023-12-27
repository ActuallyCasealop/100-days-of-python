from turtle import Screen
import time, food
from snake_settings import Snake

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

game_on = True

snake = Snake()
food = food.Food()

screen.listen()
screen.onkey(snake.turn_up,'Up')
screen.onkey(snake.turn_down,'Down')
screen.onkey(snake.turn_left,'Left')
screen.onkey(snake.turn_right,'Right')

while game_on:
    snake.initialize()

    if snake.snake_head.distance(food) < 15:
        food.refresh()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
