from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.setposition(position)

    def up(self):

        #self.setheading(UP)
        self.forward(DISTANCE)

    def down(self):

        #self.setheading(DOWN)
        self.backward(DISTANCE)



