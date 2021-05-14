"""
This file is not yet linked or used in the main file of the game "PONG-GAME.py"
This file is working independently for now
It's just for testing the implementation of the start menu
Work still in progress
When the implementation is finished, tested and confirmed to be perfect
It will be imported to the main file of the game and linked to the game
"""

import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):

        self.mouse_over = False  # indicate if the mouse is over the element

        # Create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # Create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)
        ]

        # calls the init method of the parent sprite class
        super().__init__()

    @property
    def image(self):

        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):

        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):

        if self.rect.collidepoint(mouse_pos):

            self.mouse_over = True

        else:

            self.mouse_over = False

    def draw(self, surface):

        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)


def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    # create a ui element
    uielement = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Hello World"
    )

    # main loop
    while True:
        for event in pygame.event.get():
            pass
        screen.fill(BLUE)

        uielement.update(pygame.mouse.get_pos())
        uielement.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
