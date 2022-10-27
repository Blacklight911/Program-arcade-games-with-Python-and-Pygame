import pygame

# Define some colors

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (200, 150, 150)

pygame.init()

# Set the width and height of the screen [width, height]

size = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My World")

# Loop until the user clicks the close button.

done = False

# Used to manage how fast the screen updates

clock = pygame.time.Clock()

circle_x = 0
circle_y = 100
circle_change_x = 0
rect_change_y = 500
rect_sky_color = 0x1984e2


# -------- Main Program Loop -----------

while not done:

    # --- Main event loop

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    if circle_change_x > 750:
        circle_change_x = 0
        rect_sky_color = 0x1984e2

    if circle_change_x > 200:
        rect_sky_color = 0xb58d1d

    if circle_change_x > 350:
        rect_sky_color = 0xcc6516

    if rect_change_y != 0:
        rect_change_y += -1
    else:
        rect_change_y = 0
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands

    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the

    # background image.

    screen.fill(white)

    # background
    pygame.draw.rect(screen, rect_sky_color, [0, 0, 700, 200], 0)
    pygame.draw.rect(screen, 0x208211, [0, 202, 700, 700], 0)
    pygame.draw.line(screen, 0x6f4f0c, [0, 200], [700, 200], 25)
    pygame.draw.circle(screen, 0xd6c01a, [circle_x + circle_change_x, circle_y], 70, 0)
    pygame.draw.rect(screen, black, [300, 213, 300, 700])
    pygame.draw.line(screen, 0xc1de1b, [300, 213], [300, 1000], 7)
    pygame.draw.line(screen, 0xc1de1b, [600, 213], [600, 1000], 7)

    # Road markings
    for y in range(220, 700, 30):
        pygame.draw.line(screen, 0xc1de1b, [450, y], [450, y + 20], 7)

    # Car
    pygame.draw.rect(screen, 0x0a0966, [490, 300 + rect_change_y, 78, 60], 0)
    pygame.draw.rect(screen, 0xc1de1b, [500, 350 + rect_change_y, 69, 20])
    pygame.draw.line(screen, 0xc1de1b, [495, 350 + rect_change_y], [495, 450 + rect_change_y], 3)
    pygame.draw.line(screen, 0xc1de1b, [565, 350 + rect_change_y], [565, 450 + rect_change_y], 3)
    pygame.draw.rect(screen, 0x2b3136, [490, 350 + rect_change_y, 79, 100], 0)
    pygame.draw.rect(screen, 0x97bdde, [495, 330 + rect_change_y, 69, 20])
    pygame.draw.rect(screen, 0x7c0092, [495, 330 + rect_change_y, 70, 20], 2)
    pygame.draw.line(screen, red, [500, 450 + rect_change_y], [500, 450 + rect_change_y], 5)
    pygame.draw.line(screen, red, [560, 450 + rect_change_y], [560, 450 + rect_change_y], 5)
    pygame.draw.rect(screen, 0xd8de1f, [490, 350 + rect_change_y, 79, 95], 2)

    # Дом или событие на траве
    circle_change_x += 2

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(60)

# Close the window and quit.

pygame.quit()
