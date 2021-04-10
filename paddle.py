import pygame

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the parent class (Sprite)  constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveUp(self, steps):

        self.rect.y -= steps

        if self.rect.y < 0:

            self.rect.y = 0

    def moveDown(self, steps):

        self.rect.y += steps

        if self.rect.y > 780:

            self.rect.y = 780