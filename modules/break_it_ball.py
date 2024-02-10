from random import choice
from turtle import Turtle

from static.break_it_config import speed_multiples


class BreakItBall(Turtle):
    """
    A class representing the ball in the BreakIt game.

    Attributes:
        original_speed (float | int): The original speed of the ball.
        x_move (float | int): The current horizontal movement speed of the ball.
        y_move (float | int): The current vertical movement speed of the ball.

    Methods:
        - __init__(speed: float | int = 3): Initialize the BreakItBall instance.
        - move(): Move the ball based on its current speed and handle collisions with walls.
        - reset_ball(): Reset the ball to its initial position and speed.

    Inheritance:
        - Inherits from the Turtle class.

    Example Usage:
        ball = BreakItBall()
        ball.move()
        ball.reset_ball()
    """

    def __init__(self, speed: float | int = 3):
        """
        Initialize the BreakItBall instance.

        Args:
            speed (float | int): The initial speed of the ball. Defaults to 3.
        """
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(choice([-350, 350]), 120)
        self.original_speed = speed
        self.x_move = self.original_speed * choice(speed_multiples)
        self.y_move = -self.original_speed * abs(choice(speed_multiples))

    def move(self):
        """
        Move the ball based on its current speed and handle collisions with walls.
        """
        if self.ycor() > 390:
            self.y_move *= -1
        if self.xcor() < -545 or self.xcor() > 545:
            self.x_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_ball(self):
        """
        Reset the ball to its initial position and speed.
        """
        self.goto(choice([-350, 350]), 120)
        self.x_move = self.original_speed * choice(speed_multiples)
        self.y_move = -self.original_speed * abs(choice(speed_multiples))


if __name__ == "__main__":
    help(BreakItBall)
