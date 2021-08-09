"""
This file is not yet linked or used in the main file of the game "PONG-GAME.py"
This file is working independently for now
It's just for testing the implementation of the start menu
Work still in progress
When the implementation is finished, tested and confirmed to be perfect
It will be imported to the main file of the game and linked to the game
"""

# TODO Customized Cursor
# When the mouse is over an element the cursor should change its appearance
# If hover set mouse display to invisible and draw a hand cursor
# If click draw the original image of the element with initial size


import pygame
import pygame.freetype
from pygame.sprite import Sprite
import colors
from enum import Enum
from pygame import mixer
from gamescreen import GameScreen

BLUE = (106, 159, 181)

pygame.display.set_caption("MENU")


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class GameState(Enum):
    QUIT = -1  # When you quit the game
    MAIN_MENU = 0  # The main_menu of the game
    NEW_GAME = 1  # Ready to play
    THEMES = 2  # Where you choose a special theme of the game
    LEVELS = 3  # Where you choose a level (Beginner, Medium, Hard)
    MODE = 4  # Choose the mode of the game: TRAINING, MULTIPLAYER, Versus AI, ONLINE
    MUSIC = 4  # Choose a music from library


class GameThemes(Enum):
    CLASSIC = 1
    BLACK_RED = 2
    SOCCER = 3


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


def menu_screen(screen):

    # create a ui element
    start_btn = UIElement(
        center_position=(400, 60),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="START",
        action=GameState.NEW_GAME
    )

    theme_btn = UIElement(
        center_position=(400, 120),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="CHOOSE YOUR THEME",
        action=GameState.THEMES
    )

    level_btn = UIElement(
        center_position=(400, 180),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="GAME LEVEL",
        action=GameState.LEVELS
    )

    mode_btn = UIElement(
        center_position=(400, 240),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="GAME MODE",
        action=GameState.MODE
    )
    
    music_library_btn = UIElement(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="MUSIC LIBRARY",
        action=GameState.MUSIC
    )

    quit_btn = UIElement(
        center_position=(400, 360),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="QUIT",
        action=GameState.QUIT
    )

    # This list hold the different buttons on the main_menu
    buttons = [start_btn, theme_btn, level_btn, mode_btn, quit_btn]

    while True:
        # No button is clicked yet
        mouse_up = False
        # mouse_down = False

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            """
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_down = True
            """

            quit_game_on_event_type(event)  # The block of this function is on line 101

        screen.fill(BLUE)

        for button in buttons:

            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def game_screen(screen):

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
        # mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            """
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_down = True
            """

            quit_game_on_event_type(event)  # The block of this function is on line 101

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
        action=GameThemes.CLASSIC
    )

    black_red_theme = UIElement(
        center_position=(400, 250),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="BLACK & RED",
        action=GameThemes.BLACK_RED
    )

    green_white_theme = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="GREEN & WHITE SOCCER THEME",
        action=GameThemes.SOCCER
    )

    buttons = [classic_theme, black_red_theme, green_white_theme]

    while True:
        # No button is clicked yet
        mouse_up = False
        # mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            """
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_down = True
            """

            quit_game_on_event_type(event)  # The block of this function is on line 101

        screen.fill(BLUE)

        for button in buttons:

            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def classic_screen():

    classic = GameScreen((1200, 900), colors.BLACK)
    classic.create_sprites(colors.WHITE)
    classic.position()
    classic.draw_sprites()

    pygame.display.flip()


def black_red_screen():

    black_red = GameScreen((1200, 900), colors.BLACK)
    black_red.create_sprites(colors.RED)
    black_red.position()
    black_red.draw_sprites()

    pygame.display.flip()


def soccer_screen():

    soccer = GameScreen((1200, 900), colors.GREEN)
    soccer.create_sprites(colors.WHITE)
    soccer.position()
    soccer.draw_sprites()

    pygame.display.flip()


def levels_screen(screen):

    beginner_level = UIElement(
        center_position=(400, 150),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="BEGINNER",
        action=GameState.MAIN_MENU
    )

    medium_level = UIElement(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="MEDIUM",
        action=GameState.MAIN_MENU
    )

    hard_level = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="HARD",
        action=GameState.MAIN_MENU
    )

    buttons = [beginner_level, medium_level, hard_level]

    while True:
        # No button is clicked yet
        mouse_up = False
        # mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            """
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_down = True
            """

            quit_game_on_event_type(event)  # The block of this function is on line 101

        screen.fill(BLUE)

        for button in buttons:

            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def modes_screen(screen):

    training = UIElement(
        center_position=(400, 100),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="TRAINING",
        action=GameState.MAIN_MENU
    )

    multiplayer = UIElement(
        center_position=(400, 250),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="MULTIPLAYER",
        action=GameState.MAIN_MENU
    )

    versus_ai = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="VERSUS AI",
        action=GameState.MAIN_MENU
    )

    online_mod = UIElement(
        center_position=(400, 550),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=colors.WHITE,
        text="ONLINE",
        action=GameState.MAIN_MENU
    )

    buttons = [training, multiplayer, versus_ai, online_mod]

    while True:
        # No button is clicked yet
        mouse_up = False
        # mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            """
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_down = True
            """

            quit_game_on_event_type(event)  # The block of this function is on line 101

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

            pygame.display.set_caption("Menu")
            game_state = menu_screen(screen)

        if game_state == GameState.NEW_GAME:

            pygame.display.set_caption("New Game")
            # exec("game.py")
            game_state = game_screen(screen)

        if game_state == GameState.THEMES:

            pygame.display.set_caption("Themes")
            game_state = themes_screen(screen)

        if game_state == GameThemes.CLASSIC:

            game_state = classic_screen()

        if game_state == GameThemes.BLACK_RED:

            game_state = black_red_screen()

        if game_state == GameThemes.SOCCER:

            game_state = soccer_screen()

        if game_state == GameState.LEVELS:

            pygame.display.set_caption("Levels")
            game_state = levels_screen(screen)

        if game_state == GameState.MODE:

            pygame.display.set_caption("Game Mode")
            game_state = modes_screen(screen)

        if game_state == GameState.QUIT:

            pygame.quit()
            return


if __name__ == "__main__":
    main()
