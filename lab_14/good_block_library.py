"""
Good block library
"""
import random
import pygame
import block_library

pygame.init()
good_block_sound = pygame.mixer.Sound('good_block.wav')


class GoodBlock(block_library.Block):
    """
    Good block class inherit the Block class and pygame methods from class pygame.sprite.Sprite
    """

    def update(self):
        """
        Updating position of rectangle
        :return: x and y position in randrange random function
        """
        self.rect.x += random.randrange(-3, 4)
        self.rect.y += random.randrange(-3, 4)
