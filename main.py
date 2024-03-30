import time
from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)


screen.update()
time.sleep(0.1)
paddles = Paddle()

screen.listen()
screen.onkey(paddles.up, "Up")
screen.onkey(paddles.down, "Down")


screen.exitonclick()
