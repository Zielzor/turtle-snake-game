from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 18, "normal")

with open("score.txt") as file:
    high_score = file.read()



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.score = 0
        self.highscore = int(high_score)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.refresh_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align=ALIGN, font=FONT)
