from turtle import Turtle, Screen
import turtle
import random

dimmy = Turtle()

color = ["coral2", "skyblue", "aquamarine", "khaki", "orange red", "violet", "black", "dodger blue", "blue", "red", "green"]
dimmy.shape('circle')
dimmy.speed('fastest')
dimmy.pensize(15)
degree = [0, 90, 180, 270]
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for i in range(200):
    dimmy.color(random_color())
    dimmy.forward(25)
    dimmy.penup()
    dimmy.right(random.choice(degree))
    dimmy.pendown()

screen = Screen()
screen.exitonclick()