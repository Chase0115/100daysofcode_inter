from turtle import Screen
from score_board import Scoreboard
from paddle import Paddle
from ball import Ball
import time
# import turtle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()



screen.listen()
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    #Detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
        ball.move_speed *= 0.9

    #Detect collision with r.paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect when paddle miss the ball
    if ball.xcor() > 400:
        ball.home()
        scoreboard.r_score += 1
        ball.move_speed = 0.1
    elif ball.xcor() < -400:
        ball.home()
        scoreboard.l_score += 1
        ball.move_speed = 0.1

screen.exitonclick()
