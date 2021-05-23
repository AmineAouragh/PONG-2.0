import pygame


class ScoreDisplayer:

    def __init__(self, font_family, size, txt, color):
        self.font = pygame.font.Font(font_family, size)
        self.text = self.font.render(txt, True, color)

    def draw(self, screen, x, y):
        screen.blit(self.text, (x, y))
