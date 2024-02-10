from turtle import Screen
import time

from static.break_it_config import screen_width, screen_height


class BreakItScreen:
    """
    A class representing the screen in the BreakIt game.

    Attributes:
        screen (Screen): The turtle Screen instance.

    Methods:
        - __init__(): Initialize the BreakItScreen instance.
        - screen_setup(): Configure the appearance and settings of the game screen.

    Example Usage:
        game_screen = BreakItScreen()
        game_screen.screen_setup()
    """

    def __init__(self):
        """
        Initialize the BreakItScreen instance.
        """
        self.screen = Screen()
        self.screen_setup()

    def screen_setup(self):
        """
        Configure the appearance and settings of the game screen.

        Returns:
            Screen: The configured turtle Screen instance.
        """
        self.screen.setup(width=screen_width, height=screen_height)
        self.screen.bgcolor("black")
        self.screen.title("Break It")
        self.screen.tracer(0, 0)
        time.sleep(0.01)
        return self.screen


if __name__ == "__main__":
    help(BreakItScreen)
