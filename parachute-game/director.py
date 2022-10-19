# Imports
# from # import #

# Import the word
from get_word import get_word

# Import the function to print the parachute
from parachute import parachute

# Import the function to get the user's guess
from guess import guess

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (string): The word the player is trying to guess.
        is_playing (boolean): Whether or not the game is being played.
        guessed_letters (list): A list of guessed characters.
        # ? Display Parachute
        # ? Display word with underscores
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guessed_letters = []
        self.is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            # If no letter have been guessed
            if self.guessed_letters == []:
                # Get the word from the get_word function in the get_word file
                self.word = get_word.get_word()

            # Print out the word with blanks
            self.print_word()

            # print out the current parachute
            parachute.parachute()

            # Get the player's input (guess)
            player_guess = guess.guess(self.guessed_letters)
            # Add the guessed letter to the guessed_letters list
            self.guessed_letters.append(player_guess)

            # Determine if the game is won
            if self.check_won() == True:
                print("You got it!")
                print(self.word)
                self.is_playing = False
            # Determine if the game is lost 
            elif self.check_loss() == True:
                print("Sorry, you lost!")
                parachute.parachute()
                print(f"The word was {self.word}")

            


    def print_word(self):
    def check_won(self):
    def check_loss(self):
