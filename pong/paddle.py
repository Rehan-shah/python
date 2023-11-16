from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(pos, 0)

    def forw(self):
        self.goto(self.xcor(),self.ycor()+10)

    def back(self):
        self.goto(self.xcor(), self.ycor() -10)
        self.clear()
