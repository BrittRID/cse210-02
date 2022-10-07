from game.hilo import card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[card]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True

        self.total_score = 300


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()


    def get_inputs(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        first_card = card.deal(self)

        print(f"The card is: {first_card}")

        valid = False
        while valid == False:
            is_hl = input("Higher or lower? [h/l] ")

            is_hl = is_hl.lower()

            if is_hl == "h" or is_hl == "l":
                valid = True
        

        second_card = card.deal(self)

        print(f"The next card was: {second_card}")
        

        if second_card >= first_card:
            if is_hl == "h":
                # get 100 points
                self.total_score += 100
            else:
                # lose 75 points
                self.total_score -= 75
        else:
            if is_hl == "h":
                # lose 75 points
                self.total_score -= 75
            else:
                # get 100 points
                self.total_score += 100

        
        print(f"Your score is: {self.total_score}")

        if self.total_score <= 0:
            self.is_playing = False

        valid2 = False
        while valid2 == False:
            play_again = input("Play again? [y/n] ")

            play_again = play_again.lower()

            if play_again == "y" or play_again == "n":
                valid2 = True

        

        if play_again == "n":
            self.is_playing = False
