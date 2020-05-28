
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (180, 180, 180)

        # Ship settings
        self.ship_limit = 3

        # # Laser settings
        # self.laser_width = 3
        # self.laser_height = 15
        # self.laser_color = (5, 175, 15)
        # self.lasers_allowed = 3
        # self.laser_collide_remove = True

        # Setting for large laser for testing.
        self.laser_speed = 5.0
        self.laser_width = 800
        self.laser_height = 15
        self.laser_color = (255, 255, 0)
        self.lasers_allowed = 8
        self.laser_collide_remove = False

        # Alien settings
        self.fleet_drop_speed = 10

        # Game button text
        self.button_text = ['Play', 'Easy', 'Medium', 'Hard']

        # How quickly the game speeds up.
        self.difficulties = {'easy': 1.1, 'medium': 2.2, 'hard': 3.3}

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings('easy')

    def initialize_dynamic_settings(self, difficulties):
        """Initalize setting that change throughout the game."""
        self.ship_speed = 1.5
        self.laser_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Game diffuculty
        self.speedup_scale = self.difficulties[difficulties]

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.laser_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
