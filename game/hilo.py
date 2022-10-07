import random



# Add the class declaration. Use the following class comment.
class card:
    """A standard playing card, values range from 1-13

    The responsibility of card is to keep track of the card dealt, compare to the last card 
    dealt and calculate the points for it.

    Attributes:
        value (int): The number printed on the card.
        points (int): The number of points the turn is worth.
            100 points will be added to the total if the player guesses correctly
            75 points will be subtracted from the total if they play guesses incorrectly
            Game is over when the score reaches 0.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of card with a value and points attribute.

        Args:
            self (card): An instance of card.
        """
        self.value = 0
        self.points = 300

# 3) Create the roll(self) method. Use the following method comment.
    def deal(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (card): An instance of card.
        """
          
        #   The player earns 100 points if they guessed correctly.
        #   The player loses 75 points if they guessed incorrectly.
        
        self.value = random.randint(1,13)
        return self.value


