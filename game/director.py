from game.hilo import hilo


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
        self.score = 0
        self.total_score = 0

        for i in range(5):
            card = cards()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        play_again = input("Play Again? [y/n] ")
        self.is_playing = (play_again == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        
        card = self.cards()
        card.deal()
        self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        
        card = self.cards
        values = f"{card.value} "

        print(f"Your card was: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)