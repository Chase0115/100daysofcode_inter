from turtle import Turtle, Screen
import random

dimmy = Turtle()
dimmy.shape("turtle")


chase = Turtle()
chase.shape("turtle")


color = ["coral2", "skyblue", "aquamarine", "khaki", "orange red", "violet", "black", "dodger blue", "blue", "red", "green"]

for i in range(3, 11):
    degree = 360 / i
    dimmy.color(random.choice(color))
    chase.color(random.choice(color))
    for j in range(i):
        dimmy.forward(40)
        dimmy.left(degree)
        chase.forward(40)
        chase.right(degree)

screen = Screen()
screen.exitonclick()
