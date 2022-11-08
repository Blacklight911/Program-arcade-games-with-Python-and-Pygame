import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
# Bump song for program edges.
bump = pygame.mixer.Sound('bump.wav')


class Player(pygame.sprite.Sprite):
	"""
	The class is the player-controlled sprite
	"""
	# -- Methods
	def __init__(self, x, y):
		"""Constructor function"""
		# Call the parent's constructor
		super().__init__()

		# Set height, width
		self.image = pygame.Surface([15, 15])

		# Load image
		self.image = pygame.image.load('ufo.png').convert()
		self.image.set_colorkey(BLACK)

		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		# -- Attributes
		# Set speed vector
		self.change_x = 0
		self.change_y = 0

	def changespeed(self, x, y):
		""" Change the speed of the player"""

		self.change_x += x
		self.change_y += y

	def update(self):
		""" Find a new position for the player"""

		self.rect.x += self.change_x
		self.rect.y += self.change_y
		if self.rect.x > 700:
			self.rect.x = 680
			bump.play()
		if self.rect.x < -1:
			self.rect.x = -1
			bump.play()
		if self.rect.y > 400:
			self.rect.y = 385
			bump.play()
		if self.rect.y < -1:
			self.rect.y = -1
			bump.play()
