from turtle import Turtle
from paddle import Paddle


class Paddle2(Paddle):
    def __init__(self):

        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_len=3.5)
        self.paddle.color("white")
        self.paddle.tilt(90)
        self.paddle.goto(320, 300)

