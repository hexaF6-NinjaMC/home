from game.word_gen import WordGen
from game.player import Player
from game.display import Display


class Conductor:

    def __init__(self):
        """
        This initializes an instance of the Conductor (self)
        """
        guessed = False
        self.__guessed = guessed
        self.__guessed_letters = []
        self.__guessed_words = []
        self.__tries = 4

    def start(self):
        """
        This starts the game
        Args: self (Conductor)
        """
        gen = WordGen()
        self.__word = gen.generate_word()
        self.__word_completion = "^" * len(self.__word)
        self.__play = True
        self.__guessed = False

        display = Display()
        if self.__play:
            print(display.display_parachute(self.__tries))
            print(self.__word_completion)
            self.get_guess()
            self.do_guess_logic()
        self.game_end()

    def get_guess(self):
        """
        This function retrieves the player's guess (a letter) as a result of the Player input
        Args: self (Conductor)
        Returns:
            string: A letter from the player.
        """
        player = Player()
        self.__guess = player.guess_letter()
        return self.__guess

    def do_guess_logic(self):
        """
        This function  receives necessary data to process
        Args: self (Conductor)
        """
        player = Player()
        display = Display()
        while not self.__guessed and self.__tries > 0:
            if len(self.__guess) == 1 and self.__guess.isalpha():
                if self.__guess in self.__guessed_letters:
                    print("You already guessed that letter", self.__guess)
                elif self.__guess not in self.__word:
                    print(self.__guess, "is not in the word.")
                    self.__tries -= 1
                    self.__guessed_letters.append(self.__guess)
                else:
                    print("Good job,", self.__guess, "is in the word!")
                    self.__guessed_letters.append(self.__guess)
                    self.__word_as_list = list(self.__word_completion)
                    indices = [i for i, letter in enumerate(
                        self.__word) if letter == self.__guess]
                    for index in indices:
                        self.__word_as_list[index] = self.__guess
                    self.__word_completion = "".join(self.__word_as_list)
                    if "^" not in self.__word_completion:
                        self.__guessed = True
            elif len(self.__guess) == len(self.__word) and self.__guess.isalpha():
                if self.__guess in self.__guessed_words:
                    print("You already guessed the word", self.__guess)
                elif self.__guess != self.__word:
                    print(self.__guess, "is not the word.")
                    self.__tries -= 1
                    self.__guessed_words.append(self.__guess)
                else:
                    self.__guessed = True
                    self.__word_completion = self.__word
            else:
                print("Not a valid guess.")
            print(display.display_parachute(self.__tries))
            print(self.__word_completion)
            print()

            if self.__tries != 0 and self.__guessed != True:
                self.__guess = player.guess_letter()

    def game_end(self):
        """
        This method determines whether to display the win message, or loss message, based on the "guessed" status. Then, it asks player if a new round would be desired.
        Args: self (Conductor)
        """

        if self.__guessed == True:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " +
                  self.__word + ". Maybe next time!")

        if input("Play Again? (Y/N) ").upper() == "Y":
            self.__tries = 4
            self.__guessed_letters.clear()
            self.__guessed_words.clear()
            self.start()
