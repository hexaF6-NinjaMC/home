from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """
    Artifacts are items of significant interest.
    It should give a description of itself.

    Attr:
        __art_description (str): A short description of the artifact.
    """

    def __init__(self):
        super().__init__()
        self.__art_description = ""

    def get_message(self):
        """
        Gets the artifact message
        Returns:
            string: the artifact description
        """

        return self.__art_description

    def set_message(self, description):
        """
        Updates the artifact description to a given one.
        Args:
            description (str): The given artifact description.
        """

        self.__art_description = description