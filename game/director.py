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
        # self.score = 0
        # self.total_score = 0
        self.total_score = 300

        # points = card.deal(self)
        # print(points)

        # for i in range(5):
        #     card = cards()
        #     self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            # self.do_updates()
            # self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        first_card = card.deal(self)

        print(f"The card is: {first_card}")

        is_hl = input("Higher or lower? [h/l] ")

        second_card = card.deal(self)

        print(f"The next card was: {second_card}")
        

        if second_card >= first_card:
            if is_hl == "h":
                self.total_score += 100
                # get 100 points
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

        play_again = input("Play again? [y/n] ")

        if play_again == "n":
            self.is_playing = False
        #     quit()
       
    # def do_updates(self):
    #     """Updates the player's score.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     if not self.is_playing:
    #         return 

        
    #     card = self.cards()
    #     card.deal()
    #     self.score += card.points 
    #     self.total_score += self.score

    # def do_outputs(self):
    #     """Displays the card and the score. Also asks the player if they want to play again. 

    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     if not self.is_playing:
    #         return
        
    #     values = ""
        
    #     card = self.cards
    #     values = f"{card.value} "

    #     print(f"Your card was: {values}")
    #     print(f"Your score is: {self.total_score}\n")
    #     self.is_playing == (self.score > 0)