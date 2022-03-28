from turtle import Turtle

class Player(Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()

    def move_y(self):
        self.sety(self.ycor()+10)

