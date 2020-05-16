import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """This is the Alien class for the DIY Alien Invasion."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        # Start each alien at the top right of the screen
        self.rect.x = self.settings.screen_width - (self.rect.width * 1.5)
        self.rect.y = self.rect.height * .5

        # This is the alien's exact y position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if alien at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Move the alien up/down on the screen and updates its position."""
        self.y += (self.settings.alien_speed * self.settings.alien_direction)
        self.rect.y = self.y
