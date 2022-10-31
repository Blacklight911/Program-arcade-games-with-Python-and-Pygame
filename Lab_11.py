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
font = pygame.font.Font('C:/Windows/Fonts/ARLRDBD.TTF', 8)
text = font.render('Police Box', True, white)


def telephone(screen, x, y, text):
    pygame.draw.rect(screen, 0x051099, [10 + x, 20 + y, 50, 100], 0)
    pygame.draw.rect(screen, black, [10 + x, 20 + y, 50, 100], 2)
    pygame.draw.rect(screen, 0x051099, [15 + x, 15 + y, 40, 5])
    pygame.draw.rect(screen, 0xaeb104, [30 + x, 5 + y, 10, 10], 0)
    pygame.draw.rect(screen, 0x051099, [30 + x, 5 + y, 10, 10], 1)
    for y_1 in range(7, 12, 2):
        pygame.draw.line(screen, 0x051099, [30 + x, y_1 + y], [39 + x, y_1 + y], 1)
    pygame.draw.rect(screen, black, [15 + x, 30 + y, 40, 80], 2)
    for y_1 in range(50, 100, 20):
        pygame.draw.line(screen, black, [15 + x, y_1 + y], [52 + x, y_1 + y], 2)
    pygame.draw.line(screen, black, [34 + x, 30 + y], [34 + x, 109 + y], 2)
    for x_1 in range(18, 40, 20):
        pygame.draw.rect(screen, 0xc9c2ab, [x_1 + x, 32 + y, 15, 17], 0)

    screen.blit(text, [15 + x, 20 + y])


def man(screen, x, y):
    # Man_2
    pygame.draw.line(screen, black, [10 + x, 20 + y], [10 + x, 80 + y], 5)
    for x_1 in range(0, 21, 20):
        for y_1 in range(40, 101, 40):
            pygame.draw.line(screen, black, [x_1 + x, y_1 + y], [x_1 + x, y_1 + 20 + y], 4)
    for y_1 in range(40, 101, 40):
        pygame.draw.line(screen, black, [0 + x + 20, y_1 + y], [0 + x, y_1 + y], 4)
    pygame.draw.circle(screen, black, [10 + x, 20 + y], 15, 0)
    pygame.draw.line(screen, white, [10 + x, 25 + y], [14 + x, 30 + y], 2)
    pygame.draw.line(screen, white, [5 + x, 16 + y], [15 + x, 16 + y], 1)
    pygame.draw.circle(screen, white, [5 + x, 17 + y], 3, 2)
    pygame.draw.circle(screen, white, [15 + x, 17 + y], 3, 2)
    pygame.draw.rect(screen, 0x524f53, [0 + x, 0 + y, 20, 10])


pygame.mouse.set_visible(False)

# keyboard
keyboard_x_speed = 0
keyboard_y_speed = 0

# Current pos
keyboard_x = 10
keyboard_y = 10

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_x_speed = -3
            if event.key == pygame.K_RIGHT:
                keyboard_x_speed = 3
            if event.key == pygame.K_UP:
                keyboard_y_speed = -3
            if event.key == pygame.K_DOWN:
                keyboard_y_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keyboard_x_speed = 0
            if event.key == pygame.K_RIGHT:
                keyboard_x_speed = 0
            if event.key == pygame.K_UP:
                keyboard_y_speed = 0
            if event.key == pygame.K_DOWN:
                keyboard_y_speed = 0

    keyboard_x += keyboard_x_speed
    keyboard_y += keyboard_y_speed

    # --- Game logic should go here
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    # Move the object according to the speed vector.

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(white)

    telephone(screen, keyboard_x, keyboard_y, text)
    man(screen, mouse_x, mouse_y)
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
