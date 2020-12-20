import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 2


class CarManager:
    """The cars in the Turtle Crossing game."""
    def __init__(self):
        """Initialize the CarManager."""
        # Contains all the cars on screen in the CarManager
        self.all_cars = []
        # The cars that will be removed when they pass the screen
        self.cars_to_remove = []
        self.starting_cars()
        self.level = 0

    def starting_cars(self):
        """Create the cars initially on the screen."""
        starting_num_cars = random.randint(15, 20)
        for _ in range(starting_num_cars):
            random_x = random.randint(-300, 600)
            self.create_car(random_x)

    def create_car(self, x=320):
        """Create a car for the CarManager."""
        new_car = t.Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        random_y = random.randint(-220, 220)
        new_car.goto(x, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        """Move all the cars towards the left side of the screen at the same speed."""
        speed = MOVE_INCREMENT * self.level
        for i in range(len(self.all_cars)):
            self.all_cars[i].forward(STARTING_MOVE_DISTANCE + speed)
            if self.all_cars[i].xcor() < -350:
                self.cars_to_remove.append(self.all_cars[i])
        self.remove_cars()

    def remove_cars(self):
        """Remove the cars that have travelled past the screen."""
        for car in self.cars_to_remove:
            self.all_cars.remove(car)

        # Reset the list of cars to remove
        self.cars_to_remove = []
