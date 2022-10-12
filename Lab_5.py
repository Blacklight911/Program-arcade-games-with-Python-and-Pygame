import pygame

# initialisation pygame
pygame.init()

# creating screen display with 700x500 and set caption
screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption('Blacklight Lair')

# main variable
done = False

# set object of tick-rate
clock = pygame.time.Clock()

width_for_draw_line = 0

font = pygame.font.Font('C:/WINDOWS/Fonts/BERNHC.TTF', 25)

# --------------------- Main Loop -----------------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(0x3d047a)

    text_1 = font.render('Neon', True, 0x2926a1, 0x504cd2)
    text_2 = font.render('Driver', True, 0x1b1889, 0xd3d3e7)

    screen.blit(text_1, [50, 30])
    screen.blit(text_2, [50, 90])

    for x in range(1, 700, 20):
        for y in range(300, 500, 30):
            pygame.draw.polygon(screen, 0x3f074c, [[x, y], [x, y + 30], [x + 20, y + 30], [x + 20, y]], 0)
            pygame.draw.polygon(screen, 0x6c2e7b, [[x, y], [x, y + 30], [x + 20, y + 30], [x + 20, y]], 1)

    pygame.draw.circle(screen, 0xe6670f, [500, 200], 180, 0)
    width_for_draw_line = 2
    width_for_draw_polygon = 3
    for y in range(0, 180, 30):
        pygame.draw.line(screen, 0x3d047a, [310, 130 + y], [680, 130 + y], width_for_draw_line)
        width_for_draw_line += 1
    pygame.draw.polygon(screen, 0x2e2632, [[500, 100], [350, 380], [650, 380]], 0)
    for y in range(0, 30, 10):
        pygame.draw.polygon(screen, 0xa806cf, [[500, 100 - y], [350 - y, 380 + y], [650 + y, 380 + y]],
                            width_for_draw_polygon)

    # Update the full display Surface to the screen
    pygame.display.flip()

    # Tick-rate
    clock.tick(60)

pygame.quit()
