import random

import pygame

import config_code
import config_game
import user_settings
from config_code import WINDOW_SETTINGS_GAME, WINDOW_HEIGHT
from correction.correct_color_field import correction


def main_call_point_game(WINDOW):
    if not config_code.START_DRAWING[1]:
        start_background_game(WINDOW)
        start_drawing_game(WINDOW)
        # spawn_unit()
        config_code.START_DRAWING[1] = True
    # test_units(WINDOW)
    # start_background_game(WINDOW)

def start_background_game(WINDOW):
    pygame.draw.rect(WINDOW, config_code.COLOR_GAME, (config_code.WIN_GAME_START, 0,
                                                      config_code.WINDOW_GAME_GAME, WINDOW_HEIGHT))

def start_drawing_game(WINDOW):
    config_code.SIZE_CELL = config_code.WINDOW_GAME_GAME // user_settings.GAME_WIDTH
    width_game_field = config_code.SIZE_CELL*user_settings.GAME_WIDTH
    height_game_field = config_code.SIZE_CELL*user_settings.GAME_HEIGHT

    if height_game_field > config_code.WINDOW_HEIGHT:
        config_code.SIZE_CELL = config_code.WINDOW_HEIGHT // user_settings.GAME_HEIGHT
        width_game_field = config_code.SIZE_CELL * user_settings.GAME_WIDTH
        height_game_field = config_code.SIZE_CELL * user_settings.GAME_HEIGHT

    if width_game_field < config_code.WINDOW_GAME_GAME:
        start_x = config_code.WIN_GAME_START+(config_code.WINDOW_GAME_GAME-width_game_field)//2
    else:
        start_x = config_code.WIN_GAME_START
    if height_game_field < config_code.WINDOW_HEIGHT:
        start_y = (config_code.WINDOW_HEIGHT-height_game_field)//2
    else:
        start_y = 0



    for x in range(user_settings.GAME_WIDTH):
        x_line = []
        for y in range(user_settings.GAME_HEIGHT):
            x_line.append(' ')
            pygame.draw.rect(WINDOW, config_code.COLOR_BLACK,
                             (start_x + x * config_code.SIZE_CELL, start_y + y * config_code.SIZE_CELL,
                              config_code.SIZE_CELL, config_code.SIZE_CELL),
                             config_code.BORDER_PX)
        config_game.FIELD_GAME.append(x_line)


# def spawn_unit():
#     for x in range(500):
#         x = random.randint(config_code.WIN_GAME_START, config_code.WIN_GAME_END)
#         y = random.randint(0, WINDOW_HEIGHT)
#         where = random.choice(['left'])
#         config_game.units.append([x,y, where])
#
# def test_units(WINDOW):
#     for unit in config_game.units:
#         x_correct = config_game.units[config_game.units.index(unit)][0]
#         y_correct = config_game.units[config_game.units.index(unit)][1]
#         size = config_game.size
#         correction(WINDOW, x_correct, y_correct, size, size, config_code.COLOR_GAME)
#         if unit[2] == 'left':
#             config_game.units[config_game.units.index(unit)][0]-=config_game.speed
#         elif unit[2] == 'down':
#             config_game.units[config_game.units.index(unit)][1]+=config_game.speed
#         x = config_game.units[config_game.units.index(unit)][0]
#         x_now = x
#         if 0 < x_correct + config_game.size < config_code.WINDOW_SETTINGS_END:
#             config_game.units[config_game.units.index(unit)][0] = config_code.WIN_GAME_END
#             x_now = config_game.units[config_game.units.index(unit)][0]
#
#         y = config_game.units[config_game.units.index(unit)][1]
#         size = config_game.size
#         pygame.draw.rect(WINDOW, (config_code.COLOR_BLACK), (x_now, y, size, size))
#         if 0<x<config_code.WINDOW_SETTINGS_END:
#             correction(WINDOW, x, y, config_code.WINDOW_SETTINGS_END-x, size, config_code.COLOR_SETTINGS)
#             correction(WINDOW, x_correct, y_correct, config_code.WINDOW_SETTINGS_END-x_correct, size, config_code.COLOR_SETTINGS)






