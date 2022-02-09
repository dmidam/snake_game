from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = data.read()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as data:
                self.high_score = data.write(str(self.score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        with open("data.txt") as data:
            self.high_score = data.read()
            self.write(f"Current score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("arial", 14, "normal"))
        self.score += 1
