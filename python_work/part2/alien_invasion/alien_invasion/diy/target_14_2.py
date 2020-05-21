import pygame


class Target:
    """A class for the target in Target Practice."""

    def __init__(self, ai_game):
        """Initialize target settings and position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.target_color

        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                                self.settings.target_height)
        self.rect.x = self.screen_rect.right - (self.settings.target_width * 2)

        self.y = float(self.rect.y + 1)

    def update(self):
        self.y += (self.settings.target_speed * self.settings.target_direction)
        self.rect.y = self.y

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        if (self.rect.bottom >= self.screen_rect.bottom or
                self.rect.top <= 0):
            self.settings.target_direction *= -1
