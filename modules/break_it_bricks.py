from turtle import Turtle
from static.break_it_config import brick_color_hex_list


class BreakItBricks:
    def __init__(self):
        """
        Initializes BreakItBricks.

        Attributes:
        - all_bricks: A list to store all the brick Turtle objects.
        - range_x: A range of x-coordinates for brick placement.
        - range_y: A range of y-coordinates for brick placement.
        - bricks_gps: A 2D list containing (x, y) coordinates for each brick in the grid.
        """
        self.all_bricks = list()
        self.range_x = range(-510, 503, 92)
        self.range_y = range(275, 174, -25)
        self.bricks_gps = [[(j, i) for j in self.range_x] for i in self.range_y]
        self.create_bricks()

    def create_bricks(self):
        """
        Creates the brick Turtle objects and adds them to the all_bricks list.

        Each brick is positioned at the specified coordinates in bricks_gps,
        and its color is determined by the color_hex_list.
        """
        color_ind = 0
        for i in self.bricks_gps:
            for j in i:
                dash = Turtle('square')
                height, width, other = dash.turtlesize()
                new_size = height * 1.0, width * 4.35, other
                dash.turtlesize(*new_size)
                dash.color(brick_color_hex_list[color_ind])
                dash.speed('fastest')
                dash.penup()
                dash.goto(j)
                self.all_bricks.append(dash)
            color_ind += 1


if __name__ == "__main__":
    help(BreakItBricks)
