from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.update_scoreboard(f"Score: {self.score}")

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.update_scoreboard("GAME OVER!")

    def update_scoreboard(self, text):
        self.write(arg=text, align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard(f"Score: {self.score}")
