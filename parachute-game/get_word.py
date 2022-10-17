import random


class get_word:
    """selects a random word from a list"""

    
    def __init__(self):

        # a list of words that may be chosen for the parachute game

        words = ["python", "class", "function", "encapsulation", "abstraction",
        "program", "comment", "object", "define", "random", "integer", "string", 
        "debugger", "terminal", "error", "assignment", "design", "articulate", "feedback",
        "developer", "array", "dictionary", "variable", "constant", "boolean", "operator",
        "lambda", "module", "iterator", "syntax", "tuple"]

        # chooses and returns a random word from the list
        self._word = random.choice(words)
        return self._word




