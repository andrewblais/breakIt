from turtle import Turtle

FONT = ("Source Sans 3", 16, "bold")


class BreakItRestartText(Turtle):
    """
    A class representing the restart text displayed in the BreakIt game.

    Attributes:
        space (int): The space between the "Restart" and "Quit" options.

    Methods:
        - write_game_over(): Display the game over text on the screen.
    """

    def __init__(self):
        """Initialize BreakItRestartText."""
        super().__init__()
        self.color("white")
        self.space = 50
        self.write_game_over()

    def write_game_over(self):
        """Display the 'GAME OVER' text on the screen."""
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, -100)
        space = " " * self.space
        self.write(f"(R)estart{space}(Q)uit", align="center", font=FONT)


# if __name__ == "__main__":
#     help(BreakItRestartText)
