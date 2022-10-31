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

    def get_worth(self):
        """Gets the artifact's worth.
        
        Returns:
            int: point value.
        """
        return self._worth

    def set_points(self, worth):
        """Gets the artifact's worth in points.
        
        Returns:
            int: point value.
        """
        self.worth = worth
        