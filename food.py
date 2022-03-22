from turtle import Turtle
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("orange")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-1 * SCREEN_WIDTH + 20, SCREEN_WIDTH - 20)
        random_y = random.randint(-1 * SCREEN_HEIGHT + 20, SCREEN_HEIGHT - 20)
        self.goto(random_x, random_y)
