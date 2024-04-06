from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.9)
        self.color('white')
        self.goto(x=0, y=0)
        self.y_move = 10
        self.x_move = 10


    def move(self, ):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", font=("Arial", 24, "normal"), align="center")

    def y_bounce(self):
        self.y_move *= -1
        # while self.y_move < 20:
        #     self.y_move += 3

    def x_bounce(self):
        self.x_move *= -1


