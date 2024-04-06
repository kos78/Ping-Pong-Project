import time
from turtle import Turtle, Screen
from paddle import Paddle
from paddle2 import Paddle2
from ball import Ball

SPLIT_POSITION = [(0, 280), (0, 180), (0, 80), (0, -20), (0, -100), (0, -200)]

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle2()
ball = Ball()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.down, "s")
screen.onkey(paddle2.up, "w")

game_not_over = True

# create the split in the screen

for pos in SPLIT_POSITION:
    split = Turtle()
    split.color("white")
    split.shape("square")
    split.tilt(90)
    split.shapesize(stretch_len=2, stretch_wid=0.5)
    split.penup()
    split.goto(pos)

# create bounce logic
while game_not_over:
    time.sleep(0.2)
    screen.update()
    ball.move()
    print(ball.pos())

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.game_over()
        game_not_over = False

    if ball.pos() == paddle1.pos() or ball.pos() == paddle2.pos():
        ball.bounce()

screen.exitonclick()
