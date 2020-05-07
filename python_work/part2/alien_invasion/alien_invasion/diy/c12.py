import sys

import pygame

class C12:
    """This is the class for the TIY in chapter 12."""

    def __init__(self):
        """This is the init for the C12 'game' and resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
#        pygame.display.set_caption("Chapter 12 Try It Yourself")

    def game_loop(self):
        """This is the loop for the module."""
        #self.screen.fill()
        
        while True:
            #pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            if event.type == pygame.KEYDOWN:
                print(event.key)

if __name__ == '__main__':
    c12 = C12()
    c12.game_loop()