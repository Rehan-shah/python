from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_ahemd(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def move_left(self):
        self.goto(self.xcor() - 10, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 10, self.ycor())

    def resart(self):
        self.goto(STARTING_POSITION)
