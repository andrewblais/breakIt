from turtle import Turtle


class BreakItPaddle(Turtle):
    """
    A class representing the paddle in the BreakIt game.

    Attributes:
        position (tuple): The initial position of the paddle.

    Methods:
        - __init__(position: tuple = (0, -370)): Initialize the BreakItPaddle instance.
        - create_paddle(): Create and configure the visual appearance of the paddle.
        - move_paddle_left(): Move the paddle to the left if within the left boundary.
        - move_paddle_right(): Move the paddle to the right if within the right boundary.

    Inheritance:
        - Inherits from the Turtle class.

    Example Usage:
        paddle = BreakItPaddle()
        paddle.move_paddle_left()
        paddle.move_paddle_right()
    """

    def __init__(self, position: tuple = (0, -370)):
        """
        Initialize the BreakItPaddle instance.

        Args:
            position (tuple): The initial position of the paddle. Defaults to (0, -370).
        """
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        """
        Create and configure the visual appearance of the paddle.
        """
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1.0, stretch_len=6.0)
        self.penup()
        self.goto(self.position)  # noqa
        self.showturtle()

    def move_paddle_left(self):
        """
        Move the paddle to the left if within the left boundary.
        """
        if self.xcor() > -485:
            new_x = self.xcor() - 30
            self.goto(new_x, self.ycor())

    def move_paddle_right(self):
        """
        Move the paddle to the right if within the right boundary.
        """
        if self.xcor() < 485:
            new_x = self.xcor() + 30
            self.goto(new_x, self.ycor())
