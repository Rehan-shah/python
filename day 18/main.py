import random
import turtle
from random import randint, choice

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed("fastest")
screen = turtle.Screen()
screen.colormode(255)

def random_walk():
    t.color(random_color())
    t.circle(100)
    t.left(5)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    c = (r, g, b)
    return c


for n in range(0, 72):
    random_walk()


screen.exitonclick()
