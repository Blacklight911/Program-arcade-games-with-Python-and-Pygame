import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, black, [1 + x, 0 + y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, black, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, black, [5 + x, 17 + y], [0 + x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, red, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Hands
    pygame.draw.line(screen, red, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, red, [5 + x, 7 + y], [1 + x, 17 + y], 2)


def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, white, [35 + x, 0 + y, 25, 25])
    pygame.draw.ellipse(screen, white, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, white, [0 + x, 65 + y, 100, 100])


pygame.mouse.set_visible(False)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # If User press button
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        # If User release button
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    # --- Game logic should go here
    if x_coord > 695:
        x_speed = -1
    if x_coord < 0:
        x_speed = 1
    if y_coord > 470:
        y_speed = -1
    if y_coord < 0:
        y_speed = 1
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(green)

    # --- Drawing code should go here
    draw_stick_figure(screen, x_coord, y_coord)
    draw_snowman(screen, 0, 0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
