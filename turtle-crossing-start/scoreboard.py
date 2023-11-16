from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.pendown()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", FONT)

    def increment(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)
