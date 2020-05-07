import pygame

from ship import Ship

class Friend(Ship):
    """A class to manage friendly ships."""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position."""

        super().__init__(ai_game)
        # self.screen = ai_game.screen
        # self.settings = ai_game.settings
        # self.screen_rect = ai_game.screen.get_rect()

        # # Load the friendly ship image and get its rect.
        self.image = pygame.image.load('images/friend.bmp')
        self.rect = self.image.get_rect()

        # Start each friendly ship at the middle left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y) #12.4

        # # Movement flags
        self.active = False #12.4
        # self.moving_right = False
        # self.moving_left = False
        # self.moving_up = False #12.4
        # self.moving_down = False #12.4

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        
        if self.active:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.friend_speed
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.friend_speed
            if self.moving_up and self.rect.top > 0: #12.4
                self.y -= self.settings.friend_speed #12.4
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            #12.4
                self.y += self.settings.friend_speed #12.4
            
        #Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    # def blitme(self):
    #     """Draw the ship at its current location."""
    #     self.screen.blit(self.image, self.rect)