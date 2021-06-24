import random
from turtle import Turtle, Screen
import turtle

dimmy = Turtle()
dimmy.pensize(5)
turtle.colormode(255)
dimmy.hideturtle()

extract_color = [(239, 229, 84), (191, 11, 71), (206, 158, 98), (113, 179, 205), (162, 170, 35), (26, 117, 170), (212, 137, 168), (161, 71, 37), (9, 35, 83), (32, 135, 74), (121, 181, 138), (232, 70, 41), (239, 221, 5), (210, 85, 131), (80, 20, 77)]

x = -200
y = -200

for i in range(101):
    dimmy.penup()
    dimmy.goto(x, y)
    dimmy.color(random.choice(extract_color))
    dimmy.pendown()
    dimmy.dot(20)

    x += 50
    if x > 250:
        x = -200
        y += 50

screen = Screen()
screen.exitonclick()
