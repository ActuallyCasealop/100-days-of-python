from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.car_list = []
        self.generate_cars()
        self.display_cars()

    def generate_cars(self):
        for new_car in range(0,10):
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
    
    def display_cars(self):
        for car in self.car_list:
            car.goto((random.randint(-280,280),random.randint(-280,280)))
