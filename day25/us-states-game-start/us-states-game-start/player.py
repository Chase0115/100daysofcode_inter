from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def correct_answer(self, answer, x, y):
        self.goto(x, y)
        self.write(f"{answer}", align=ALIGNMENT, font=FONT)
