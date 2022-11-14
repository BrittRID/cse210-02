from game.casting.actor import Actor


class Time(Actor):
    """
    A record of Time

    Attributes:
        _time (int): The time passed in the game.
    """
    def __init__(self):
        super().__init__()
        self._time = 0
        self._len = 0
        self.add_time(0)

    def add_time(self, time):
        """Adds the given time.
        
        Args:
            time (int): The time to add.
        """
        # time = time / 100
        self._time += time
        # self.set_text(f"Score: {self._time}")