from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        r1 = random.randint(-280, 280)
        r2 = random.randint(-280, 280)
        self.goto(r1, r2)
