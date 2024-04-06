from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 16, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 16, "normal"))
