from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(x=0, y = 0)
        self.x_move = 10
        self.y_move = 10
        self.sleep_timer = 0.1

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        print("Bounce!")
        self.y_move *= -1

    def bounce_x(self):
        print("Bounce!")
        self.x_move *= -1
        self.sleep_timer *= 0.9

    def reset_position(self):
        self.home()
        self.sleep_timer = 0.1
        self.bounce_x()






