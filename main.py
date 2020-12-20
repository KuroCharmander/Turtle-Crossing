import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle_name = screen.textinput(title="Turtle Name",
                               prompt="Please help your turtle cross the road using the Up arrow key! "
                                      "What is your turtle's name?")

player = Player()
cars = CarManager()
scoreboard = Scoreboard(turtle_name)

# Set listeners
screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    cars.move_cars()

    # Add more cars if there are not enough cars on the screen
    if len(cars.all_cars) < 20:
        cars.create_car()

    # If the player collides with a car, the game ends
    for car in cars.all_cars:
        if player.distance(car) < 38 and abs(player.ycor() - car.ycor()) < 20:
            game_is_on = False
            scoreboard.game_over()

    # If the player reaches the other side, increase the level and difficulty
    if player.ycor() > 300:
        cars.level += 1
        scoreboard.update_scoreboard()
        player.reset_start()

screen.exitonclick()
