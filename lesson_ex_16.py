import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Grid of numbers
grid = []

for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
width = 20
height = 20
margin = 5
size = (255, 255)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            grid[row][column] = 1
            print('Click', pos, 'Grid coordinates', row, column)
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()