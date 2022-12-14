import pygame
# Part A.
# x = 10
# for rows in range(10):
#     for i in range(1, rows+1):
#         print(x, end=' ')
#         x += 1
#     print()

# Part B.
# n = int(input('enter value: '))
#
# for line in range(n*2):
#     print('o', end='')
# print()
# for line in range(n-1):
#     print('o', end=' '*(n*2-2))
#     print('o')
# for line in range(n*2):
#     print('o', end='')


# Part C.
n = 5

# for i in range(n):
#     for j in range(1, n-i+1):
#         print(j*2-1, end=' ')
#     for space in range(1, i+1):
#         print(' ', end=' ')
#     for space in range(1, i+1):
#         print(' ', end=' ')
#     for j in range(n-i, 0, -1):
#         print(j * 2 - 1, end=' ')
#     print()
#
# for i in range(n):
#     for j in range(1, i+2):
#         print(j*2-1, end=' ')
#     for space in range(1, n-i):
#         print(' ', end=' ')
#     for space in range(1, n-i):
#         print(' ', end=' ')
#     for j in range(i+1, 0, -1):
#         print(j * 2 - 1, end=' ')
#     print()


# Part D.

"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    for x in range(0, 700, 10):
        for y in range(0, 500, 10):
            pygame.draw.rect(screen, 0x17cc0f, [x, y, 5, 5], 3)
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

