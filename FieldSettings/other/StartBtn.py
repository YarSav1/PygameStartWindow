import pygame

import config_code
import config_game
import user_settings
from FieldSettings.SetFieldAspect.DrawText import input_text_set_field
from correction.correct_color_field import correction


def _start_btn(WINDOW, descent_y):
    h = config_code.ONE_PERCENT_HEIGHT * 5
    m_x, m_y = pygame.mouse.get_pos()

    if config_code.START_SETTINGS:
        x_btn = config_code.width_btn_section*3
        if not config_code.ACTIVE_INPUT[0]:
            if config_game.START_SIMULATION:
                text_ = 'Стоп'
            else:
                text_ = 'Старт'
            Text = config_code.ShentoxRegular30.render(text_, True, (0, 0, 0))
            w = Text.get_width()
            centre_x = x_btn + config_code.WIDTH_BTN // 2 - w // 2
            h_btn = descent_y + (h // 5)
            WINDOW.blit(Text, (centre_x, h_btn))
        if x_btn < m_x < x_btn + config_code.WIDTH_BTN and descent_y < m_y < descent_y + h:
            pygame.draw.rect(WINDOW, config_code.COLOR_BLACK, (x_btn, descent_y, config_code.WIDTH_BTN, h), 1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    correction(WINDOW, x_btn, descent_y, config_code.WIDTH_BTN, h, config_code.COLOR_SETTINGS)
                    if config_game.START_SIMULATION:
                        config_game.START_SIMULATION = False
                    elif not config_game.START_SIMULATION:
                        config_game.START_SIMULATION = True
        else:
            pygame.draw.rect(WINDOW, config_code.COLOR_SETTINGS, (x_btn, descent_y, config_code.WIDTH_BTN, h), 1)

    descent_y += config_code.WINDOW_HEIGHT / 100 + h
    return descent_y
