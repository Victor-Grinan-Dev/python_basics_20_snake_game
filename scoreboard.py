from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial", 14, "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())  # I think python reads it as int, no need to convert
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} high Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
