from turtle import Turtle

STARTING_POSITION = [(-320, 300)]


class Paddle:
    def __init__(self):
        for pos in STARTING_POSITION:
            self.paddle = Turtle()
            self.paddle.penup()
            self.paddle.shape("square")
            self.paddle.shapesize(stretch_len=3.5)
            self.paddle.color("white")
            self.paddle.tilt(90)
            self.paddle.goto(pos)

    def up(self):
        new_y = self.paddle.ycor() + 10
        self.paddle.goto(x=self.paddle.xcor(), y=new_y)

    def down(self):
        new_y = self.paddle.ycor() - 10
        self.paddle.goto(x=self.paddle.xcor(), y=new_y)
