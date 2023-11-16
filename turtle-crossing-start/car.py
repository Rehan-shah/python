from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):

    def __init__(self, pos, incerment):
        super().__init__()
        self.incerment = incerment
        self.color(COLORS[randint(0, len(COLORS) - 1)])
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setpos(pos)

    def forward(self, incerment):
        if self.xcor() >= 320:
            self.goto(-320, self.ycor())
        super().forward(incerment)

    def collide(self, player):
        if self.distance(player) < 35:
            return True
        return False
