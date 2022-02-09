from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

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

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        _ = Turtle(shape="square")
        _.color("white")
        _.penup()
        _.goto(position)
        self.turtles.append(_)
    def reset(self):
        for seg in self.turtles:
            seg.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for tur_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[tur_num - 1].xcor()
            new_y = self.turtles[tur_num - 1].ycor()
            self.turtles[tur_num].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)
