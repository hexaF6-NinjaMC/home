from game.casting.score import Score

# class Director:


class Director (Score):
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        super().__init__()
        self._keyboard_service = keyboard_service
        self._video_service = video_service

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        # gem = cast.get_first_actor("gems")
        # rock = cast.get_first_actor("rocks")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)
        # gem.set_velocity(velocity)
        # rock.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with rocks or gems, and updates the scoreboard.

        Args:
            cast (Cast): The cast of actors.
            scoreboard: The score banner with the current session score.
        """

        score = cast.get_first_actor("scores")
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        # rocks = cast.get_actors("rocks")

        score.set_text(self.display_score())
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        # for rock in rocks:
        #     rock.move_next(max_x, max_y)
        #     if robot.get_position().equals(rock.get_position()):
        #         point = rock.get_point_value()
        #         scoreboard += point
        #         cast.remove_actor("rocks", rock)

        # for gem in gems:
        #     gem.move_next(max_x, max_y)
        #     if robot.get_position().equals(gem.get_position()):
        #         point = gem.get_point_value()
        #         scoreboard += point
        #         cast.remove_actor("gems", gem)

        # score.set_text(f"Score: {scoreboard}")

        for index, gem in enumerate(gems):
            gem.move_next(max_x, max_y)
            if robot.get_position().equals(gem.get_position()):
                calc = gem.get_message()
                self.update_points(calc)
                cast.remove_actor_by_index("gems", index)
                message = self.display_score()
                score.set_text(message)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
