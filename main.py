import time
from turtle import Turtle, Screen
from paddle import Paddle
from paddle2 import Paddle2

SPLIT_POSITION = [(0, 300), (0, 150), (0, 0), (0, -150), (0, -300)]

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)


screen.update()
time.sleep(0.1)
paddle1 = Paddle()
paddle2 = Paddle2()


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.down, "s")
screen.onkey(paddle2.up, "w")

# create the split in the screen

for pos in SPLIT_POSITION:
    split = Turtle()
    split.color("white")
    split.shape("square")
    split.tilt(90)
    split.shapesize(stretch_len=3.5, stretch_wid=0.5)
    split.penup()
    split.goto(pos)

screen.exitonclick()
