from random import choice, randint

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class for creating and storing stars in the sky."""

    def __init__(self, ai_game):
        """Initializes the stars and their starting positions."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.speed = randint(1, 100)
        # Load a random image for a list and set its rect attribute.
        self.images = [
            'images/star_1.bmp', 'images/star_2.bmp',
            'images/star_3.bmp', 'images/star_4.bmp'
        ]

        self.image = pygame.image.load(choice(self.images))
        self.image = pygame.transform.rotate(self.image, randint(0, 360))
        self.rect = self.image.get_rect()

        # Start each star near the top left of the screen and rotate randomly
        self.rect.x = self.rect.width
        self.rect.y = -45

        # Store the stars exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if star is off the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        """Update the positions of the falling stars"""

        self.y += self.speed * .01
        self.rect.y = self.y
