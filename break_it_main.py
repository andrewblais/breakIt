import time

from modules.break_it_ball import BreakItBall
from modules.break_it_balls_remaining import BreakItBallsRemaining
from modules.break_it_bricks import BreakItBricks
from modules.break_it_game_over_text import BreakItGameOverText
from static.break_it_config import *
from modules.break_it_paddle import BreakItPaddle
from modules.break_it_restart_text import BreakItRestartText
from modules.break_it_scoreboard import BreakItScoreboard
from modules.break_it_screen import BreakItScreen


class BreakIt:
    """
    Main class for the BreakIt game.

    Attributes:
        screen (turtle.Screen): The game screen.
        scoreboard (BreakItScoreboard): The scoreboard displaying the player's score.
        paddle (BreakItPaddle): The paddle controlled by the player.
        ball (BreakItBall): The ball that bounces around the screen.
        bricks (BreakItBricks): The collection of bricks in the game.
        brick_list (list): List of all bricks in the game.
        brick_count (int): The current count of remaining bricks in the game.
        pause_game (bool): Flag to indicate whether the game is paused.
        game_on (bool): Flag to indicate if the game is currently running.
        game_over_text (BreakItGameOverText): The "Game Over" text displayed when the game ends.
        recent_paddle_collision (bool): Flag to track recent paddle collision.
        recent_brick_collision (bool): Flag to track recent brick collision.
        restart_text (BreakItRestartText): Text indicating how to restart the game.
        x_spin (int | float): Determines speed increase for side-paddle hit.

    Methods:
        - is_x_cond_met(obj): Check if the x-condition is met for a given object.
        - paddle_x_spin(): Adjust ball's x-move based on paddle hit for spin effect.
        - is_y_cond_met(obj): Check if the y-condition is met for a given object.
        - are_x_y_cond_met(obj): Check if both x and y conditions are met for a given object.
        - key_listeners(): Creates key listeners for movement/pause/quit/restart methods.
        - paddle_collision(): Handle collisions with the paddle. Resets y_move to original_speed.
        - brick_collision(): Handle collisions with bricks.
        - reset_recent_paddle_collision_flag(): Reset the recent paddle collision flag.
        - reset_recent_brick_collision_flag(): Reset the recent brick collision flag.
        - next_round(): Start the next round after all bricks are eliminated.
        - restart_game(): Restart the BreakIt game. Reinitiates all relevant attributes.
        - quit_game(): Quit the BreakIt game.
        - pause_toggle(): Toggle the pause state of the game.
        - run_game(): Run the BreakIt game loop.
        - speed_score_utility(brick): Adjust ball speed based on brick color.
    """

    def __init__(self, speed: int | float = 3, score: int = 0, remain: int = 5):
        """Initialize the BreakIt game."""
        self.screen = BreakItScreen().screen
        self.scoreboard = BreakItScoreboard(score=score)
        self.paddle = BreakItPaddle()
        self.speed = speed
        self.ball = BreakItBall(speed=self.speed)
        self.balls_remaining = BreakItBallsRemaining(balls_remaining_int=remain)
        self.bricks = BreakItBricks()
        self.brick_list = self.bricks.all_bricks
        self.brick_count = len(self.bricks.all_bricks)
        self.game_on = True
        self.game_over_text = None
        self.pause_game = False
        self.recent_paddle_collision = False
        self.recent_brick_collision = False
        self.restart_text = None
        self.x_spin = 1.25
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

    def paddle_x_spin(self):
        """Adjust ball's x-move based on paddle hit for spin effect."""

        # Ensure x_move is reset to original_speed, continuing direction:
        if self.ball.x_move < 0:
            original_speed_cont_dir = -self.ball.original_speed
        else:
            original_speed_cont_dir = self.ball.original_speed
        # Get ball's x-coordinate:
        ball_x = self.ball.xcor()
        # Define paddle's left side for left spin:
        paddle_x_left = self.paddle.xcor() - 30
        # Define paddle's right side for right spin:
        paddle_x_right = self.paddle.xcor() + 30
        # Ball continues in same direction if it hits middle of paddle:
        if paddle_x_left < ball_x < paddle_x_right:
            self.ball.x_move = original_speed_cont_dir
        # Ball always goes left if it hits left side of paddle:
        elif ball_x <= paddle_x_left:
            self.ball.x_move = -self.ball.original_speed * self.x_spin
        # Ball always goes right if it hits right side of paddle:
        elif ball_x >= paddle_x_right:
            self.ball.x_move = self.ball.original_speed * self.x_spin

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
        """Handle collisions with the paddle. Resets y_move to original_speed."""
        if self.are_x_y_cond_met(self.paddle) and not self.recent_paddle_collision:
            self.paddle_x_spin()
            self.ball.y_move = self.ball.original_speed
            self.recent_paddle_collision = True
            self.screen.ontimer(self.reset_recent_paddle_collision_flag, 1000)

    def brick_collision(self):
        """Handle collisions with bricks."""
        for i in self.brick_list:
            if self.are_x_y_cond_met(i) and not self.recent_brick_collision:
                self.speed_score_utility(i)

    def reset_recent_paddle_collision_flag(self):
        """Reset the recent paddle collision flag."""
        self.recent_paddle_collision = False

    def reset_recent_brick_collision_flag(self):
        """Reset the recent brick collision flag."""
        self.recent_brick_collision = False

    def next_round(self):
        """Start the next round after all bricks eliminated.
        Reinitiates all relevant attributes.
        Preserves score and number of balls.
        Increases ball speed."""
        self.screen.clear()
        self.__init__(speed=self.speed + .5,
                      score=self.scoreboard.score,
                      remain=self.balls_remaining.number)

    def restart_game(self):
        """Restart the BreakIt game.
        Calls `self.__init__()` with default values."""
        self.screen.clear()
        self.__init__()

    def quit_game(self):
        """Quit the BreakIt game."""
        self.screen.bye()

    def pause_toggle(self):
        self.pause_game = not self.pause_game

    def key_listeners(self):
        """Creates key listeners for movement/pause/quit/restart methods."""
        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_paddle_left, 'Left')
        self.screen.onkeypress(self.paddle.move_paddle_right, 'Right')
        self.screen.onkeypress(self.pause_toggle, 'p')
        self.screen.onkeypress(self.quit_game, 'q')
        self.screen.onkeypress(self.restart_game, 'r')

    def run_game(self):
        """Run the BreakIt game loop."""
        # Listen for keypresses:
        self.key_listeners()
        while self.game_on:
            if not self.pause_game:
                # time.sleep(ball.move_speed)
                time.sleep(0.0005)
                self.screen.update()
                self.ball.move()
                self.paddle_collision()
                self.brick_collision()
                if self.brick_count < 1:
                    self.next_round()
                if self.ball.ycor() < -450:
                    self.balls_remaining.decrease_balls_remaining()
                    if self.balls_remaining.number < 0:
                        self.game_over_text = BreakItGameOverText()
                        self.restart_text = BreakItRestartText()
                    else:
                        self.screen.ontimer(self.ball.reset_ball, 10)
            else:
                # time.sleep(0.0005)
                self.screen.update()
        self.screen.exit_on_click()

    def speed_score_utility(self, brick):
        """Adjust ball speed based on brick color.

        Args:
            brick (turtle.Turtle): The brick that was hit.
        """
        for i in brick_color_name_list:
            if brick.color()[0] == brick_color_rgb_dict[i]:
                if self.ball.y_move < 0:
                    self.ball.y_move = -self.ball.original_speed
                else:
                    self.ball.y_move = self.ball.original_speed
                self.ball.y_move *= brick_color_speed_dict[i]
                self.scoreboard.score += brick_color_score_dict[i]
                self.scoreboard.update_scoreboard()
                brick.reset()
                self.brick_count -= 1
                self.recent_brick_collision = True
                self.screen.ontimer(self.reset_recent_brick_collision_flag, 5)


if __name__ == "__main__":
    help(BreakIt)
    break_it = BreakIt()
