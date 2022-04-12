import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(fun=player.move, key="Up")

car_manager = CarManager()
score_board = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_cars()
    car_manager.move_car()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # detect if player manage to cross all cars
    if player.at_finishing():
        player.go_to_starting()
        car_manager.level_up()
        score_board.increase_level()
    
        
screen.exitonclick()