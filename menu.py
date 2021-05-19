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
    QUIT = -1  # When you quit the game
    MAIN_MENU = 0  # The main_menu of the game
    NEWGAME = 1  # Ready to play
    THEMES = 2  # Where you choose a special theme of the game


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

            """pygame.mouse.set_visible(False)
            hand_hover_cursor = pygame.image.load("hand-hover.png").convert_alpha()
            hand_hover_cursor_rect = hand_hover_cursor.get_rect()
            hand_hover_cursor_rect.center = pygame.mouse.get_pos()"""

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


def quit_game_on_event_type(event):
    # When to quit the game and close the screen
    if event.type == pygame.QUIT:  # When the cross at the upper right of the screen is pressed
        pygame.quit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:  # When the user press X on the keyboard
            pygame.quit()


def title_screen(screen):

    # create a ui element
    start_btn = UIElement(
        center_position=(400, 180),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="START",
        action=GameState.NEWGAME
    )

    theme_btn = UIElement(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="CHOOSE YOUR THEME",
        action=GameState.THEMES
    )

    quit_btn = UIElement(
        center_position=(400, 420),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="QUIT",
        action=GameState.QUIT
    )

    # This list hold the different buttons on the main_menu
    buttons = [start_btn, theme_btn, quit_btn]

    while True:
        # No button is clicked yet
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            quit_game_on_event_type(event)  # The block of this function is on line 110

        screen.fill(BLUE)

        for button in buttons:

            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def play_level(screen):

    return_btn = UIElement(
        center_position=(400, 520),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="Return to Main Menu",
        action=GameState.MAIN_MENU
    )

    while True:

        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            quit_game_on_event_type(event)  # The block of this function is on line 110

        screen.fill(BLUE)

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()


def themes_screen(screen):

    classic_theme = UIElement(
        center_position=(400, 150),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="CLASSIC BLACK & WHITE",
        action=GameState.MAIN_MENU
    )

    black_red_theme = UIElement(
        center_position=(400, 250),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="BLACK & RED",
        action=GameState.MAIN_MENU
    )

    green_white_theme = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="GREEN & WHITE SOCCER THEME",
        action=GameState.MAIN_MENU
    )

    buttons = [classic_theme, black_red_theme, green_white_theme]

    while True:
        # No button is clicked yet
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            quit_game_on_event_type(event)  # The block of this function is on line 110

        screen.fill(BLUE)

        for button in buttons:

            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def main():

    pygame.init()

    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.MAIN_MENU

    # main loop
    while True:

        if game_state == GameState.MAIN_MENU:

            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:

            game_state = play_level(screen)

        if game_state == GameState.THEMES:

            game_state = themes_screen(screen)

        if game_state == GameState.QUIT:

            pygame.quit()
            return


if __name__ == "__main__":
    main()
