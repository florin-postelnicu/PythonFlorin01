

"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

# Set the width and height of the screen [WIDTH, HEIGHT]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
plat1_x = 250
dx = 0

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
       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               dx = -10
            if event.key == pygame.K_RIGHT:
                dx= 10

        elif event.type == pygame.KEYUP:
            if ( event.key == pygame.K_RIGHT) or ( event.key == pygame.K_LEFT):
                dx = 0



    # --- Game logic should go here
    plat1_x = plat1_x + dx
     if (plat1_x < -150 or plat1_x > WIDTH +150):
        plat1_x = plat1_x % (WIDTH + 150)




    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(YELLOW)

    # --- Drawing code should go here
    font = pygame.font.SysFont('Calibri', 25,True,True)
    text = font.render("Hello World !!!",True,BLUE,WHITE)
    screen.blit(text, [250,300])

    # --- Draw rectangles
   
    plat1 = pygame.draw.rect(screen, GREEN, [plat1_x, 200, 150, 50])
    plat2 = pygame.draw.rect(screen, RED, [250, 75, 150, 50], 3)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
