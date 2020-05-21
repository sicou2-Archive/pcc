import sys
from random import randint
from time import sleep

import pygame

from settings_c12_4 import Settings
from game_stats_13_6 import GameStats
from ship_c12_4 import Ship
from friend_c12_4 import Friend
from laser_c12_6 import Laser
from target_14_2 import Target
from button_c14_2 import Button


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create a game resources."""
        pygame.init()
        self.settings = Settings()

        # This block is for windowed mode
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # This block is for full screen mode.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.button = Button(self, "PLAY")
        self.target = Target(self)
        self.ship = Ship(self)
        self.friend = Friend(self)
        self.lasers = pygame.sprite.Group()

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_target()
                self.ship.update()
                self.friend.update()
                self._update_lasers()

            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self):
        if mouse_pos == self.button.rect:
            self.stats.game_active = True

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit(0)
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            # self.friend.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            # self.friend.moving_left = True
        elif event.key == pygame.K_UP:
            # self.ship.moving_up = True
            self.friend.moving_up = True
        elif event.key == pygame.K_DOWN:
            # self.ship.moving_down = True
            self.friend.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_laser()
        elif event.key == pygame.K_s:
            if self.ship.active == True:
                self.ship.active = False
                self.friend.active = True
            elif self.ship.active == False:
                self.ship.active = True
                self.friend.active = False

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            # self.friend.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            # self.friend.moving_left = False
        elif event.key == pygame.K_UP:  # 12.4
            #            self.ship.moving_up = False #12.4
            self.friend.moving_up = False
        elif event.key == pygame.K_DOWN:  # 12.4
            #            self.ship.moving_down = False
            self.friend.moving_down = False

    def _fire_laser(self):
        """Create a new laser and add it to the lasers group."""
        if len(self.lasers) < self.settings.max_lasers:
            new_laser = Laser(self)
            self.lasers.add(new_laser)

    def _update_lasers(self):
        """Update position of the beam and remove old lasers."""
        if self.stats.target_miss == 0:
            self.stats.game_active = False

        # Update laser position
        self.lasers.update()

        # Get rid of lasers off screen.
        for laser in self.lasers.copy():
            if laser.rect.left >= self.settings.screen_width:
                self.lasers.remove(laser)
                self.stats.target_miss -= 1
                print(self.stats.target_miss)

        self._check_laser_target_collisions()

    def _check_laser_target_collisions(self):
        for laser in self.lasers.copy():
            if pygame.sprite.spritecollideany(self.target, self.lasers):
                self.lasers.remove(laser)

        # self.stats.game_active = False

    def _create_target(self):
        target = Target(self)
        target_width, target_height = target.rect.size
        target.y = target_height
        target.x = self.settings.screen_width - (target_width * 2)
        target.rect.y = target.y
        target.rect.x = target.x

    def _check_target_edges(self):
        if self.target.check_edges():
            self._target_change_direction()

    def _update_target(self):
        self._check_target_edges()
        self.target.update()

    def _ship_collide(self):
        if pygame.sprite.spritecollideany(self.friend, self.aliens):
            if self.stats.ships_left > 0:
                self.aliens.empty()
                self.lasers.empty()

                self._create_fleet()
                self.ship.center_ship()
                self.stats.ships_left -= 1

                sleep(0.5)
            # else:
            #    self.stats.game_active = False

    def _target_change_direction(self):
        self.settings.alien_direction *= -1

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        self._ship_collide()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.target.draw_target()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        self.ship.blitme()
        self.friend.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
