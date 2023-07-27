import random

"""
Change director imports to match what I assume will be scene_manager in batter program.
"""
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.artifact import Artifact
from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed Fighter"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 50


def main():

    # create the cast
    cast = Cast()

    # create the scoreboard banner
    score = Actor()
    score.set_text("")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("scores", score)

    # create the robot
    """
    The image we are looking for:

        -   -   -
        -   -   -
        -   -   -
        -   -   -
        -   x   -
        -   -   -

    to get an idea of the placement of the fighter (labelled "x").
    I believe this doesn't put too much initial stress on the player at the first scene.
    """

    x = int(MAX_X / 2)  # Start in the middle at the bottom of the window ~AB
    y = int(MAX_Y / 2)  # Set the robot to the bottom of the window ~AB - can change this to start at the top of the lower third

    position = Point(x, (MAX_Y - FONT_SIZE))

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(["o", "*"])
        message = ("-", "+")[text == "*"]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_velocity(Point(0, 5))
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("gems", artifact)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
