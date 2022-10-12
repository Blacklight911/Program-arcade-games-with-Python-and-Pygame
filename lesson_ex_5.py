import pygame

# Initialisation engine.
pygame.init()

# Define some colors.
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Hexadecimal.

white_hex = [0xFF, 0xFF, 0xFF]

pi = 3.141592653

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Blacklight cool game')

# loop in
done = False

# Screen frame rate
clock = pygame.time.Clock()

font = pygame.font.Font('C:/WINDOWS/Fonts/BERNHC.TTF', 25)

# -------------- Main Loop ----------------
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(white)

    score = 100
    text = font.render('Score ' + str(score), True, black)

    screen.blit(text, [300, 400])

    # --- Drawing code should go here
    for x in range(0, 100, 20):
        # draw line witch x and y parameters.
        pygame.draw.line(screen, green, [x, 0], [x, 100], 5)

    # Draw a rectangle.
    pygame.draw.rect(screen, black, [150, 50, 250, 100], 5)

    # Draw a ellipsoid.
    pygame.draw.ellipse(screen, black, [150, 50, 250, 100], 5)

    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(screen, green, [150, 151, 250, 200], pi / 2, pi, 2)
    pygame.draw.arc(screen, black, [150, 151, 250, 200], 0, pi / 2, 2)
    pygame.draw.arc(screen, red, [150, 151, 250, 200], 3 * pi / 2, 2 * pi, 2)
    pygame.draw.arc(screen, blue, [150, 151, 250, 200], pi, 3 * pi / 2, 2)

    # This draw a triangle using polygon command
    pygame.draw.polygon(screen, black, [[500, 100], [400, 200], [600, 200]], 5)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

