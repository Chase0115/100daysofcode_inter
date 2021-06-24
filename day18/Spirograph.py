from turtle import Turtle, Screen
import turtle
import random

dimmy = Turtle()

dimmy.shape('circle')
dimmy.speed('fastest')
dimmy.pensize(1)
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(90):
    dimmy.color(random_color())
    dimmy.circle(40)
    dimmy.penup()
    dimmy.left(4)
    dimmy.pendown()

screen = Screen()
screen.exitonclick()