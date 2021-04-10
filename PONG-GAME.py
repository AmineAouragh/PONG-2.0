# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
size = (1200, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG 2.0")


paddleA = Paddle(WHITE, 20, 120)
paddleA.rect.x = 50
paddleA.rect.y = 350

paddleB = Paddle(WHITE, 20, 120)
paddleB.rect.x = 1120
paddleB.rect.y = 350

# This will be a list that will contain all the sprites we intend to use in the game
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the sprites list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

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


    # Clear the screen to black
    screen.fill(BLACK)

    # Draw the net
    pygame.draw.line(screen, WHITE, [599, 0], [599, 900], 5)

    # Draw the sprites
    all_sprites_list.draw(screen)

    # Updating the screen what we've drawn
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick()

# Once we have exited the main program loop we can stop the game engine
pygame.quit()
