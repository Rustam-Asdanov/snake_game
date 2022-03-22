# Day 20

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake_parts = []

for i in range(0, 60, 20):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.setposition(-1 * i, 0)
    snake.speed("slow")
    snake_parts.append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for part in range(len(snake_parts) - 1, 0, -1):
        new_x = snake_parts[part - 1].xcor()
        new_y = snake_parts[part - 1].ycor()
        snake_parts[part].goto(new_x, new_y)
    snake_parts[0].forward(20)

screen.exitonclick()
