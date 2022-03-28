from turtle import Turtle
from level_board import BOTTOM_POSITION


class Player(Turtle):

    def __init__(self, color):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.setheading(90)
        self.start_position()
        self.showturtle()

    def move_forward(self):
        self.sety(self.ycor() + 10)

    def move_backward(self):
        self.sety(self.ycor() - 10)

    def start_position(self):
        self.setposition(x=0, y=BOTTOM_POSITION + 10)
