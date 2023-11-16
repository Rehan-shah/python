from turtle import Turtle, Screen
from random import choice

t = Turtle()
t.speed(0)
screen = Screen()
screen.colormode(255)
t.penup()
t.pendown()
color_list = [(1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59),
              (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91),
              (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179),
              (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7),
              (132, 223, 209), (229, 173, 165)]


sieve = [
    True
] * 5

def draw_cricle():
    t.pendown()
    t.color(choice(color_list))


    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()

for n in range(0,10) :
    h = t.pos()[0]
    for n in range(0,10):
        draw_cricle()
        t.forward(50)
    t.setpos((h,t.pos()[1]+50))

screen.exitonclick()
