from turtle import Turtle

STARTING_POSITION = [(-330, 250)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        for pos in STARTING_POSITION:

            self.penup()
            self.shape("square")
            self.shapesize(stretch_len=3.5)
            self.color("white")
            self.tilt(90)
            self.goto(pos)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(x=self.xcor(), y=new_y)
