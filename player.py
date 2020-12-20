from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """The turtle in the Turtle Crossing game."""
    def __init__(self):
        """Initialize the turtle player."""
        super(Player, self).__init__("turtle")
        self.penup()
        self.setheading(90)
        self.reset_start()

    def move(self):
        """Move the turtle up."""
        self.forward(MOVE_DISTANCE)

    def reset_start(self):
        """Reset the turtle to the starting position at the bottom of the screen."""
        self.goto(STARTING_POSITION)
