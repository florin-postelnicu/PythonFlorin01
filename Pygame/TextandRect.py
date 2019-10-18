

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)
YELLOW = (255, 255, 0)

# INITIATE THE PYGAME ENGINE
pygame.init()

# Set the dimensions ( HEIGHT, WIDTH) OF THE SCREEN

WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TEXT & RECT DRAWING")


# loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#--------------MAIN PROGRAM LOOP ----------

while not done:
    #----Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen - clearing code goes here.
    # Don't put other drawing commands above this, or
    # they will be erased with this command

    # If you want a background command image, replace this clear with blit'ing
    # the background image

    screen.fill(YELLOW)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Hello World!", True, RED, WHITE)
    screen.blit(text, [250, 250])

    # ---Drawing code should go here
    platform1 = pygame.draw.rect(screen, GREEN,[250, 200, 120, 20], 4)

    # --- Update the screen with what we have drawn/
    pygame.display.flip()

    # --- limit to 60 frames per second
    clock.tick(60)

# Close the window , and quit.

pygame.quit()





