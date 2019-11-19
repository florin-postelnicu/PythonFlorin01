"""
**********************
Write here some info about you and your program!
Your name:
Program's Objective :
Date when created :
Resources :
**********************
"""

def boom():
    pygame.mixer.music.pause()  # This stops the music when boom() activated
    time.sleep(0.05)
    pygame.mixer.Sound.play(hit)  # the sound at the collision
    pygame.mixer.music.unpause()  # restart the music

def write_msg(text, x_txt, y_txt):
    font = pygame.font.SysFont('gigi', 25, True, True)
    text = font.render(text, True, BLUE, WHITE)
    screen.blit(text, [x_txt, y_txt])
import pygame
import math
import random
import time
import os
import datetime

# Define some colors (red, green, blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()

# Set the width and height of the screen [WIDTH, HEIGHT]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
# initiate the variables for motion here
# if you do it inside the while loop, then the rectangle
# would not move
plat1_x = 250
dx = 0

ball_y = 50
ball_x = 300
dy = 20
dir = 0
score_pl1 = 0
score_pl2 = 0

pygame.display.set_caption("My Game")
print(pygame.font.get_fonts())


#
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'C:/Users/postelnicu/PycharmProjects/Star1/venv/Sounds/whip01.ogg')

# import pictures
backgd = pygame.image.load("backg1.jpg").convert()

# import music
hit = pygame.mixer.Sound('C:/Users/postelnicu/PycharmProjects/Star1/venv/Sounds/whip01.ogg')
pygame.mixer.music.load("TimeTravel.mp3")

pygame.mixer.music.play(-1) # the sound would be played indefinitely




# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # here you choose what are the controls of the window
        if event.type == pygame.QUIT:  # This closes the window if pressing the x button
            done = True

        elif event.type == pygame.KEYDOWN:  # This is to control the keys of the keyboard
            if event.key == pygame.K_LEFT:  # If pressing LEFT the velocity is negative
                dx = -10
            if event.key == pygame.K_RIGHT:  # if pressing RIGHT the velocity  is positive
                dx = 10

        elif event.type == pygame.KEYUP:  # This is to ensure when keys are not pressed the motion stops
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT):
                dx = 0


        # --- Game logic should go here

    if plat1_x < -150 or plat1_x > WIDTH:  # This takes care of keeping the platform inside
        dx = -dx  # your window, and not loosing it
        # whenever the platform reaches the end of the
        # window, by changing the sign of velocity
        # it will be changed the direction of motion
    plat1_x = plat1_x + dx

    if ball_y <10 or ball_y > HEIGHT -10 :
        dy = - dy

    if ball_x <10 or ball_x > WIDTH -10:
        dir = -dir
    ball_x = ball_x + dir
    ball_y = ball_y + dy

    date = datetime.datetime.now()
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # screen.fill(YELLOW)  Replace this comand with a screen.blit(background , (0,0))
    screen.blit(backgd, (0,0))

    # --- Drawing code should go here
  
    write_msg(" Player1 : " + str(score_pl1),10, 20)
    write_msg("Player2 : " +str(score_pl2), 580, 20)
    write_msg(str(date), 200, 20)

    # --- Draw rectangles

    plat1 = pygame.draw.rect(screen, GREEN, [plat1_x, 200, 150, 10])
    plat2 = pygame.draw.rect(screen, BLUE, [250, 75, 150, 10])
    ball = pygame.draw.circle(screen, RED, (ball_x, ball_y ),10)

    # --- Collision

    if ball.colliderect(plat1) :

        boom()
        score_pl1 = score_pl1 +1
        dir = random.randint(-5,5)
        dy = - dy





    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
