from turtle import Turtle

FONT = ("Source Sans 3", 96, "bold")


class BreakItGameOverText(Turtle):
    """
    A class representing the 'GAME OVER' text displayed in the BreakIt game.

    Methods:
        - write_game_over(): Display the "Game Over" text on the screen.
    """

    def __init__(self):
        """Initialize BreakItGameOverText."""
        super().__init__()
        self.color("white")
        self.write_game_over()

    def write_game_over(self):
        """Display the 'GAME OVER' text on the screen."""
        self.penup()
        self.hideturtle()
        self.goto(0, -100)
        self.write(f"GAME OVER", align="center", font=FONT)


# if __name__ == "__main__":
#     help(BreakItGameOverText)
