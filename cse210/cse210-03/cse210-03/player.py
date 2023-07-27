class Player:
    """Receives player input and pushes it to the Conductor in a 
    variable type that the Conductor can process properly

    Attributes:
        _choosen_letters: A list that contains the user letters.
        _guess (str): The user's letter guess.
    """

    def __init__(self):
        """ Constructs a new list of letters for the player

        Args: self (player): an instance of player.
        """
        self.__chosen_letters = []

    def guess_letter(self):
        """Gets an input letter from the user

        Args:
            self (player): An instance of Player.

        Returns:
            string: A letter from the player.
        """
        self.__guess = str(input("Guess your letter A-Z! ")).lower()
        self.__chosen_letters.append(self.__guess.lower())
        return self.__guess
