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
            # self.guessed_letters is sent in for input validation
            # to make sure the player doesn't guess a letter they
            # already guessed
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
        """Print out the word with underscores for unknown characters.

        Args:
            self (Director): An instance of Director.
        """

        self._display_word = ""

        # For every letter in the word
        for letter in self.word:
            # Check to see if it was guessed
            if letter in self.guessed_letters:
                self._display_word += letter
            else:
                self._display_word += "_"
        
        print(self._display_word)
                

    def check_won(self):
        """Check if the player won the game.
        
        Args:
            self (Director): An instance of Director.
        """

        self._display_word = ""

        # For every letter in the word
        for letter in self.word:
            # Check to see if it was guessed
            if letter in self.guessed_letters:
                self._display_word += letter
            else:
                self._display_word += "_"

        if self._display_word == self.word:
            return True
        else:
            return False


    def check_loss(self):
        """Check if the player lost the game.
        
        Args:
            self (Director): An instance of Director.
        """
        wrong_guesses = 0
        
        # For every guessed letter
        for guessed_letter in self.guessed_letters:
            # Check to see if it was correct
            if guessed_letter not in self.word:
                wrong_guesses += 1


        # If the number of wrong guessed letters is greater than 7 than the player loses
        if wrong_guesses > 7:
            return True
        else:
            return False
