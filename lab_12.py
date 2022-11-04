"""This is Lab number 12 in course Simpson College"""
import random
import pygame


# Initialisation
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Classes
class Rectangle:
    """This Clas creating Rectangle on the screen"""
    def __init__(self):
        """Initializing random module and set it to x and y"""
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        self.width = random.randint(20, 70)
        self.height = random.randint(20, 70)
        self.x_change = random.randint(-3, 3)
        self.y_change = random.randint(-3, 3)
        self.color = [random.randint(0, 255) for _ in range(3)]

    def draw(self, surface):
        """This function draw rectangle on positions class fields"""
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.height], 0)

    def move(self):
        """This function move rectangle on positions class fields"""
        self.x += self.x_change
        self.y += self.y_change


class Ellipse(Rectangle):
    """Creating an Ellipsoid"""
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, [self.x, self.y, self.width, self.height], 0)


# Loop until User clicks the close button
DONE = False
# Set width and height of the screen
size = (799, 500)
screen = pygame.display.set_mode(size)
# Title
pygame.display.set_caption('My game')
# Used to manage how fast screen updates
clock = pygame.time.Clock()

my_list = []
for _ in range(500):
    MyObject = Rectangle()
    my_list.append(MyObject)

for _ in range(500):
    MyObject = Ellipse()
    my_list.append(MyObject)

    # ------------Main Loop Program---------------
while not DONE:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True

    # --- Game logic should go here

    # --- Screen-cleaning should go here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    for item in my_list:
        item.draw(screen)
        item.move()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
