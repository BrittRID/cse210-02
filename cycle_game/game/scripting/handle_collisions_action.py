import constants
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
            # snake and snake collision
            self._handle_snake_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            # Grow the snake
            self._tail_growth_over_time(cast)
            


    # New function that grows the tail over time
    def _tail_growth_over_time(self, cast):
        """Updates the length of the snake's tailes over time.

        Args:
            cast (Cast): The cast of Actors in the game.
        """

        snake = cast.get_first_actor("snake 1")
        snake2 = cast.get_first_actor("snake 2")
        time = cast.get_first_actor("time")
        time.add_time(1)

        if time._time == 10:
            snake2.grow_tail(1)
            snake.grow_tail(1)
            time.reset_time()

    def _handle_snake_collision(self, cast):
        "If the snakes collide the game ends"

        # print("checking")
        snake = cast.get_first_actor("snake 1")
        snake2 = cast.get_first_actor("snake 2")

        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]

        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]

        if head.get_position().equals(head2.get_position()):
            self._is_game_over = True
        
        for segment in segments2:
            if head.get_position().equals(segment.get_position()):
            
                self._is_game_over = True
        
        for segment in segments:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snake 1")
        snake2 = cast.get_first_actor("snake 2")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]

        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snake 1")
            snake2 = cast.get_first_actor("snake 2")
            segments = snake.get_segments()
            segments2 = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)
