from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOV = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segs = []
        self.create_s()
        self.head = self.segs[0]

    def create_s(self):
        for pos in STARTING_POSITIONS:
            self.add(pos)

    def add(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segs.append(seg)

    def extend(self):
        self.add(self.segs[-1].pos())

    def move(self):
        for i in range(len(self.segs) - 1, 0, -1):
            self.segs[i].goto(self.segs[i - 1].pos())
        self.head.forward(MOV)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segs:
            seg.goto(1000, 1000)
        self.segs.clear()
        self.create_s()
        self.head = self.segs[0]
