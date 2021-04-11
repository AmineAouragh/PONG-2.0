# Import the pygame library and initialise the game engine
import pygame
from time import sleep
from paddle import Paddle
from ball import Ball


pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
size = (1200, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG 2.0")


def init_position(sprite, x, y):

    sprite.rect.x = x
    sprite.rect.y = y


paddleA = Paddle(WHITE, 20, 120)
init_position(paddleA, 50, 350)

paddleB = Paddle(WHITE, 20, 120)
init_position(paddleB, 1120, 350)

ball = Ball(WHITE, 20, 20)
init_position(ball, 590, 440)

# This will be a list that will contain all the sprites we intend to use in the game
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the sprites list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0

# ----Main program loop----
while True:

    # --- Main event loop ---
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            carryOn = False  # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:  # Pressing x will quit the game

                carryOn = False

    # Moving the paddles when the user uses the arrow keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddleA.moveUp(1)

    if keys[pygame.K_s]:
        paddleA.moveDown(1)

    if keys[pygame.K_UP]:
        paddleB.moveUp(1)

    if keys[pygame.K_DOWN]:
        paddleB.moveDown(1)


    all_sprites_list.update()


    if ball.rect.x >= 1180:

        scoreA += 1
        ball.rect.x = 590
        ball.rect.y = 440

    if ball.rect.x <= 0:

        scoreB += 1
        ball.rect.x = 590
        ball.rect.y = 440

    if ball.rect.y >= 880:

        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.y <= 0:

        ball.velocity[1] = -ball.velocity[1]


    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):

        ball.bounce()

    # Clear the screen to black
    screen.fill(BLACK)

    # Draw the net
    pygame.draw.line(screen, WHITE, [599, 0], [599, 900], 5)

    # Draw the sprites
    all_sprites_list.draw(screen)

    # Display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (280, 30))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (880, 30))

    # Updating the screen what we've drawn
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick()

# Once we have exited the main program loop we can stop the game engine
pygame.quit()
