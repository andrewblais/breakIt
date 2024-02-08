"""
Configuration File for Break It Game

This file contains configuration parameters and data used by the Break It game.

Variables:
- screen_width: Width of the game screen.
- screen_height: Height of the game screen.
- color_name_list: Iterable containing color names used for utility.
- color_hex_list: List of hexadecimal color codes used to build the brick wall.
- color_rgb_dict: Dictionary mapping color names to RGB tuples for checking colors during the game.
- color_speed_dict: Dictionary mapping color names to ball speed adjustments when hitting bricks.
- other_colors: Additional unused colors that may be considered for future use in the game.

Imported by `break_it_screen.py` to determine screen dimensions.
"""

# Imported by `break_it_screen.py` to determine screen dimensions:
screen_width = 1120
screen_height = 800

# Simple iterable for utility:
color_name_list = ["red",
                   "orange",
                   "yellow",
                   "blue",
                   "green"]

# Used to build brick wall:
color_hex_list = ['#ec3e40',  # red
                  '#ff9b2b',  # orange
                  '#f5d800',  # yellow
                  '#377fc7',  # blue
                  '#01a46d']  # green

# Used during game to check colors.
# Turtle uses these long floats, so when in Rome...
color_rgb_dict = {
    "red": (0.9254901960784314, 0.24313725490196078, 0.25098039215686274),
    "orange": (1.0, 0.6078431372549019, 0.16862745098039217),
    "yellow": (0.9607843137254902, 0.8470588235294118, 0.0),
    "blue": (0.21568627450980393, 0.4980392156862745, 0.7803921568627451),
    "green": (0.00392156862745098, 0.6431372549019608, 0.42745098039215684)
}

# Gets the ball speed based on brick it hits:
color_speed_dict = {"green": -1.25,
                    "blue": -1.5,
                    "yellow": -1.75,
                    "orange": -2,
                    "red": -2.5}

# Unused colors to possibly be used in game:
other_colors = ['#8b0000',  # red4
                '#006400',  # darkgreen
                "#808080",  # grey
                "#7f37c7"]  # purple
