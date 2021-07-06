import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.cross_road, "Up")

game_is_on = True
car_speed = 0.1
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() == 280:
        scoreboard.level += 1
        scoreboard.update_scoreboard()
        player.go_home()
        car_speed *= 0.9
        print(car_speed)

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()