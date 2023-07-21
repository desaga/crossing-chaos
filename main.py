"""
In the game, the player's goal is to guide the turtle safely across a busy highway filled with fast-moving
vehicles, avoiding collisions and reaching the other side unharmed to complete each level. The objective is to test
the player's reflexes, timing, and strategic thinking to achieve a high score and advance through challenging
road-crossing scenarios.
"""
import random
import time

from turtle import Screen, Turtle
from scoreboard import ScoreBoard
from car import Car
from highway_manager import HighWayManager


def abort_game():
    global game_over
    game_over = True


def add_cars():
    for i in range(highway_manager.number_lines - 1):
        if random.randint(0, 1000) == 1:
            cars_pull.append(
                Car((280, -200 + i * 400 / highway_manager.number_lines + 200 / highway_manager.number_lines)))


def move_forward():
    player.forward(10)


PLAYER_START_POSITION = (-180, -250)
PLAYER_END_POSITION = (-180, 150)
SCREEN_SIZE = (600, 600)
cars_pull = []
# TODO use max_cars to create a pool of cars to put on road
# max_cars = 50
speed_step = 0.001

# set up the screen
highway = Screen()
highway.bgcolor("gray60")
highway.tracer(0)
highway.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
highway.title("Guide Turbo turtle safely across a busy highway.")
highway.listen()
highway.onkey(abort_game, "e")
highway.onkey(move_forward, "Up")

# draw lanes
highway_manager = HighWayManager(SCREEN_SIZE)
# set a player turtle
player = Turtle()
player.shape("turtle")
player.penup()
player.color("green")
player.setheading(90)
player.setposition(PLAYER_START_POSITION)

scoreboard = ScoreBoard()
highway.update()
game_over = False
speed = 0.01
while not game_over:
    time.sleep(speed)
    add_cars()
    for index, car in enumerate(cars_pull):
        car.go()
        if car.distance(player) < 20:
            game_over = True
            player.setheading(125)
            player.forward(10)
            highway.tracer(1)
            scoreboard.forward(0)
            scoreboard.game_over()
        if car.xcor() < -280:
            car.hideturtle()
            cars_pull.pop(index)
            # NOTE There are no ways to delete a car object from memory
            # TODO refactor a code to use a limited amount of cars
            # print(f"Highway has {len(highway.turtles())} cars")
        if player.ycor() > PLAYER_END_POSITION[1]:
            if player.xcor() < 0:
                player.setx(player.xcor() + 20)
            player.sety(PLAYER_START_POSITION[1])
            scoreboard.level_up()
            if speed >= speed_step:
                speed -= speed_step
            else:
                speed = 0

    highway.update()

highway.exitonclick()
