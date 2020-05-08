import pygame

from pygame.sprite import Sprite

class Laser(Sprite):
    """A class to manage lasers."""

    def __init__(self, ai_game):
        """Initialize the properties of a laser beam and its position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.laser_color

        # Create a laser rect at (0, 0) then move to correct position.
        self.rect = pygame.Rect(0, 0, self.settings.laser_width, 
            self.settings.laser_height)
        self.rect.midright = ai_game.friend.rect.midright

        # Store the laser's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the beam from left to right on the screen."""
        # Update the decimal position of the beam. 
        self.x += self.settings.laser_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_laser(self):
        """Draw the laser on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)