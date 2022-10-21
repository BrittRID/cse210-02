# Jumper is played according to the following rules.
# The puzzle is a secret word randomly chosen from a list.
# The player guesses a letter in the puzzle.
# If the guess is correct, the letter is revealed.
# If the guess is incorrect, a line is cut on the player's parachute.
# If the puzzle is solved the game is over.
# If the player has no more parachute the game is over.

from curses.ascii import isalpha

class Jumper:
    def user_inputs(self, guessed_letters):
        valid = False
        while valid == False:
            print('Enter a letter:')
            letter = input()
            letter = letter.lower()
            if letter == letter.isalpha():
                if letter not in guessed_letters:
                    if letter.len() == 1:
                        valid = True

        print(f'The letter is: {letter}.')
        return letter


            
        # try:
        #     letter = letter.isalpha()
        # except:
        #     print('The correct letter.')
        #     continue
        # if letter < 1:
        #     print('Incorrect letter.')
        #     continue
        # break

    