# Import the pygame library and initialise the game engine
import pygame
from scoredisplayer import ScoreDisplayer
from paddle import Paddle
from ball import Ball
import colors

pygame.init()


class GameScreen:

    def __init__(self, size, color):
        self.screen = pygame.display.set_mode(size)
        self.color = self.screen.fill(color)


pygame.display.set_caption("PONG 2.0")

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0

# ----Main program loop----
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:

                pygame.quit()

    classic = GameScreen((1200, 900), colors.BLACK)

    # Updating the screen what we've drawn
    pygame.display.flip()
