from turtle import Turtle

FONT = 40
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        # self.write(self.l_score, align="center", font=("courier", FONT, "normal"))
        # self.write(self.r_score, align="center", font=("courier", FONT, "normal"))

    def r_point(self):
        self.r_score += 1

    def l_point(self):
        self.l_score += 1


    def update_scoreboard(self):
        self.clear()
        self.goto(x=100, y=220)
        self.write(self.r_score, align="center", font=("courier", FONT, "normal"))
        self.goto(x=-100, y=220)
        self.write(self.l_score, align="center", font=("courier", FONT, "normal"))





