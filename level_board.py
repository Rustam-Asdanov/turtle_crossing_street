from turtle import Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TOP_POSITION = int(SCREEN_HEIGHT / 2)
BOTTOM_POSITION = -1 * TOP_POSITION
RIGHT_POSITION = int(SCREEN_WIDTH / 2)
LEFT_POSITION = -1 * RIGHT_POSITION


class LevelBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(TOP_POSITION - 30)
        self.level = 1
        self.update_text()

    def increase_level(self):
        self.level += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(align="center", font=("Arial", 15, "normal"), arg=f"Level: {self.level}")
