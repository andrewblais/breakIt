import time

from break_it_bricks import BreakItBricks
from break_it_config import color_name_list, color_rgb_dict, color_speed_dict
from break_it_paddle import BreakItPaddle
from break_it_ball import BreakItBall
from break_it_screen import BreakItScreen


class BreakIt:
    """
    Main class for the BreakIt game.

    Attributes:
        screen (turtle.Screen): The game screen.
        paddle (BreakItPaddle): The paddle controlled by the player.
        ball (BreakItBall): The ball that bounces around the screen.
        bricks (BreakItBricks): The collection of bricks in the game.
        brick_list (list): List of all bricks in the game.
        recent_paddle_collision (bool): Flag to track recent paddle collision.
        recent_brick_collision (bool): Flag to track recent brick collision.

    Methods:
        - is_x_cond_met(obj): Check if the x-condition is met for a given object.
        - is_y_cond_met(obj): Check if the y-condition is met for a given object.
        - are_x_y_cond_met(obj): Check if both x and y conditions are met for a given object.
        - paddle_collision(): Handle collisions with the paddle.
        - brick_collision(): Handle collisions with bricks.
        - reset_recent_paddle_collision_flag(): Reset the recent paddle collision flag.
        - reset_recent_brick_collision_flag(): Reset the recent brick collision flag.
        - run_game(): Run the BreakIt game loop.
        - speed_adjust(brick): Adjust ball speed based on brick color.
    """

    def __init__(self):
        """Initialize the BreakIt game."""
        self.screen = BreakItScreen().screen
        self.paddle = BreakItPaddle()
        self.ball = BreakItBall(speed=5)
        self.bricks = BreakItBricks()
        self.brick_list = self.bricks.all_bricks
        self.recent_paddle_collision = False
        self.recent_brick_collision = False
        self.run_game()

    def is_x_cond_met(self, obj):
        """Check if the x-condition is met for a given object.

        Args:
            obj (turtle.Turtle): The object to check.

        Returns:
            bool: True if the x-condition is met, False otherwise.
        """
        obj_x = obj.xcor()
        obj_w = obj.shapesize()[1] * 20
        x_condition = obj_x - obj_w <= self.ball.xcor() - 10 <= obj_x + obj_w / 2
        return x_condition

    def is_y_cond_met(self, obj):
        """Check if the y-condition is met for a given object.

        Args:
            obj (turtle.Turtle): The object to check.

        Returns:
            bool: True if the y-condition is met, False otherwise.
        """
        obj_y = obj.ycor()
        y_condition = obj_y - 10 <= self.ball.ycor() - 10 <= obj_y + 10
        return y_condition

    def are_x_y_cond_met(self, obj):
        """Check if both x and y conditions are met for a given object.

        Args:
            obj (turtle.Turtle): The object to check.

        Returns:
            bool: True if both x and y conditions are met, False otherwise.
        """
        check = self.is_x_cond_met(obj) and self.is_y_cond_met(obj)
        return check

    def paddle_collision(self):
        """Handle collisions with the paddle."""
        if self.are_x_y_cond_met(self.paddle) and not self.recent_paddle_collision:
            self.ball.y_move = self.ball.original_speed
            self.recent_paddle_collision = True
            self.screen.ontimer(self.reset_recent_paddle_collision_flag, 1000)

    def brick_collision(self):
        """Handle collisions with bricks."""
        for i in self.brick_list:
            if self.are_x_y_cond_met(i) and not self.recent_brick_collision:
                self.speed_adjust(i)

    def reset_recent_paddle_collision_flag(self):
        """Reset the recent paddle collision flag."""
        self.recent_paddle_collision = False

    def reset_recent_brick_collision_flag(self):
        """Reset the recent brick collision flag."""
        self.recent_brick_collision = False

    def run_game(self):
        """Run the BreakIt game loop."""
        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_paddle_left, 'Left')
        self.screen.onkeypress(self.paddle.move_paddle_right, 'Right')
        game_on = True
        while game_on:
            time.sleep(0.0005)
            self.screen.update()
            self.ball.move()
            self.paddle_collision()
            self.brick_collision()
            if self.ball.ycor() < -450:
                self.screen.ontimer(self.ball.reset_ball, 10)
        self.screen.exit_on_click()

    def speed_adjust(self, brick):
        """Adjust ball speed based on brick color.

        Args:
            brick (turtle.Turtle): The brick that was hit.
        """
        for i in color_name_list:
            if brick.color()[0] == color_rgb_dict[i]:
                if self.ball.y_move < 0:
                    self.ball.y_move = -self.ball.original_speed
                else:
                    self.ball.y_move = self.ball.original_speed
                self.ball.y_move *= color_speed_dict[i]
                brick.reset()
                self.recent_brick_collision = True
                self.screen.ontimer(self.reset_recent_brick_collision_flag, 5)


break_it = BreakIt()
