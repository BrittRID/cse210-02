import random


class get_word:
    """selects a random word from a list"""

    
    def __init__(self):

    # def get_word(self)

        # a list of words that may be chosen for the parachute game

        self.words = ["python", "class", "function", "encapsulation", "abstraction",
        "program", "comment", "object", "define", "random", "integer", "string", 
        "debugger", "terminal", "error", "assignment", "design", "articulate", "feedback",
        "developer", "array", "dictionary", "variable", "constant", "boolean", "operator",
        "lambda", "module", "iterator", "syntax", "tuple"]

        
    def get_word(self):
        # chooses and returns a random word from the list
        self._word = random.choice(self.words)
        return self._word




