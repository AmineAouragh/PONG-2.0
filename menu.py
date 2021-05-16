"""
This file is not yet linked or used in the main file of the game "PONG-GAME.py"
This file is working independently for now
It's just for testing the implementation of the start menu
Work still in progress
When the implementation is finished, tested and confirmed to be perfect
It will be imported to the main file of the game and linked to the game
"""

import sys

import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import colors
from enum import Enum
from pygame import mixer

BLUE = (106, 159, 181)


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class GameState(Enum):
    QUIT = -1


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):

        self.mouse_over = False  # indicate if the mouse is over the element

        # Create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # Create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=colors.VIVID_ORANGE, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)
        ]

        # calls the init method of the parent sprite class
        super().__init__()

        self.action = action

    @property
    def image(self):

        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):

        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """
          Updates the element's appearance depending on the mouse position
          and returns the button's action if clicked
        """

        if self.rect.collidepoint(mouse_pos):

            self.mouse_over = True
            """
              The sound still needs to be fixed coz it's playing in loop
              when button is hovered
              I have to make it play once and stop
            """
            pygame.mixer.Sound("beep.mp3").play()
            if mouse_up:
                return self.action

        else:

            self.mouse_over = False
            pygame.mixer.Sound("beep.mp3").stop()

    def draw(self, surface):

        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)


def main():

    pygame.init()

    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()

    screen = pygame.display.set_mode((800, 600))

    # create a ui element
    start_btn = UIElement(
        center_position=(400, 180),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="Start",
        action=None
    )

    theme_btn = UIElement(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="Theme",
        action=None
    )

    quit_btn = UIElement(
        center_position=(400, 420),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="Quit",
        action=GameState.QUIT
    )

    def setElement(uielement):
        uielement.update(pygame.mouse.get_pos(), mouse_up)
        uielement.draw(screen)

    # main loop
    while True:

        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_x:
                    pygame.quit()

        screen.fill(BLUE)

        setElement(start_btn)
        setElement(theme_btn)

        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)

        if ui_action is not None:
            return
        quit_btn.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
