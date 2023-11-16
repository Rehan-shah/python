from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.incerment_score()

    def incerment_score(self):
        self.update_scoreboard()
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score is {self.score} High Score: {self.high_score}", move=False, align='center', font=('mono', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align='center', font=('mono', 20, 'normal'))