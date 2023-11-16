from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.head = 0
        self.create_snake()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            prev = self.segments[i - 1]
            self.segments[i].goto(prev.xcor(), prev.ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def create_snake(self):
        for i in range(0, 3):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.setpos(0 + i * -20, 0)
            self.segments.append(t)
        self.head = self.segments[0]

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def reset(self):
        for n in self.segments:
            n.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def add_segement(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
