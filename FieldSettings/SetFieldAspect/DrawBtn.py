import pygame

import config_code
import config_game
import user_settings
from FieldSettings.SetFieldAspect.DrawText import input_text_set_field


def set_field(WINDOW, descent_y):
    h = config_code.ONE_PERCENT_HEIGHT * 5
    m_x, m_y = pygame.mouse.get_pos()

    if not config_game.START_SIMULATION:
        x_btn = config_code.width_btn_section
        if not config_code.ACTIVE_INPUT[0]:
            Text = config_code.ShentoxRegular30.render(f'{user_settings.GAME_WIDTH}', True, (0, 0, 0))
            w = Text.get_width()
            centre_x = x_btn + config_code.WIDTH_BTN // 2 - w // 2
            h_btn = descent_y + (h // 5)
            WINDOW.blit(Text, (centre_x, h_btn))
        if x_btn < m_x < x_btn + config_code.WIDTH_BTN and descent_y < m_y < descent_y + h:
            if config_code.ACTIVE_INPUT[0]:
                input_text_set_field(WINDOW, x_btn, descent_y, h, 'w')
            pygame.draw.rect(WINDOW, config_code.COLOR_BLACK, (x_btn, descent_y, config_code.WIDTH_BTN, h), 1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    config_code.ACTIVE_INPUT[0] = True
        else:
            pygame.draw.rect(WINDOW, config_code.COLOR_SETTINGS, (x_btn, descent_y, config_code.WIDTH_BTN, h), 1)
        if config_code.ACTIVE_INPUT[0]:
            input_text_set_field(WINDOW, x_btn, descent_y, h, 'h')

        x_btn += config_code.width_btn_section * 4

        if not config_code.ACTIVE_INPUT[1]:
            Text = config_code.ShentoxRegular30.render(f'{user_settings.GAME_HEIGHT}', True, (0, 0, 0))
            w = Text.get_width()
            centre_x = x_btn + config_code.WIDTH_BTN // 2 - w // 2
            h_btn = descent_y + (h // 5)
            WINDOW.blit(Text, (centre_x, h_btn))
        if x_btn < m_x < x_btn + config_code.WIDTH_BTN and descent_y < m_y < descent_y + h:
            if config_code.ACTIVE_INPUT[1]:
                input_text_set_field(WINDOW, x_btn, descent_y, h, 'h')
            pygame.draw.rect(WINDOW, config_code.COLOR_BLACK, (x_btn, descent_y, config_code.WIDTH_BTN, h), 1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    config_code.ACTIVE_INPUT[1] = True
        else:
            pygame.draw.rect(WINDOW, config_code.COLOR_SETTINGS, (x_btn, descent_y, config_code.WIDTH_BTN, h), 1)
        if config_code.ACTIVE_INPUT[1]:
            input_text_set_field(WINDOW, x_btn, descent_y, h, 'h')
        # pygame.draw.rect(WINDOW, config_code.COLOR_BLACK, (x_btn, descent_y, config_code.WIDTH_BTN, h))

    descent_y += config_code.WINDOW_HEIGHT / 100 + h
    return descent_y
