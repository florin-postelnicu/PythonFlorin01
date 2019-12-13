



"""
**********************
Write here some info about you and your program!
Your name:
Program's Objective : The player getting first 3 sets wins
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


# initialize variables for Plat1
plat1_y = 250
dp1 = 0
score_pl1 = 0

# Initialize variables for Plat2
plat2_y = 250
dp2 = 0
score_pl2 = 0

# Initaialize vars for ball
ball_y = 200
ball_x = 300
dbx = 20
dir = 0

# Initialize vars for Sets
set_1 = 2
set_2 = 2

pygame.display.set_caption("My Game")
print(pygame.font.get_fonts())


#
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'C:/Users/postelnicu/PycharmProjects/Star1/venv/Sounds/whipmod.ogg')

# import pictures
backgd = pygame.image.load("backg1.jpg").convert()
pygame.transform.scale(backgd, (700,500),screen)

# import music
hit = pygame.mixer.Sound('C:/Users/postelnicu/PycharmProjects/Star1/venv/Sounds/whipmod.ogg')
pygame.mixer.music.load("//ahs-wl.puhsd.loc/staff/postelnicu/Desktop/ResourcesPy/machine.mp3")

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
            if event.key == pygame.K_UP:  # If pressing UP the velocity is negative
                dp2 = -10
            if event.key == pygame.K_DOWN:  # if pressing DOWN the velocity  is positive
                dp2 = 10

                # Move the second Plat2
            if event.key == pygame.K_w:
                dp1 = -10
            if event.key == pygame.K_s:
                dp1 = 10

        elif event.type == pygame.KEYUP:  # This is to ensure when keys are not pressed the motion stops
            if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                dp2 = 0
            if(event.key == pygame.K_w) or (event.key == pygame.K_s):
                dp1 = 0

        # --- Game logic should go here

    if plat1_y < -100 or plat1_y > HEIGHT:  # This takes care of keeping the platform inside
        dp1 = -dp1  # your window, and not loosing it
        # whenever the platform reaches the end of the
        # window, by changing the sign of velocity
        # it will be changed the direction of motion
    plat1_y = plat1_y + dp1
    if plat2_y < -100 or plat2_y > HEIGHT:  # This takes care of keeping the platform inside
        dp2 = -dp2
    plat2_y = plat2_y + dp2

    if ball_y <10 or ball_y > HEIGHT -10 :

        dir = -dir

    if ball_x <0 :
        ball_y = random.randint(10,HEIGHT -10)
        ball_x = WIDTH -11
        dbx = -20
        score_pl2 = score_pl2 + 1

    if ball_x > WIDTH:
        ball_y = random.randint(10,HEIGHT -10)
        ball_x = 11
        dbx = 20
        score_pl1 = score_pl1 + 1

    ball_x = ball_x + dbx
    ball_y = ball_y + dir

    date = datetime.datetime.now()


    if(score_pl1 > 21 and (score_pl1- score_pl2>= 2)):
        set_1 = set_1 + 1
        score_pl2 = 0
        score_pl1 = 0

    if (score_pl2 > 21 and (score_pl2 - score_pl1 >= 2)):
        set_2 = set_2 + 1
        score_pl2 = 0
        score_pl1 = 0

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    screen.blit(backgd, (0,0))


    # --- Drawing code should go here

    write_msg(" Player1 : " + str(score_pl1),10, 20)
    write_msg("Player2 : " +str(score_pl2), 500, 20)
    write_msg("Set Score", 245, 20)
    write_msg(str(set_1), 245, 60)
    write_msg(str(set_2), 335, 60)

    # Update the set score
    if (set_1 >= 3):

        write_msg("Player 1 wins the Game with the score " + str(set_1) + " to " + str(set_2), 50, 250)
        dbx = 0
        



    if (set_2 >= 3):

        write_msg("Player 2 wins the Game with the score " + str(set_2) + " to " + str(set_1), 50, 250)
        dbx = 0




    # write_msg(str(date), 200, 20)

    # --- Draw rectangles

    plat1 = pygame.draw.rect(screen, GREEN, [0, plat1_y, 10, 200])
    plat2 = pygame.draw.rect(screen, BLUE, [WIDTH -10, plat2_y, 10, 200])
    ball = pygame.draw.circle(screen, RED, (ball_x, ball_y ),10)

    # --- Collision

    if ball.colliderect(plat1) or ball.colliderect(plat2) :

        boom()
        # score_pl1 = score_pl1 +1
        dir = random.randint(-5,5)
        dbx = - dbx





    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
