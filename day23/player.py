from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    def cross_road(self):
        if self.ycor() < FINISH_LINE_Y:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def go_home(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
