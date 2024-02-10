from turtle import Turtle


class BreakItScoreboard(Turtle):
    """
    A class representing the scoreboard in the BreakIt game.

    Attributes:
        score (int): The current score of the player.

    Methods:
        - __init__(score: int = 0): Initialize the BreakItScoreboard.
        - update_scoreboard(): Update and display the current score on the scoreboard.
    """

    def __init__(self, score: int = 0):
        """Initialize BreakItScoreboard."""
        super().__init__()
        self.color("white")
        self.score = score
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update and display the current score on the scoreboard.

        Clears the existing content, sets up the turtle, and writes the current score.
        """
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-505, 340)
        self.write(f"{self.score:04d}",
                   align="center",
                   font=("Source Sans 3 Black", 32, "italic"))


if __name__ == "__main__":
    help(BreakItScoreboard)
