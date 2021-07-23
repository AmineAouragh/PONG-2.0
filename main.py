# TODO Voice Assistant with Speech Recognition
# Implement a voice assistant which takes commands from the user and reacts to it
# The user can pause the game by saying "PAUSE" or quit by saying "QUIT" or "EXIT"

# Import the pygame library and initialise the game engine
import pygame
from time import sleep
from scoredisplayer import ScoreDisplayer
from paddle import Paddle
from ball import Ball
import colors

pygame.init()


# Open a new window
size = (1200, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG 2.0")


def position(sprite, x, y):

    sprite.rect.x = x
    sprite.rect.y = y


paddleL = Paddle(colors.WHITE, 20, 120)
position(paddleL, 50, 350)

paddleR = Paddle(colors.WHITE, 20, 120)
position(paddleR, 1120, 350)

ball = Ball(colors.WHITE, 20, 20)
position(ball, 590, 440)

# This will be a list that will contain all the sprites we intend to use in the game
sprites = pygame.sprite.Group()

# Add the paddles to the sprites list
sprites.add(paddleL, paddleR, ball)

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0


def pause_game():

    paused = True

    while paused:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:

                pygame.quit()

            if ev.type == pygame.KEYDOWN:

                if ev.key == pygame.K_c or event.key == pygame.K_SPACE:

                    paused = False

                elif ev.key == pygame.K_q:

                    pygame.quit()

        large_text = pygame.font.SysFont("comicsansms", 115)
        text_surf = large_text.render("Paused", True, colors.VIVID_ORANGE)
        text_rect = text_surf.get_rect()
        text_rect.center = (600, 400)
        screen.blit(text_surf, text_rect)

        pygame.display.update()
        clock.tick(5)


# ----Main program loop----
while True:

    pause = False

    # --- Main event loop ---
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            pygame.quit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:  # Pressing x will quit the game

                pygame.quit()

            # TODO Fix the pause feature because when the game is paused if I move the mouse the system quit the game

            if event.key == pygame.K_p:

                pause_game()

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
        position(ball, 590, 440)
        sleep(0.3)

    if ball.rect.x <= 0:

        scoreB += 1
        position(ball, 590, 440)
        sleep(0.3)

    if ball.rect.y >= 880:

        ball.speed[1] = -ball.speed[1]

    if ball.rect.y <= 0:

        ball.speed[1] = -ball.speed[1]

    if pygame.sprite.collide_mask(ball, paddleL) or pygame.sprite.collide_mask(ball, paddleR):

        ball.bounce()

    # Clear the screen to black
    screen.fill(colors.BLACK)

    # Draw the net
    pygame.draw.line(screen, colors.WHITE, [599, 0], [599, 900], 5)

    # Draw the sprites
    sprites.draw(screen)

    # Display scores
    scoreLeft = ScoreDisplayer(None, 74, str(scoreA), colors.WHITE)
    scoreLeft.draw(screen, 280, 30)

    scoreRight = ScoreDisplayer(None, 74, str(scoreB), colors.WHITE)
    scoreRight.draw(screen, 880, 30)

    # Updating the screen what we've drawn
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick()
