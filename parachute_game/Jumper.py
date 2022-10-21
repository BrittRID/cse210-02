# Jumper is played according to the following rules.
# The puzzle is a secret word randomly chosen from a list.
# The player guesses a letter in the puzzle.
# If the guess is correct, the letter is revealed.
# If the guess is incorrect, a line is cut on the player's parachute.
# If the puzzle is solved the game is over.
# If the player has no more parachute the game is over.

from curses.ascii import isalpha

class Jumper:
    def user_inputs(guessed_letters):
        valid = False
        while valid == False:
            # print('Enter a letter:')
            letter = input("Enter a letter: ")
            letter = letter.lower()
            if letter.isalpha() == True:
                if letter not in guessed_letters:
                    if len(letter) == 1:
                        valid = True
                    else:
                        print("Enter only one letter")
                else:
                    print("You already guessed that letter.")
            else:
                print("Must be a letter")

        # print(f'The letter is: {letter}.')
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

    