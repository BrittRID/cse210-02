from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide it's worth, a point value.

    Attributes:
        _worth (int): either -1 or 1
    """
    def __init__(self):
        super().__init__()
        self.worth = 0
        self._message = ""

    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_worth(self):
        """Gets the artifact's worth.
        
        Returns:
            int: point value.
        """
        return self.worth

    def set_points(self, worth):
        """Gets the artifact's worth in points.
        
        Returns:
            int: point value.
        """
        self._worth = worth
        