import pygame

import config_code
import config_game
import user_settings


def input_text_set_field(WINDOW, x_btn, descent_y, h, w_or_h):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if w_or_h == 'w':
                    user_settings.GAME_WIDTH = int(config_code.TEXT_INPUT)
                    config_code.ACTIVE_INPUT[0] = False
                elif w_or_h == 'h':
                    user_settings.GAME_HEIGHT = int(config_code.TEXT_INPUT)
                    config_code.ACTIVE_INPUT[1] = False
                config_code.TEXT_INPUT = ''
                config_code.START_DRAWING[1] = False
                config_game.FIELD_GAME = []
            elif event.key == pygame.K_BACKSPACE:
                pygame.draw.rect(WINDOW, config_code.COLOR_SETTINGS,
                                 (x_btn, descent_y, config_code.WIDTH_BTN, h))
                config_code.TEXT_INPUT = config_code.TEXT_INPUT[:-1]
            else:
                if len(config_code.TEXT_INPUT) != 3:
                    config_code.TEXT_INPUT += event.unicode
            TextInput = config_code.ShentoxRegular16.render(f'{config_code.TEXT_INPUT}', True, (0, 0, 0))
            pygame.draw.rect(WINDOW, config_code.COLOR_SETTINGS,
                             (x_btn, descent_y, config_code.WIDTH_BTN, h))
            w = TextInput.get_width()
            centre_x = x_btn + config_code.WIDTH_BTN // 2 - w // 2
            h_btn = descent_y + (h // 5)
            WINDOW.blit(TextInput, (centre_x, h_btn))

