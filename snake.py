from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            snake.speed("slow")
            self.snake_parts.append(snake)

    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        self.snake_parts[0].setheading(90)

    def down(self):
        self.snake_parts[0].setheading(270)

    def left(self):
        self.snake_parts[0].setheading(180)

    def right(self):
        self.snake_parts[0].setheading(0)
