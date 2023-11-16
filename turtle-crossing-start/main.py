import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
car_manager = CarManager()
player = Player()

screen.listen()

screen.onkey(player.move_ahemd, "w")
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")

scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    car_manager.move()
    screen.update()
    if car_manager.collide(player):
        scoreboard.game_over()
        game_is_on = False

    if player.ycor() > 280:
        scoreboard.increment()
        player.resart()

screen.exitonclick()
