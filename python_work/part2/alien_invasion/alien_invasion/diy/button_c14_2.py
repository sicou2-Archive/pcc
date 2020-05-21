import pygame.font


class Button:
    """A class for a button in the game."""

    def __init__(self, ai_game, msg):
        """Initializes the button and places it on the screen."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.btn_color = (50, 255, 10)
        self.msg_color = (205, 0, 245)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):

        self.msg_img = self.font.render(msg, True, self.msg_color,
                                        self.btn_color)
        self.msg_rect = self.msg_img.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_rect)
