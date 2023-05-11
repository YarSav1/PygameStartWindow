import pygame

import user_settings
from user_settings import WIDTH_SETTINGS_USER

FPS = 60

pygame.init()  # Инициация модулей pygame
infoObject = pygame.display.Info()  # Информация о размерах экрана.
# Определяем размер экрана.
WINDOW_WIDTH = infoObject.current_w
WINDOW_HEIGHT = infoObject.current_h // 100 * 85

WINDOW_SETTINGS_GAME = WINDOW_WIDTH//100*WIDTH_SETTINGS_USER
WINDOW_GAME_GAME = WINDOW_WIDTH-WINDOW_SETTINGS_GAME

WIN_SETTINGS_START, WINDOW_SETTINGS_END = 0, WINDOW_SETTINGS_GAME
WIN_GAME_START, WIN_GAME_END = WINDOW_SETTINGS_END, WINDOW_WIDTH

CENTRE_SETTINGS = WINDOW_SETTINGS_GAME//2
ONE_PERCENT_HEIGHT = WINDOW_HEIGHT // 100

START_DRAWING = [False, False]
START_SETTINGS = True

START_X_FOR_UNIT = 0
START_Y_FOR_UNIT = 0
SIZE_CELL = 0



COLOR_SETTINGS = (192,192,192)
COLOR_GAME = (96,96,96)
COLOR_BLACK = (0,0,0)
COLOR_ACTIVE_BTN = ()

ACTIVE_INPUT = [False, False]
TEXT_INPUT = ''

BORDER_PX = 1

width_btn_section = WINDOW_SETTINGS_GAME // 9
WIDTH_BTN = width_btn_section*3

# Шрифты
ShentoxRegular30 = pygame.font.Font('Fonts/ShentoxRegular.ttf', 30)
ShentoxRegular16 = pygame.font.Font('Fonts/ShentoxRegular.ttf', 16)
