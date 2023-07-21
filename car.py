import random
from turtle import Turtle

cars_count = 0
car_colors = ["red", "blue", "brown", "orange", "black", "white", "purple", "pink", "cyan"]
class Car(Turtle):
    def __init__(self, position):
        global cars_count
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.turtlesize(1, 2)
        self.color(self.rnd_color())
        self.setposition(position)
        cars_count += 1

    def rnd_color(self):
        return random.choice(car_colors)

    def go(self):
        self.forward(1)
