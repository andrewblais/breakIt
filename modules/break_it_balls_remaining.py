from turtle import Turtle


class BreakItBallsRemaining(Turtle):
    """
    A class representing the remaining balls indicator in the BreakIt game.

    Attributes:
        number (int): The number of remaining balls.
        balls_remaining_str (str): A visual representation of the remaining balls.

    Methods:
        - update_balls_remaining(): Update and display the remaining balls indicator.
        - decrease_balls_remaining(): Decrease the number of remaining balls and update the indicator.
    """

    def __init__(self, balls_remaining_int: int = 5):
        """Initialize BreakItBallsRemaining."""
        super().__init__()
        self.color("white")
        self.number = balls_remaining_int
        self.balls_remaining_str = self.number * "●"
        self.update_balls_remaining()

    def update_balls_remaining(self):
        """
        Update and display the remaining balls indicator.

        Clears the existing content, sets up the turtle, and writes the visual representation of remaining balls.
        """
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(544, 340)
        self.write(f"{self.balls_remaining_str}",
                   align="right",
                   font=("Source Sans 3 Black", 32, "italic"))

    def decrease_balls_remaining(self):
        """
        Decrease the number of remaining balls and update the indicator.

        Decreases the number of remaining balls, updates the visual representation, and calls update_balls_remaining.
        """
        self.number -= 1
        self.balls_remaining_str = self.number * "●"
        self.update_balls_remaining()


if __name__ == "__main__":
    help(BreakItBallsRemaining)
