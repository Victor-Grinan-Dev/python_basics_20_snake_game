from turtle import Turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

            time.sleep(0.1)

    def move_snake(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

        time.sleep(0.1)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        new_segment.speed('slowest')
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            time.sleep(0.1)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            time.sleep(0.1)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            time.sleep(0.1)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            time.sleep(0.1)
