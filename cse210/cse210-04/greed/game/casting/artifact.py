from game.casting.actor import Actor

""" create gems and rock and upates on the screen for Score value
"""


class Artifact(Actor):

    def __init__(self):
        """Constructs a new Actor."""
        self.__message = ""

    def set_message(self, message):
        self.__message = message

    def get_message(self):
        return self.__message
