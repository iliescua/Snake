from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]

    def generate_snake(self):
        '''Create the starting snake segment'''
        for position in START_POSITIONS:
            self.add_seg(position)

    def add_seg(self, position):
        '''Add an individual segment to the snake'''
        t = Turtle("square")
        t.pu()
        t.color("lime green")
        t.pencolor("black")
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        '''Determines where to add the new snake segment and then adds it'''
        self.add_seg(self.segments[-1].position())

    def move(self):
        '''Controls the movement of the snake'''
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def border_collision(self):
        '''Detects if the snake collided with the border and makes it appear on the opposite side of the screen'''
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.goto(-self.head.xcor(), self.head.ycor())
        elif self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.goto(self.head.xcor(), -self.head.ycor())

    def up(self):
        '''Sets snake head's heading North'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Sets snake head's heading South'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Sets snake head's heading West'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Sets snake head's heading East'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
