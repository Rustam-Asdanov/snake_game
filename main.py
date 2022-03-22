# Day 20

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_parts = []


def start():
    for i in range(0, 60, 20):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.setposition(-1 * i, 0)
        snake_parts.append(snake)


def move():
    while True:
        for snake in snake_parts:
            previous_position = snake.position()[0]
            snake.goto(previous_position + 20, 0)


start()
move()

screen.exitonclick()
