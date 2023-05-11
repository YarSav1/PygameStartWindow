import pygame

import config_code
import user_settings
from FieldSettings.SetFieldAspect.DrawBtn import set_field
from FieldSettings.other.StartBtn import _start_btn
from config_code import COLOR_SETTINGS, WINDOW_SETTINGS_GAME, WINDOW_HEIGHT


def main_call_point(WINDOW, CLOCK):
    if not config_code.START_DRAWING[0]:
        start_drawing(WINDOW)
        config_code.START_DRAWING[0] = True

    descent_y = draw_fps(WINDOW, CLOCK)
    descent_y = line(WINDOW, descent_y)
    descent_y = set_field(WINDOW, descent_y)
    descent_y = _start_btn(WINDOW, descent_y)





def start_drawing(WINDOW):
    pygame.draw.rect(WINDOW, COLOR_SETTINGS, (0, 0, WINDOW_SETTINGS_GAME, WINDOW_HEIGHT))

def update_background(WINDOW, x,y,width,height):
    pygame.draw.rect(WINDOW, COLOR_SETTINGS, (x, y, width, height))

def line(WINDOW, descent_y):
    h = config_code.ONE_PERCENT_HEIGHT
    pygame.draw.rect(WINDOW, config_code.COLOR_BLACK, (0, descent_y, config_code.WINDOW_SETTINGS_GAME, h))
    descent_y += WINDOW_HEIGHT / 100 + h
    return descent_y

def draw_fps(WINDOW, CLOCK):
    FPS = int(CLOCK.get_fps())
    Text = config_code.ShentoxRegular30.render(f'FPS: {FPS}', True, (0, 0, 0))

    w, h = Text.get_width(), Text.get_height()  # узнаем размер текста
    centre_x = config_code.CENTRE_SETTINGS - w // 2
    descent_y = config_code.ONE_PERCENT_HEIGHT * 2
    update_background(WINDOW, centre_x-5, descent_y, w+10, h)
    WINDOW.blit(Text, (centre_x, descent_y))
    descent_y += config_code.ONE_PERCENT_HEIGHT + h

    return descent_y

