from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as score_file:
            text = score_file.read()
            self.high_score = int(text[len(text) - 1])
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.update_scoreboard("GAME OVER!")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("score.txt", mode="w") as score_file:
            score_file.write(f"High score is {self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        text = f"Score: {self.score} High Score: {self.high_score}"
        self.write(arg=text, align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
