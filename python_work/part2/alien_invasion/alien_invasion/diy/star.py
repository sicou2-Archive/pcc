from random import choice, randint

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class for creating and storing stars in the sky."""

    def __init__(self, ai_game):
        """Initializes the stars and their starting positions."""
        super().__init__()
        self.screen = ai_game.screen

        # Load a random image for a list and set its rect attribute.
        self.images = [
            'images/star_1.bmp', 'images/star_2.bmp',
            'images/star_3.bmp', 'images/star_4.bmp'
        ]
        self.image = pygame.transform.rotate(
            pygame.image.load(choice(self.images)), randint(0, 72))

        # self.image = pygame.image.load(choice(self.images))

        self.rect = self.image.get_rect()

        # Start each star near the top left of the screen and rotate randomly
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the stars exact positions
        self.x = float(self.rect.x)
