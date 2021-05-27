import pygame
from random import randint
from colors import BLACK
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, (10, 10), 10)

        self.speed = [1, 1]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = -self.speed[1]
