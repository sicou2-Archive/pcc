class GameStats:
    """A class for all game statistics."""

    def __init__(self, ai_game):
        """Initialize the statistics."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_game()
        self.game_active = False
        self.hits_on_level = 0

    def reset_game(self):
        """Statistics for current game state."""
        self.ships_left = self.settings.ship_limit
        self.fleets_left = self.settings.fleet_waves
        self.target_miss = self.settings.target_max_miss
        self.reset_level()

    def reset_level(self):
        self.hits_on_level = 0

    def target_level_hit(self):
        self.hits_on_level += 1
