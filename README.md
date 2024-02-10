# breakIt

_MIT License, Copyright (c) 2024 Andrew Blais_

_First version finished February 10, 2024_

---

## Description:

A [Turtle](https://docs.python.org/3/library/turtle.html) Breakout-style game.

Written from scratch in completing Angela Yu's 100 Days of Python Professional
Portfolio Project assigment (see below for more details).

Written with Python Class/OOP structure.

Includes many methods and separate modules to separate concerns, improve efficiency and
enhance readability.

The static folder contains variables/definitions which determine the dimensions of the
layout/pieces and the speed of gameplay.

---

## Pending Improvements:

Future updates:

Add point bonus if player eliminates row of bricks without interrupting the process
with other colors.

Add badges/awards if user goes above 1000(?) pts. Make a color decal/circle to the
right of points to keep track (essentially a thousands placeholder).

Make the sides/bumpers of paddle which allow spin a different shade.

Print directions, key-binding instructions.

Improve logic so only the edges of bricks/paddle being hit cause effect.

Create separate module for collision logic.

Improve/revise/proofread documentation/docstrings.

---

## Documentation:

_Printed via `help(BreakIt)` in `break_it_main.py`:_

```
Help on class BreakIt in module __main__:

class BreakIt(builtins.object)
 |  BreakIt(speed: int | float = 3, score: int = 0, remain: int = 5)
 |
 |  Main class for the BreakIt game.
 |
 |  Attributes:
 |      screen (turtle.Screen): The game screen.
 |      scoreboard (BreakItScoreboard): The scoreboard displaying the player's score.
 |      paddle (BreakItPaddle): The paddle controlled by the player.
 |      ball (BreakItBall): The ball that bounces around the screen.
 |      bricks (BreakItBricks): The collection of bricks in the game.
 |      brick_list (list): List of all bricks in the game.
 |      brick_count (int): The current count of remaining bricks in the game.
 |      pause_game (bool): Flag to indicate whether the game is paused.
 |      game_on (bool): Flag to indicate if the game is currently running.
 |      game_over_text (BreakItGameOverText): The "Game Over" text displayed when the game ends.
 |      recent_paddle_collision (bool): Flag to track recent paddle collision.
 |      recent_brick_collision (bool): Flag to track recent brick collision.
 |      restart_text (BreakItRestartText): Text indicating how to restart the game.
 |      x_spin (int | float): Determines speed increase for side-paddle hit.
 |
 |  Methods:
 |      - is_x_cond_met(obj): Check if the x-condition is met for a given object.
 |      - determine_paddle_x_spin(): Adjust ball's x-move based on paddle hit for spin effect.
 |      - is_y_cond_met(obj): Check if the y-condition is met for a given object.
 |      - are_x_y_cond_met(obj): Check if both x and y conditions are met for a given object.
 |      - key_listeners(): Creates key listeners for movement/pause/quit/restart methods.
 |      - paddle_collision(): Handle collisions with the paddle. Resets y_move to original_speed.
 |      - brick_collision(): Handle collisions with bricks.
 |      - reset_recent_paddle_collision_flag(): Reset the recent paddle collision flag.
 |      - reset_recent_brick_collision_flag(): Reset the recent brick collision flag.
 |      - next_round(): Start the next round after all bricks are eliminated.
 |      - restart_game(): Restart the BreakIt game. Reinitiates all relevant attributes.
 |      - quit_game(): Quit the BreakIt game.
 |      - pause_toggle(): Toggle the pause state of the game.
 |      - run_game(): Run the BreakIt game loop.
 |      - speed_score_utility(brick): Adjust ball speed based on brick color.
 |
 |  Methods defined here:
 |
 |  __init__(self, speed: int | float = 3, score: int = 0, remain: int = 5)
 |      Initialize the BreakIt game.
 |
 |  are_x_y_cond_met(self, obj)
 |      Check if both x and y conditions are met for a given object.
 |      Helps determine if ball hits paddle and bricks.
 |
 |      Args:
 |          obj (turtle.Turtle): The object to check.
 |
 |      Returns:
 |          bool: True if both x and y conditions are met, False otherwise.
 |
 |  brick_collision(self)
 |      Handle collisions with bricks.
 |
 |  determine_paddle_x_spin(self)
 |      Adjust ball's x-move based on paddle hit for spin effect.
 |
 |  is_x_cond_met(self, obj)
 |      Check if the x-condition is met for a given object.
 |      Helps determine if ball hits paddle and bricks.
 |
 |      Args:
 |          obj (turtle.Turtle): The object to check.
 |
 |      Returns:
 |          bool: True if the x-condition is met, False otherwise.
 |
 |  is_y_cond_met(self, obj)
 |      Check if the y-condition is met for a given object.
 |      Helps determine if ball hits paddle and bricks.
 |
 |      Args:
 |          obj (turtle.Turtle): The object to check.
 |
 |      Returns:
 |          bool: True if the y-condition is met, False otherwise.
 |
 |  key_listeners(self)
 |      Creates key listeners for movement/pause/quit/restart methods.
 |
 |  next_round(self)
 |      Start the next round after all bricks eliminated.
 |      Reinitiates all relevant attributes.
 |      Preserves score and number of balls.
 |      Increases ball speed.
 |
 |  paddle_collision(self)
 |      Handle collisions with the paddle. Resets y_move to original_speed.
 |
 |  pause_toggle(self)
 |
 |  quit_game(self)
 |      Quit the BreakIt game.
 |
 |  reset_recent_brick_collision_flag(self)
 |      Reset the recent brick collision flag.
 |
 |  reset_recent_paddle_collision_flag(self)
 |      Reset the recent paddle collision flag.
 |
 |  restart_game(self)
 |      Restart the BreakIt game.
 |      Calls `self.__init__()` with default values.
 |
 |  run_game(self)
 |      Run the BreakIt game loop.
 |
 |  speed_score_utility(self, brick)
 |      Adjust ball speed based on brick color.
 |
 |      Args:
 |          brick (turtle.Turtle): The brick that was hit.
```

_Printed via `print(__doc__)` in `static.break_it_config.py`:_

```
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
```

_Printed via `help(BreakItGameOverText)` in `break_it_game_over_text.py`:_

```
class BreakItGameOverText(turtle.Turtle)
 |  A class representing the 'GAME OVER' text displayed in the BreakIt game.
 |
 |  Methods:
 |      - write_game_over(): Display the "Game Over" text on the screen.
 |
 |  Method resolution order:
 |      BreakItGameOverText
 |      turtle.Turtle
 |      turtle.RawTurtle
 |      turtle.TPen
 |      turtle.TNavigator
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize BreakItGameOverText.
 |
 |  write_game_over(self)
 |      Display the 'GAME OVER' text on the screen.
```

_Printed via `help(BreakItRestartText)` in `break_it_restart_text.py`:_

```
Help on class BreakItRestartText in module __main__:

class BreakItRestartText(turtle.Turtle)
 |  A class representing the restart text displayed in the BreakIt game.
 |
 |  Attributes:
 |      space (int): The space between the "Restart" and "Quit" options.
 |
 |  Methods:
 |      - write_game_over(): Display the game over text on the screen.
 |
 |  Method resolution order:
 |      BreakItRestartText
 |      turtle.Turtle
 |      turtle.RawTurtle
 |      turtle.TPen
 |      turtle.TNavigator
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize BreakItRestartText.
 |
 |  write_game_over(self)
 |      Display the 'GAME OVER' text on the screen.
```

_Printed via `help(BreakItScoreboard)` in `break_it_scoreboard.py`:_

```
Help on class BreakItScoreboard in module __main__:

class BreakItScoreboard(turtle.Turtle)
 |  BreakItScoreboard(score: int = 0)
 |
 |  A class representing the scoreboard in the BreakIt game.
 |
 |  Attributes:
 |      score (int): The current score of the player.
 |
 |  Methods:
 |      - __init__(score: int = 0): Initialize the BreakItScoreboard.
 |      - update_scoreboard(): Update and display the current score on the scoreboard.
 |
 |  Method resolution order:
 |      BreakItScoreboard
 |      turtle.Turtle
 |      turtle.RawTurtle
 |      turtle.TPen
 |      turtle.TNavigator
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, score: int = 0)
 |      Initialize BreakItScoreboard.
 |
 |  update_scoreboard(self)
 |      Update and display the current score on the scoreboard.
 |
 |      Clears the existing content, sets up the turtle, and writes the current score.
```

_Printed via `help(BreakItBallsRemaining)` in `break_it_balls_remaining.py`:_

```
Help on class BreakItBallsRemaining in module __main__:

class BreakItBallsRemaining(turtle.Turtle)
 |  BreakItBallsRemaining(balls_remaining_int: int = 5)
 |
 |  A class representing the remaining balls indicator in the BreakIt game.
 |
 |  Attributes:
 |      number (int): The number of remaining balls.
 |      balls_remaining_str (str): A visual representation of the remaining balls.
 |
 |  Methods:
 |      - update_balls_remaining(): Update and display the remaining balls indicator.
 |      - decrease_balls_remaining(): Decrease the number of remaining balls and update the indicator.
 |
 |  Method resolution order:
 |      BreakItBallsRemaining
 |      turtle.Turtle
 |      turtle.RawTurtle
 |      turtle.TPen
 |      turtle.TNavigator
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, balls_remaining_int: int = 5)
 |      Initialize BreakItBallsRemaining.
 |
 |  decrease_balls_remaining(self)
 |      Decrease the number of remaining balls and update the indicator.
 |
 |      Decreases the number of remaining balls, updates the visual representation, and calls update_balls_remaining.
 |
 |  update_balls_remaining(self)
 |      Update and display the remaining balls indicator.
 |
 |      Clears the existing content, sets up the turtle, and writes the visual representation of remaining balls.
```

_Printed via `help(BreakItBall)` in `break_it_ball.py`:_

```
Help on class BreakItBall in module __main__:

class BreakItBall(turtle.Turtle)
 |  BreakItBall(speed: float | int = 3)
 |
 |  A class representing the ball in the BreakIt game.
 |
 |  Attributes:
 |      original_speed (float | int): The original speed of the ball.
 |      x_move (float | int): The current horizontal movement speed of the ball.
 |      y_move (float | int): The current vertical movement speed of the ball.
 |
 |  Methods:
 |      - __init__(speed: float | int = 3): Initialize the BreakItBall instance.
 |      - move(): Move the ball based on its current speed and handle collisions with walls.
 |      - reset_ball(): Reset the ball to its initial position and speed.
 |
 |  Inheritance:
 |      - Inherits from the Turtle class.
 |
 |  Example Usage:
 |      ball = BreakItBall()
 |      ball.move()
 |      ball.reset_ball()
 |
 |  Method resolution order:
 |      BreakItBall
 |      turtle.Turtle
 |      turtle.RawTurtle
 |      turtle.TPen
 |      turtle.TNavigator
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, speed: float | int = 3)
 |      Initialize the BreakItBall instance.
 |
 |      Args:
 |          speed (float | int): The initial speed of the ball. Defaults to 3.
 |
 |  move(self)
 |      Move the ball based on its current speed and handle collisions with walls.
 |
 |  reset_ball(self)
 |      Reset the ball to its initial position and speed.
```

_Printed via `help(BreakItPaddle)` in `break_it_paddle.py`:_

```
Help on class BreakItPaddle in module __main__:

class BreakItPaddle(turtle.Turtle)
 |  BreakItPaddle(position: tuple = (0, -370))
 |
 |  A class representing the paddle in the BreakIt game.
 |
 |  Attributes:
 |      position (tuple): The initial position of the paddle.
 |
 |  Methods:
 |      - __init__(position: tuple = (0, -370)): Initialize the BreakItPaddle instance.
 |      - create_paddle(): Create and configure the visual appearance of the paddle.
 |      - move_paddle_left(): Move the paddle to the left if within the left boundary.
 |      - move_paddle_right(): Move the paddle to the right if within the right boundary.
 |
 |  Inheritance:
 |      - Inherits from the Turtle class.
 |
 |  Example Usage:
 |      paddle = BreakItPaddle()
 |      paddle.move_paddle_left()
 |      paddle.move_paddle_right()
 |
 |  Method resolution order:
 |      BreakItPaddle
 |      turtle.Turtle
 |      turtle.RawTurtle
 |      turtle.TPen
 |      turtle.TNavigator
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, position: tuple = (0, -370))
 |      Initialize the BreakItPaddle instance.
 |
 |      Args:
 |          position (tuple): The initial position of the paddle. Defaults to (0, -370).
 |
 |  create_paddle(self)
 |      Create and configure the visual appearance of the paddle.
 |
 |  move_paddle_left(self)
 |      Move the paddle to the left if within the left boundary.
 |      Allows right edge of paddle to stick out slightly for x-spin from that side.
 |
 |  move_paddle_right(self)
 |      Move the paddle to the right if within the right boundary.
 |      Allows left edge of paddle to stick out slightly for x-spin from that side.
```

_Printed via `help(BreakItScreen)` in `break_it_screen.py`:_

```
Help on class BreakItScreen in module __main__:

class BreakItScreen(builtins.object)
 |  A class representing the screen in the BreakIt game.
 |
 |  Attributes:
 |      screen (Screen): The turtle Screen instance.
 |
 |  Methods:
 |      - __init__(): Initialize the BreakItScreen instance.
 |      - screen_setup(): Configure the appearance and settings of the game screen.
 |
 |  Example Usage:
 |      game_screen = BreakItScreen()
 |      game_screen.screen_setup()
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize the BreakItScreen instance.
 |
 |  screen_setup(self)
 |      Configure the appearance and settings of the game screen.
 |
 |      Returns:
 |          Screen: The configured turtle Screen instance.
```

_Printed via `help(BreakItBricks)` in `break_it_bricks.py`:_

```
Help on class BreakItBricks in module __main__:

class BreakItBricks(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initializes BreakItBricks.
 |
 |      Attributes:
 |      - all_bricks: A list to store all the brick Turtle objects.
 |      - range_x: A range of x-coordinates for brick placement.
 |      - range_y: A range of y-coordinates for brick placement.
 |      - bricks_gps: A 2D list containing (x, y) coordinates for each brick in the grid.
 |
 |  create_bricks(self)
 |      Creates the brick Turtle objects and adds them to the all_bricks list.
 |
 |      Each brick is positioned at the specified coordinates in bricks_gps,
 |      and its color is determined by the color_hex_list.
```

---

## Assignment for Angela Yu's Course:

### I created this project in completing Day 87, Professional Portfolio

**Project - [GUI]: _Assignment 6, "Breakout Game"_**

- _from [Angela Yu 100 Days of Code](https://www.udemy.com/course/100-days-of-code/)_

### Here are the instructions for the assignment:

**Assignment: Breakout Game**

_Using Python Turtle, build a clone of the 80s hit game Breakout._

Assignment instructions

Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started
Apple. It's a simple game that is similar to Pong where you use a ball and paddle to
break down a wall.

[Breakout Wikipedia Page](https://en.wikipedia.org/wiki/Breakout_(video_game))

![Breakout Game Image](./.projectReference/imagesCreation/breakout.png)

You can try out the gameplay here:

https://elgoog.im/breakout/

A good starting point is to review the lessons on Day 22 when we built the Pong game. But
you will have plenty of things to Google, figure out and struggle through to complete
this project. Try to avoid going to a tutorial on how to build breakout, instead spec out
the project, figure out how it's going to work. Write down a checklist of todos and draw
out a flow chart (if it helps).

### My reflections on the assignment:

The course asks:

```
This is a place to journal your experience of completing this project. This will help you
figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve
for the next project? What was your biggest learning from today? What would you do differently
if you were to tackle this project again?
```

My answers:
Here's my project repo's address: https://github.com/andrewblais/breakIt

First I looked at the goal, how the game works, etc...

I wanted to create something unique, so I tried to use the game as a guide and not 
copy every aspect of it. After completing the project and looking again at the official
version of the game, I discovered that I had come up with many of the same features:
having the sides of the paddle cause the ball cause 'spin' on the ball, adding more
points per brick for the upper rows. I saw in the official game that it speeds up from 
time to time, but didn't figure out the exact logic. My thinking was to reset the ball's
speed every time it hit the paddle. But whenever it hit a brick it should speed up to a 
multiple of the default speed, faster for bricks in the higher row.

It was also very challenging figuring out how to pause the game, but I found my way 
through. I tried not to rely to heavily on advice from Stack Overflow and ChatGPT, but
they did provide vital and helpful information. But it is important to me to work
through problems on my own as much as possible, to really understand and to be able to
consider this project my own.

It was a challenge to get the ball to hit only the outside of the paddle and the bricks
without padding issues, so the hits look clean. This involved some math/geometry and 
conditional statments to ensure the ball reacts exactly the way it needs to when it
is in the correct proximity to the paddle/bricks.

It was also a challenge to get the ball to bounce once and not get 'stuck' in a quick
staggering effect after contact. This involved setting a 'recent collision' tag which 
expired after a fraction of a second, but giving the ball time to 'get away' from the 
collision cleanly.

There are many improvements which can be implemented, and I will save those for future 
versions, feeling like I've completed the project, for now, to my satisfaction. Future
improvments may include adding a badge system for when the score goes over 100 or 1000, 
with different color badges for higher and higher multiples of these numbers. This will
make things more interesting and fun, and also be a way to keep track of higher scores
without maxing out the score counter.

I can also think of other fun features: adding 'special' bricks here and there which 
have interesting and random effects, changing the color scheme and brick layout for
higher levels, and adding animation between rounds.

I'm getting better at prioritizing aspects/steps of the project which need to be
accomplished, doing them in a reasonable order, and not getting stuck for too long on
issues which don't have vital importance -- learning to move on and sometimes drop things
or at least save them for later if it feels like the best thing, if I've spent enough
time on something without a solution.

What a great project to work on! I have to admit I was a bit daunted as the Turtle 
lessons happened much earlier in the course and I'd forgotten much. Also, I'm more 
interested in Machine Learning and Data Science than game design -- but I found that 
even though we were building a game here, there were many, many apsects of the project
which forced me to review and learn skills which can be applied across the spectrum
of programming: OOP/Class Inheritance, functionality which depends on efficient 
algorithms and math/geometry, and many tools from Turtle and the Python Standard 
Library were good to revisit.

On to the next project!

Andrew Blais
February 10, 2024