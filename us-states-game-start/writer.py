import turtle


class Writer:
    def __init__(self):
        self.writer = turtle.Turtle()
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.speed(0)

    def write(self, state):
        for n in state["state"]:
            self.writer.goto(state['x'][n], state['y'][n])
            self.writer.write(state["state"][n], font=("Verdana", 12, "normal"))
