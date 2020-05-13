
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5
        self.friend_speed = .5

        # Laser settings
        self.laser_width = 15
        self.laser_height = 3
        self.laser_speed = 1.0
        self.laser_color = (250, 5, 30)
        self.max_lasers = 3
