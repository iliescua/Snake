from turtle import Turtle
import random as rand

X_BOUND = 280
Y_BOUND = 230


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        '''Moves the food to a new random location on the screen'''
        self.goto(rand.randint(-X_BOUND, X_BOUND),
                  rand.randint(-Y_BOUND, Y_BOUND))
