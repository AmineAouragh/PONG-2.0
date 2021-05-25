import pygame
import colors

class GameScreen:

    def __init__(self, size, color):
        self.screen = pygame.display.set_mode(size)
        self.color = self.screen.fill(color)
        self.right_paddle, self.left_paddle = Paddle(colors.WHITE, 20, 120)
