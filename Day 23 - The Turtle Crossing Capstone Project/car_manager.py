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
        self.carspeed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for new_car in range(0,30):
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            self.car_list.append(new_car)
    
    def display_cars(self):
        for car in self.car_list:
            car.setpos(random.randint(-280,280),random.randint(-250,280))
    
    def move_cars(self):
        for car in self.car_list:
            car.setx(car.xcor() + self.carspeed)
            if car.xcor() > 310:
                self.reset_car_pos(car)
    
    def reset_car_pos(self, car):
        car.setpos(-310,random.randint(-250,280))
    
    def increment_speed(self):
        self.carspeed += MOVE_INCREMENT
