# Import the pygame library and initialise the game engine
import pygame
from scoredisplayer import ScoreDisplayer
from paddle import Paddle
from ball import Ball
import colors

pygame.init()


class GameScreen:

    sprites_list = []

    def __init__(self, size, color):
        self.screen = pygame.display.set_mode(size)
        self.color = self.screen.fill(color)

        self.right_paddle = Paddle(colors.WHITE, 20, 120)
        self.left_paddle = Paddle(colors.WHITE, 20, 120)

        self.right_paddle.rect.x = 1120
        self.right_paddle.rect.y = 350

        self.left_paddle.rect.x = 50
        self.left_paddle.rect.y = 350

        self.ball = Ball(colors.WHITE, 20, 20)
        self.ball.rect.x = 590
        self.ball.rect.y = 440

        self.sprites_list = pygame.sprite.Group()

        self.sprites_list.add(self.right_paddle, self.left_paddle, self.ball)

    def draw_sprites(self):
        self.sprites_list.draw(self.screen)
        pygame.draw.line(self.screen, colors.WHITE, [599, 0], [599, 900], 5)


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

    classic.draw_sprites()

    # Updating the screen what we've drawn
    pygame.display.flip()
