from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 60, 20):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.setposition(-1 * i, 0)
            snake.speed("slow")
            self.snake_parts.append(snake)

    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.snake_parts[0].forward(20)
