"""
	This lab practices using Pygame sprites as described in Chapter 13.
"""
import random
import pygame
import player_library
import block_library
import good_block_library
import bad_block_library

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
# This is a list of every sprite.
# All blocks and the player block as well.
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
	# This represents a block
	block = good_block_library.GoodBlock('star.png', 20, 15)

	# Set a random location for the block
	block.rect.x = random.randrange(SCREEN_WIDTH)
	block.rect.y = random.randrange(SCREEN_HEIGHT)

	# Add the block to the list of objects
	good_block_list.add(block)
	all_sprites_list.add(block)

for i in range(50):
	# This represents a block
	block = bad_block_library.BadBlock('alien.png', 20, 15)

	# Set a random location for the block
	block.rect.x = random.randrange(SCREEN_WIDTH)
	block.rect.y = random.randrange(SCREEN_HEIGHT)

	# Add the block to the list of objects
	bad_block_list.add(block)
	all_sprites_list.add(block)

# Create a Blue player block
player = player_library.Player(20, 15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
DONE = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
font = pygame.font.Font(None, 20)


# -------- Main Program Loop -----------
while not DONE:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			DONE = True

		# Set the speed based on the key pressed
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_d:
				player.changespeed(3, 0)
			elif event.key == pygame.K_w:
				player.changespeed(0, -3)
			elif event.key == pygame.K_s:
				player.changespeed(0, 3)

		# Reset speed when key goes up
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				player.changespeed(3, 0)
			elif event.key == pygame.K_d:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_w:
				player.changespeed(0, 3)
			elif event.key == pygame.K_s:
				player.changespeed(0, -3)

	# Clear the screen
	screen.fill(WHITE)

	# Blit score on screen
	text = font.render('Score: ' + str(score), True, BLACK)
	screen.blit(text, [10, 350])

	# Updating moving sprites
	all_sprites_list.update()
	# See if the player block has collided with good_block.
	blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
	if blocks_hit_list:
		good_block_library.good_block_sound.play()

	# See if the player block has collided with bad_block.
	blocks_hit_list_red = pygame.sprite.spritecollide(player, bad_block_list, True)
	if blocks_hit_list_red:
		bad_block_library.bad_block_sound.play()

	# Check the list of collisions.
	for block in blocks_hit_list:
		score += 1

	for block in blocks_hit_list_red:
		score -= 1
	# Draw all the spites
	all_sprites_list.draw(screen)

	# Go ahead and update the screen with 	what we've drawn.
	pygame.display.flip()

	# Limit to 60 frames per second
	clock.tick(60)

pygame.quit()
