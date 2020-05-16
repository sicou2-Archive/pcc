import sys
from random import randint

import pygame

from settings_c12_4 import Settings
from ship_c12_4 import Ship
from friend_c12_4 import Friend
from laser_c12_6 import Laser
from star import Star
from alien_c13_5 import Alien


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

        self.ship = Ship(self)
        self.friend = Friend(self)
        self.lasers = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_field()
        self._create_fleet()

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self._update_stars()
            # self._update_fleet()
            self.ship.update()
            self.friend.update()
            self._update_lasers()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

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
        # Update laser position
        self.lasers.update()

        # Get rid of lasers off screen.
        for laser in self.lasers.copy():
            if laser.rect.left >= self.settings.screen_width:
                self.lasers.remove(laser)

        self._check_laser_alien_collisions()

    def _check_laser_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.lasers, self.aliens,
                                                True, True)

        if not self.aliens:
            self.lasers.empty()
            self._create_fleet()

    def _create_field(self):
        """Create a field of stars."""
        # Create a star and determine the number of stars in the row.
        # Spacing between each star is equal to one star width.
        star = Star(self)
        star_width, star_height = star.rect.size
        self.available_space_x = int((
            self.settings.screen_width - (.5 * star_width)))
        self.number_stars_x = self.available_space_x // star_width

        # Determine the number of rows of aliens that fit on the screen.
        # ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * star_height)

        # Create the full field of stars
        # for row_number in range(number_rows):
        #     for star_number in range(number_stars_x):
        #         self._create_star(star_number, row_number)

    def _create_star(self, star_number=0, row_number=0):
        """Create a star and place it in the row."""
        if len(self.stars) < 100:
            star = Star(self)
            star_width, star_height = star.rect.size
            # star.x = star_width + 2 * star_width * star_number
            star.x = randint(0, self.available_space_x)
            star.rect.x = star.x + randint(-15, 15)
            star.rect.y = ((star.rect.height + 2 * star.rect.height *
                            row_number) + randint(-15, 15))
            self.stars.add(star)

    def _remove_star(self):
        for star in self.stars.copy():
            if star.rect.top >= self.settings.screen_height:
                self.stars.remove(star)

    def _update_stars(self):
        """Update the location of the stars on the screen."""
        self._create_star()
        self._remove_star()
        self.stars.update()

    def _create_fleet(self):

        alien = Alien(self)
        available_space_y, available_space_x = self._calculate_fleet()

        for alien_number in range(available_space_y):
            for row_number in range(available_space_x):
                self._create_alien(alien_number, row_number)

    def _calculate_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # return available_space_y, available_space_x
        return ((self.settings.screen_height // (alien_height * 2)),
                (self.settings.screen_width // (alien_height * 2)) - 3)

    def _create_alien(self, alien_number, alien_row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = (alien_number * alien_height * 2) + 5
        alien.x = self.settings.screen_width - (
            (alien_row + 1) * alien_width * 2)
        alien.rect.y = alien.y
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._fleet_change_direction()
                break

    def _fleet_change_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.alien_advance
        self.settings.alien_direction *= -1

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.aliens.draw(self.screen)
        self.ship.blitme()
        self.friend.blitme()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
