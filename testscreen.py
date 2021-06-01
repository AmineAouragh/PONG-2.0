# Import the pygame library and initialise the game engine
import pygame
import colors
from paddle import Paddle
from ball import Ball

pygame.init()


class GameScreen:
    
    sprites_list = []

    def __init__(self, size, color):
        self.screen = pygame.display.set_mode(size)
        self.color = self.screen.fill(color)
        
    def create_sprites(self, color):
        
        self.left_paddle, self.right_paddle = Paddle(color, 20, 120)
        self.ball = Ball(color, 20, 20)
        
    def draw(self):
        
        self.sprites_list = pygame.sprite.Group()    
        self.sprites_list.add(self.left_paddle, self.right_paddle, self.ball)
        self.sprites_list.draw(self.screen)
        
        
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
