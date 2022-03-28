# Day 23
"""
The idea of the game:
user with arrow move turtle and turtle should cross
the street where a lot of cars
1) create game screen
2) create car class
3) create car objects which are moving in one speed
4) car objects appear in random position on the left side of
screen and should go to right side and disappear
5) create turtle class which is appearing in the middle bottom
of the screen
6) if turtle touch the car game is over
7) if turtle can cross the street it appearing again but now
cars are moving faster
"""
import time
from turtle import Screen
from car import Car
from score_board import SCREEN_WIDTH, SCREEN_HEIGHT, BOTTOM_POSITION, TOP_POSITION

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(titlestring="Turtle crossing street")
screen.tracer(0)
screen.colormode(255)
game_is_on = True
cars_array = [Car(BOTTOM_POSITION + 60)]
last_car_y = cars_array[-1].ycor()
while last_car_y < TOP_POSITION-60:
    new_car = Car(last_car_y+40)
    cars_array.append(new_car)
    last_car_y = cars_array[-1].ycor()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars_array:
        car.move()

screen.exitonclick()
