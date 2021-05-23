# Import the pygame library and initialise the game engine
import pygame
import sys
from time import sleep
from playsound import playsound

from paddle import Paddle
from ball import Ball
import colors

pygame.init()


# Open a new window
size = (1200, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG 2.0")


def init_position(sprite, x, y):

    sprite.rect.x = x
    sprite.rect.y = y


paddleL = Paddle(colors.WHITE, 20, 120)
init_position(paddleL, 50, 350)

paddleR = Paddle(colors.WHITE, 20, 120)
init_position(paddleR, 1120, 350)

ball = Ball(colors.WHITE, 20, 20)
init_position(ball, 590, 440)

# This will be a list that will contain all the sprites we intend to use in the game
sprites = pygame.sprite.Group()

# Add the paddles to the sprites list
sprites.add(paddleL, paddleR, ball)

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0

# ----Main program loop----
while True:

    pause = False

    # --- Main event loop ---
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:  # Pressing x will quit the game

                pygame.quit()
                sys.exit()

            if event.key == pygame.K_p or event.key == pygame.K_SPACE:

                pause = True

    while pause:

        pause = True

    # Moving the paddles when the user uses the arrow keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddleL.moveUp(2)

    if keys[pygame.K_s]:
        paddleL.moveDown(2)

    if keys[pygame.K_UP]:
        paddleR.moveUp(2)

    if keys[pygame.K_DOWN]:
        paddleR.moveDown(2)

    sprites.update()

    if ball.rect.x >= 1180:

        scoreA += 1
        init_position(ball, 590, 440)
        sleep(0.3)

    if ball.rect.x <= 0:

        scoreB += 1
        init_position(ball, 590, 440)
        sleep(0.3)

    if ball.rect.y >= 880:

        ball.speed[1] = -ball.speed[1]

    if ball.rect.y <= 0:

        ball.speed[1] = -ball.speed[1]

    if pygame.sprite.collide_mask(ball, paddleL) or pygame.sprite.collide_mask(ball, paddleR):

        ball.bounce()
        # playsound("collision.wav")

    # Clear the screen to black
    screen.fill(colors.BLACK)

    # uielement.update(pygame.mouse.get_pos())
    # uielement.draw(screen)

    # Draw the net
    pygame.draw.line(screen, colors.WHITE, [599, 0], [599, 900], 5)

    # Draw the sprites
    sprites.draw(screen)

    # Display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), True, colors.WHITE)
    screen.blit(text, (280, 30))
    text = font.render(str(scoreB), True, colors.WHITE)
    screen.blit(text, (880, 30))

    # Updating the screen what we've drawn
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick()
