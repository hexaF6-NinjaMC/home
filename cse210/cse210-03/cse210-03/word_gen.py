import random


class WordGen:
    """A class that generates a random word from an existing list for gameplay.

    Attributes:
    _word_list: A list of potential words to be used for gameplay
    _game_word (str): The randomly chosen word to be used for a single playthrough of the game
    """

    def __init__(self):
        """ Provides database of words for the word generator

        Args: self (word_gen): an instance of word_gen.
        """

        self.__word_list = ["skateboard", "book", "rain", "key", "worm",
                           "chimney", "coin", "dog", "starfish", "cupcake"]

    def generate_word(self):
        """Selects a random word to be used for gameplay

        Args:
            self (word_gen): An instance of word_gen.

        Returns:
            string: A random word from the word list.
        """

        __game_word = random.choice(self.__word_list)

        return __game_word
