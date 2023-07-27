from game.casting.actor import Actor


class Gem(Actor):
    """
    Gems are items of significant interest. Try to obtain these!!!
    It should give a value of positive 1.

    Attr:
        __point (integer): A value assigned to the gem.
    """

    def __init__(self):
        super().__init__()
        self.__gempoint = 1

    def get_point_value(self):
        """
        Assigns the gem's point value
        Returns:
            point (integer): 1
        """

        return self.__gempoint

    def set_point_value(self, gempoint):
        """
        Updates the colloid value to a given one.
        Args:
            point (integer): The given colloid value.
        """

        self.__point = gempoint