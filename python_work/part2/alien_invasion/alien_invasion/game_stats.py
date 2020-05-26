class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = self._get_high_score()

        # Button status
        self.show_play = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score(self):
        file = "high_score.txt"
        with open(file) as f:
            high_score = int(f.read())
            if high_score:
                return high_score
            else:
                return 0

    def _export_high_score(self):
        file = "high_score.txt"
        with open(file, "w") as f:
            f.write(str(self.score))
