from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-270, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)

