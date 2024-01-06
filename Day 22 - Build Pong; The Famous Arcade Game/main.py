from turtle import Screen
from paddle_settings import Paddle
from ball import Ball
from pong_scoreboard import Score_board
import time

time_sleep = 0.1

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.tracer(0)

paddle_1 = Paddle((-350,0))
paddle_2 = Paddle((350,0))
screen.listen()
screen.onkey(paddle_2.move_up,'Up')
screen.onkey(paddle_2.move_down,'Down')
screen.onkey(paddle_1.move_up,'w')
screen.onkey(paddle_1.move_down,'s')

game_on = True

score_board = Score_board()
ball = Ball()

def refresh_game(side):
    global time_sleep
    if ball.xcor() > 410:
        ball.reset_pos(side)
        score_board.score_increase(side)
    elif ball.xcor() < -410:
        ball.reset_pos(side)
        score_board.score_increase(side)
    
    paddle_1.reset_pong()
    paddle_2.reset_pong()
    time_sleep -= 0.005
    

while game_on:
    time.sleep(time_sleep)
    ball.move()

    if ball.distance(paddle_2) <= 40 or ball.distance(paddle_1) <= 40:
        ball.paddle_coll()

    if ball.xcor() > 410:
        refresh_game('left')
    elif ball.xcor() < -410:
        refresh_game('right')
    

    screen.update()

screen.exitonclick()