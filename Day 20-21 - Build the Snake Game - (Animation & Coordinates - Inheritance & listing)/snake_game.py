from turtle import Screen
import time, food
from scoreboard import Scoreboard
from snake_settings import Snake

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

game_on = True

snake = Snake()
food = food.Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.turn_up,'Up')
screen.onkey(snake.turn_down,'Down')
screen.onkey(snake.turn_left,'Left')
screen.onkey(snake.turn_right,'Right')

while game_on:
    snake.initialize()
    
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_on = False
        score_board.score_reset()
        score_board.game_over()

    if snake.snake_head.distance(food) < 15:
        score_board.score_increase()
        snake.extend()
        food.refresh()
    
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_on = False
            score_board.score_reset()
            score_board.game_over()
    

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
