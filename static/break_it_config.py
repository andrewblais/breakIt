"""
Configuration File for Break It Game

This file contains configuration parameters and data used by the Break It game.

Variables:
- screen_width (int): Width of the game screen.
- screen_height (int): Height of the game screen.
- brick_color_award_dict (dict): Dictionary mapping brick colors to corresponding score awards.
- brick_color_name_list (list): Iterable containing color names used for utility.
- brick_color_hex_list (list): List of hexadecimal color codes used to build the brick wall.
- brick_color_rgb_dict (dict): Dictionary mapping color names to RGB tuples for checking colors during the game.
- brick_color_speed_dict (dict): Dictionary mapping color names to ball speed adjustments when hitting bricks.
- brick_color_score_dict (dict): Dictionary mapping brick colors to their respective scores.
- other_colors (list): Additional unused colors that may be considered for future use in the game.
- speed_multiples (list): List of speed adjustments for the ball, randomly chosen for each serve.

Imported by `break_it_screen.py` to determine screen dimensions.
"""

# Imported by `break_it_screen.py` to determine screen dimensions:
screen_width = 1120
screen_height = 800

# Dictionary mapping brick colors to corresponding score awards.
#  To be used in future versions to simplify scoring and add badges/awards.
brick_color_award_dict = {"green": 1000,
                          "blue": 2000,
                          "yellow": 3000,
                          "orange": 4000,
                          "red": 5000}

# Simple iterable for utility:
brick_color_name_list = ["red",
                         "orange",
                         "yellow",
                         "blue",
                         "green"]

# Used to build brick wall:
brick_color_hex_list = ['#ec3e40',  # red
                        '#ff9b2b',  # orange
                        '#f5d800',  # yellow
                        '#377fc7',  # blue
                        '#01a46d']  # green

# Used during the game to check colors.
# Turtle uses these long floats, so when in Rome...
brick_color_rgb_dict = {
    "red": (0.9254901960784314, 0.24313725490196078, 0.25098039215686274),
    "orange": (1.0, 0.6078431372549019, 0.16862745098039217),
    "yellow": (0.9607843137254902, 0.8470588235294118, 0.0),
    "blue": (0.21568627450980393, 0.4980392156862745, 0.7803921568627451),
    "green": (0.00392156862745098, 0.6431372549019608, 0.42745098039215684)
}

# Dictionary mapping brick colors to their respective scores.
brick_color_score_dict = {"green": 1,
                          "blue": 2,
                          "yellow": 3,
                          "orange": 4,
                          "red": 5}

# Gets the ball speed based on the brick it hits:
brick_color_speed_dict = {"green": -1.25,
                          "blue": -1.5,
                          "yellow": -1.75,
                          "orange": -2,
                          "red": -2.5}

# Unused colors to possibly be used in the game:
other_colors = ['#8b0000',  # red4
                '#006400',  # darkgreen
                "#808080",  # grey
                "#7f37c7"]  # purple

# Change up the ball speed every serve, chosen at random in `break_it_main.py`:
speed_multiples = [-2, -1.75, -1.5, -1.25, -1, 1, 1.25, 1.5, 1.75, 2]

if __name__ == "__main__":
    print(__doc__)
