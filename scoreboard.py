from turtle import Turtle

LEFT = "left"
CENTER = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    """The scoreboard for the Turtle Crossing game."""
    def __init__(self, turtle_name):
        """Initialize the scoreboard."""
        super(Scoreboard, self).__init__()
        self.level = 0
        self.turtle_name = turtle_name
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays the difficulty level."""
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=LEFT, font=FONT)

    def game_over(self):
        """Displays 'GAME OVER' in the center of the screen."""
        self.home()
        self.write("GAME OVER", align=CENTER, font=FONT)
        self.goto(0, -40)
        self.write(f"{self.turtle_name} got run over...", align=CENTER, font=FONT)
