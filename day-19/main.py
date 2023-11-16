import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
color = screen.textinput(title="Make your bet", prompt="Witch turtle will win the race enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

print(color)
for n in range(0, len(colors)):
    t2 = Turtle(shape="turtle")
    t2.color(colors[n])
    t2.penup()
    t2.goto(x=-230, y=-100 + n * 30)
    all_turtles.append(t2)

if color:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if color == turtle.pencolor():
                print(f"You've won! The {turtle.pencolor()} turtle is the winner")
                is_race_on = False
                break 
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner")
                is_race_on = False
                break;

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
