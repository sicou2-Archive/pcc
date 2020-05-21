class GameStats:
    """A class for all game statistics."""

    def __init__(self, ai_game):
        """Initialize the statistics."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.game_stats()
        self.game_active = True

    def game_stats(self):
        """Statistics for current game state."""
        self.ships_left = self.settings.ship_limit
        self.fleets_left = self.settings.fleet_waves
        self.target_miss = self.settings.target_max_miss
