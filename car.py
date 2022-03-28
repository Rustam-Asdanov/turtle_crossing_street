import time
from turtle import Turtle
import random

from level_board import TOP_POSITION, RIGHT_POSITION, LEFT_POSITION, BOTTOM_POSITION


class Car(Turtle):
    def __init__(self, y_pos):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.set_random_color()
        self.set_x_random_position()
        self.sety(y=y_pos)
        self.speed = 1
        self.showturtle()

    def set_x_random_position(self):
        x_pos = random.randrange(LEFT_POSITION, RIGHT_POSITION, 10)
        self.setposition(x=x_pos, y=self.ycor())

    def start_again(self):
        self.showturtle()
        self.setx(RIGHT_POSITION + 10)

    def set_random_color(self):
        R = random.randrange(0, 255, 10)
        G = random.randrange(0, 255, 10)
        B = random.randrange(0, 255, 10)
        self.color((R, G, B))

    def move(self):
        self.setx(self.xcor() - self.speed)
        if self.xcor() < LEFT_POSITION - 10:
            self.hideturtle()
            self.start_again()

    def increase_speed(self):
        self.speed += 5