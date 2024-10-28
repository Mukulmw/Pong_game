import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))
screen.listen()

screen.onkeypress(r_paddle.up, key="Up")
screen.onkeypress(r_paddle.down, key="Down")
screen.onkeypress(l_paddle.up, key="w")
screen.onkeypress(l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.sleep_timer)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        print("hit")
        ball.bounce_x()
        print(ball.sleep_timer)


    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        print("hit")
        ball.bounce_x()
        print(ball.sleep_timer)


    if ball.xcor() > 380:  # right paddle misses
        print("missed")
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:  # left paddle misses
        print("missed")
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
