import constants
import math
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # No need for food
            # self._handle_food_collision(cast)
            # snake and snake collision will likely happen here
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            # Grow the snake
            self._tail_growth_over_time(cast)

    # def _handle_food_collision(self, cast):
    #     """Updates the score and moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     snake = cast.get_first_actor("snakes")
    #     head = snake.get_head()

    #     if head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(points)
    #         score.add_points(points)
    #         food.reset()

    # New function that grows the tail over time
    def _tail_growth_over_time(self, cast):
        """Updates the length of the snake's tailes over time.

        Args:
            cast (Cast): The cast of Actors in the game.
        """

        time = cast.get_first_actor("time")
        # time = cast.get_first_actor("time")
        # time.time += 1
        time.add_time(1)
        snake = cast.get_first_actor("snakes")
        time._len = math.ceil(time._time / 1000)
        print(time._len)
        if time._len < 2:
            snake.grow_tail(time._len)
        # time._len = time._time / 100
        # if time._len > 10:
        #     sn_ln = math.ceil(time._len / 100)
        # else:
        #     sn_ln = 0
        # sn_ln = time._len / 100
        # sn_ln = math.ceil(time._time / 1000)
        

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            # food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            # food.set_color(constants.WHITE)