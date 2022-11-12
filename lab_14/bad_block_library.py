"""
Bad block library
"""
import random
import pygame
import block_library
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 700
pygame.init()
bad_block_sound = pygame.mixer.Sound('bad_block.wav')


class BadBlock(block_library.Block):
    """
    Bad block class inherit the Block class and pygame methods from class pygame.sprite.Sprite
    """

    def reset_position(self):
        self.rect.y = random.randrange(-100, -10)
        self.rect.x = random.randrange(0, SCREEN_WIDTH)

    def update(self):
        """
        Updating position of rectangle
        :return: x and y position in randrange random function
        """
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT:
            self.reset_position()
