
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (180, 180, 180)

        # Ship settings
        self.ship_speed = 1.5

        # Laser settings
        self.laser_speed = 1.0
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (5, 175, 15)
        self.lasers_allowed = 3
        self.laser_collide_remove = True

        # # Setting for large laser for testing.
        # self.laser_speed = 5.0
        # self.laser_width = 800
        # self.laser_height = 15
        # self.laser_color = (255, 255, 0)
        # self.lasers_allowed = 8
        # self.laser_collide_remove = False

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 represents right; -1 represents left.
        self.fleet_direction = 1
