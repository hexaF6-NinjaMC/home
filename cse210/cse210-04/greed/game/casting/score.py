# from game.casting.actor import Actor

# from game.casting.actor import Actor


# class Score(Actor):
class Score:
    """
    The responsibility of a Score is to update and display the user's score.

    Attributes:
        _points: The current user points.
    """

    def __init__(self):
        # super().__init__()
        # self._points = 0
        self.__score = 0
        self.__substract = 1
        self.__add = 1

    def update_points(self, calc):
        """Returns the current score.

        Returns:
            int: The current score.
        """
        if calc == "+":
            self.__score = self.__score + self.__add
        elif calc == "-":
            print("discounting")
            self.__score = self.__score - self.__substract
        else:
            self.__score = 0

    # def add_points(self, points):

    def display_score(self):
        """Updates and displays the points as the user plays.

        Args:
            points: The user points.
        """

        score_message = "Score: " + str(self.__score)
        # self._points += points
        # self.set_text(f"Score: {self._points}")
        return score_message
