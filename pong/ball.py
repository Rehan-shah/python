from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.yrate = 1
        self.xrate = 1
        self.shape("circle")
        self.penup()
        self.color("blue")

    def move(self):
        new_x = self.xcor() + self.xrate
        new_y = self.ycor() + self.yrate
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.yrate *= -1

    def bounce_x(self):
        self.xrate *= -1
        self.xrate += 0.5
        self.yrate += 0.5

    def restart(self):
        self.goto(0,0)
        self.bounce_x()
