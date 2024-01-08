import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.move_cars()

    for car in cars.car_list:
        if player.distance(car) <= 20:
            print('hit')
            game_is_on = False
            score_board.game_over()
    
    if player.player_num == 1:
        cars.increment_speed()
        player.player_num = 0
        score_board.scoreboard_refresh()
    
    screen.update()

screen.exitonclick()
