from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle.forw, "w")
screen.onkey(paddle.back, "s")
screen.onkey(paddle2.forw, "i")
screen.onkey(paddle2.back, "j")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if 300 < ball.ycor() or -300 > ball.ycor():
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if 380 < ball.xcor():
        ball.restart()
        scoreboard.l_point()

    if -380 > ball.xcor():
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
