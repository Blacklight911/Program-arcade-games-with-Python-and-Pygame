import pygame

# Initialisation
pygame.init()

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Loop until User clicks the close button
done = False
# Set width and height of the screen
size = (799, 500)
screen = pygame.display.set_mode(size)
# Title
pygame.display.set_caption('My game')
# Used to manage how fast screen updates
clock = pygame.time.Clock()


# Classes
class Ball:
    # --- Attributes Class ---
    # Ball position
    x = 0
    y = 0

    # Ball's vector
    change_x = 0
    change_y = 0

    # Ball size
    size = 10

    # Ball color
    color = [255, 255, 255]

    # --- Class methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)


# Create handle
theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255, 0, 0]

theBall.move()
theBall.draw(screen)

# ------------Main Loop Program---------------
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-cleaning should go here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(0xffffff)

    # --- Drawing code should go here
    theBall.move()
    theBall.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
