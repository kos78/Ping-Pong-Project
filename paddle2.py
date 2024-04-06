from turtle import Turtle


class Paddle2(Turtle):
    def __init__(self):

        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=3.5)
        self.color("white")
        self.tilt(90)
        self.goto(340, 250)

