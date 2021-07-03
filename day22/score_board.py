from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.setpos(0, 250)
        self.color("white")
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.r_score}  {self.l_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)


    def increase_user_score(self):
        self.user_score += 1

    def increase_com_score(self):
        self.com_score += 1

