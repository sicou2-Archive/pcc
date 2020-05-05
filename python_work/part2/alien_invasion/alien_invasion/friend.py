import pygame

class Friend:
    """A class to manage friendly ships."""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the friendly ship image and get its rect.
        self.image = pygame.image.load('images/friend.bmp')
        self.rect = self.image.get_rect()

        # Start each friendly ship at the middle left of the screen.
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)